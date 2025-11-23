# Password

management for SRT password encryption

In AWS Elemental MediaConnect, you can use SRT password encryption to secure content in
sources, outputs and router I/O. To use this method, you store an SRT password as a
_secret_ in AWS Secrets Manager, and you give AWS Elemental MediaConnect
permission to access the secret. Secrets Manager keeps your password secure, allowing it
be accessed only by entities that you specify in an AWS Identity and Access Management (IAM)
policy.

With SRT password encryption, all participants (the owner of the source, the
flow, the outputs and the router I/O) need the SRT password.

For more information, see [Setting up SRT
password encryption](encryption-srt-password-set-up.md "encryption-srt-password-set-up.md").
