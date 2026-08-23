# Analysis logging in AWS Clean Rooms

_Analysis logging_ is a feature in AWS Clean Rooms. When you [create a collaboration](create-collaboration.md "create-collaboration.md") and turn on **Analysis
logging**, members can store relevant logs from queries or jobs in
Amazon CloudWatch Logs.

With analysis logs, members can determine if the queries comply with the analysis
rules and align with the collaboration agreement. In addition, analysis logs help support
audits.

When logs are exported, AWS Clean Rooms records an event in the same log group for every log export. You receive the log export event if
you ran the analysis, or if you contributed a table that the analysis referenced. The event shows who
requested the export, which analysis the export was requested for, the destination in Amazon S3, and
whether the request succeeded. For more information about exporting logs, see [Exporting query analysis logs](export-analysis-logs.md "export-analysis-logs.md").

When **Analysis logging** is turned on, AWS Clean Rooms generates logs at two stages: when the analysis runs and when the analysis completes.

Analysis log fields| Field | Delivered when | Description |
| --- | --- | --- |
| `eventId` | Always delivered | The unique identifier for the analysis run. For queries, this is the same as the protectedQueryID. For jobs, this is the same as the protectedJobID. |
| `eventTimestamp` | Always delivered | The time the analysis ran. |
| `collaborationId` | Always delivered | The unique identifier for the collaboration. |
| `logStage` | Always delivered | Indicates whether the log is from submission validation (SUBMISSION) or terminal completion (TERMINATION). |
| `analysisCategory` | Always delivered | The type of analysis: SQL (for queries) or PYSPARK (for jobs). |
| `analysisCategoryVersion` | Always delivered | The version of the analysis category (for example, 1.0). |
| `schemaName` | An analysis runs | The name of the configured table association referenced in the analysis. |
| `configuredTableId` | An analysis runs | The unique identifier for the configured table referenced in the analysis. |
| `analysisTemplateArn` | An analysis runs | The analysis template that was run (appears depending on analysis rule). |
| `parameters` | An analysis runs | The parameter values (appears depending on the analysis text). |
| `queryText` | A query runs | The SQL definition of the query that was run. If there are parameters, they are labeled as `:parametervalue`. |
| `directQueryAnalysisRuleType` | A query runs | The type of analysis rule for the configured table. |
| `directQueryAnalysisRulePolicy` | A query runs | The analysis rule policy including allowed analyses and allowed analysis providers. |
| `queryValidationErrors` | A query runs | The query errors at query validation. |
| `resultReceivers` | A query runs | The members designated to receive query results. |
| `queryRunners` | A query runs | The members designated to run queries. |
| `resultRegions` | A query runs | The AWS Regions where results can be delivered. |
| `analysisTemplateArtifactHashList` | A job runs | The hash list of artifacts associated with the analysis template. |
| `directJobAnalysisRuleType` | A job runs | The type of analysis rule for the configured table. |
| `directJobAnalysisRulePolicy` | A job runs | The analysis rule policy including allowed analyses and allowed analysis providers. |
| `jobValidationErrors` | A job runs | The job errors at job validation. |
| `jobRunners` | A job runs | The members designated to run jobs. |
| `status` | An analysis finishes | The execution status of the analysis. |
| `errorCode` | An analysis finishes | The error code when an analysis failed to execute properly. |
| `errorMessage` | An analysis finishes | The error message when an analysis failed to execute properly. |
| `memberSchemaMapping` | Always delivered | A mapping of member accounts to their schema information. |
| `memberDisplayNames` | Always delivered | A mapping of member accounts to their display names. |
| `additionalAnalyses` | Synthetic data is created | Additional analyses configured for the collaboration. |
| `isSynthetic` | Synthetic data is created | Whether the analysis created [privacy-enhanced synthetic data](synthetic-data-generation.md "synthetic-data-generation.md"). |
| `epsilon` | Synthetic data is created | The epsilon value required to successfully create [privacy-enhanced synthetic data](synthetic-data-generation.md "synthetic-data-generation.md"). |
| `maxMembershipInferenceAttackScore` | Synthetic data is created | The maximum membership inference attack score allowed to successfully create [privacy-enhanced synthetic data](synthetic-data-generation.md "synthetic-data-generation.md"). |
| `machineLearningInputChannelArn` | Synthetic data is created | The ARN of the machine learning input channel. |
| `analysisId` | Logs are exported | The unique identifier of the analysis for which logs were exported. |
| `callerAccountId` | Logs are exported | The account ID of the member who requested the export. |
| `s3OutputPath` | Logs are exported | The Amazon S3 destination where the exported logs were written. |
| `operationName` | Logs are exported | The operation that generated the export event. |
| `logExportValidationErrors` | Logs are exported | Any validation errors during the log export. |

## Delivery, recipients, and log groups

You don't need to perform any actions outside of AWS Clean Rooms to set up query logs and job logs.
AWS Clean Rooms creates log groups for collaborations after each collaboration member [creates a membership](create-membership.md "create-membership.md").

Members who can query, members who can run queries and jobs, members who can receive
results, and members whose configured tables are referenced in the query receive an analysis log.

The member who can query and member who can receive results receive query logs for
each configured table that is referenced in the query. If they don't own the configured table,
they can't view the configured table ID (`configuredTableId`).

The member who can run queries and jobs and member who can receive results receive
job logs for each configured table that is referenced in the job. If they don't own the
configured table, they can't view the configured table ID
(`configuredTableId`).

If a member has multiple configured table associations referenced in the analysis, they
receive an analysis log for each configured table.

Logs are created for queries that contain unsupported and supported SQL in AWS Clean Rooms. For more
details, see the [AWS Clean Rooms
SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md").

Logs are also created when queries or jobs reference configured tables that are not
associated with the collaboration.

Logs might contain information about incorrect SQL.

Query and job logs indicate the status of a query but don't report whether query output
was delivered. They confirm that a query or job was submitted by the member who can query.
Query logs also confirm that the query contains supported SQL in AWS Clean Rooms and references
configured tables that are associated with the collaboration.

###### Note

A log isn't produced if the query was canceled after AWS Clean Rooms validated
its compliance with analysis rules and during query processing.

If you delete the log group, you must re-create the log group manually with the same log
group name (collaboration ID of the collaboration). Or, you can turn the logging off and on in
your membership.

For more information about how to turn on analysis logging, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").

For more information about Amazon CloudWatch Logs, see the [Amazon CloudWatch Logs User
Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
