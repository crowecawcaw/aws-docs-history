

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Supported AWS regions for the AWS Partner Central Revenue Measurement API
<a name="revenue-measurement-regions"></a>

You can access the AWS Partner Central Revenue Measurement service from any AWS commercial region with the following end point.

```
partnercentral-prm.global.api.aws
```

## Signing requests with SigV4a
<a name="revenue-measurement-sigv4a"></a>

Because the revenue measurement service uses a global endpoint, requests are signed with *Signature Version 4a (SigV4a)*, an extension of SigV4 that supports signing with asymmetric cryptography, enabling signatures that are verifiable across multiple AWS Regions.

**Using the AWS SDK or CLI**

If you use an AWS SDK or the AWS CLI, SigV4a signing is handled automatically when you call the global endpoint. No additional configuration is required.

**Signing requests manually**

If you sign requests manually without an SDK, be aware of the following differences from standard SigV4:
+ SigV4a derives an Elliptic Curve Digital Signature Algorithm (ECDSA) keypair from your existing AWS secret access key, rather than using HMAC-based key derivation.
+ The credential scope uses `*` for the region component instead of a specific Region name, because the signature is valid across Regions.

For more information about how SigV4a works, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). For code examples of SigV4a signing, see the [sigv4a-signing-examples](https://github.com/aws-samples/sigv4a-signing-examples) project on GitHub.