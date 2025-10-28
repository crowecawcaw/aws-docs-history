Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Granting permissions to

Amazon Redshift Serverless

To access other AWS services, Amazon Redshift Serverless requires permissions. Some Amazon Redshift
features require Amazon Redshift to access other AWS services on your behalf. For your
Amazon Redshift Serverless instance to act for you, supply security credentials to it. The
preferred method to supply security credentials is to specify an AWS Identity and Access Management (IAM) role.
You can also create an IAM role through the Amazon Redshift console and set it as the
default. For more information, see [Creating an IAM role as default for
Amazon Redshift](#serverless-default-iam-role "#serverless-default-iam-role").

To access other AWS services, create an IAM role with the appropriate permissions.
You also need to associate the role with Amazon Redshift Serverless. In addition, either specify
the Amazon Resource Name (ARN) of the role when you run the Amazon Redshift command or specify
the `default` keyword.

When changing the trust relationship for the IAM role in the [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), make
sure that it contains `redshift-serverless.amazonaws.com` and
`redshift.amazonaws.com` as principal service names. For information
about how to manage IAM roles to access other AWS services on your behalf, see [Authorizing Amazon Redshift to access AWS services on
your behalf](authorizing-redshift-service.md "authorizing-redshift-service.md").

## Creating an IAM role as default for

Amazon Redshift

When you create IAM roles through the Amazon Redshift console, Amazon Redshift programmatically
creates the roles in your AWS account. Amazon Redshift also automatically attaches
existing AWS managed policies to them. This approach means that you can stay
within the Amazon Redshift console and don't have to switch to the IAM console for role
creation.

The IAM role that you create through the console for your cluster has the
`AmazonRedshiftAllCommandsFullAccess` managed policy automatically
attached. This IAM role allows Amazon Redshift to copy, unload, query, and analyze data
for AWS resources in your IAM account. The related commands include COPY,
UNLOAD, CREATE EXTERNAL FUNCTION, CREATE EXTERNAL TABLE, CREATE EXTERNAL SCHEMA,
CREATE MODEL, and CREATE LIBRARY. For more information about how to create an IAM
role as default for Amazon Redshift, see Creating an IAM role as default for
Amazon Redshift.

To get started creating an IAM role as default for Amazon Redshift, open the AWS Management Console,
choose the Amazon Redshift console, and then choose **Redshift Serverless**
in the menu. From the Serverless dashboard you can create a new workgroup. The
creation steps walk you selecting an IAM role or configuring a new IAM
one.

When you have an existing Amazon Redshift Serverless workgroup and you want to configure
IAM roles for it, open the AWS Management Console. Choose the Amazon Redshift console, and then choose
**Redshift Serverless**. On the Amazon Redshift Serverless console,
choose **Namespace configuration** for an existing workgroup. Under
**Security and encryption**, you can edit the
permissions.

### Assigning IAM roles

to a namespace

Each IAM role is an AWS identity with permissions policies that determine
what actions each role can perform in
AWS.
The role is intended to be assumable by anyone who needs it. Additionally, each
namespace is a collection of objects, like tables and schemas, and users. When
you use Amazon Redshift Serverless, you can associate multiple IAM roles with your
namespace. This makes it easier to structure your permissions appropriately for
a collection of database objects, so roles can perform actions on both internal
and external data. For example, so you can run a `COPY` command in an
Amazon Redshift database to retrieve data from Amazon S3 and populate a Redshift table.

You can associate multiple roles to a namespace using the console, as
described previously in this section. You can also use the API command
`CreateNamespace`, or the CLI command
`create-namespace`. With the API or CLI command, you can assign
IAM roles to the namespace by populating `IAMRoles` with one or
more roles. Specifically, you add ARNs for specific roles to the
collection.

#### Managing

namespace associated IAM roles

On the AWS Management Console you can manage permissions policies for roles in
AWS Identity and Access Management. You can manage IAM roles for the namespace, using settings
available under **Namespace configuration**. For more
information about namespaces and their use in Amazon Redshift Serverless, see [Workgroups and namespaces](serverless-workgroup-namespace.md "serverless-workgroup-namespace.md").
