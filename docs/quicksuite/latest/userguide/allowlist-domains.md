# Allowlisting Amazon Quick Suite domains

If your end users are signing in to Amazon Quick Suite using AWS root (not recommended),
AWS Identity and Access Management (IAM), corporate Active Directory, or native Quick Suite credentials, make
sure to allow-list the following domains within your organization's network.

| User type                                                                           | Domain or domains to allow-list          |
| ----------------------------------------------------------------------------------- | ---------------------------------------- |
| Users who sign in directly through Amazon Quick Suite and Active Directory<br>users | `signin.aws` and `awsapps.com`           |
| AWS root user                                                                       | `signin.aws.amazon.com` and `amazon.com` |
| IAM users                                                                           | `signin.aws.amazon.com`                  |

###### Important

We strongly recommend that you don't use the AWS root user for your everyday tasks,
even the administrative ones. Instead, adhere to the best practice of using the root
user only to create your first IAM user. Then securely lock away the root user
credentials and use them to perform only a few account and service management tasks. For
more information, see [AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md") in the
_IAM User Guide_.
