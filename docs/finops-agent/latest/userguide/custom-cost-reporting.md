

AWS FinOps Agent is in preview release and is subject to change.

# Generating cost reports
<a name="custom-cost-reporting"></a>

Ask the agent to generate financial reports in natural language. The agent creates HTML, PDF, and PPT reports with cost summaries, breakdowns by service, account, Region, or tag, trend analyses, month-over-month comparisons, and forecast projections. If you don't specify a format, the agent defaults to HTML.

Describe the report you want. The agent retrieves data from Cost Explorer and Cost Anomaly Detection, processes the data, builds charts, and assembles the report in the format you request. Reports include visual elements such as charts, stat callouts, comparison columns, and icon-annotated sections rather than plain text and bullet points. The agent runs a quality assurance pass that inspects the output for visual issues before delivering the final file. You can also upload sample reports as [context files](context-files-and-memory.md) for the agent to replicate format and style.

<a name="custom-cost-reporting-formats"></a>**Report formats.** Choose the format that matches your audience and how the report will be consumed.


| Format | When to use it | 
| --- | --- | 
| HTML (.html) | Default. Best for browser viewing and for quickly sharing a link to the artifact. Charts render in the browser. | 
| PDF (.pdf) | Best for archival, email attachments, and reports that need to print well. Layout is fixed across viewers. | 
| PPT (.pptx) | Best for executive reviews and walkthroughs. The agent produces an editable slide deck so you can rearrange, retitle, or annotate slides before presenting. | 

Reports are delivered as artifacts in the agent's response. Download the report from the **Artifacts** workspace in the web application, send it to a Slack channel through a connected [Slack integration](slack-integration.md), or reference it in a follow-up turn so the agent can revise it without regenerating from scratch.

For recurring reporting needs, create a scheduled task that generates and delivers reports on a defined cadence. For details on scheduled tasks, see [Task management](task-management.md).

Sample prompts:
+ “Generate an HTML cost report summarizing our cost trends, top cost drivers, and optimization opportunities. I want to share this with my CFO.”
+ “Generate a PowerPoint covering last month's costs by service, including the anomalies.”
+ “Create a PDF report of last month's spend by linked account.”
+ “Take the weekly report and add a section for anomalies.”
+ “Every Monday at 9 AM, generate a cost summary for the VP of Engineering and post it to {{<slack-channel>}}.”