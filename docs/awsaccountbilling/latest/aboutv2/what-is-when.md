

# When to use Data Hub

Enable Data Hub when you want AWS FinOps Agent to answer questions that need an individual resource, hourly detail, or a field such as a resource identifier, a cost allocation tag, or a usage quantity. Without Data Hub, AWS FinOps Agent continues to answer questions at the service and account level by using the AWS Cost Explorer API.

Continue to use AWS Data Exports to export your cost and usage data to Amazon S3, apply your own transformations, join your cost data with data from outside AWS, or load the data into your data warehouse and BI tools. Use Data Hub when you want AWS FinOps Agent to query the same resource-level data for you, without setting up an export or building a pipeline. Data Hub does not read your existing Data Exports and does not change them. Your existing Data Exports keep running with the same fields, values, and delivery.