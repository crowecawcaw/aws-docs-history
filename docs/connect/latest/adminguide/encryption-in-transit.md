# Encryption in transit in Amazon Connect

All data exchanged with Amazon Connect is protected in transit between the user’s web browser
and Amazon Connect using industry-standard TLS encryption. [Which version of TLS?](infrastructure-security.md#supported-version-tls "infrastructure-security.md#supported-version-tls")

External data is additionally encrypted while being processed by AWS KMS.

When Amazon Connect integrates with AWS services, such as AWS Lambda, Amazon Kinesis, or Amazon Polly, data
is always encrypted in transit using TLS.

When event data is forwarded from external applications to Amazon Connect it is always
encrypted in transit using TLS.
