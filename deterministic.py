# Run fully local with Ollama + HuggingFace embeddings and deterministic settings.

# ---------- Reproducibility & seeds (set these BEFORE importing torch-dependent libs) ----------
import os, random, numpy as np
SEED = 42
os.environ["PYTHONHASHSEED"] = str(SEED)
# For strict CUDA determinism (if using GPU):
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
random.seed(SEED)

import torch
torch.manual_seed(SEED)
try:
    torch.use_deterministic_algorithms(True)
except Exception:
    print("missing hardware support for deterministic algo")
    # Some builds/hardware may not support strict deterministic algorithms
    pass

# ---------- Imports ----------
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_correctness
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings

# ---------- LLM (Ollama) ----------
# Make sure Ollama is running and you've pulled a model, e.g.:
#   ollama pull llama3.1:8b
# You can pin a specific quantization for exact reproducibility (e.g., llama3.1:8b-q4_K_M).
llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,     # greedy decoding
    top_p=1,
    top_k=1,
    mirostat=0,        # disable adaptive sampling
    repeat_penalty=1.0,
    seed=SEED,         # critical for reproducibility
    num_ctx=4096,
    num_predict=256,
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

data_samples = {
    "question": [
        "When was the first super bowl?",
        "Who won the most super bowls?",
    ],
    "answer": [
        "The first superbowl was held on Jan 15, 1967",
        "The most super bowls have been won by The New England Patriots",
    ],
    "contexts": [
        [
            "The First AFL–NFL World Championship Game was an American football game played on January 15, 1967, at the Los Angeles Memorial Coliseum in Los Angeles,"
        ],
        [
            "The Green Bay Packers...Green Bay, Wisconsin.",
            "The Packers compete...Football Conference",
        ],
    ],
    "ground_truth": [
        "The first superbowl was held on January 15, 1967",
        "The New England Patriots have won the Super Bowl a record six times",
    ],
}
dataset = Dataset.from_dict(data_samples)

score = evaluate(
    dataset,
    metrics=[faithfulness, answer_correctness],
    llm=llm,
    embeddings=embeddings,
)

df = score.to_pandas()
df.to_csv("score.csv", index=False)
print("\nRagas scores:")
print(df.to_string(index=False))
print("\nSaved to score.csv")

