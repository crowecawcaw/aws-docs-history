# Summarize query results in natural language

###### Note

The query summarization feature is in preview release for 
 CloudTrail Lake and is subject to change.

After your query finishes, you can get a summary of your query results in natural language 
 from the **Query results** tab in the query editor. This option uses 
 generative artificial intelligence (generative AI) to produce the summary.

###### To summarize query results

1. From the **Query results** tab of the query editor, choose
 **Summarize results** to generate a natural language
 summary of the query results. The summary is provided in English.
2. (Optional) Provide feedback about the summary by choosing the thumbs up or thumbs down
 button that appears below the generated summary.
If the related event data store is encrypted using a KMS key, 
 you cannot use the KMS key to encrypt the query results and summary. The query results and summary are instead encrypted by CloudTrail.

Access to the generated summary is authorized against the
 `GetQueryResults`, `GenerateQueryResultsSummary`, and KMS
 permissions (if the related event date store is encrypted with a KMS key). When a
 summary is generated, CloudTrail records an event named
 `GenerateQueryResultsSummary` for visibility.


## Required permissions


The [`AWSCloudTrail_FullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") 
 and [`AdministratorAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html") managed policies both provide the necessary 
 permissions to use this feature.


You can also include the `cloudtrail:GenerateQueryResultsSummary` and `cloudtrail:GetQueryResults` actions in a new or existing customer managed or inline policy.


If the event data store related to the query results being summarized is encrypted with a KMS key, you also need permissions for the KMS key.


## Region support


This feature is available in the following AWS Regions:



* Asia Pacific (Tokyo) Region (ap-northeast-1)
* US East (N. Virginia) Region (us-east-1)
* US West (Oregon) Region (us-west-2)

## Limitations


The following are limitations of this feature:



* Summaries are in English only.
* Summaries are limited to event data stores that collect CloudTrail events
 (management events, data events, network activity events).
* Each summary is for the results of a single query.
* The query results size must be less than 250 KB.
* The monthly quota of query results that can be summarized is 3 MB.
