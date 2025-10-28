For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Encryption at rest

Timestream for InfluxDB encryption at rest provides enhanced security by encrypting all your data at rest using
encryption keys stored in [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/").
This functionality helps reduce the operational burden and complexity involved in protecting
sensitive data. With encryption at rest, you can build security-sensitive applications that meet
strict encryption compliance and regulatory requirements.

- Encryption is turned on by default on your Timestream for InfluxDB DB instance, and cannot be turned off. The
  industry standard AES-256 encryption algorithm is the default encryption algorithm
  used.
- AWS KMS is used for encryption at rest in Timestream for InfluxDB.
- You don't need to modify your DB instance client applications to use encryption.
