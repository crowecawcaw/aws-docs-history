

# Assessment
<a name="dotnet-web-assessment"></a>

After you confirm repositories for assessment in the *Discovery* phase, your job will enter the *Assessment* phase. AWS Transform analyzes your repositories for modernization suitability based on the following considerations.
+ Framework version and upgrade path
+ Code complexity and solution structure
+ NuGet dependencies (public vs. private)
+ Database connections and ORM patterns

After analysis is complete, you'll see a summary in chat showing the following for each repository:
+ Repository name
+ Complexity
+ Number of solutions
+ Number of projects
+ Lines of code

You can now review the assessment details, select repos for transformation, or assess additional repos.

You can ask questions about the assessment in chat. When you are done reviewing the assessment, instruct the agent to generate a modernization plan for some or all of the repositories.

## Assessment Summary and Report
<a name="assessment-summary-and-report"></a>

To review the assessment, choose the **Assess > General** assessment step at left, or the assessment details link in agent chat. The right panel shows additional detail, including language, complexity rating, and Linux readiness rating. The ratings identify which repositories require minor, moderate, or significant effort to transform.

Detailed assessment information is available in assessment reports. Using the **Download report** button, you can download assessment reports in 5 formats:
+ **Excel assessment report:** package compatibility findings.
+ **HTML assessment report:** detailed assessment including executive summary, portfolio details, repositories, project analysis, findings, Linux incompatibilities, package and API compatibility, and recommendations.
+ **Markdown assessment report:** assessment detail in markdown format.
+ **Spreadsheet assessment report:** tabular assessment detail in CSV format.
+ **JSON assessment report:** assessment detail in JSON format.