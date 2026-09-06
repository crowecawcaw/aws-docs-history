

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Use AMS SSP to provision Amazon Quick in your AMS account
<a name="quicksight"></a>

Use AMS Self-Service Provisioning (SSP) mode to access Quick capabilities directly in your AMS managed account. Quick is a fast, cloud-powered business intelligence service that delivers insights to everyone in your organization. As a fully managed service, Quick lets you easily create and publish interactive dashboards that include machine learning (ML) insights. To learn more, see [Amazon Quick](https://aws.amazon.com/quicksight/).

## Quick in AWS Managed Services FAQ
<a name="set-quicksight-faqs"></a>

Common questions and answers:

**Q: How do I request access to Quick in my AMS account?**

Request access by submitting a Management \| AWS service \| Self-provisioned service \| Add change type (ct-1w8z66n899dct). This RFC provisions the following IAM role to your account: `customer_quicksight_console_admin_role`. After it's provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Quick in my AMS account?**
+ AWS resource settings on Quick won’t be accessible to you because of the IAM policy dependency. However, the AMS team enables each resource for you in response to your request to enable the service.
+ Resource access for individual users and groups are not supported in this model because this feature enables users to alter IAM permissions that could compromise AMS infrastructure.
+ The ability to invite IAM identities from within QuickSight is not supported due to the risk involved altering IAM objects.
+ Quick service offers two editions: Enterprise and Standard. Both provide a single sign-on (SSO) option that is supported on AMS. However, the Enterprise Edition has an option to integrate Quick with Active Directory (AD). Quick on AMS does not support integration with AD due to incompatibilities between AMS account structure and the Quick trust requirements.

**Q: What are the prerequisites or dependencies to using Quick in my AMS account?**
+ When AMS receives this RFC to add Quick, you are sent a service request for additional information; provide them the following:
  + Quick account name (for example, `{{CustomerName}}-quicksight`
  + Quick Edition (Standard versus Enterprise)
  + The AWS Region in which to enable the Quick service (defaults to your AMS AWS Region).
  + A notification email address for Quick account.
  + (Optional) The S3 bucket where data files to be analyzed are located.
  + The VPC and subnet IDs that connect to Quick support a feature to add a VPC connection, which enables private connectivity between Quick and resources inside the account.

An AMS operator performs the sign up process on your behalf and configures two QuickSight functionalities:
+  [Auto discovery](https://docs.aws.amazon.com/quicksight/latest/user/autodiscover-aws-data-sources.html) to data sources.
+  [VPC connections](https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html).

**Note**  
These actions need to be performed by an AMS operator because elevated IAM and VPC permissions are required during the sign-in process.