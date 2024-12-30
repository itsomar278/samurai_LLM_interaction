# LLM Interaction Service

[System Overview Documentation](https://daffodil-throne-f06.notion.site/SamurAI-System-Overview-14c82c979e8480348029ec1cc43e9249?pvs=4)

A sophisticated Retrieval-Augmented Generation (RAG) service that transforms video content into interactive learning experiences. The service leverages FAISS (Facebook AI Similarity Search) for efficient vector search, enabling rapid retrieval of relevant context from video transcripts. Combined with GPT-4's capabilities, it provides dynamic features like intelligent chat, quiz generation, smart summarization, and automatic article creation.

The system employs [FAISS](https://github.com/facebookresearch/faiss), Meta AI's state-of-the-art similarity search library, which is capable of efficient similarity search and clustering of dense vectors. FAISS contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. This enables our service to handle large-scale video transcripts efficiently while maintaining quick response times.

## System Overview
![System Architecture](https://github.com/itsomar278/samurai_video_service/blob/main/ezgif-4-77c29e34de%20(1).gif)

## Core Features

### Content Interaction
- Contextual chat with video content
- Dynamic quiz generation with difficulty levels
- Smart content summarization
- Automatic Medium-style article generation

### Technical Stack
- LangChain for RAG pipeline
- FAISS for vector similarity search
- OpenAI GPT-4 for content generation
- Ada-002 for embeddings
- RabbitMQ for async processing
- AWS S3 for storage

## API Endpoints

### Chat Interaction
`POST /api/chat`
```json
{
    "selected_index": "string",
    "user_id": "string",
    "user_query": "string",
    "chat_history": "string",
    "additional_notes": "string"
}
```

### Quiz Generation
`POST /api/quiz`
```json
{
    "selected_index": "string",
    "user_id": "string",
    "total_questions": "integer",
    "hard_questions": "integer",
    "additional_notes": "string"
}
```

### Summarization
`POST /api/summary`
```json
{
    "selected_index": "string",
    "user_id": "string",
    "summary_length": "integer",
    "additional_notes": "string"
}
```

### Article Conversion
`POST /api/article`
```json
{
    "selected_index": "string",
    "user_id": "string"
}
```

## Prompt Engineering & Context Management

### Dynamic Prompting System
- Context-aware prompt generation based on user interaction type
- Role-specific prompting (quiz creator, summarizer, content writer)
- Automatic incorporation of chat history and additional notes
- Structured output formatting for consistent responses

### Prompt Design Principles
- Clear role definitions for targeted LLM behavior
- Specific format instructions for structured outputs
- Dynamic difficulty adjustment for quiz generation
- Contextual preservation across chat interactions
- Comprehensive instruction sets for article formatting

### Best Practices Implementation
- Consistent output structure using JSON and Markdown
- Memory-efficient context windowing
- Strategic content chunking for optimal retrieval
- Dynamic temperature adjustment based on task requirements
- Robust error handling and response validation

## Prerequisites

- RabbitMQ server running on default port 5672
- Python 3.8+
- CUDA-capable GPU (recommended)

## Installation

1. Clone repository:
```bash
git clone https://github.com/itsomar278/samurai_LLM_interaction
cd samurai_LLM_interaction
```

2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the service:
```bash
# Start Django server
python manage.py runserver 0.0.0.0:8080

# In a separate terminal, start RabbitMQ consumer
python manage.py rabbitmq_start_consume
```

## Environment Variables

```env
OPENAI_API_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
S3_BUCKET_NAME=
RABBITMQ_HOST=
RABBITMQ_PORT=
RABBITMQ_USERNAME=
RABBITMQ_PASSWORD=
MYSQL_DB=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=
```

## Processing Pipeline

1. Receives transcription via RabbitMQ
2. Downloads content from S3
3. Generates embeddings using Ada-002
4. Creates FAISS index
5. Enables RAG-powered features:
   - Context-aware chat
   - Intelligent quiz generation
   - Dynamic summarization
   - Article transformation

## Related Services

- Transclation Service: [samurai_video_service](https://github.com/itsomar278/samurai_video_service)
- Authentication Service: [samurai_auth_service](https://github.com/itsomar278/samurai_auth_service)
- API Gateway: [samurai_api_gateway](https://github.com/itsomar278/samurai_api_gateway)
