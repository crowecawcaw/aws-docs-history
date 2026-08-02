# Migration strategy (7Rs) recommendations

During migration planning, AWS Transform can analyze your discovered inventory and
recommend a migration strategy, one of the industry-standard
_7Rs_, for every server and application. Each
recommendation includes a suggested AWS target service, a confidence score, and
the reasoning behind it. This gives you a defensible starting point for your wave
plan and surfaces modernization opportunities that you might otherwise miss.

The seven strategies are _rehost_,
_replatform_, _refactor_,
_repurchase_, _retire_,
_retain_, and _relocate_. AWS Transform reads
signals in your data, such as operating system, utilization, and workload
type, to make explainable recommendations. For example, it can recommend
retiring idle or end-of-life servers, moving SQL Server or open-source databases to
Amazon RDS, shifting email and collaboration workloads to Microsoft 365, retaining
specialized legacy systems, and rehosting the remaining workloads on Amazon EC2.
Recommendations roll up from individual servers to applications and across your
entire portfolio, with a criticality view by strategy and wave-level
summaries.

To generate a migration strategy (7Rs) report:

1. Complete the _Discover on-premises data_ step
   and group your servers into applications. Both are required so that
   AWS Transform can provide per-server and per-application
   recommendations.
2. In the migration planning chat, ask AWS Transform for a migration
   strategy (7Rs) report. For example,
   _Generate an R-strategy report_. After application
   grouping completes, AWS Transform also offers to generate the report for
   you.
3. AWS Transform analyzes your inventory, applies the 7Rs framework, and
   generates the report. You can provide details such as your organization
   name and any filters to scope the analysis.
4. Review the recommendations. To adjust a recommendation, tell
   AWS Transform in the chat. You can change a single server or application, or apply
   a change in bulk (for example, by operating system, environment, wave, or
   priority). AWS Transform updates the report with your
   changes.
   By default, AWS Transform produces an interactive HTML dashboard that you can filter
   and explore. On request, you can also generate a PDF document to share with
   stakeholders, or a Microsoft PowerPoint (PPTX) slide deck to present; the PDF and
   PowerPoint outputs are point-in-time snapshots of the same analysis. The report
   includes a recommended strategy and AWS target service for every server and
   application, confidence scores and reasoning, highlighted modernization
   opportunities, a criticality view by strategy, wave-level summaries, and risk
   flags.

The strategy recommended in this report complements the per-wave strategy that
you assign during wave planning. For source code containerization, see [Source code containerization](transform-containers.md "transform-containers.md").
