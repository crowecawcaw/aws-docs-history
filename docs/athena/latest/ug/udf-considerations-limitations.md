# Considerations and limitations

Consider the following points when you use user defined function (UDFs) in
Athena.

- **Built-in Athena functions** – Built-in
  functions in Athena are designed to be highly performant. We recommend that you
  use built-in functions over UDFs when possible. For more information about
  built-in functions, see [Functions in Amazon Athena](functions.md "functions.md").
- **Scalar UDFs only** – Athena only supports
  scalar UDFs, which process one row at a time and return a single column value.
  Athena passes a batch of rows, potentially in parallel, to the UDF each time it
  invokes Lambda. When designing UDFs and queries, be mindful of the potential
  impact to network traffic of this processing.
- UDF handler functions use abbreviated format
  – Use abbreviated format (not full format), for your UDF functions (for
  example, `package.Class` instead of
  `package.Class::method`).
- UDF methods must be lowercase – UDF
  methods must be in lowercase; camel case is not permitted.
- UDF methods require parameters – UDF
  methods must have at least one input parameter. Attempting to invoke a UDF
  defined without input parameters causes a runtime exception. UDFs are meant to
  perform functions against data records, but a UDF without arguments takes in no
  data, so an exception occurs.
- **Java runtime support** – Currently,
  Athena UDFs support the Java 8, Java 11, and Java 17 runtimes for Lambda. For more
  information, see [Building Lambda functions with
  Java](../../../lambda/latest/dg/lambda-java.md "../../../lambda/latest/dg/lambda-java.md") in the _AWS Lambda Developer Guide_.

###### Note

For Java 17, you must set the value of `JAVA_TOOL_OPTIONS` environment variable as `--add-opens=java.base/java.nio=ALL-UNNAMED` in your Lambda.

- **IAM permissions** – To run and create
  UDF query statements in Athena, the IAM principal running the query must be
  allowed to perform actions in addition to Athena functions. For more information,
  see [Allow access to Athena UDFs: Example policies](udf-iam-access.md "udf-iam-access.md").
- **Lambda quotas** – Lambda quotas apply to
  UDFs. For more information, see [Lambda quotas](../../../lambda/latest/dg/limits.md "../../../lambda/latest/dg/limits.md") in the
  _AWS Lambda Developer Guide_.
- Row-level filtering – Lake Formation row-level
  filtering is not supported for UDFs.
- Views – You cannot use views with UDFs.
- **Known issues** – For the most up-to-date
  list of known issues, see [Limitations and issues](https://github.com/awslabs/aws-athena-query-federation/wiki/Limitations_And_Issues "https://github.com/awslabs/aws-athena-query-federation/wiki/Limitations_And_Issues") in the awslabs/aws-athena-query-federation
  section of GitHub.
