## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool

## Creating custom pdf reader tool
@tool("Read Financial Document")
def read_data_tool(path: str = 'data/sample.pdf') -> str:
    """Tool to read data from a pdf file from a path

    Args:
        path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

    Returns:
        str: Full Financial Document file
    """
    try:
        from pypdf import PdfReader
        
        reader = PdfReader(path)
        full_report = ""
        
        for page in reader.pages:
            # Extract text from each page
            content = page.extract_text()
            
            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
        return full_report
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

## Creating Investment Analysis Tool
@tool("Analyze Investment")
def analyze_investment_tool(financial_document_data: str) -> str:
    """Analyze financial document data for investment insights"""
    # Process and analyze the financial document data
    processed_data = financial_document_data
    
    # Clean up the data format
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":  # Remove double spaces
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
            
    # TODO: Implement investment analysis logic here
    return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
@tool("Create Risk Assessment")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """Create risk assessment from financial document data"""
    # TODO: Implement risk assessment logic here
    return "Risk assessment functionality to be implemented"