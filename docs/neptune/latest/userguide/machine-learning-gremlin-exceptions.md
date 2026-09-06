

# List of exceptions for Neptune ML Gremlin inference queries
<a name="machine-learning-gremlin-exceptions"></a>

 This is a comprehensive list of exceptions that can occur when executing Neptune ML Gremlin inference queries. These exceptions cover a range of issues, from problems with the specified IAM role or endpoint, to unsupported Gremlin steps and limitations on the number of ML inference queries per query. Each entry includes a detailed message describing the issue. 
+ **`BadRequestException`**   –   The credentials for the supplied role cannot be loaded.

  *Message*: `Unable to load credentials for role: {{the specified IAM Role ARN}}.`
+ **`BadRequestException`**   –   The specified IAM role is not authorized to invoke the SageMaker AI endpoint.

  *Message*: `User: {{the specified IAM Role ARN}} is not authorized to perform: sagemaker:InvokeEndpoint on resource: {{the specified endpoint}}.`
+ **`BadRequestException`**   –   The specified endpoint does not exist.

  *Message*: `Endpoint {{the specified endpoint}} not found.`
+ **`InternalFailureException`**   –   Unable to fetch Neptune ML real-time inductive inference metadata from Amazon S3.

  *Message*: `Unable to fetch Neptune ML - Real-Time Inductive Inference metadata from S3. Check the permissions of the S3 bucket or if the Neptune instance can connect to S3.`
+ **`InternalFailureException`**   –   Neptune ML cannot find the metadata file for real-time inductive inference in Amazon S3.

  *Message*: `Neptune ML cannot find the metadata file for Real-Time Inductive Inference in S3.`
+ **`InvalidParameterException`**   –   The specified endpoint is not syntactically valid.

  *Message*: `Invalid endpoint provided for external service query.`
+ **`InvalidParameterException`**   –   The specified SageMaker execution IAM Role ARN is not syntactically valid.

  *Message*: `Invalid IAM role ARN provided for external service query.`
+ **`InvalidParameterException`**   –   Multiple property keys are specified in the `properties()` step in a query.

  *Message*: `ML inference queries are currently supported for one property key.`
+ **`InvalidParameterException`**   –   Multiple edge labels are specified in a query.

  *Message*: `ML inference are currently supported only with one edge label.`
+ **`InvalidParameterException`**   –   Multiple vertex label constraints are specified in a query.

  *Message*: `ML inference are currently supported only with one vertex label constraint.`
+ **`InvalidParameterException`**   –   Both `Neptune#ml.classification` and `Neptune#ml.regression` predicates are present in the same query.

  *Message*: `Both regression and classification ML predicates cannot be specified in the query.`
+ **`InvalidParameterException`**   –   More than one edge label was specified in the `in()` or `out()` step in a link-prediction query.

  *Message*: `ML inference are currently supported only with one edge label.`
+ **`InvalidParameterException`**   –   More than one property key was specified with Neptune\#ml.score.

  *Message*: `Neptune ML inference queries are currently supported for one property key and one Neptune#ml.score property key.`
+ **`MissingParameterException`**   –   The endpoint was not specified in the query or as a DB cluster parameter.

  *Message*: `No endpoint provided for external service query.`
+ **``MissingParameterException**   –   The SageMaker AI execution IAM role was not specified in the query or as a DB cluster parameter.

  *Message*: `No IAM role ARN provided for external service query.`
+ **`MissingParameterException`**   –   The property key is missing from the `properties()` step in a query.

  *Message*: `Property key needs to be specified using properties() step for ML inference queries.`
+ **`MissingParameterException`**   –   No edge label was specified in the `in()` or `out()` step of a link-prediction query.

  *Message*: `Edge label needs to be specified while using in() or out() step for ML inference queries.`
+ **`MissingParameterException`**   –   No property key was specified with Neptune\#ml.score.

  *Message*: `Property key needs to be specified along with Neptune#ml.score property key while using the properties() step for Neptune ML inference queries.`
+ **`UnsupportedOperationException`**   –   The `both()` step is used in a link-prediction query.

  *Message*: `ML inference queries are currently not supported with both() step.`
+ **`UnsupportedOperationException`**   –   No predicted vertex label was specified in the `has()` step with the `in()` or `out()` step in a link-prediction query.

  *Message*: `Predicted vertex label needs to be specified using has() step for ML inference queries.`
+ **`UnsupportedOperationException`**   –   Gremlin ML inductive inference queries are not currently supported with unoptimized steps.

  *Message*: `Neptune ML - Real-Time Inductive Inference queries are currently not supported with Gremlin steps which are not optimized for Neptune. Check the Neptune User Guide for a list of Neptune-optimized steps.`
+ **`UnsupportedOperationException`**   –   Neptune ML inference queries are not currently supported inside a `repeat` step.

  *Message*: `Neptune ML inference queries are currently not supported inside a repeat step.`
+ **`UnsupportedOperationException`**   –   No more than one Neptune ML inference query is currently supported per Gremlin query.

  *Message*: `Neptune ML inference queries are currently supported only with one ML inference query per gremlin query.`