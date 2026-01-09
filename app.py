import streamlit as st
import os
from typing import Dict, List, Optional
import tempfile

# Import our custom modules
from document_processor import DocumentProcessor
from content_analyzer import ContentAnalyzer
from script_generator import ScriptGenerator

def main():
    st.set_page_config(
        page_title="Document Analyzer & Script Generator",
        page_icon="📄",
        layout="wide"
    )
    
    st.title("📄 Document Analyzer & Script Generator")
    st.markdown("Upload your slide deck or document to get AI-powered feedback and generate voiceover scripts.")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # OpenAI API Key input
        api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        
        # Audience type selection
        audience_type = st.selectbox(
            "Target Audience",
            ["Executives", "Product Team", "External Stakeholders", "General"],
            help="Select the target audience for tailored feedback"
        )
        
        st.markdown("---")
        st.markdown("### Supported Formats")
        st.markdown("- PDF (.pdf)")
        st.markdown("- PowerPoint (.pptx)")
        st.markdown("- Word Documents (.docx)")
    
    # Main content area
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header("📤 Upload Document")
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'pptx', 'docx'],
            help="Upload your slide deck or document"
        )
        
        if uploaded_file:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            st.info(f"File size: {uploaded_file.size / 1024:.1f} KB")
    
    with col2:
        if uploaded_file and api_key:
            # Initialize processors
            processor = DocumentProcessor()
            analyzer = ContentAnalyzer(api_key)
            generator = ScriptGenerator(api_key)
            
            # Process the uploaded file
            with st.spinner("Processing document..."):
                try:
                    # Save uploaded file temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_file_path = tmp_file.name
                    
                    # Extract text from document
                    extracted_content = processor.extract_text(tmp_file_path, uploaded_file.type)
                    
                    # Clean up temporary file
                    os.unlink(tmp_file_path)
                    
                    if not extracted_content:
                        st.error("❌ Could not extract text from the document. Please check the file format.")
                        return
                    
                    st.success("✅ Document processed successfully!")
                    
                    # Display extracted content preview
                    with st.expander("📋 Extracted Content Preview"):
                        if isinstance(extracted_content, dict):
                            for i, (section, content) in enumerate(extracted_content.items(), 1):
                                st.markdown(f"**{section}**")
                                st.text(content[:200] + "..." if len(content) > 200 else content)
                                if i < len(extracted_content):
                                    st.markdown("---")
                        else:
                            st.text(extracted_content[:500] + "..." if len(extracted_content) > 500 else extracted_content)
                    
                    # Feature buttons
                    col_btn1, col_btn2 = st.columns(2)
                    
                    with col_btn1:
                        if st.button("🔍 Run Document Review", use_container_width=True):
                            with st.spinner("Analyzing document..."):
                                review_results = analyzer.analyze_document(extracted_content, audience_type)
                                st.session_state.review_results = review_results
                    
                    with col_btn2:
                        if st.button("🎤 Generate Voiceover Script", use_container_width=True):
                            with st.spinner("Generating script..."):
                                script = generator.generate_script(extracted_content, audience_type)
                                st.session_state.script_results = script
                    
                    # Display results
                    if 'review_results' in st.session_state:
                        st.markdown("---")
                        st.header("📊 Document Review Results")
                        
                        with st.expander("📋 Key Messages Summary", expanded=True):
                            st.markdown(st.session_state.review_results.get("key_messages", "No key messages identified."))
                        
                        with st.expander("✏️ Suggested Improvements"):
                            st.markdown(st.session_state.review_results.get("improvements", "No improvements suggested."))
                        
                        with st.expander("🎨 Formatting & Tone Recommendations"):
                            st.markdown(st.session_state.review_results.get("formatting", "No formatting recommendations."))
                    
                    if 'script_results' in st.session_state:
                        st.markdown("---")
                        st.header("🎤 Voiceover Script")
                        
                        with st.expander("📝 Generated Script", expanded=True):
                            st.markdown(st.session_state.script_results)
                            
                            # Download button for script
                            st.download_button(
                                label="💾 Download Script",
                                data=st.session_state.script_results,
                                file_name=f"{uploaded_file.name.split('.')[0]}_voiceover_script.txt",
                                mime="text/plain"
                            )
                
                except Exception as e:
                    st.error(f"❌ Error processing document: {str(e)}")
        
        elif uploaded_file and not api_key:
            st.warning("⚠️ Please enter your OpenAI API key in the sidebar to proceed.")
        elif not uploaded_file:
            st.info("👆 Please upload a document to get started.")

if __name__ == "__main__":
    main()

