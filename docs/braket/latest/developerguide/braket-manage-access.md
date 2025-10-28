# Managing access to Amazon Braket

This chapter describes the permissions that are required to run
Amazon Braket, or to restrict the access of specific users and roles. You can grant (or deny) the
required permissions to any user or role in your account. To do so, attach the appropriate
Amazon Braket policy to that user or role in your account as described in the following
sections.

As a prerequisite, you must [enable Amazon Braket](braket-enable-overview.md "braket-enable-overview.md"). To enable Braket, be sure to sign in as a user or role
that has (1) administrator permissions or (2) is assigned the **AmazonBraketFullAccess** policy and has permissions to create Amazon Simple Storage Service (Amazon S3)
buckets.

###### In this section:

- [Amazon Braket resources](#resources "#resources")
- [Notebooks and roles](#notebooks-and-roles "#notebooks-and-roles")
- [AWS managed policies for Amazon Braket](security-iam-aws-managed-policies.md "security-iam-aws-managed-policies.md")
- [Restrict user access to certain devices](restrict-access.md "restrict-access.md")
- [Restrict user access to certain notebook instances](restrict-access-notebook-instances.md "restrict-access-notebook-instances.md")
- [Restrict user access to certain S3 buckets](restrict-access-s3-buckets.md "restrict-access-s3-buckets.md")

## Amazon Braket resources

Braket creates one type of resource: the _quantum-task_
resource. The AWS Resource Name (ARN) for this resource type is as follows:

- **Resource Name:**
  _AWS::Service::Braket_
- **ARN Regex:**
  _arn:${Partition}:braket:${Region}:${Account}:quantum-task/${RandomId}_

## Notebooks and roles

You can use the noteboook resource type in Braket. A notebook is an Amazon SageMaker AI
resource that Braket is able to share. To use a notebook with Braket, you must
specify an IAM role with a name that begins with
`AmazonBraketServiceSageMakerNotebook`.

To create a notebook, you must use a role with admin permissions or that has the
following inline policy attached to it.

To create the role, follow the steps given in the [Create a notebook](braket-get-started-create-notebook.md "braket-get-started-create-notebook.md") page or have your administrator create it for you. Ensure
that the **AmazonBraketFullAccess** policy is
attached.

After you've created the role, you can reuse that role for all notebooks you launch in
the future.
