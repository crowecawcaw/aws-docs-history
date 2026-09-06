

# Organization and account instances of IAM Identity Center
<a name="identity-center-instances"></a>

An instance is a single deployment of IAM Identity Center. There are two types of instances available for IAM Identity Center: *organization instances* and *account instances*.
+ Organization instance (recommended)

  An instance of IAM Identity Center that you enable in the AWS Organizations management account. Organization instances support all features of IAM Identity Center. We recommend that you deploy an organization instance rather than account instances to minimize the number of management points. 
+ Account instance

  An instance of IAM Identity Center that is bound to a single AWS account, and that is visible only within the AWS account and AWS Region in which it is enabled. Use an account instance for simpler, single-account scenarios. You can enable an account instance from either of the following: 
  + An AWS account that isn't managed by AWS Organizations
  + A member account in AWS Organizations

## AWS account types that can enable IAM Identity Center
<a name="identity-center-instances-account-types"></a>

To enable IAM Identity Center, sign in to the AWS Management Console by using one of the following credentials, depending on the instance type you want to create:
+ **Your AWS Organizations management account (recommended)** – Required to create an [organization instance](organization-instances-identity-center.md) of IAM Identity Center. Use an organization instance for multi-account permissions and application assignments across the organization.
+ **Your AWS Organizations member account** – Use to create an [account instance](account-instances-identity-center.md) of IAM Identity Center to enable application assignments within that member account. One or more accounts with a member level instance can exist in an organization.
+ **A standalone AWS account** – Use to create an [organization instance](organization-instances-identity-center.md) or [account instance](account-instances-identity-center.md) of IAM Identity Center. The standalone AWS account isn't managed by AWS Organizations. You can associate only one instance of IAM Identity Center with a standalone AWS account and use that instance for application assignments within that standalone AWS account.

Use the following table to compare the capabilities provided by the instance type:


| Capability | Instance in the AWS Organizations management account (recommended) | Instance in a member account | Instance in a standalone AWS account | 
| --- | --- | --- | --- | 
| Manage users |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes | 
| AWS access portal for single-sign on access to your AWS managed applications |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes | 
| OAuth 2.0 (OIDC) customer managed applications |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png)Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png)Yes | 
| Multi-account permissions |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 
| AWS access portal for single-sign on access to your AWS accounts |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 
| SAML 2.0 customer managed applications |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 
| Delegated administrator can manage instance |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 
| Encryption at rest using a customer-managed KMS key |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 
| Replicating IAM Identity Center to additional Regions |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-yes.png) Yes |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No |  ![](http://docs.aws.amazon.com/singlesignon/latest/userguide/images/icon-no.png) No | 

For more information about AWS managed applications and IAM Identity Center, see [AWS managed applications that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md).

**Topics**
+ [AWS account types that can enable IAM Identity Center](#identity-center-instances-account-types)
+ [Organization instances of IAM Identity Center](organization-instances-identity-center.md)
+ [Account instances of IAM Identity Center](account-instances-identity-center.md)
+ [Delete your IAM Identity Center instance](delete-config.md)