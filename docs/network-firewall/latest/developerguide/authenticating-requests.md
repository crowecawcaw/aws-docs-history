# Authenticating requests

If you use a language that AWS provides an SDK for, we recommend that you use the SDK. All
the AWS SDKs greatly simplify the process of signing requests and save you a
significant amount of time when compared with using the Network Firewall API. In
addition, the SDKs integrate easily with your development environment and provide easy
access to related commands.

Network Firewall requires that you authenticate every request that you send by signing the request. To sign a request, you calculate a
digital signature using a cryptographic hash function, which returns a hash value based on the input. The input includes the
text of your request and your secret access key. The hash function returns a hash value that you include in the request
as your signature. The signature is part of the `Authorization` header of your request.

Network Firewall supports authentication using [AWS Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
Follow the process for signing your request at see the [Signing AWS requests with Signature Version 4](../../../general/latest/gr/sigv4_signing.md "../../../general/latest/gr/sigv4_signing.md") in the _AWS
General Reference_.

After receiving your request, Network Firewall recalculates the signature using the same
hash function and input that you used to sign the request. If the resulting signature
matches the signature in the request, Network Firewall processes the request. If not,
Network Firewall rejects the request.
