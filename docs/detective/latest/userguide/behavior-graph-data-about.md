# Data in a Detective behavior graph

In Amazon Detective, you conduct investigations using data from a Detective behavior graph. In this section you can learn about the core data sources used in a Detective behavior graph and how Detective uses the source data to populate it.

A behavior graph is a linked set of data generated from the Detective source data that is
ingested from one or more Amazon Web Services (AWS) accounts.

The behavior graph uses the source data to do the following.

- Generate an overall picture of your systems, users, and the interactions among them over
  time
- Perform more detailed analysis of specific activity to help you answer questions that arise
  as you conduct investigations
- Correlate collections of findings, entities, and evidence that may be related to the same event or security issue.
  Note that all extraction, modeling, and analytics of behavior graph data occurs within the
  context of each individual behavior graph.

Each behavior graph contains data from one or more accounts. When an account enables
Detective, it becomes the administrator account for the behavior graph, and it chooses the member
accounts for the behavior graph. A behavior graph can have up to 1,200 member accounts. For
information about how an administrator account manages the member accounts in a behavior graph,
see [Managing
accounts in Detective](accounts.md "accounts.md").

###### Contents

- [How Detective populates a
  behavior graph](behavior-graph-population-about.md "behavior-graph-population-about.md")
- [Training period for new Detective behavior graphs](detective-data-training-period.md "detective-data-training-period.md")
- [Overview of the behavior graph data
  structure](graph-data-structure-overview.md "graph-data-structure-overview.md")
- [Source data used in a Detective behavior graph](detective-source-data-about.md "detective-source-data-about.md")
