# Requirements for C2PA manifests

To include C2PA manifests in your MediaConvert outputs, you need the following:

**MP4 container**

C2PA manifests are only supported for MP4 outputs.

**C2PA certificate**

A public certificate chain in PEM format stored in Secrets Manager. The certificate chain should include the signer's certificate and all intermediate certificates, but not the root certificate.

For information about obtaining C2PA-compatible certificates, see [https://opensource.contentauthenticity.org/docs/signing/get-cert](https://opensource.contentauthenticity.org/docs/signing/get-cert "https://opensource.contentauthenticity.org/docs/signing/get-cert")

For information about Secrets Manager, see the [Secrets Manager user guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

**AWS KMS key**

An AWS KMS key with ECDSA_SHA_256 signing capability. This key is used to sign the
C2PA manifest. Currently, MediaConvert only supports the ES256 (ECDSA with SHA-256) signing
algorithm.

For information about AWS KMS, see the [AWS KMS user guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

**IAM permissions**

Your MediaConvert service role must have permissions to access the specified Secrets Manager secret and AWS KMS key. Add the following permissions to your service role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:Sign",
 "Resource": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 },
 {
 "Effect": "Allow",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "arn:aws:secretsmanager:us-west-2:111122223333:secret:c2pa-certificate-abc123"
 }
 ]
}`

```

**Size limitations**

The C2PA manifest has a size limit of 32KB. If your certificate chain or other manifest components exceed this limit, the job will fail with an error.
