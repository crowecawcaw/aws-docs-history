

# Encryption in transit
<a name="nx-security-encryption-transit"></a>

AWS End User Messaging uses HTTPS and Transport Layer Security (TLS) 1.2 to communicate with your clients and applications. To communicate with other AWS services, AWS End User Messaging uses HTTPS and TLS 1.2. In addition, when you create and manage AWS End User Messaging resources by using the console, an AWS SDK, or the AWS Command Line Interface, all communications are secured using HTTPS and TLS 1.2.

When you use AWS End User Messaging to send an SMS message to an external mobile device, your data is transferred outside the AWS boundary through the SMS protocol. The SMS protocol has several inherent limitations, such as a lack of end-to-end encryption, that may be relevant for your use case. For more information about the limitations of SMS and security best practices, see [SMS protocol security considerations](nx-security-protocol-considerations.md) and [SMS protocol security best practices](nx-security-protocol-best-practices.md).