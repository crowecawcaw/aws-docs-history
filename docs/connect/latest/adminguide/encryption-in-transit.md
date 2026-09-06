

# Encryption in transit in Connect Customer
<a name="encryption-in-transit"></a>

All data exchanged with Connect Customer is protected in transit between the user’s web browser and Connect Customer using industry-standard TLS encryption. [Which version of TLS?](infrastructure-security.md#supported-version-tls)

External data is additionally encrypted while being processed by AWS KMS.

When Connect Customer integrates with AWS services, such as AWS Lambda, Amazon Kinesis, or Amazon Polly, data is always encrypted in transit using TLS.

When event data is forwarded from external applications to Connect Customer it is always encrypted in transit using TLS.