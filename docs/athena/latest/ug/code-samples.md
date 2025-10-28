# Code samples

The examples in this topic use SDK for Java 2.x as a starting point for writing Athena
applications.

###### Note

For information about programming Athena using other language-specific AWS SDKs, see
the following resources:

- AWS Command Line Interface (`athena`)
- AWS SDK for .NET ([`Amazon.Athena.Model`](../../../sdkfornet/v3/apidocs/items/Athena/NAthenaModel.md "../../../sdkfornet/v3/apidocs/items/Athena/NAthenaModel.md"))
- AWS SDK for C++ (`Aws::Athena::AthenaClient`)
- AWS SDK for Go ([`athena`](../../../sdk-for-go/api/service/athena.md "../../../sdk-for-go/api/service/athena.md"))
- AWS SDK for JavaScript v3 ([`AthenaClient`](../../../AWSJavaScriptSDK/v3/latest/client/athena.md "../../../AWSJavaScriptSDK/v3/latest/client/athena.md"))
- AWS SDK for PHP 3.x ([`Aws\Athena`](../../../aws-sdk-php/v3/api/namespace-Aws.md "../../../aws-sdk-php/v3/api/namespace-Aws.md"))
- AWS SDK for Python (Boto3) ([`Athena.Client`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html"))
- AWS SDK for Ruby v3 ([`Aws::Athena::Client`](../../../sdk-for-ruby/v3/api/Aws/Athena/Client.md "../../../sdk-for-ruby/v3/api/Aws/Athena/Client.md"))
  For more information about running the Java code examples in this section, see the [Amazon Athena Java readme](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/example_code/athena "https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/example_code/athena") on the [AWS code examples
  repository](https://github.com/awsdocs/aws-doc-sdk-examples "https://github.com/awsdocs/aws-doc-sdk-examples") on GitHub. For the Java programming reference for Athena, see [AthenaClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/athena/AthenaClient.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/athena/AthenaClient.html") in the AWS SDK for Java 2.x.

###### Note

These samples use constants (for example, `ATHENA_SAMPLE_QUERY`) for
strings, which are defined in an `ExampleConstants.java` class declaration.
Replace these constants with your own strings or defined constants.

###### Topics

- [Constants](constants.md "constants.md")
- [Create a client to access
  Athena](create-a-client-to-access-athena.md "create-a-client-to-access-athena.md")
- [Start query execution](start-query-execution.md "start-query-execution.md")
- [Stop query execution](stop-query-execution.md "stop-query-execution.md")
- [List query executions](list-query-executions.md "list-query-executions.md")
- [Create a named query](create-a-named-query.md "create-a-named-query.md")
- [Delete a named query](delete-a-named-query.md "delete-a-named-query.md")
- [List named queries](list-named-queries.md "list-named-queries.md")
