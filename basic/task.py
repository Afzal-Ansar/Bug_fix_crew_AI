## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import read_data_tool, analyze_investment_tool, create_risk_assessment_tool

## Creating a task to help solve user's query
analyze_financial_document_task = Task(
    description="""Thoroughly analyze the financial document to address the user's query: {query}
    
    Your analysis should include:
    1. Read and extract key financial data from the document at path: {file_path}
    2. Identify relevant financial metrics (revenue, profit margins, cash flow, debt levels, etc.)
    3. Analyze trends and year-over-year or quarter-over-quarter changes
    4. Evaluate the company's financial health and performance
    5. Provide insights specific to the user's query
    6. Highlight any notable strengths, weaknesses, or concerns
    7. Reference specific data points and page numbers from the document
    
    Be thorough, accurate, and ensure all claims are backed by actual data from the document.""",

    expected_output="""A comprehensive financial analysis report that includes:
    
    **Executive Summary:**
    - Brief overview of key findings
    
    **Financial Metrics Analysis:**
    - Revenue and growth trends
    - Profitability metrics (gross margin, operating margin, net margin)
    - Cash flow analysis
    - Balance sheet health (assets, liabilities, equity)
    - Key financial ratios
    
    **Key Insights:**
    - Notable trends and patterns
    - Strengths and competitive advantages
    - Areas of concern or risk
    - Year-over-year or quarter-over-quarter comparisons
    
    **Response to User Query:**
    - Direct answer to the specific question asked
    - Supporting evidence from the document
    
    All analysis should cite specific numbers and sections from the financial document.""",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis_task = Task(
    description="""Based on the financial document analysis, provide balanced investment recommendations.
    
    User query: {query}
    Document path: {file_path}
    
    Your analysis should:
    1. Review key financial metrics and company performance
    2. Assess valuation relative to fundamentals
    3. Identify potential growth catalysts and risks
    4. Consider market conditions and competitive positioning
    5. Provide evidence-based investment perspective
    6. Highlight important considerations for investors
    
    Ensure recommendations are grounded in the actual financial data and appropriate for the company's situation.""",

    expected_output="""A professional investment analysis including:
    
    **Investment Thesis:**
    - Summary of the investment case (bullish, bearish, or neutral)
    - Key supporting factors from financial data
    
    **Financial Strength Assessment:**
    - Revenue growth trajectory
    - Profitability trends
    - Cash generation capability
    - Balance sheet strength
    
    **Valuation Considerations:**
    - Key valuation metrics if available (P/E, P/S, EV/EBITDA, etc.)
    - Comparison to historical performance
    
    **Risk Factors:**
    - Financial risks identified in the document
    - Market and competitive risks
    
    **Investment Considerations:**
    - Key factors investors should monitor
    - Potential catalysts or concerns
    
    **Conclusion:**
    - Balanced perspective on investment attractiveness
    - Important disclaimers about the analysis
    
    Note: This is educational analysis, not personalized investment advice.""",

    agent=investment_advisor,
    tools=[read_data_tool, analyze_investment_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment_task = Task(
    description="""Conduct a comprehensive risk assessment based on the financial document.
    
    User query: {query}
    Document path: {file_path}
    
    Your assessment should:
    1. Identify financial risks (liquidity, solvency, profitability)
    2. Assess operational risks mentioned in the document
    3. Evaluate market and competitive risks
    4. Analyze debt levels and leverage ratios
    5. Review cash flow stability and working capital
    6. Identify any risk factors disclosed in the document
    7. Provide practical risk mitigation insights
    
    Base your assessment on actual data and disclosures from the financial document.""",

    expected_output="""A thorough risk assessment report including:
    
    **Risk Overview:**
    - Summary of primary risk factors
    - Overall risk level assessment
    
    **Financial Risk Analysis:**
    - Liquidity risk (current ratio, quick ratio, cash reserves)
    - Solvency risk (debt-to-equity, interest coverage)
    - Profitability risk (margin trends, revenue volatility)
    - Cash flow risk (operating cash flow consistency)
    
    **Operational Risk Factors:**
    - Business model risks
    - Operational challenges disclosed
    - Supply chain or execution risks
    
    **Market and Competitive Risks:**
    - Market position and competition
    - Industry trends and challenges
    - Regulatory or external risks
    
    **Risk Mitigation Strategies:**
    - Company's current risk management approaches
    - Areas where risk mitigation may be needed
    
    **Key Risk Indicators to Monitor:**
    - Metrics investors should watch
    - Warning signs to be aware of
    
    All risk assessments should be evidence-based and reference specific data points.""",

    agent=risk_assessor,
    tools=[read_data_tool, create_risk_assessment_tool],
    async_execution=False,
)

    
verification_task = Task(
    description="""Verify that the uploaded document is a legitimate financial document.
    
    Document path: {file_path}
    
    Your verification should:
    1. Confirm the document can be read and parsed
    2. Check for presence of financial statements or data
    3. Verify document contains financial terminology and structure
    4. Identify the type of financial document (quarterly report, annual report, financial statement, etc.)
    5. Flag any issues with document quality or completeness
    
    Provide a clear verification status.""",

    expected_output="""A verification report including:
    
    **Document Status:**
    - Verification result (Valid/Invalid)
    - Document type identified
    
    **Document Contents:**
    - Key sections found (income statement, balance sheet, cash flow, etc.)
    - Financial data present
    
    **Quality Assessment:**
    - Document readability
    - Completeness of financial information
    - Any issues or warnings
    
    **Recommendation:**
    - Whether document is suitable for financial analysis
    - Any limitations or concerns""",

    agent=verifier,
    tools=[read_data_tool],
    async_execution=False
)