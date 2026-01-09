import openai
from typing import Dict, List, Union

class ScriptGenerator:
    """Generates voiceover scripts from document content."""
    
    def __init__(self, api_key: str):
        """Initialize with OpenAI API key."""
        self.client = openai.OpenAI(api_key=api_key)
    
    def generate_script(self, content: Union[str, Dict[str, str]], audience_type: str) -> str:
        """
        Generate a voiceover script from document content.
        
        Args:
            content: Extracted text content (string or dict with sections)
            audience_type: Target audience for script tone
            
        Returns:
            Generated voiceover script
        """
        try:
            # Prepare content for script generation
            if isinstance(content, dict):
                formatted_content = self._format_sectioned_content(content)
            else:
                formatted_content = content
            
            # Create script generation prompt
            prompt = self._create_script_prompt(formatted_content, audience_type)
            
            # Generate script
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert scriptwriter specializing in clear, engaging voiceover scripts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2500
            )
            
            return self._format_script_output(response.choices[0].message.content)
            
        except Exception as e:
            return f"Error generating script: {str(e)}\n\nPlease check your API key and try again."
    
    def _format_sectioned_content(self, content: Dict[str, str]) -> str:
        """Format sectioned content for script generation."""
        formatted = ""
        for section, text in content.items():
            formatted += f"\n=== {section} ===\n{text}\n"
        return formatted
    
    def _create_script_prompt(self, content: str, audience_type: str) -> str:
        """Create a script generation prompt."""
        audience_tone = self._get_audience_tone(audience_type)
        
        return f"""
Create a voiceover script based on the following document content. The script should be written for a {audience_type.lower()} audience.

DOCUMENT CONTENT:
{content}

SCRIPT REQUIREMENTS:
- Write in a {audience_tone} tone
- Use natural, conversational language suitable for spoken narration
- Include smooth transitions between sections
- Keep sentences concise and clear for easy reading aloud
- Add [PAUSE] markers where natural breaks would occur
- Include timing suggestions in brackets like [2 seconds]
- Make it engaging and easy to follow when heard, not read

AUDIENCE: {audience_type}
TONE: {audience_tone}

Please structure the script with clear section breaks and natural flow. Start with a compelling introduction and end with a strong conclusion.
"""
    
    def _get_audience_tone(self, audience_type: str) -> str:
        """Get appropriate tone for audience type."""
        tone_mapping = {
            "Executives": "professional yet accessible, focusing on key insights and strategic value",
            "Product Team": "collaborative and technical, emphasizing actionable insights and implementation details",
            "External Stakeholders": "professional and persuasive, highlighting benefits and value propositions",
            "General": "friendly and informative, making complex topics accessible to everyone"
        }
        return tone_mapping.get(audience_type, "professional and clear")
    
    def _format_script_output(self, script: str) -> str:
        """Format the generated script for better readability."""
        # Add line breaks for better readability
        formatted_script = script.replace('. ', '.\n\n')
        
        # Format timing and pause markers
        formatted_script = formatted_script.replace('[PAUSE]', '\n\n[PAUSE]\n\n')
        formatted_script = formatted_script.replace('[pause]', '\n\n[PAUSE]\n\n')
        
        # Clean up extra line breaks
        lines = formatted_script.split('\n')
        cleaned_lines = []
        for i, line in enumerate(lines):
            if line.strip():  # Non-empty line
                cleaned_lines.append(line)
            elif i > 0 and cleaned_lines and cleaned_lines[-1].strip():  # Add single break after content
                cleaned_lines.append('')
        
        return '\n'.join(cleaned_lines)
    
    def generate_section_script(self, section_content: str, section_title: str, audience_type: str) -> str:
        """Generate script for a specific section."""
        try:
            audience_tone = self._get_audience_tone(audience_type)
            
            prompt = f"""
Create a voiceover script for this specific section of a presentation:

SECTION TITLE: {section_title}
SECTION CONTENT: {section_content}

Requirements:
- {audience_tone} tone for {audience_type.lower()} audience
- Conversational and natural for voiceover
- 1-2 minutes speaking time
- Include natural transitions
- Add [PAUSE] markers where appropriate

Generate only the script content, no additional formatting.
"""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a voiceover scriptwriter."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            return self._format_script_output(response.choices[0].message.content)
            
        except Exception as e:
            return f"Error generating section script: {str(e)}"
    
    def estimate_reading_time(self, script: str) -> str:
        """Estimate reading time for the script."""
        # Average speaking rate: 150-160 words per minute for narration
        words = len(script.split())
        minutes = words / 155  # Use 155 as average
        
        if minutes < 1:
            seconds = int(minutes * 60)
            return f"{seconds} seconds"
        else:
            mins = int(minutes)
            secs = int((minutes - mins) * 60)
            if secs > 0:
                return f"{mins} minutes, {secs} seconds"
            else:
                return f"{mins} minutes"

