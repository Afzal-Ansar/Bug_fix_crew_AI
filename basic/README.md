# Basic Version - Financial Document Analyzer

## Overview
This is the **basic version** with all bugs fixed but without queue/database enhancements.

## Features
- ✅ All 25 bugs fixed
- ✅ Professional agent prompts
- ✅ Synchronous processing
- ✅ Simple API (2 endpoints)
- ✅ PDF document analysis
- ✅ AI-powered financial analysis

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Update `.env` file:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run Server
```bash
python main.py
```

Server runs on: http://localhost:8000

## API Endpoints

### GET /
Health check
```bash
curl http://localhost:8000/
```

### POST /analyze
Analyze a financial document (synchronous)
```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@data/TSLA-Q2-2025-Update.pdf" \
  -F "query=What is Tesla's Q2 2025 revenue?"
```

**Note:** This waits for the analysis to complete before returning (30-60 seconds).

## Files
- `main.py` - FastAPI server (basic, synchronous)
- `agents.py` - AI agents (fixed bugs)
- `task.py` - Task definitions (fixed bugs)
- `tools.py` - Custom tools (fixed bugs)
- `requirements.txt` - Dependencies
- `.env` - Your API key
- `data/` - Sample financial documents

## What's Different from Enhanced Version?
- ❌ No queue system (Celery/Redis)
- ❌ No database (no result storage)
- ❌ No async processing
- ❌ No status tracking
- ❌ No history
- ✅ Simpler setup
- ✅ Fewer dependencies
- ✅ Easier to run

## When to Use This Version
- Quick testing
- Simple deployments
- Learning the codebase
- Single-user scenarios
- No need for result storage

## Upgrade to Enhanced Version
See `../enhanced/` folder for the full version with:
- Queue worker system
- Database integration
- Async processing
- Status tracking
- Result storage

---

**Version:** 1.0 (Basic)  
**Status:** ✅ Production Ready

