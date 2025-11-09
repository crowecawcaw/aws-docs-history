Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Signing an HTTP request

Amazon Redshift requires that every request you send to the management API be authenticated with a
signature. This topic explains how to sign your requests.

If you are using one of the AWS Software Development Kits (SDKs) or the AWS Command Line Interface, request signing is
handled automatically, and you can skip this section. For more
information about using AWS SDKs, see [Using the Amazon Redshift management interfaces for provisioned
clusters](using-aws-sdk.md "using-aws-sdk.md"). For more information about using the Amazon Redshift
Command Line Interface, go to [Amazon Redshift command
line reference](../../../cli/latest/reference/redshift/index.md "../../../cli/latest/reference/redshift/index.md").

To sign a request, you calculate a digital signature by using a cryptographic hash function.
A cryptographic hash is a function that returns a unique hash value that is based on the
input. The input to the hash function includes the text of your request and your secret
access key that you can get from temporary credentials. The hash function returns a hash
value that you include in the request as your signature. The signature is part of the
`Authorization` header of your request.

###### Note

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

After Amazon Redshift receives your request, it recalculates the signature by using the same hash
function and input that you used to sign the request. If the resulting signature matches the
signature in the request, Amazon Redshift processes the request; otherwise, the request is
rejected.

Amazon Redshift supports authentication using
[AWS signature version
4](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md"). The process for calculating a signature is composed of three tasks. These
tasks are illustrated in the example that follows.

- [Task 1: Create a canonical request](../../../IAM/latest/UserGuide/create-signed-request.md#create-canonical-request "../../../IAM/latest/UserGuide/create-signed-request.md#create-canonical-request")

Rearrange your HTTP request into a canonical form. Using a canonical form is necessary
because Amazon Redshift uses the same canonical form to calculate the signature it
compares with the one you sent.

- [Task 2: Create a string to sign](../../../IAM/latest/UserGuide/create-signed-request.md#create-string-to-sign "../../../IAM/latest/UserGuide/create-signed-request.md#create-string-to-sign")

Create a string that you will use as one of the input values to your
cryptographic hash function. The string, called the _string to
sign_, is a concatenation of the name of the hash algorithm, the
request date, a _credential scope_ string, and the
canonicalized request from the previous task. The _credential
scope_ string itself is a concatenation of date, region, and
service information.

- [Task 3: Calculate a signature](../../../IAM/latest/UserGuide/create-signed-request.md#calculate-signature "../../../IAM/latest/UserGuide/create-signed-request.md#calculate-signature")

Calculate a signature for your request by using a cryptographic hash function that accepts
two input strings, your string to sign and a _derived key_.
The derived key is calculated by starting with your secret access key and using
the credential scope string to create a series of hash-based message
authentication codes (HMAC-SHA256).

## Example signature calculation

The following example walks you through the details of creating a signature for [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") request. You can use this example as a reference to check
your own signature calculation method. Other reference calculations are included in the
[Request signature examples section](../../../IAM/latest/UserGuide/signature-v4-examples.md "../../../IAM/latest/UserGuide/signature-v4-examples.md") of the IAM User Guide.

You can use a GET or POST request to send requests to Amazon Redshift. The difference
between the two is that for the GET request your parameters are sent as query string
parameters. For the POST request they are included in the body of the request. The
example below shows a POST request.

The example assumes the following:

- The time stamp of the request is `Fri, 07 Dec 2012 00:00:00
GMT`.
- The endpoint is US East (Northern Virginia) Region,
  `us-east-1`.
  The general request syntax is:

```
https://redshift.us-east-1.amazonaws.com/
   ?Action=CreateCluster
   &ClusterIdentifier=examplecluster
   &MasterUsername=masteruser
   &MasterUserPassword=12345678Aa
   &NumberOfNode=2
   &NodeType=dc2.large
   &Version=2012-12-01
   &x-amz-algorithm=AWS4-HMAC-SHA256
   &x-amz-credential=AKIAIOSFODNN7EXAMPLE/20121207/us-east-1/redshift/aws4_request
   &x-amz-date=20121207T000000Z
   &x-amz-signedheaders=content-type;host;x-amz-date
```

The canonical form of the request calculated for [Task 1: Create a Canonical Request](#SignatureCalculationTask1 "#SignatureCalculationTask1")
is:

```
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-1.amazonaws.com
x-amz-date:20121207T000000Z

content-type;host;x-amz-date
55141b5d2aff6042ccd9d2af808fdf95ac78255e25b823d2dbd720226de1625d
```

The last line of the canonical request is the hash of the request body. The third line in
the canonical request is empty because there are no query parameters for this API.

The string to sign for [Task 2: Create a String to
Sign](#SignatureCalculationTask2 "#SignatureCalculationTask2") is:

```
AWS4-HMAC-SHA256
20121207T000000Z
20121207/us-east-1/redshift/aws4_request
06b6bef4f4f060a5558b60c627cc6c5b5b5a959b9902b5ac2187be80cbac0714
```

The first line of the _string to sign_ is the algorithm, the second
line is the time stamp, the third line is the _credential scope_, and
the last line is a hash of the canonical request from [Task 1: Create a Canonical Request](#SignatureCalculationTask1 "#SignatureCalculationTask1"). The
service name to use in the credential scope is `redshift`.

For [Task 3: Calculate a Signature](#SignatureCalculationTask3 "#SignatureCalculationTask3"), the derived
key can be represented as:

```
*derived key* = HMAC(HMAC(HMAC(HMAC("AWS4" + YourSecretAccessKey,"20121207"),"us-east-1"),"redshift"),"aws4_request")
```

The derived key is calculated as series of hash functions. Starting from the inner HMAC
statement in the formula above, you concatenate the phrase `AWS4` with your secret
access key and use this as the key to hash the data "us-east-1". The result of this
hash becomes the key for the next hash function.

After you calculate the derived key, you use it in a hash function that accepts two
input strings, your string to sign and the derived key. For example, if you use the
secret access key `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` and the string to sign given earlier,
then the calculated signature is as follows:

```
9a6b557aa9f38dea83d9215d8f0eae54100877f3e0735d38498d7ae489117920
```

The final step is to construct the `Authorization` header. For the
demonstration access key `AKIAIOSFODNN7EXAMPLE`, the header (with line
breaks added for readability) is:

```
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20121207/us-east-1/redshift/aws4_request,
SignedHeaders=content-type;host;x-amz-date,
Signature=9a6b557aa9f38dea83d9215d8f0eae54100877f3e0735d38498d7ae489117920
```
