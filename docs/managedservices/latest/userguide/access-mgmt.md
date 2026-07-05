End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](SunsetPlan.md "SunsetPlan.md").

# Access management in AMS

Learn how to access resources by using SSH, or remote desktop protocol (RDP), and how to use bastions.

The AWS Managed Services (AMS) access management system is configured during onboarding. Only users with the AMS IAM user role,
federated through AMS, can access AMS resources in the account.

In addition to the federated trust, described next, AMS security groups are an
important element in private and public application access. For information about AMS security groups and how to change them, see
[Security groups](about-security-groups.md "about-security-groups.md").

###### Topics

- [What is Access Management?](what-is-access-mgmt.md "what-is-access-mgmt.md")
- [How and when to use the root user account in AMS](how-when-to-use-root.md "how-when-to-use-root.md")
- [AMS Advanced console and Amazon EC2 access](access-how-works-prereqs.md "access-how-works-prereqs.md")
- [Accessing the AWS Management console and the AMS console](access-console.md "access-console.md")
- [Accessing instances using bastions](using-bastions.md "using-bastions.md")
