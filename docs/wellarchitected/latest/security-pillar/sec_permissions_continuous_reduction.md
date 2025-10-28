# SEC03-BP04 Reduce permissions continuously

As your teams determine what access is required, remove unneeded permissions and establish review processes to achieve least privilege permissions. Continually monitor and remove unused identities and permissions for both human and machine access.

**Desired outcome:** Permission policies should adhere to the least privilege principle. As job duties and roles become better defined, your permission policies need to be reviewed to remove unnecessary permissions. This approach lessens the scope of impact should credentials be inadvertently exposed or otherwise accessed without authorization.

**Common anti-patterns:**

- Defaulting to granting users administrator permissions.
- Creating policies that are overly permissive, but without full administrator privileges.
- Keeping permission policies after they are no longer needed.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

As teams and projects are just getting started, permissive permission policies might be used to inspire innovation and agility. For example, in a development or test environment, developers can be given access to a broad set of AWS services. We recommend that you evaluate access continuously and restrict access to only those services and service actions that are necessary to complete the current job. We recommend this evaluation for both human and machine identities. Machine identities, sometimes called system or service accounts, are identities that give AWS access to applications or servers. This access is especially important in a production environment, where overly permissive permissions can have a broad impact and potentially expose customer data.

AWS provides multiple methods to help identify unused users, roles, permissions, and credentials. AWS can also help analyze access activity of IAM users and roles, including associated access keys, and access to AWS resources such as objects in Amazon S3 buckets. AWS Identity and Access Management Access Analyzer policy generation can assist you in creating restrictive permission policies based on the actual services and actions a principal interacts with. [Attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") can help simplify permissions management, as you can provide permissions to users using their attributes instead of attaching permissions policies directly to each user.

### Implementation steps

- **Use [AWS Identity and Access Management Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md"):** IAM Access Analyzer helps identify resources in your organization and accounts, such as Amazon Simple Storage Service (Amazon S3) buckets or IAM roles that are [shared with an external entity](../../../IAM/latest/UserGuide/access-analyzer-getting-started.md "../../../IAM/latest/UserGuide/access-analyzer-getting-started.md").
- **Use [IAM Access Analyzer policy generation](../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md"):** IAM Access Analyzer policy generation helps you [create fine-grained permission policies based on an IAM user or role’s access activity](../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md#access-analyzer-policy-generation-howitworks "../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md#access-analyzer-policy-generation-howitworks").
- **Test permissions across lower
  environments before production:** Start by using
  the
  [less
  critical sandbox and development environments](../../../prescriptive-guidance/latest/choosing-git-branch-approach/understanding-the-devops-environments.md "../../../prescriptive-guidance/latest/choosing-git-branch-approach/understanding-the-devops-environments.md") to test
  the permissions required for various job functions using IAM Access Analyzer. Then, progressively tighten and validate
  these permissions across the testing, quality assurance, and
  staging environments before applying them to production. The
  lower environments can have more relaxed permissions
  initially, as service control policies (SCPs) enforce
  guardrails by limiting the maximum permissions granted.
- **Determine an acceptable timeframe and usage policy for IAM users and roles:** Use the [last accessed timestamp](../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data.md "../../../IAM/latest/UserGuide/access_policies_access-advisor-view-data.md") to [identify unused users and roles](https://aws.amazon.com/blogs/security/identify-unused-iam-roles-remove-confidently-last-used-timestamp/ "https://aws.amazon.com/blogs/security/identify-unused-iam-roles-remove-confidently-last-used-timestamp/") and remove them. Review service and action last accessed information to identify and [scope permissions for specific users and roles](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md"). For example, you can use last accessed information to identify the specific Amazon S3 actions that your application role requires and restrict the role’s access to only those actions. Last accessed information features are available in the AWS Management Console and programmatically allow you to incorporate them into your infrastructure workflows and automated tools.
- **Consider [logging data events in AWS CloudTrail](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md"):** By default, CloudTrail does not log data events such as Amazon S3 object-level activity (for example, `GetObject` and `DeleteObject`) or Amazon DynamoDB table activities (for example, `PutItem` and `DeleteItem`). Consider using logging for these events to determine what users and roles need access to specific Amazon S3 objects or DynamoDB table items.

## Resources

**Related documents:**

- [Grant least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege")
- [Remove unnecessary credentials](../../../IAM/latest/UserGuide/best-practices.md#remove-credentials "../../../IAM/latest/UserGuide/best-practices.md#remove-credentials")
- [What is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- [Working with Policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md")
- [Logging and monitoring DynamoDB](../../../amazondynamodb/latest/developerguide/MonitoringDynamoDB.md "../../../amazondynamodb/latest/developerguide/MonitoringDynamoDB.md")
- [Using CloudTrail event logging for Amazon S3 buckets and objects](../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md "../../../AmazonS3/latest/userguide/enable-cloudtrail-logging-for-s3.md")
- [Getting credential reports for your AWS account](../../../IAM/latest/UserGuide/id_credentials_getting-report.md "../../../IAM/latest/UserGuide/id_credentials_getting-report.md")

**Related videos:**

- [Become an IAM Policy Master in 60 Minutes or
  Less](https://youtu.be/YQsK4MtsELU "https://youtu.be/YQsK4MtsELU")
- [Separation of Duties, Least Privilege,
  Delegation, and CI/CD](https://youtu.be/3H0i7VyTu70 "https://youtu.be/3H0i7VyTu70")
- [AWS re:Inforce 2022 - AWS Identity and Access Management (IAM) deep dive](https://www.youtube.com/watch?v=YMj33ToS8cI "https://www.youtube.com/watch?v=YMj33ToS8cI")
