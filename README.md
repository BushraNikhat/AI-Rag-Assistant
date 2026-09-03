# AI RAG Assistant

An AI-powered RAG (Retrieval-Augmented Generation) assistant built using
React, Python, FastAPI, LLMs, embeddings, and vector databases.

The project is being developed step by step, starting with the fundamentals
of LLM integration and gradually evolving into a complete RAG application.

---

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- HTML5
- CSS3
- Material UI

### Backend
- Python
- FastAPI
- Pydantic
- Async/Await

### AI / GenAI
- LLM Integration
- Prompt Engineering
- Structured LLM Output
- Embedding Models
- Vector Search
- RAG Pipeline

### AI Infrastructure
- Ollama
- Local LLMs
- Vector Database

---

## Project Architecture

```text
                    React Frontend
                          |
                          | HTTP / API
                          ↓
                    FastAPI Backend
                          |
              +-----------+-----------+
              |                       |
              ↓                       ↓
         LLM Services          RAG Services
                                      |
                         +------------+------------+
                         |            |            |
                         ↓            ↓            ↓
                    Documents    Embeddings   Vector DB
                         |
                         ↓
                     Retrieval
                         |
                         ↓
                       LLM
                         |
                         ↓
                     Response
                         |
                         ↓
                    React UI
