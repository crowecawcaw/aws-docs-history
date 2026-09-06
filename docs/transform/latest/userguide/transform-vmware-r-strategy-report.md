

# Migration strategy (7Rs) recommendations
<a name="transform-vmware-r-strategy-report"></a>

During migration planning, AWS Transform can analyze your discovered inventory and recommend a migration strategy, one of the industry-standard *7Rs*, for every server and application. Each recommendation includes a suggested AWS target service, a confidence score, and the reasoning behind it. This gives you a defensible starting point for your wave plan and surfaces modernization opportunities that you might otherwise miss.

The seven strategies are *rehost*, *replatform*, *refactor*, *repurchase*, *retire*, *retain*, and *relocate*. AWS Transform reads signals in your data, such as operating system, utilization, and workload type, to make explainable recommendations. For example, it can:
+ Recommend retiring idle or end-of-life servers.
+ Move SQL Server or open-source databases to Amazon RDS.
+ Shift email and collaboration workloads to Microsoft 365.
+ Retain specialized legacy systems.
+ Rehost the remaining workloads on Amazon EC2.

Recommendations roll up from individual servers to applications and across your entire portfolio, with a criticality view by strategy and wave-level summaries.

To generate a migration strategy (7Rs) report:

1. Complete the *Discover on-premises data* step and group your servers into applications. Both are required so that AWS Transform can provide per-server and per-application recommendations.

1. In the migration planning chat, ask AWS Transform for a migration strategy (7Rs) report. For example, *Generate an R-strategy report*. After application grouping completes, AWS Transform also offers to generate the report for you.

1. AWS Transform analyzes your inventory, applies the 7Rs framework, and generates the report. You can provide details such as your organization name and any filters to scope the analysis.

1. Review the recommendations. To adjust a recommendation, tell AWS Transform in the chat. You can change a single server or application, or apply a change in bulk (for example, by operating system, environment, wave, or priority). AWS Transform updates the report with your changes.

By default, AWS Transform produces an interactive HTML dashboard that you can filter and explore. On request, you can also generate a PDF document to share with stakeholders, or a Microsoft PowerPoint (PPTX) slide deck to present. The PDF and PowerPoint outputs are point-in-time snapshots of the same analysis. The report includes:
+ A recommended strategy and AWS target service for every server and application
+ Confidence scores and reasoning
+ Highlighted modernization opportunities
+ A criticality view by strategy
+ Wave-level summaries
+ Risk flags

The strategy recommended in this report complements the per-wave strategy that you assign during wave planning. For source code containerization, see [Source code containerization](transform-containers.md).