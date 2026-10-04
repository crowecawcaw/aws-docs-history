

# Encryption at rest
<a name="nx-security-encryption-rest"></a>

AWS End User Messaging encrypts all the data that it stores for you within the AWS boundary. This includes configuration data, registration data, and any data that you add into AWS End User Messaging. To encrypt your data, AWS End User Messaging uses internal AWS Key Management Service (AWS KMS) keys that the service owns and maintains on your behalf. We rotate these keys on a regular basis. For information about AWS KMS, see the [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/).