

# Diagramming and reporting
<a name="transform-vmware-diagrams-and-reports"></a>

During migration planning, AWS Transform turns your discovered inventory and planning results into visual *diagrams* and analytical *reports*. You generate them conversationally in the planning chat. For example, "Show me a network topology diagram" or "Generate a risk report." AWS Transform builds them from the data you have already provided, with no setup required.

**Diagrams** are interactive and let you explore your environment visually. Available diagrams include:
+ *Network topology* – An interactive map of your servers and their network relationships, designed to scale to large environments of thousands of nodes.
+ *Application dependency* – Directed application-to-application relationships derived from your observed network connections.
+ *Wave Gantt chart* – A timeline view of your migration waves showing schedules, dependencies, milestones, and progress (available after wave planning).
+ *General charts* – Pie charts, bar charts, histograms, treemaps, and summary tables over the dimensions of your data that you choose.

**Reports** provide narrative analysis and recommendations over your migration data. Available reports include:
+ *Risk assessment* – Scores each application across technical complexity, dependency risk, migration readiness, and operational risk, with per-application, per-wave, and portfolio-wide summaries.
+ *Migration strategy (7Rs)* – Per-server and per-application strategy recommendations. For more information, see [Migration strategy (7Rs) recommendations](transform-vmware-r-strategy-report.md).
+ *General and custom reports* – Analytical reports for requests such as executive readiness summaries, cost-versus-risk tradeoffs, and containerization-candidate assessments.

Some outputs depend on how far you are in planning. For example, application dependency diagrams use your network connection data. The wave Gantt chart and wave-level report summaries become available after wave planning completes. If a prerequisite is missing, AWS Transform tells you what is needed and can run the required step first.

AWS Transform delivers diagrams as interactive HTML that you can filter and explore. By default, AWS Transform delivers reports as a self-contained HTML file. On request, AWS Transform can also generate a PDF document to share with stakeholders or a Microsoft PowerPoint (PPTX) slide deck to present. PDF and PowerPoint outputs are point-in-time snapshots of the same analysis.