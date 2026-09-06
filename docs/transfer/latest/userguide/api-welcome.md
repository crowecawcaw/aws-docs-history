

# AWS Transfer Family API Reference
<a name="api-welcome"></a>

The complete API Reference guide for Transfer Family is available at [AWS Transfer Family API Reference](https://docs.aws.amazon.com/transfer/latest/APIReference/api-welcome.html). 

AWS Transfer Family is a secure transfer service that you can use to transfer files into and out of Amazon Simple Storage Service (Amazon S3) storage over the following protocols:
+ Secure Shell (SSH) File Transfer Protocol (SFTP)
+ File Transfer Protocol Secure (FTPS)
+ File Transfer Protocol (FTP)
+ Applicability Statement 2 (AS2)

Servers, users, and roles are all identified by their Amazon Resource Name (ARN). You can assign tags, which are key-value pairs, to entities with an ARN. Tags are metadata that can be used to group or search for these entities. One example where tags are useful is for accounting purposes.

The following conventions are observed in AWS Transfer Family ID formats:
+ `ServerId` values take the form `s-01234567890abcdef`.
+ `SshPublicKeyId` values take the form `key-01234567890abcdef`.

Amazon Resource Name (ARN) formats take the following form:
+ For servers, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:server/{{server-id}}`.

  An example of a server ARN is: `arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef`.
+ For users, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:user/{{server-id}}/{{username}}`.

  An example is `arn:aws:transfer:us-east-1:123456789012:user/s-01234567890abcdef/user1`.

DNS entries (endpoints) in use are as follows:
+ API endpoints take the form `transfer.{{region}}.amazonaws.com`.
+ Server endpoints take the form `{{server-id}}.server.transfer.{{region}}.amazonaws.com`.

This API interface reference for AWS Transfer Family contains documentation for a programming interface that you can use to manage AWS Transfer Family. The reference structure is as follows:
+ For the alphabetical list of API actions, see [Actions](https://docs.aws.amazon.com/transfer/latest/APIReference/API_Operations.html).
+ For the alphabetical list of data types, see [Types](https://docs.aws.amazon.com/transfer/latest/APIReference/API_Types.html).
+ For a list of common query parameters, see [Common Parameters](https://docs.aws.amazon.com/transfer/latest/APIReference/CommonParameters.html).
+ For descriptions of the error codes, see [Common Errors](https://docs.aws.amazon.com/transfer/latest/APIReference/CommonErrors.html).

**Tip**  
Rather than actually running a command, you can use the `--generate-cli-skeleton` parameter with any API call to generate and display a parameter template. You can then use the generated template to customize and use as input on a later command. For details, see [Generate and use a parameter skeleton file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html#cli-usage-skeleton-generate).

## Making API requests
<a name="making-api-requests"></a>

In addition to using the console, you can use the AWS Transfer Family API to programmatically configure and manage your servers. This section describes the AWS Transfer Family operations, request signing for authentication and the error handling. For information about the regions and endpoints available for Transfer Family, see [AWS Transfer Family endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transfer-service.html) in the *AWS General Reference*

**Note**  
You can also use the AWS SDKs when developing applications with Transfer Family;. The AWS SDKs for Java, .NET, and PHP wrap the underlying Transfer Family API, simplifying your programming tasks. For information about downloading the SDK libraries, see [Sample code libraries](https://aws.amazon.com/code).

### Transfer Family required request headers
<a name="request-headers"></a>

This section describes the required headers that you must send with every POST request to AWS Transfer Family. You include HTTP headers to identify key information about the request including the operation you want to invoke, the date of the request, and information that indicates the authorization of you as the sender of the request. Headers are case insensitive and the order of the headers is not important.

The following example shows headers that are used in the [ListServers](https://docs.aws.amazon.com/transfer/latest/userguide/API_ListServers.html) operation.

```
POST / HTTP/1.1
Host: transfer.us-east-1.amazonaws.com
x-amz-target: TransferService.ListServers
x-amz-date: 20220507T012034Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIDEXAMPLE/20220507/us-east-1/transfer/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-target,
    Signature=13550350a8681c84c861aac2e5b440161c2b33a3e4f302ac680ca5b686de48de
Content-Type: application/x-amz-json-1.1
Content-Length: 17

{"MaxResults":10}
```

The following are the headers that must include with your POST requests to Transfer Family. Headers shown below that begin with "x-amz" are specific for AWS. All other headers listed are common header used in HTTP transactions.

### Transfer Family request inputs and signing
<a name="tf-request-structure"></a>

All request inputs must be sent as part of JSON payload in request body. For Actions in which all request fields are optional, for example `ListServers`, you still need to provide an empty JSON object in the request body, such as `{}`. The structure of Transfer Family payload request/response is documented in existing the API reference, for example [DescribeServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_DescribeServer.html). 

Transfer Family supports authentication using AWS Signature Version 4. For details, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html).

### Error responses
<a name="RESTErrorResponses"></a>

When there is an error, the response header information contains:
+ Content-Type: `application/x-amz-json-1.1`
+ An appropriate `4xx` or `5xx` HTTP status code

The body of an error response contains information about the error that occurred. The following sample error response shows the output syntax of response elements common to all error responses.

```
{
    "__type": "String",
    "Message": "String", <!-- Message is lowercase in some instances -->
    "Resource": "String",
    "ResourceType": "String",
    "RetryAfterSeconds": "String"
}
```

The following table explains the JSON error response fields shown in the preceding syntax.

**\_\_type**  
One of the exceptions from a Transfer Family API call.   
*Type*: String

**Message** or **message**  
One of the operation error code messages.  
Some exceptions use `message`, and others use `Message`. You can check the code for your interface to determine the proper case. Alternatively, you can test each option to see which works.
*Type*: String

**Resource**  
The resource for which the error is invoked. For example, if you try to create a user that already exists, the `Resource` is the username for the existing user.  
*Type*: String

**ResourceType**  
The resource type for which the error is invoked. For example, if you try to create a user that already exists, the `ResourceType` is `User`.  
*Type*: String

**RetryAfterSeconds**  
The number of seconds to wait before retrying the command.  
*Type*: String

#### Error response examples
<a name="RESTErrorResponsesExamples"></a>

The following JSON body is returned if you call the `DescribeServer` API and specify a server that does not exist.

```
{
  "__type": "ResourceNotFoundException",
  "Message": "Unknown server",
  "Resource": "s-11112222333344444",
  "ResourceType": "Server"
}
```

The following JSON body is returned if executing an API causes throttling to occur.

```
{
   "__type":"ThrottlingException",
   "RetryAfterSeconds":"1"
}
```

The following JSON body is returned if you use the `CreateServer` API and you do not have sufficient permissions to create a Transfer Family server.

```
{
  "__type": "AccessDeniedException",
  "Message": "You do not have sufficient access to perform this action."
}
```

The following JSON body is returned if you use the `CreateUser` API and specify a user that already exists.

```
{
  "__type": "ResourceExistsException",
  "Message": "User already exists",
  "Resource": "Alejandro-Rosalez",
  "ResourceType": "User"
}
```

### Available libraries
<a name="using-libraries"></a>

AWS provides libraries, sample code, tutorials, and other resources for software developers who prefer to build applications using language-specific APIs instead of the command-line tools and Query API. These libraries provide basic functions (not included in the APIs), such as request authentication, request retries, and error handling so that it is easier to get started. See [Tools to build on AWS](https://aws.amazon.com/tools/?id=docs_gateway)

For libraries and sample code in all languages, see [Sample code & libraries](http://aws.amazon.com/code).

## Identity Providers
<a name="identity-providers"></a>

AWS Transfer Family supports multiple identity provider types to authenticate and manage users. Each server can use only one authentication method, which must be selected when the server is created.

Service Managed  
With the `SERVICE_MANAGED` authentication method, user credentials are stored and managed within AWS Transfer Family. Users are authenticated using SSH public keys that are associated with their username on the server.  
Each user can have one or more SSH public keys stored in the service. When a client requests a file operation, it provides the username and SSH private key, which is authenticated against the stored public key.

Directory Service  
The `AWS_DIRECTORY_SERVICE` authentication method allows you to integrate with AWS Directory Service for Microsoft Active Directory (AWS Directory Service for Microsoft Active Directory).  
This option enables you to manage user authentication and access through your existing Active Directory groups. Users can authenticate using their Active Directory credentials.  
There is a default limit of 100 Active Directory groups per server, which can be increased to a maximum of 150 groups through a service limit increase.

Lambda  
The `AWS_LAMBDA` authentication method allows you to connect to a custom identity provider using AWS Lambda.  
This option provides flexibility to integrate with your existing identity management systems. The Lambda function is responsible for authenticating users and returning the appropriate access policies.

Custom (API Gateway)  
The `API_GATEWAY` authentication method (displayed as **Custom** in the console) allows you to use a custom authentication method that provides both user authentication and access control.  
This method relies on the Amazon API Gateway to use your API call from your identity provider to validate user requests. You might use this custom method to authenticate users against a directory service, a database name/password pair, or some other mechanism.

For all authentication methods, users are assigned policies that define their access to Amazon S3 buckets or Amazon Elastic File System file systems. The server inherits the trust relationship from the user through an IAM role with an `AssumeRole` action, allowing it to perform file operations on behalf of the user.

## Naming Conventions
<a name="conventions"></a>

AWS Transfer Family uses standardized formats for resource identifiers and Amazon Resource Names (ARNs). Understanding these conventions is important when working with the AWS Transfer Family API.

### ID Formats
<a name="id-formats"></a>

The following conventions are observed in AWS Transfer Family ID formats:

Server IDs  
`ServerId` values take the form `s-01234567890abcdef`.

SSH Public Key IDs  
`SshPublicKeyId` values take the form `key-01234567890abcdef`.

Connector IDs  
`ConnectorId` values take the form `c-01234567890abcdef`.

Workflow IDs  
`WorkflowId` values take the form `w-01234567890abcdef`.

Profile IDs  
`ProfileId` values take the form `p-01234567890abcdef`.

WebApp IDs  
`WebAppId` values take the form `webapp-01234567890abcdef`.

### ARN Formats
<a name="arn-formats"></a>

Amazon Resource Name (ARN) formats take the following form:

Server ARNs  
For servers, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:server/{{server-id}}`.  
Example: `arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef`.

User ARNs  
For users, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:user/{{server-id}}/{{username}}`.  
Example: `arn:aws:transfer:us-east-1:123456789012:user/s-01234567890abcdef/user1`.

Connector ARNs  
For connectors, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:connector/{{connector-id}}`.  
Example: `arn:aws:transfer:us-east-1:123456789012:connector/c-01234567890abcdef`.

Workflow ARNs  
For workflows, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:workflow/{{workflow-id}}`.  
Example: `arn:aws:transfer:us-east-1:123456789012:workflow/w-01234567890abcdef`.

WebApp ARNs  
For web applications, ARNs take the form `arn:aws:transfer:{{region}}:{{account-id}}:webapp/{{webapp-id}}`.  
Example: `arn:aws:transfer:us-east-1:123456789012:webapp/webapp-01234567890abcdef`.

You can assign tags, which are key-value pairs, to entities with an ARN. Tags are metadata that can be used to group or search for these entities. One example where tags are useful is for accounting purposes.

## DNS and Endpoints
<a name="dns-endpoints"></a>

AWS Transfer Family uses standardized DNS naming conventions for both API endpoints and server endpoints. Understanding these endpoints is essential for configuring clients and making API calls.

### API Endpoints
<a name="api-endpoints"></a>

API endpoints are used for making API calls to manage AWS Transfer Family resources. These endpoints take the following forms:

Standard API Endpoints  
Standard API endpoints take the form `transfer.{{region}}.amazonaws.com`.  
Example: `transfer.us-east-1.amazonaws.com`

Dual-Stack API Endpoints  
AWS Transfer Family offers dual-stack API endpoints that can be accessed using either IPv4 or IPv6 requests:  
+ https://transfer.*{{region-code}}*.api.aws
+ https://transfer-fips.*{{region-code}}*.api.aws

### Server Endpoints
<a name="server-endpoints"></a>

Server endpoints are used by file transfer clients to connect to AWS Transfer Family servers. These endpoints take the following forms:

Standard Server Endpoints  
Standard server endpoints take the form `{{server-id}}.server.transfer.{{region}}.amazonaws.com`.  
Example: `s-01234567890abcdef.server.transfer.us-east-1.amazonaws.com`

Custom Hostnames  
You can also configure custom hostnames for your AWS Transfer Family servers. Custom hostnames can be used to provide a more user-friendly or branded experience for your users.  
To use a custom hostname, you must:  

1. Own the domain name

1. Provide a valid certificate

1. Configure DNS records to point to your AWS Transfer Family server

For a complete list of AWS Transfer Family endpoints by AWS Region, see the [AWS Transfer Family endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transfer-service.html) in the *AWS General Reference*.