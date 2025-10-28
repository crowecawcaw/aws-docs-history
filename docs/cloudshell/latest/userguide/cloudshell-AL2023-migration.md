# AWS CloudShell migrating

from AL2 to
AL2023

AWS CloudShell, which was based on Amazon Linux 2 (AL2), has migrated to Amazon Linux 2023 (AL2023). For more
information about AL2023, see [What is Amazon Linux 2023 (AL2023)](../../../linux/al2023/ug/what-is-amazon-linux.md "../../../linux/al2023/ug/what-is-amazon-linux.md") in the
_Amazon Linux 2023 User Guide_.

With AL2023, you can continue to access your existing CloudShell environment with all
tools provided by CloudShell. For more information about available tools, see [Pre-installed software](vm-specs.md#pre-installed-software "vm-specs.md#pre-installed-software").

AL2023 provides several improvements to development tools, including newer versions of
packages such as Node.js 18 and Python 3.9.

###### Note

In AL2023, Python 2 is no longer shipped with your CloudShell
environment.

For more information about the key differences between AL2 and AL2023, see [Comparing Amazon Linux 2 and
Amazon Linux 2023](../../../linux/al2023/ug/compare-with-al2.md "../../../linux/al2023/ug/compare-with-al2.md") in the _Amazon Linux 2023 User Guide_.

If you've any questions, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/"). You can also search for answers and post questions in [AWS re:Post](https://repost.aws/tags/TA5ZaPf1NkT4uNitnWVitlyQ/aws-cloudshell "https://repost.aws/tags/TA5ZaPf1NkT4uNitnWVitlyQ/aws-cloudshell"). When
you enter AWS re:Post, you might be required to sign in to AWS.

## AWS CloudShell Migration FAQs

The following are answers to some common questions about the migration from AL2 to AL2023 with AWS CloudShell.

- [Will
  the
  migration to AL2023
  affect any of my other AWS resources,
  such
  as Amazon EC2 instances running on AL2?](#migration-effect "#migration-effect")
- [What are the packages that will be changed with the migration to AL2023?](#package-update "#package-update")
- [Can I opt-out from migration?](#migration-opt-out "#migration-opt-out")
- [Can I create a backup of my AWS CloudShell
  environment?](#migration-backup "#migration-backup")

### Will

the
migration to AL2023
affect any of my other AWS resources,
such
as Amazon EC2 instances running on AL2?

No service or resource other than your AWS CloudShell environment is affected by this migration.
This includes resources that you
might
have created or accessed from within AWS CloudShell. For example, if you have created an Amazon EC2
instance running on AL2 this will not be migrated to AL2023.

### What are the packages that have been changed with the

migration to AL2023?

AWS CloudShell environments currently include pre-installed software. To learn about the
complete list of pre-installed software, see [Pre-installed software](vm-specs.md#pre-installed-software "vm-specs.md#pre-installed-software"). AWS CloudShell will continue delivering these packages, with the
exception of Python 2. For the complete difference between the packages provided by AL2 and
AL2023, see [Comparing AL2 and AL2023](../../../linux/al2023/ug/compare-with-al2.md#package-changes "../../../linux/al2023/ug/compare-with-al2.md#package-changes"). For customers with specific package and version
requirements that will no longer be met after the migration to AL2023, we recommend reaching
out to AWS Support to submit a request.

### Can I opt-out from

migration?

No, you can't opt-out
from migration. AWS CloudShell environments are managed by AWS, therefore, all
the environments have been upgraded to AL2023.

### Can I create a backup of my AWS CloudShell environment?

AWS CloudShell will continue to persist the user home directory. For more information, see [Service quotas and restrictions for AWS CloudShell](limits.md#persistent-storage-limitations "limits.md#persistent-storage-limitations").
If you have any files or configurations stored in your home folder and if you want to create a backup for the same, complete [Step 6: Create a home directory backup](getting-started.md#home-directory-backup "getting-started.md#home-directory-backup").
