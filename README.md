# Document Analyzer & Script Generator

A Streamlit web app that analyzes slide decks and documents, providing AI-powered feedback and generating voiceover scripts.

## Features

### 📊 Document Review
- Extracts text from PDF, PPTX, and DOCX files
- Identifies key messages in each section/slide
- Provides suggestions for improving clarity and engagement
- Offers formatting and tone recommendations
- Tailored feedback based on audience type (Executives, Product Team, External, General)

### 🎤 Voiceover Script Generation
- Generates natural, conversational scripts for narration
- Includes timing markers and pause suggestions
- Adapts tone based on target audience
- Provides estimated reading time

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get OpenAI API Key:**
   - Sign up at [OpenAI](https://platform.openai.com/)
   - Create an API key
   - Enter it in the app's sidebar

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload Document:** Use the file uploader to select your PDF, PowerPoint, or Word document
2. **Configure Settings:** 
   - Enter your OpenAI API key in the sidebar
   - Select your target audience type
3. **Analyze Document:** Click "Run Document Review" to get AI feedback
4. **Generate Script:** Click "Generate Voiceover Script" to create a narration script
5. **Download Results:** Use the download button to save your generated script

## Supported File Formats

- **PDF** (.pdf) - Presentations and documents
- **PowerPoint** (.pptx) - Slide decks
- **Word Documents** (.docx) - Text documents

## File Structure

```
document_analyzer/
├── app.py                    # Main Streamlit application
├── document_processor.py     # Handles file text extraction
├── content_analyzer.py       # AI-powered document analysis
├── script_generator.py       # Voiceover script generation
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for AI processing

## Cost Considerations

This app uses OpenAI's GPT-4 and GPT-3.5-turbo models. Costs will depend on:
- Document length
- Number of analyses performed
- Current OpenAI pricing

Typical costs are very low (under $0.10 per document analysis).

## Privacy & Security

- Documents are processed temporarily and not stored
- API key is entered locally and not saved
- All processing happens in real-time

## Troubleshooting

**File upload issues:** Ensure your document is in a supported format and not corrupted.

**API errors:** Check that your OpenAI API key is valid and has sufficient credits.

**Text extraction problems:** Some PDFs with complex layouts may not extract perfectly.

## Future Enhancements

- Support for additional file formats
- Batch processing capabilities
- Custom prompt templates
- Export to multiple script formats
- Local LLM integration option

