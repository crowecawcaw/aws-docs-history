

# Identity and access management in Quick
<a name="identity"></a>


|  | 
| --- |
|    Applies to: Enterprise Edition and Standard Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

The following topics describe how to set up identity and access for Quick.
+ [Using IAM Identity Center](setting-up-sso.md)
+ [IAM federation](iam-federation.md)
+ [Using Active Directory with Amazon Quick Enterprise edition](aws-directory-service.md)
+ [Setting up IdP federation using IAM and Amazon Quick](external-identity-providers-setting-up-saml.md)
+ [Using multi-factor authentication (MFA) with Amazon Quick](using-multi-factor-authentication-mfa.md)

**Note**  
In the following AWS Regions, Amazon Quick accounts can only use [IAM Identity Center](setting-up-sso.md) for identity and access management:  
`af-south-1` Africa (Cape Town)
`ap-southeast-3` Asia Pacific (Jakarta)
`ap-southeast-5` Asia Pacific (Malaysia)
`eu-south-1` Europe (Milan)
`eu-south-2` Europe (Spain)
`eu-central-2` Europe (Zurich)
`il-central-1` Israel (Tel Aviv)
`me-central-1` Middle East (UAE)

The following sections help you configure the identity management method of your choice for Quick.

IAM permissions control access to some sections of the Amazon Quick administration console. The following table lists admin actions and whether they require IAM permissions.


| Admin action | IAM permissions required | 
| --- | --- | 
| **Account settings** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage assets** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Amazon Q** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage subscriptions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **SPICE capacity** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Index capacity** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage users (view)** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Manage users > Role groups** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage domains** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Mobile settings** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/negative_icon.png) No | 
| **Manage IP/VPC restrictions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage VPC connections** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Manage OAuth client applications** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **KMS keys** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **AWS resources** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Default access policy** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **IAM policy assignments** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **AWS actions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Extension access** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Custom permissions** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Configure SageMaker** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Brand customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Agent customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Email customization** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 
| **Quick Usage Metrics** | ![](http://docs.aws.amazon.com/quick/latest/userguide/images/success_icon.png) Yes | 

If you have the Amazon Quick admin role, you can perform actions that do not require IAM permissions. To perform actions that require IAM permissions, sign in to the AWS Management Console as an IAM principal with the appropriate `quicksight:*` permissions. You can also perform some admin actions programmatically through the Amazon Quick API. For a list of available API operations, see the [Amazon Quick API Reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

**Topics**
+ [Using IAM](iam.md)
+ [Using IAM Identity Center](setting-up-sso.md)
+ [IAM federation](iam-federation.md)
+ [Using Active Directory with Amazon Quick Enterprise edition](aws-directory-service.md)
+ [Using multi-factor authentication (MFA) with Amazon Quick](using-multi-factor-authentication-mfa.md)