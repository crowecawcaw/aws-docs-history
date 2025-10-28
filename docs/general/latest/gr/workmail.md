# Amazon WorkMail endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name           | Region    | Service                          | Endpoint                                                                              |
| --------------------- | --------- | -------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (N. Virginia) | us-east-1 | Amazon WorkMail SDK              | https://workmail.us-east-1.amazonaws.com                                              |
| US East (N. Virginia) | us-east-1 | Amazon WorkMail Message Flow SDK | https://workmailmessageflow.us-east-1.amazonaws.com                                   |
| US West (Oregon)      | us-west-2 | Amazon WorkMail SDK              | https://workmail.us-west-2.amazonaws.com                                              |
| US West (Oregon)      | us-west-2 | Amazon WorkMail Message Flow SDK | https://workmailmessageflow.us-west-2.amazonaws.com                                   |
| Europe (Ireland)      | eu-west-1 | Amazon WorkMail SDK              | https://workmail.eu-west-1.amazonaws.com                                              |
| Europe (Ireland)      | eu-west-1 | Amazon WorkMail Message Flow SDK | https://workmailmessageflow.eu-west-1.amazonaws.com                                   | ## Email protocols endpoints                                                                                                                                                           |
| Region Name           | Region    | Service                          | Endpoint                                                                              |
| ---                   | ---       | ---                              | ---                                                                                   |
| US East (N. Virginia) | us-east-1 | Autodiscover                     | https://autodiscover-service.mail.us-east-1.awsapps.com/autodiscover/autodiscover.xml |
| US East (N. Virginia) | us-east-1 | Exchange web services (EWS)      | https://ews.mail.us-east-1.awsapps.com/EWS/Exchange.asmx                              |
| US East (N. Virginia) | us-east-1 | Exchange ActiveSync (EAS)        | https://mobile.mail.us-east-1.awsapps.com/Microsoft-Server-ActiveSync                 |
| US East (N. Virginia) | us-east-1 | IMAP over SSL/TLS (IMAPS)        | imap.mail.us-east-1.awsapps.com:993                                                   |
| US East (N. Virginia) | us-east-1 | SMTP over SSL/TLS (SMTPS)        | smtp.mail.us-east-1.awsapps.com:465                                                   |
| US West (Oregon)      | us-west-2 | Autodiscover                     | https://autodiscover-service.mail.us-west-2.awsapps.com/autodiscover/autodiscover.xml |
| US West (Oregon)      | us-west-2 | Exchange web services (EWS)      | https://ews.mail.us-west-2.awsapps.com/EWS/Exchange.asmx                              |
| US West (Oregon)      | us-west-2 | Exchange ActiveSync (EAS)        | https://mobile.mail.us-west-2.awsapps.com/Microsoft-Server-ActiveSync                 |
| US West (Oregon)      | us-west-2 | IMAP over SSL/TLS (IMAPS)        | imap.mail.us-west-2.awsapps.com:993                                                   |
| US West (Oregon)      | us-west-2 | SMTP over SSL/TLS (SMTPS)        | smtp.mail.us-west-2.awsapps.com:465                                                   |
| Europe (Ireland)      | eu-west-1 | Autodiscover                     | https://autodiscover-service.mail.eu-west-1.awsapps.com/autodiscover/autodiscover.xml |
| Europe (Ireland)      | eu-west-1 | Exchange web services (EWS)      | https://ews.mail.eu-west-1.awsapps.com/EWS/Exchange.asmx                              |
| Europe (Ireland)      | eu-west-1 | Exchange ActiveSync (EAS)        | https://mobile.mail.eu-west-1.awsapps.com/Microsoft-Server-ActiveSync                 |
| Europe (Ireland)      | eu-west-1 | IMAP over SSL/TLS (IMAPS)        | imap.mail.eu-west-1.awsapps.com:993                                                   |
| Europe (Ireland)      | eu-west-1 | SMTP over SSL/TLS (SMTPS)        | smtp.mail.eu-west-1.awsapps.com:465                                                   | ## Service quotas For more information, see [Amazon WorkMail Quotas](../../../workmail/latest/adminguide/workmail_limits.md "../../../workmail/latest/adminguide/workmail_limits.md"). |
