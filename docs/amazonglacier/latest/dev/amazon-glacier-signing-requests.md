**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Signing Requests

Amazon Glacier requires that you authenticate every request you send by signing the
request. To sign a request, you calculate a digital signature using a cryptographic hash
function. A cryptographic hash is a function that returns a unique hash value based on the
input. The input to the hash function includes the text of your request and your secret
access key. The hash function returns a hash value that you include in the request as your
signature. The signature is part of the `Authorization` header of your request.

After receiving your request, Amazon Glacier recalculates the signature using the same
hash function and input that you used to sign the request. If the resulting signature
matches the signature in the request, Amazon Glacier processes the request. Otherwise, the
request is rejected.

Amazon Glacier supports authentication using [AWS
Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). The process for calculating a signature can be broken into
three tasks:

- [Task 1: Create a Canonical Request](../../../general/latest/gr/sigv4-create-canonical-request.md "../../../general/latest/gr/sigv4-create-canonical-request.md")

Rearrange your HTTP request into a canonical format. Using a canonical form is necessary
because Amazon Glacier uses the same canonical form when it recalculates a
signature to compare with the one you sent.

- [Task 2: Create a String to Sign](../../../general/latest/gr/sigv4-create-string-to-sign.md "../../../general/latest/gr/sigv4-create-string-to-sign.md")

Create a string that you will use as one of the input values to your cryptographic hash
function. The string, called the _string to
sign_, is a concatenation of the name of the hash algorithm, the
request date, a _credential scope_ string, and the
canonicalized request from the previous task. The _credential
scope_ string itself is a concatenation of date, AWS Region, and
service information.

- [Task 3: Create a Signature](../../../general/latest/gr/sigv4-calculate-signature.md "../../../general/latest/gr/sigv4-calculate-signature.md")

Create a signature for your request by using a cryptographic hash function that accepts
two input strings: your _string to sign_ and a
_derived key_. The _derived key_ is
calculated by starting with your secret access key and using the
_credential scope_ string to create a series of
hash-based message authentication codes (HMACs). Note that the hash function
used in this signing step is not the tree-hash algorithm used in Amazon Glacier APIs
that upload data.

###### Topics

