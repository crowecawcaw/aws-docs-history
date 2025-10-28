# Password

management for SRT password encryption

In AWS Elemental MediaConnect, you can use SRT password encryption to secure content in
sources and outputs. To use this method, you store an SRT password as a
_secret_ in AWS Secrets Manager, and you give AWS Elemental MediaConnect
permission to access the secret. Secrets Manager keeps your password secure, allowing it
be accessed only by entities that you specify in an AWS Identity and Access Management (IAM)
policy.

With SRT password encryption, all participants (the owner of the source, the
flow, and any outputs) need the SRT password.

For more information, see [Setting up SRT
password encryption](encryption-srt-password-set-up.md "encryption-srt-password-set-up.md").
