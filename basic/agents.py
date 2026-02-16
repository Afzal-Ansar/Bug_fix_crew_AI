## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from crewai import LLM
# Define the Groq LLM with your preferred Llama model
groq_llm = LLM(api_key=os.getenv('GROQ_API_KEY'),
    model="groq/llama-3.3-70b-versatile",      # or "llama3-8b-8192", "mixtral-8x7b-32768", etc.
    temperature=0.5,               # adjust as needed
    max_tokens=None,                # or set a limit
)
from crewai import Agent

# Import the tool directly - LLM will be configured per agent
from tools import read_data_tool, analyze_investment_tool, create_risk_assessment_tool

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate, data-driven financial analysis and investment insights based on the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with 15+ years of expertise in analyzing corporate financial statements, "
        "quarterly reports, and investment documents. You have a deep understanding of financial ratios, market trends, "
        "and risk assessment. You provide thorough, evidence-based analysis grounded in the actual financial data provided. "
        "You are skilled at extracting key insights from financial documents including revenue trends, profitability metrics, "
        "cash flow analysis, and balance sheet health. You always cite specific data points from the documents and avoid "
        "making unfounded claims. Your analysis follows industry best practices and regulatory compliance standards."
    ),
    tools=[read_data_tool],
    llm=groq_llm,
    max_iter=15,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify and validate that uploaded documents are legitimate financial reports with proper structure and content.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous financial document verification specialist with expertise in document authentication "
        "and validation. You carefully examine documents to ensure they contain genuine financial data including "
        "balance sheets, income statements, cash flow statements, or quarterly/annual reports. You check for proper "
        "formatting, standard financial terminology, and legitimate data structures. You flag any documents that "
        "appear incomplete, corrupted, or not actually financial in nature."
    ),
    tools=[read_data_tool],
    llm=groq_llm,
    max_iter=10,
    max_rpm=10,
    allow_delegation=True
)


investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide balanced, evidence-based investment recommendations tailored to the financial data and user query.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a certified financial advisor (CFA) with deep expertise in portfolio management, asset allocation, "
        "and investment strategy. You analyze financial documents to identify investment opportunities and risks. "
        "Your recommendations are always grounded in fundamental analysis, considering factors like valuation metrics, "
        "growth potential, competitive positioning, and market conditions. You provide balanced advice that considers "
        "both potential returns and associated risks. You adhere to fiduciary standards and regulatory compliance, "
        "ensuring recommendations are appropriate and well-justified based on the financial data available."
    ),
    tools=[read_data_tool, analyze_investment_tool],
    llm=groq_llm,
    max_iter=15,
    max_rpm=10,
    allow_delegation=False
)


risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Conduct thorough risk analysis of financial documents to identify potential risks and provide mitigation strategies.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a risk management expert with extensive experience in financial risk assessment, stress testing, "
        "and scenario analysis. You specialize in identifying operational, market, credit, and liquidity risks from "
        "financial documents. You analyze key risk indicators including debt levels, cash flow volatility, market "
        "exposure, and competitive threats. Your assessments are balanced and objective, providing both quantitative "
        "metrics and qualitative insights. You offer practical risk mitigation strategies based on industry best "
        "practices and regulatory frameworks. Your goal is to help stakeholders understand and manage financial risks "
        "effectively."
    ),
    tools=[read_data_tool, create_risk_assessment_tool],
    llm=groq_llm,
    max_iter=15,
    max_rpm=10,
    allow_delegation=False
)