- [Example Signature Calculation](#example-signature-calculation "#example-signature-calculation")
- [Calculating Signatures for the Streaming Operations](#signature-calculation-streaming "#signature-calculation-streaming")

## Example Signature Calculation

The following example walks you through the details of creating a signature for [Create Vault (PUT vault)](api-vault-put.md "api-vault-put.md"). The example could be used as a
reference to check your signature calculation method. For more information, see [Signing AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the
_IAM User Guide_.

The example assumes the following:

- The time stamp of the request is `Fri, 25 May 2012 00:24:53 GMT`.
- The endpoint is US East (N. Virginia) Region
  `us-east-1`.
  The general request syntax (including the JSON body) is:

```
PUT /-/vaults/examplevault HTTP/1.1
Host: glacier.us-east-1.amazonaws.com
Date: Fri, 25 May 2012 00:24:53 GMT
Authorization: `SignatureToBeCalculated`
x-amz-glacier-version: 2012-06-01
```

The canonical form of the request calculated for [Task 1: Create a Canonical Request](#SignatureCalculationTask1 "#SignatureCalculationTask1")
is:

```
PUT
/-/vaults/examplevault

host:glacier.us-east-1.amazonaws.com
x-amz-date:20120525T002453Z
x-amz-glacier-version:2012-06-01

host;x-amz-date;x-amz-glacier-version
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The last line of the canonical request is the hash of the request body. Also, note the
empty third line in the canonical request. This is because there are no query parameters
for this API.

The _string to sign_ for [Task 2: Create a String to Sign](#SignatureCalculationTask2 "#SignatureCalculationTask2") is:

```
AWS4-HMAC-SHA256
20120525T002453Z
20120525/us-east-1/glacier/aws4_request
5f1da1a2d0feb614dd03d71e87928b8e449ac87614479332aced3a701f916743
```

The first line of the _string to sign_ is the algorithm, the second line
is the time stamp, the third line is the _credential scope_, and the
last line is a hash of the canonical request from [Task 1: Create a Canonical Request](#SignatureCalculationTask1 "#SignatureCalculationTask1"). The
service name to use in the credential scope is `glacier`.

For [Task 3: Create a Signature](#SignatureCalculationTask3 "#SignatureCalculationTask3"), the _derived key_
can be represented as:

```
*derived key* = HMAC(HMAC(HMAC(HMAC("AWS4" + YourSecretAccessKey,"20120525"),"us-east-1"),"glacier"),"aws4_request")
```

If the secret access key, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`, is used, then the calculated
signature is:

```
3ce5b2f2fffac9262b4da9256f8d086b4aaf42eba5f111c21681a65a127b7c2a
```

The final step is to construct the `Authorization` header. For the demonstration
access key `AKIAIOSFODNN7EXAMPLE`, the header (with line breaks added for
readability) is:

```
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120525/us-east-1/glacier/aws4_request,
SignedHeaders=host;x-amz-date;x-amz-glacier-version,
Signature=3ce5b2f2fffac9262b4da9256f8d086b4aaf42eba5f111c21681a65a127b7c2a
```

## Calculating Signatures for the Streaming Operations

[Upload Archive (POST archive)](api-archive-post.md "api-archive-post.md") and [Upload Part (PUT uploadID)](api-upload-part.md "api-upload-part.md") are streaming operations
that require you to include an additional header `x-amz-content-sha256` when
signing and sending your request. The signing steps for the streaming operations are
exactly the same as those for other operations, with the addition of the streaming
header.

The calculation of the streaming header `x-amz-content-sha256` is based on the
SHA256 hash of the entire content (payload) that is to be uploaded. Note that this
calculation is different from the SHA256 tree hash ([Computing Checksums](checksum-calculations.md "checksum-calculations.md")). Besides trivial cases, the SHA 256 hash
value of the payload data will be different from the SHA256 tree hash of the payload
data.

If the payload data is specified as a byte array, you can use the following Java code
snippet to calculate the SHA256 hash.

```
public static byte[] computePayloadSHA256Hash2(byte[] payload) throws NoSuchAlgorithmException, IOException {
    BufferedInputStream bis =
       new BufferedInputStream(new ByteArrayInputStream(payload));
    MessageDigest messageDigest = MessageDigest.getInstance("SHA-256");
    byte[] buffer = new byte[4096];
    int bytesRead = -1;
    while ( (bytesRead = bis.read(buffer, 0, buffer.length)) != -1 ) {
        messageDigest.update(buffer, 0, bytesRead);
    }
    return messageDigest.digest();
}
```

Similarly, in C# you can calculate the SHA256 hash of the payload data as shown in the
following code snippet.

```
public static byte[] CalculateSHA256Hash(byte[] payload)
{
    SHA256 sha256 = System.Security.Cryptography.SHA256.Create();
    byte[] hash = sha256.ComputeHash(payload);

    return hash;
}
```

### Example Signature Calculation for Streaming API

The following example walks you through the details of creating a signature for [Upload Archive (POST archive)](api-archive-post.md "api-archive-post.md"), one of the two
streaming APIs in Amazon Glacier. The example assumes the following:

- The time stamp of the request is `Mon, 07 May 2012 00:00:00 GMT`.
- The endpoint is the US East (N. Virginia) Region,
  us-east-1.
- The content payload is a string "Welcome to Amazon Glacier."
  The general request syntax (including the JSON body) is shown in the
  example below. Note that the `x-amz-content-sha256` header is included.
  In this simplified example, the `x-amz-sha256-tree-hash` and
  `x-amz-content-sha256` are the same value. However, for archive
  uploads greater than 1 MB, this is not the
  case.

```
POST /-/vaults/examplevault HTTP/1.1
Host: glacier.us-east-1.amazonaws.com
Date: Mon, 07 May 2012 00:00:00 GMT
x-amz-archive-description: my archive
x-amz-sha256-tree-hash: SHA256 tree hash
x-amz-content-sha256: SHA256 payload hash
Authorization: `SignatureToBeCalculated`
x-amz-glacier-version: 2012-06-01
```

The canonical form of the request calculated for [Task 1: Create a Canonical Request](#SignatureCalculationTask1 "#SignatureCalculationTask1") is shown below. Note that the
streaming header `x-amz-content-sha256` is included with its value. This
means you must read the payload and calculate the SHA256 hash first and then compute
the signature.

```
POST
/-/vaults/examplevault

host:glacier.us-east-1.amazonaws.com
x-amz-content-sha256:726e392cb4d09924dbad1cc0ba3b00c3643d03d14cb4b823e2f041cff612a628
x-amz-date:20120507T000000Z
x-amz-glacier-version:2012-06-01

host;x-amz-content-sha256;x-amz-date;x-amz-glacier-version
726e392cb4d09924dbad1cc0ba3b00c3643d03d14cb4b823e2f041cff612a628
```

The remainder of the signature calculation follows the steps outlined in [Example Signature Calculation](#example-signature-calculation "#example-signature-calculation"). The `Authorization`
header using the secret access key `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` and the access
key `AKIAIOSFODNN7EXAMPLE` is shown below (with line breaks added for
readability):

```
Authorization=AWS4-HMAC-SHA256
Credential=AKIAIOSFODNN7EXAMPLE/20120507/us-east-1/glacier/aws4_request,
SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-glacier-version,
Signature=b092397439375d59119072764a1e9a144677c43d9906fd98a5742c57a2855de6
```
