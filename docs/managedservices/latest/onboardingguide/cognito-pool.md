# Use AMS SSP to provision Amazon Cognito user pools in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Cognito user pools capabilities directly in your AMS managed account. Amazon Cognito user pools provide a secure user directory that scales to hundreds of millions of users. As a fully managed service,
Amazon Cognito user pools can be set up without any worries about standing up server infrastructure.
This service enables you to manage a pool of final users that you can use to integrate with your internal
applications. This service provides you an alternative to a customized database or a
directory of final users for web or mobile applications. At the same time, Amazon Cognito user pools provides the full set of
functionalities of a directory service like passwords policies, multi factor authentication,
password recovery and self-sign up into services. It also allows the application to federate the access in other
popular public services like OpenID, Facebook, Amazon or Google.

Amazon Cognito is divided into two main products. Amazon Cognito user pools and Amazon Cognito Identity Provider. This section focuses
on Amazon Cognito user pools, which provide access to other AWS services like Amazon S3 or DynamoDB.
The service allows you to use Amazon Cognito user pools, or a third party identity provider, to provide access to AWS services. It
also provides access to AWS services using anonymous guest access.
Because of the powerful nature of Amazon Cognito user pools, it would be managed manually on a case-by-case basis as an
operation manual service, in order to avoid potential security breaks into the account.
To learn more, see [Amazon Cognito User Pools](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md").

## Amazon Cognito user pools in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Cognito user pools in my AMS account?**

Implementation of Amazon Cognito user pools in AMS is a 2 step process:

1. Submit a Management | Other | Other | Create (ct-1e1xtak34nx76) change type and request
   the creation of the Amazon Cognito user pools in your AMS Account. Include the following information:
   - AWS Region.
   - Name for the Cognito User Pool.
   - If the you want to use the Amazon Simple Email Service (Amazon SES) to send messages and notifications instead of the default internal Cognito mail
     service, then the customer should provide an already validated email address for the Amazon SES Service in the
     account. This address will be used for the "From" and "REPLY-TO" fields of the message. They must also indicate
     the Region where Amazon SES was activated (us-east-1, eu-west-1 or us-west-2).
   - If the you want to use SMS messages for one-time passwords and verification, then the customer
     should indicate so.

2. Request user access by submitting a Management | AWS service | Self-provisioned service | Add
   change type (ct-1w8z66n899dct). This RFC provisions the following IAM roles to your account: `customer_cognito_admin_role` and
   `customer_cognito_importjob_role`. After it's provisioned in your account, you must onboard the role in your
   federation solution. These roles allow you to manage the Amazon Cognito user pools, manage your users and groups in the pool, create importjobs for
   users, modify the notification and subscription messages, associate applications to
   the user pool, self-manage adding federation services to the pool, and delete already created pools.

**Q: What are the restrictions to using Amazon Cognito user pools in my AMS account?**

You won't be able to create the Amazon Cognito user pools. That action requires
the creation of IAM roles to leverage services used by Amazon Cognito, like Amazon SES and Amazon Simple Notification Service (Amazon SNS).

**Q: What are the prerequisites or dependencies to using Amazon Cognito user pools in my AMS
account?**

If you want to use Amazon SES to send messages and notifications by email to your user pools, they should already activate the
Amazon SES service in the account, and already validate the email address that should be used in the "FROM" and "REPLY-TO" fields of the sent emails. For
more information about validating email address using Amazon SES, see
[Verifying Email Addresses in Amazon SES](../../../ses/latest/DeveloperGuide/verify-email-addresses.md "../../../ses/latest/DeveloperGuide/verify-email-addresses.md").
