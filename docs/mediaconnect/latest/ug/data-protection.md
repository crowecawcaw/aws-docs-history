# Data protection for AWS Elemental MediaConnect

You can protect your data using tools that are provided by AWS. AWS Elemental MediaConnect
can decrypt your incoming video (source) and encrypt your outgoing video (outputs and
entitlements).

You have three options for encrypting content in transit:

- **Static key encryption:** You can use this
  option to encrypt sources, outputs, and entitlements. You store your encryption
  key in AWS Secrets Manager, and then you give MediaConnect permission to obtain the
  encryption key from Secrets Manager.

Advantages: You have full control over storage of the encryption key for your
account. The key is stored in AWS Secrets Manager, where you can access it any
time.

Challenges: All parties (the owners of the source, the flow, any outputs, and
any entitlements) need the encryption key. If the content is shared using an
entitlement, both the originator and the subscriber must store the encryption
key in AWS Secrets Manager. If the encryption key changes, you must notify all parties of
the new key.

- **Secure Packager and Encoder Key Exchange (SPEKE):** You can use this option to
  encrypt content that is sent through an entitlement. You partner with a
  conditional access (CA) platform key provider who manages and provides
  encryption keys. Then you give Amazon API Gateway permission to act as a proxy between
  the CA platform key provider and your AWS account.

Advantages: The content originator has full control over access to the
encryption key. As the content originator, you partner with your CA platform key
provider who manages the encryption key, but you don't handle the key itself and
you don't share it with any other parties. Depending on the capabilities of your
key provider, this option allows you to assign time limitations to an encryption
key or revoke the key entirely. The subscriber doesn't need to set up
encryption. This information is automatically provided through the
entitlement.

Challenges: You must work with a third party (the key provider).

- **Secure Reliable Transport (SRT) password encryption:** You
  can use this option to encrypt sources and outputs when using
  SRT
  protocols.
  SRT protocols
  are
  highly available, low-latency
  protocols
  that
  are
  suitable for long-distance applications. You store your encryption password in
  AWS Secrets Manager, and then you give MediaConnect permission to obtain the encryption
  password from Secrets Manager.

Advantages: Uses 128/256 bit AES for encryption and decryption.
SRT
protocols
use
error correction to minimize packet loss. You have full control over storage of
the encryption password. The password is stored in AWS Secrets Manager, where you can
access it any time.

Challenges: Only usable with
SRT
protocols.
MediaConnect does not support source failover if you use
an
SRT
protocol.

###### Note

Encryption is supported only for entitlements, for sources that use the Zixi or
SRT
protocols, and for outputs that use the Zixi or
SRT
protocols.

###### Topics

- [Static key encryption in
  AWS Elemental MediaConnect](encryption-static-key.md "encryption-static-key.md")
- [SPEKE encryption in AWS Elemental MediaConnect](encryption-speke.md "encryption-speke.md")
- [SRT password encryption in
  AWS Elemental MediaConnect](encryption-srt-password.md "encryption-srt-password.md")
- [Internetwork traffic privacy](internetwork-traffic-privacy.md "internetwork-traffic-privacy.md")
