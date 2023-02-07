```mermaid
graph TD

A[Obsidian Vault]
B[Obsidian Documents]
C[OpenAI Word Embedding API]
D[]
E[Tree]
F[Published]
G[Worm]

F --> E
E --> D
D --> E
F --> D
D --> C
C --> P
D --> S
F --> S
C --> S
```