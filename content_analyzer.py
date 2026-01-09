import openai
from typing import Dict, List, Union
import json

class ContentAnalyzer:
    """Analyzes document content and provides improvement suggestions."""
    
    def __init__(self, api_key: str):
        """Initialize with OpenAI API key."""
        self.client = openai.OpenAI(api_key=api_key)
    
    def analyze_document(self, content: Union[str, Dict[str, str]], audience_type: str) -> Dict[str, str]:
        """
        Analyze document content and provide structured feedback.
        
        Args:
            content: Extracted text content (string or dict with sections)
            audience_type: Target audience for tailored feedback
            
        Returns:
            Dictionary with analysis results
        """
        try:
            # Prepare content for analysis
            if isinstance(content, dict):
                formatted_content = self._format_sectioned_content(content)
            else:
                formatted_content = content
            
            # Create analysis prompt
            prompt = self._create_analysis_prompt(formatted_content, audience_type)
            
            # Get AI analysis
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert document reviewer and communication consultant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Parse and structure the response
            analysis_text = response.choices[0].message.content
            return self._parse_analysis_response(analysis_text)
            
        except Exception as e:
            return {
                "key_messages": f"Error analyzing document: {str(e)}",
                "improvements": "Please check your API key and try again.",
                "formatting": "Analysis unavailable due to error."
            }
    
    def _format_sectioned_content(self, content: Dict[str, str]) -> str:
        """Format sectioned content for analysis."""
        formatted = ""
        for section, text in content.items():
            formatted += f"\n=== {section} ===\n{text}\n"
        return formatted
    
    def _create_analysis_prompt(self, content: str, audience_type: str) -> str:
        """Create a comprehensive analysis prompt."""
        return f"""
Please analyze the following document content for a {audience_type.lower()} audience and provide structured feedback:

DOCUMENT CONTENT:
{content}

Please provide your analysis in the following structured format:

## KEY MESSAGES SUMMARY
[Identify and summarize the main messages of each section/slide. Be specific about what each section is trying to communicate.]

## SUGGESTED IMPROVEMENTS
[Provide specific, actionable suggestions to improve clarity, engagement, and impact. Format as bullet points.]

## FORMATTING & TONE RECOMMENDATIONS
[Suggest improvements for formatting, structure, tone, and flow. Consider the {audience_type.lower()} audience.]

Focus on:
1. Clarity and conciseness of messages
2. Logical flow and structure
3. Audience appropriateness for {audience_type.lower()}
4. Engagement and impact
5. Consistency in tone and formatting
"""
    
    def _parse_analysis_response(self, response: str) -> Dict[str, str]:
        """Parse the AI response into structured sections."""
        sections = {
            "key_messages": "",
            "improvements": "",
            "formatting": ""
        }
        
        try:
            # Split response by section headers
            current_section = None
            lines = response.split('\n')
            
            for line in lines:
                line = line.strip()
                
                if "KEY MESSAGES" in line.upper():
                    current_section = "key_messages"
                elif "SUGGESTED IMPROVEMENTS" in line.upper() or "IMPROVEMENTS" in line.upper():
                    current_section = "improvements"
                elif "FORMATTING" in line.upper() or "TONE" in line.upper():
                    current_section = "formatting"
                elif line.startswith('##') or line.startswith('#'):
                    continue  # Skip section headers
                elif current_section and line:
                    sections[current_section] += line + "\n"
            
            # Clean up sections
            for key in sections:
                sections[key] = sections[key].strip()
                if not sections[key]:
                    sections[key] = "No specific recommendations for this section."
            
            return sections
            
        except Exception as e:
            # Fallback: return the full response in key_messages
            return {
                "key_messages": response,
                "improvements": "Could not parse structured recommendations.",
                "formatting": "Please review the full analysis above."
            }
    
    def get_key_messages_only(self, content: Union[str, Dict[str, str]]) -> List[str]:
        """Extract just the key messages from content."""
        try:
            if isinstance(content, dict):
                formatted_content = self._format_sectioned_content(content)
            else:
                formatted_content = content
            
            prompt = f"""
Extract the key messages from this document content. Provide a concise bullet-point list of the main points:

{formatted_content}

Format as:
• Main message 1
• Main message 2
• etc.
"""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a content summarization expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip().split('\n')
            
        except Exception as e:
            return [f"Error extracting key messages: {str(e)}"]

