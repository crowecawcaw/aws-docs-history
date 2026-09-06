

# Resiliency design and Regional behavior
<a name="resiliency-regional-behavior"></a>

 The IAM Identity Center service is fully managed and uses highly available and durable AWS services, such as Amazon S3 and Amazon EC2. To ensure availability in the event of an Availability Zone disruption, IAM Identity Center operates across multiple Availability Zones. You can replicate your IAM Identity Center instance to additional Regions to maintain account access with already provisioned permissions in the event of a Regional disruption. For more information, see [Using IAM Identity Center across multiple AWS Regions](multi-region-iam-identity-center.md). 

You enable IAM Identity Center in your AWS Organizations management account. This is required for IAM Identity Center to provision, deprovision, and update roles across all your AWS accounts. When you enable IAM Identity Center, it is deployed to the AWS Region that is currently selected, referred to as the "primary Region". If you want to deploy to a specific AWS Region, change the Region selection before enabling IAM Identity Center because the primary Region cannot be changed after IAM Identity Center is enabled. 

IAM Identity Center supports most administrative functions only from the primary Region. This includes the connection to an external identity provider, synchronization of users and groups, and the creation and assignment of permission sets to users and groups. In contrast, the management of applications and their assignments must take place in the IAM Identity Center Region where the application was created.

**Note**  
Even if your IAM Identity Center is replicated to additional Regions, we recommend that you set up [AWS break-glass access](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.5-implement-break-glass-procedures.html). This helps you maintain AWS access for a small group of privileged users during events such as a service disruption in the external IdP. [Emergency access](emergency-access.md) is another option that uses identities from an external IdP instead of IAM users; however, it does not protect against a disruption in the external IdP. 

Although IAM Identity Center determines access from the Region in which you enable the service, AWS accounts are global. This means that after users sign in to IAM Identity Center, they can operate in any Region when they access AWS accounts through IAM Identity Center. Most AWS managed applications such as Amazon SageMaker AI, however, must be installed in a Region of your IAM Identity Center instance for users to authenticate and assign access to these applications. For information about Regional constraints when using an application with IAM Identity Center, see the documentation for the application and [Deploying and managing AWS managed applications across multiple AWS Regions](multi-region-application-use.md#multi-region-aws-managed-applications).

You can also use IAM Identity Center to authenticate and authorize access to SAML-based customer managed applications that are reachable through a public URL, regardless of the platform or cloud on which the application is built.

We do not recommend using [Account instances of IAM Identity Center](account-instances-identity-center.md) as a means to implement resiliency because they do not support AWS account access and because they create a second, isolated control point that isn't connected to your organization instance. 

## Designed for availability
<a name="availability-design"></a>

The following table provides the availability that IAM Identity Center is designed to achieve in a single AWS Region. These values don’t represent a Service Level Agreement or guarantee, but rather provide insight to the design goals. The availability percentages reference access to data or functions, and aren’t a reference to durability (for example, long term retention of data).



| Service component | Availability design goal | 
| --- | --- | 
| Data plane (including sign-in) | 99.95% | 
| Control plane | 99.90% | 