# Walkthroughs that use policies to

manage access to your Amazon S3 resources

This topic provides the following introductory walkthrough examples for granting access to
Amazon S3 resources. These examples use the AWS Management Console to create resources (buckets, objects,
users) and grant them permissions. The examples then show you how to verify permissions
using the command line tools, so you don't have to write any code. We provide commands using
both the AWS Command Line Interface (AWS CLI) and the AWS Tools for Windows PowerShell.

- [Example 1: Bucket owner
  granting its users bucket permissions](example-walkthroughs-managing-access-example1.md "example-walkthroughs-managing-access-example1.md")

The IAM users you create in your account have no permissions by default. In this
exercise, you grant a user permission to perform bucket and object
operations.

- [Example 2: Bucket owner
  granting cross-account bucket permissions](example-walkthroughs-managing-access-example2.md "example-walkthroughs-managing-access-example2.md")

In this exercise, a bucket owner, Account A, grants cross-account permissions to another
AWS account, Account B. Account B then delegates those permissions to users in its
account.

- **Managing object permissions when the object and bucket owners are not the same**

The example scenarios in this case are about a bucket owner granting object permissions to
others, but not all objects in the bucket are owned by the bucket owner. What
permissions does the bucket owner need, and how can it delegate those permissions?

The AWS account that creates a bucket is called the _bucket
owner_. The owner can grant other AWS accounts permission to upload
objects, and the AWS accounts that create objects own them. The bucket owner has
no permissions on those objects created by other AWS accounts. If the bucket owner
writes a bucket policy granting access to objects, the policy doesn't apply to
objects that are owned by other accounts.

In this case, the object owner must first grant permissions to the bucket owner
using an object ACL. The bucket owner can then delegate those object permissions to
others, to users in its own account, or to another AWS account, as illustrated by
the following examples.

    + [Example 3: Bucket owner
     granting permissions to objects it does not own](example-walkthroughs-managing-access-example3.md "example-walkthroughs-managing-access-example3.md")


    In this exercise, the bucket owner first gets permissions from the object owner. The
     bucket owner then delegates those permissions to users in its own
     account.
    + [Example 4 - Bucket owner granting
     cross-account permission to objects it does not own](example-walkthroughs-managing-access-example4.md "example-walkthroughs-managing-access-example4.md")


    After receiving permissions from the object owner, the bucket owner can't delegate
     permission to other AWS accounts because cross-account delegation isn't
     supported (see [Permission delegation](access-policy-language-overview.md#permission-delegation "access-policy-language-overview.md#permission-delegation")). Instead, the bucket owner can
     create an IAM role with permissions to perform specific operations (such
     as get object) and allow another AWS account to assume that role. Anyone
     who assumes the role can then access objects. This example shows how a
     bucket owner can use an IAM role to enable this cross-account delegation.

## Before you try the example

walkthroughs

These examples use the AWS Management Console to create resources and grant permissions. To test
permissions, the examples use the command line tools, AWS CLI, and AWS Tools for Windows PowerShell, so you
don't need to write any code. To test permissions, you must set up one of these tools.
For more information, see [Setting up the tools for the
walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").

In addition, when creating resources, these examples don't use root user credentials of an
AWS account. Instead, you create an administrator user in these accounts to perform
these tasks.

### About using an administrator user to create resources

and grant permissions

AWS Identity and Access Management
(IAM) recommends not using the root user credentials of your
AWS account to make requests. Instead, create an IAM user or role, grant them
full access, and then use their credentials to make requests. We refer to this as an
administrative user or role. For more information, go to [AWS account root user credentials and IAM
identities](../../../general/latest/gr/root-vs-iam.md "../../../general/latest/gr/root-vs-iam.md") in the _AWS General Reference_ and [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

All example walkthroughs in this section use the administrator user credentials. If you
have not created an administrator user for your AWS account, the topics show you
how.

To sign in to the AWS Management Console using the user credentials, you must use the IAM user sign-In
URL. The [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") provides this URL for your AWS account. The topics
show you how to get the URL.
