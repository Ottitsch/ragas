
ollama pull llama3.1:8b-q4_K_M  
ollama serve

python deterministic.py

```bash
C:\>ollama list
NAME           ID              SIZE      MODIFIED
llama3.1:8b    46e0c10c039e    4.9 GB    22 minutes ago
gemma3:1b      8648f39daa8f    815 MB    4 months ago

C:\>ollama show llama3.1:8b
  Model
    architecture        llama
    parameters          8.0B
    context length      131072
    embedding length    4096
    quantization        Q4_K_M

  Capabilities
    completion
    tools

  Parameters
    stop    "<|start_header_id|>"
    stop    "<|end_header_id|>"
    stop    "<|eot_id|>"

  License
    LLAMA 3.1 COMMUNITY LICENSE AGREEMENT
    Llama 3.1 Version Release Date: July 23, 2024
    ...

C:\>fastfetch
/////////////////  /////////////////    
/////////////////  /////////////////    --------
/////////////////  /////////////////    OS: Windows 11 Home x86_64
/////////////////  /////////////////    Host: X570 AORUS ELITE (-CF)
/////////////////  /////////////////    Kernel: WIN32_NT 10.0.22631.5624 (23H2)
/////////////////  /////////////////    Uptime: 19 hours, 43 mins
/////////////////  /////////////////    Packages: 15 (choco)
/////////////////  /////////////////    Shell: CMD 10.0.22621.5547
                                        BIOS (UEFI): F39 (5.17)
/////////////////  /////////////////    Display (VG279QM): 1920x1080 @ 240 Hz in 27" [External] *
/////////////////  /////////////////    Display (VG278): 1920x1080 @ 144 Hz in 27" [External]
/////////////////  /////////////////    Display (VG278): 1920x1080 @ 144 Hz in 27" [External]
/////////////////  /////////////////    DE: Fluent
/////////////////  /////////////////    WM: Desktop Window Manager 10.0.22621.5415
/////////////////  /////////////////    WM Theme: Custom - Blue (System: Dark, Apps: Dark)
/////////////////  /////////////////    Icons: Recycle Bin
/////////////////  /////////////////    Font: Segoe UI (12pt) [Caption / Menu / Message / Status]
                                        Cursor: Windows Default (32px)
                                        Terminal: Windows Terminal 1.22.12111.0
                                        Terminal Font: Cascadia Mono (12pt)
                                        CPU: AMD Ryzen 9 3900X (24) @ 4,65 GHz
                                        GPU: NVIDIA GeForce RTX 2080 SUPER @ 2,15 GHz (7,80 GiB) [Discrete]
                                        Memory: 16,81 GiB / 31,92 GiB (53%)
                                        Swap: 474,66 MiB / 2,00 GiB (23%)
                                        Disk (C:\): 1,44 TiB / 1,82 TiB (79%) - NTFS
                                        Disk (D:\): 144,77 MiB / 110,23 GiB (0%) - NTFS
                                        Disk (E:\): 677,80 GiB / 931,51 GiB (73%) - NTFS
                                        Wifi: Disconnected
                                        Locale: en-AT
