# Overview of AWS SDK support for

DynamoDB

The following diagram provides a high-level overview of Amazon DynamoDB application
programming using the AWS SDKs.

![Programming model for using DynamoDB with AWS SDKs.](images/SDKSupport.png)

1. You write an application using an AWS SDK for your programming
   language.
2. Each AWS SDK provides one or more programmatic interfaces for working with
   DynamoDB. The specific interfaces available depend on which programming language
   and AWS SDK you use. Options include:
   - [Low-level interfaces that
     work with DynamoDB](Programming.SDKs.md#Programming.SDKs.Interfaces.LowLevel "Programming.SDKs.md#Programming.SDKs.Interfaces.LowLevel")
   - [Document interfaces that
     work with DynamoDB](Programming.SDKs.md#Programming.SDKs.Interfaces.Document "Programming.SDKs.md#Programming.SDKs.Interfaces.Document")
   - [Object persistence
     interfaces that work with DynamoDB](Programming.SDKs.md#Programming.SDKs.Interfaces.Mapper "Programming.SDKs.md#Programming.SDKs.Interfaces.Mapper")
   - [High Level
     Interfaces](HigherLevelInterfaces.md "HigherLevelInterfaces.md")

3. The AWS SDK constructs HTTP(S) requests for use with the low-level DynamoDB
   API.
4. The AWS SDK sends the request to the DynamoDB endpoint.
5. DynamoDB runs the request. If the request is successful, DynamoDB returns an HTTP
   200 response code (OK). If the request is unsuccessful, DynamoDB returns an HTTP
   error code and an error message.
6. The AWS SDK processes the response and propagates it back to your
   application.
   Each of the AWS SDKs provides important services to your application, including the
   following:

- Formatting HTTP(S) requests and serializing request parameters.
- Generating a cryptographic signature for each request.
- Forwarding requests to a DynamoDB endpoint and receiving responses from
  DynamoDB.
- Extracting the results from those responses.
- Implementing basic retry logic in case of errors.
  You do not need to write code for any of these tasks.

###### Note

For more information about AWS SDKs, including installation instructions and
documentation, see [Tools for Amazon Web
Services](https://aws.amazon.com/tools "https://aws.amazon.com/tools").

## SDK support of AWS account-based

endpoints

AWS is rolling out SDK support for AWS-account-based endpoints for DynamoDB,
starting with the AWS SDK for Java V1 on September 4, 2024. These new endpoints
help AWS to ensure high performance and scalability. The updated SDKs will
automatically use the new endpoints, which have the format
`https://(account-id).ddb.(region).amazonaws.com`.

If you use a single instance of an SDK client to make requests to multiple
accounts, your application will have fewer opportunities to reuse connections. AWS
recommends modifying your applications to connect to fewer accounts per SDK client
instance. An alternative is to set your SDK client to continue using Regional
endpoints using the `ACCOUNT_ID_ENDPOINT_MODE` setting, as documented in
the [_AWS SDKs
and Tools Reference Guide_](../../../sdkref/latest/guide/feature-account-endpoints.md "../../../sdkref/latest/guide/feature-account-endpoints.md").
