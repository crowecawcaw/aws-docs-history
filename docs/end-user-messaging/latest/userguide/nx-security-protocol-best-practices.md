

# SMS protocol security best practices
<a name="nx-security-protocol-best-practices"></a>

Given the limitations of the SMS protocol, here are some industry best practices to consider depending on your use case and your own security assessments:
+ Choose a short time-to-live (TTL) for one-time passwords (OTP).
+ Block sending SMS messages to countries you do not do business in with AWS End User Messaging Protect configurations.
+ For sensitive information, refer your customer to a secure portal.
+ Use URL shorteners with caution to avoid the appearance of phishing or social engineering.
+ Keep message content concise and include only necessary information.

For channel-specific guidance on sending reliably and avoiding filtering, see [Best practices](nx-mms-scale-best-practices.md).