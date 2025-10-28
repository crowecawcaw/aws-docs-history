End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Signing Requests

If you're using a language for which AWS provides an SDK, we recommend that you use the SDK.
All of the AWS SDKs greatly simplify the process of signing requests and save you a
significant amount of time when compared with using the Elastic Transcoder API. In addition,
the SDKs integrate easily with your development environment and provide easy access to
related commands.

Elastic Transcoder requires that you authenticate every request you send by signing the request. To sign a request, you calculate a
digital signature using a cryptographic hash function, which returns a hash value based on the input. The input includes
the text of your request and your secret access key. The hash function returns a hash value that you include in the request
as your signature. The signature is part of the `Authorization` header of your request.

After receiving your request, Elastic Transcoder recalculates the signature using the same hash function and input that you used
to sign the request. If the resulting signature matches the signature in the request, Elastic Transcoder processes the request. Otherwise,
the request is rejected.

Elastic Transcoder supports authentication using [AWS Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
The process for calculating a signature can be broken into three tasks:

- [Task 1: Create a Canonical Request](../../../general/latest/gr/sigv4-create-canonical-request.md "../../../general/latest/gr/sigv4-create-canonical-request.md")

Create your HTTP request in canonical format as described in
[Task 1: Create a Canonical Request For Signature Version 4](../../../general/latest/gr/sigv4-create-canonical-request.md "../../../general/latest/gr/sigv4-create-canonical-request.md")
in the _Amazon Web Services General Reference_.

- [Task 2: Create a String to Sign](../../../general/latest/gr/sigv4-create-string-to-sign.md "../../../general/latest/gr/sigv4-create-string-to-sign.md")

Create a string that you will use as one of the input values to your cryptographic hash function.
The string, called the _string to sign_, is a concatenation of the name of the hash algorithm, the
request date, a _credential scope_ string, and the canonicalized request from the previous task.
The _credential scope_ string itself is a concatenation of date, region, and
service information.

For the `X-Amz-Credential` parameter, specify:

    + The code for the endpoint to which you're sending the request, for example, `us-east-1`.
     For a list of regions and endpoints for Elastic Transcoder, see the
     [Regions and Endpoints](../../../general/latest/gr/rande.md#elastictranscoder_region "../../../general/latest/gr/rande.md#elastictranscoder_region")
     chapter of the *Amazon Web Services General Reference*. When specifying the code for the endpoint, include only the part between
     `elastictranscoder.` and `.amazonaws.com`
    + `elastictranscoder` for the service abbreviation

For example:

`X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20130501/us-east-1/elastictranscoder/aws4_request`

- [Task 3: Create a Signature](../../../general/latest/gr/sigv4-calculate-signature.md "../../../general/latest/gr/sigv4-calculate-signature.md")

Create a signature for your request by using a cryptographic hash function that accepts two input strings:
your _string to sign_ and a _derived key_. The _derived key_ is
calculated by starting with your secret access key and using the _credential scope_ string
to create a series of hash-based message authentication codes (HMACs).
