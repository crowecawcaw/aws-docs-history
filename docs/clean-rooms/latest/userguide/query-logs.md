# Analysis logging in AWS Clean Rooms

_Analysis logging_ is a feature in AWS Clean Rooms. When you [create a collaboration](create-collaboration.md "create-collaboration.md") and turn on **Analysis
logging**, members can store relevant logs from queries or logs from jobs in
Amazon CloudWatch Logs.

With query logs and job logs, members can determine if the queries comply with the analysis
rules and align with the collaboration agreement. In addition, query logs help support
audits.

When the **Analysis logging** option is turned on in the AWS Clean Rooms console, the
query logs include the following:

- `analysisRule` – The analysis rule for the configured table.
- `analysisTemplateArn` – The analysis template that was run (appears
  depending on analysis rule).
- `collaborationId` – The unique identifier for collaboration in which
  the query was run.
- `configuredTableID` – The unique identifier for configured table
  referenced in the query.
- `directQueryAnalysisRulePolicy.custom.allowedAnalysis` – The analysis
  template allowed to run on configured table (appears depending on analysis rule).
- `directQueryAnalysisRulePolicy.v1.custom.allowedAnalysisProviders` –
  The query providers allowed to create query (appears depending on analysis rule).
- `errorCode` – The error code when a query failed to execute properly.
- `errorMessage` – The error message when a query failed to execute properly.
- `eventID` – The unique identifier for the query run. After August 31,
  2023, the unique identifier is the same as the `protectedQueryID`.
- `eventTimestamp` – The query run time.
- `parameters.parametervalue` – The parameter values (appears depending
  on the query text).
- `queryText` – The SQL definition of query run. If there are
  parameters, they are labelled as `:parametervalue`.
- `queryValidationErrors` – The query errors at query validation.
- `schemaName` – The name of configured table association referenced in
  the query.
- `status` – The execution status of the query.
