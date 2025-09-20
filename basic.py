from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, answer_correctness
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings  # local embeddings

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0,
    num_ctx=4096,
)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

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

