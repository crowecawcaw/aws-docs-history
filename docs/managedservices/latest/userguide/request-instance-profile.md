# Restrict permissions with Amazon EC2 IAM instance profiles

An IAM instance profile is a container for an IAM role that you can use to pass role information to an Amazon EC2 instance when the instance starts.

Currently there is one AWS Managed Services (AMS) default instance profile,
`customer-mc-ec2-instance-profile`, that grants permissions to the applications running on the instance, not to users logging into the
instance. You might want to modify the default instance profile, or create a new one, if you want
to give an instance access to something, without granting other instances access as well. You can request a new IAM instance profile with the
Management | Applications | IAM instance profile | Create change type (ct-0ixp4ch2tiu04). When submitting the
RFC, you could fashion your own instance profile and include that as the InstanceProfileDescription, or you could just inform AMS (using the same field) of
what changes you want. Because this is a Manual CT, AMS must approve the change and will be in contact with you about it.

If you're unfamiliar with Amazon IAM policies, see
[Overview of IAM Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
for important information. There is also a good blog post,
[Demystifying Amazon EC2
Resource-Level Permissions](https://aws.amazon.com/blogs/security/demystifying-ec2-resource-level-permissions/ "https://aws.amazon.com/blogs/security/demystifying-ec2-resource-level-permissions/"). Note that AMS does not currently support Resource-based access control, but does support Resource-level
controls using IAM role policies (for an explanation of the difference, see
[AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").

**Single-Account Landing Zone AMS**:

To see a table of permissions that the default AMS IAM instance profile grants, go to
[EC2 IAM Instance Profile](defaults-user-role.md "defaults-user-role.md").
