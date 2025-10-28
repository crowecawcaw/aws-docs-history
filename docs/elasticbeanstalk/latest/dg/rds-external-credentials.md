# Storing the Amazon RDS credentials in AWS Secrets Manager

This topic explains how AWS Secrets Manager can improve your security posture for credential retrieval with Elastic Beanstalk. It also provides references to specific
resources that can help you configure credentials for your Elastic Beanstalk application.

AWS Secrets Manager helps you improve your security posture, by providing the ability to store and retrieve encrypted credentials. Storing the credentials in
Secrets Manager helps avoid possible compromise by anyone who can inspect your application or the components related to it. Your code can make a runtime call to the
Secrets Manager service to retrieve credentials dynamically. Secrets Manager also offers features like client-side secret caching components for runtime languages,
which include Python, Go, and Java.

For more information, see the following topics in the _AWS Secrets Manager User Guide_.

- [How Amazon RDS uses
  AWS Secrets Manager](../../../secretsmanager/latest/userguide/integrating_how-services-use-secrets_RDS.md "../../../secretsmanager/latest/userguide/integrating_how-services-use-secrets_RDS.md")
- [Create an AWS Secrets Manager database secret](../../../secretsmanager/latest/userguide/create_database_secret.md "../../../secretsmanager/latest/userguide/create_database_secret.md")
- [Retrieve secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md")
