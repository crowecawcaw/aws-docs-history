

# About member accounts
<a name="member-accounts"></a>

Member accounts are the accounts through which your users perform their AWS workloads. AWS Control Tower member accounts can be created and customized by various methods, including automated methods. In some cases, you can bring existing AWS accounts into AWS Control Tower. When member accounts are created or enrolled, they must exist inside an organizational unit (OU) that was created in the AWS Control Tower console, or registered with AWS Control Tower. For more information, see these related topics:
+ [Methods of provisioning](https://docs.aws.amazon.com/controltower/latest/userguide/methods-of-provisioning.html)
+ [Provision and manage accounts with Account Factory](account-factory.md)
+ [Automate tasks in AWS Control Tower](automating-tasks.md)
+ [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md)
+ [Provision accounts with AWS Control Tower Account Factory for Terraform (AFT)](taf-account-provisioning.md)
+ [AWS Organizations Terminology and Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*.

**Accounts and controls**  
Member accounts can be *enrolled* in AWS Control Tower, or they can be *unenrolled*. Controls apply differently to enrolled and unenrolled accounts, and controls may apply to accounts in nested OUs based on inheritance.

For information about member account resources that AWS Control Tower allocates, see [Resource Considerations for Account Factory](account-factory-considerations.md).