

# Data Hub (preview)

Data Hub is a feature of AWS Billing and Cost Management that provides agents with a SQL-based managed data layer over cost and usage data. In public preview, AWS FinOps Agent queries Data Hub to attribute cost to individual resources, charge spend back to the teams that own the resources, and track how unit cost moves over time, without a dedicated cost data pipeline for you to build or maintain. You create a dataset of your cost and usage data in Data Hub, and the agent queries the dataset. AWS provisions the data, refreshes it, stores it in AWS-managed storage, and maintains the schema as new services, commitments, and charge types appear on the bill.

**Topics**
+ [When to use Data Hub](what-is-when.md)
+ [Concepts](what-is-concepts.md)
+ [Account scope and billing views](hiw-scope.md)
+ [Prerequisites](setup-prereq.md)
+ [Connect AWS FinOps Agent to Data Hub](gs-create.md)
+ [Turn the Data Hub setting off for one agent](q-turnoff.md)
+ [Tag a dataset](mg-edit.md)
+ [Delete a dataset](mg-delete.md)
+ [Query results](q-results.md)