

# Amazon Neptune security best practices
<a name="best-practices-general-security"></a>

Use AWS Identity and Access Management (IAM) accounts to control access to Neptune API actions. Control actions that create, modify, or delete Neptune resources (such as DB instances, security groups, option groups, or parameter groups), and actions that perform common administrative actions (such as backing up and restoring DB instances).
+ Use temporary rather than persistent credentials whenever possible.
+ Assign an individual IAM account to each person who manages Amazon Relational Database Service (Amazon RDS) resources. Never use AWS account root users to manage Neptune resources. Create an IAM user for everyone, including yourself.
+ Grant each user the minimum set of permissions required to perform their duties.
+ Use IAM groups to effectively manage permissions for multiple users.
+ Rotate your IAM credentials regularly.

For more information about using IAM to access Neptune resources, see [Securing your Amazon Neptune database](security.md). For general information about working with IAM, see [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/Welcome.html) and [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html) in the *IAM User Guide*.