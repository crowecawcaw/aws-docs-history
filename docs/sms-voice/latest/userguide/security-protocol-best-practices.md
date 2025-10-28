# SMS protocol security best practices

Given the limitations of the SMS protocols, here are some industry best practices to consider depending on your use case and your own security assessments:

- Choose a short time-to-live (TTL) for one time passwords (OTP).
- Block sending SMS messages to countries you don't do business in with AWS End User Messaging SMS Protect configurations.
- For sensitive information refer your customer to a secure portal.
- Use URL shorteners with caution to avoid the appearance of phishing or social
  engineering.
- Keep message content concise and include only necessary information.
  For more information on the best practices of creating and sending SMS and MMS messages, see [SMS and MMS best practices](best-practices.md#best-practices-sms "best-practices.md#best-practices-sms").
