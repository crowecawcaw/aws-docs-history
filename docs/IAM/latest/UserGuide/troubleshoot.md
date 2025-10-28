# Troubleshoot IAM

Use the information here to help you diagnose and fix common issues when you work with
AWS Identity and Access Management (IAM).

###### Issues

- [I can't sign in to my AWS
  account](#troubleshoot_general_cant-sign-in "#troubleshoot_general_cant-sign-in")
- [I lost my access keys](#troubleshoot_general_access-keys "#troubleshoot_general_access-keys")
- [Policy variables aren't
  working](#troubleshoot_general_policy-variables-dont-work "#troubleshoot_general_policy-variables-dont-work")
- [Changes that I make are not always
  immediately visible](#troubleshoot_general_eventual-consistency "#troubleshoot_general_eventual-consistency")
- [I am not authorized to
  perform: iam:DeleteVirtualMFADevice](#troubleshoot_general_access-denied-delete-mfa "#troubleshoot_general_access-denied-delete-mfa")
- [How do I securely create
  IAM users?](#troubleshoot_general_securely-create-iam-users "#troubleshoot_general_securely-create-iam-users")
- [Additional resources](#troubleshoot_general_resources "#troubleshoot_general_resources")
- [Troubleshoot access denied error
  messages](troubleshoot_access-denied.md "troubleshoot_access-denied.md")
- [Troubleshoot issues with the root user](troubleshooting_root-user.md "troubleshooting_root-user.md")
- [Troubleshoot IAM policies](troubleshoot_policies.md "troubleshoot_policies.md")
- [Troubleshoot Passkeys and FIDO Security Keys](troubleshoot_mfa-fido.md "troubleshoot_mfa-fido.md")
- [Troubleshoot IAM roles](troubleshoot_roles.md "troubleshoot_roles.md")
- [Troubleshoot IAM and Amazon EC2](troubleshoot_iam-ec2.md "troubleshoot_iam-ec2.md")
- [Troubleshoot IAM and Amazon S3](troubleshoot_iam-s3.md "troubleshoot_iam-s3.md")
- [Troubleshoot SAML federation with IAM](troubleshoot_saml.md "troubleshoot_saml.md")

## I can't sign in to my AWS

account

Verify that you have the correct credentials and that you are using the correct method to
sign in. For more information, see [Troubleshooting sign-in
issues](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md") in the _AWS Sign-In User Guide_.

## I lost my access keys

Access keys consist of two parts:

- **The access key identifier**. This is not a secret, and
  can be seen in the IAM console wherever access keys are listed, such as on the user
  summary page.
- **The secret access key**. This is provided when you
  initially create the access key pair. Just like a password, it **_cannot be retrieved later_**. If you lost
  your secret access key, then you must create a new access key pair. If you already have
  the [maximum number of access keys](reference_iam-quotas.md#reference_iam-quotas-entities "reference_iam-quotas.md#reference_iam-quotas-entities"),
  you must delete an existing pair before you can create another.

If you lose your secret access key, you must delete the access key and create a new one.
For more instructions, see [Update access keys](id-credentials-access-keys-update.md "id-credentials-access-keys-update.md").

## Policy variables aren't

working

If your policy variables are not working, one of the following errors has occurred:

**The date is wrong in the Version policy element.**

Verify that all policies that include variables include the following version number
in the policy: `"Version": "2012-10-17"`. Without the
correct version number, the variables are not replaced during evaluation. Instead, the
variables are evaluated literally. Policies that don't include variables still work when
you include the latest version number.

A `Version` policy element is different from a policy version. The
`Version` policy element is used within a policy and defines the version of
the policy language. A policy version is created when you modify a customer managed
policy in IAM. The changed policy doesn't overwrite the existing policy. Instead,
IAM creates a new version of the managed policy. To learn more about the
`Version` policy element see [IAM JSON policy elements:
Version](reference_policies_elements_version.md "reference_policies_elements_version.md"). To learn more about policy
versions, see [Versioning IAM policies](access_policies_managed-versioning.md "access_policies_managed-versioning.md").

**Variable characters are in the wrong letter case.**

Verify that your policy variables are in the right case. For details, see [IAM policy elements: Variables and tags](reference_policies_variables.md "reference_policies_variables.md").

## Changes that I make are not always

immediately visible

As a service that is accessed through computers in data centers around the world, IAM
uses a distributed computing model called [eventual consistency](https://wikipedia.org/wiki/Eventual_consistency "https://wikipedia.org/wiki/Eventual_consistency").
Any changes that
you make in IAM (or other AWS services), including [attribute-based access
control (ABAC)](introduction_attribute-based-access-control.md "introduction_attribute-based-access-control.md") tags, take time to become visible from all possible endpoints. Some
delay results from the time it takes to send data from server to server, replication zone to
replication zone, and Region to Region. IAM also uses caching to improve performance, but in
some cases this can add time. The change might not be visible until the previously cached data
times out.

You must design your global applications to account for these potential delays. Ensure
that they work as expected, even when a change made in one location is not instantly visible
at another. Such changes include creating or updating users, groups, roles, or policies. We
recommend that you do not include such IAM changes in the critical, high availability code
paths of your application. Instead, make IAM changes in a separate initialization or setup
routine that you run less frequently. Also, be sure to verify that the changes have been
propagated before production workflows depend on them.

For more information about how some other AWS services are affected by this, consult the
following resources:

- **Amazon DynamoDB**: [Read
  consistency](../../../amazondynamodb/latest/developerguide/HowItWorks.md "../../../amazondynamodb/latest/developerguide/HowItWorks.md") in the _DynamoDB Developer Guide_, and
  [Read Consistency](../../../amazondynamodb/latest/developerguide/HowItWorks.md "../../../amazondynamodb/latest/developerguide/HowItWorks.md") in
  the Amazon DynamoDB Developer Guide.
- **Amazon EC2**: [EC2 Eventual
  Consistency](../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency "../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency") in the _Amazon EC2 API Reference_.
- **Amazon EMR**: [Ensuring Consistency When Using Amazon S3 and Amazon EMR for ETL Workflows](https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/ "https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/") in the AWS
  Big Data Blog
- **Amazon Redshift**: [Managing Data Consistency](../../../redshift/latest/dg/managing-data-consistency.md "../../../redshift/latest/dg/managing-data-consistency.md") in
  the _Amazon Redshift Database Developer Guide_
- **Amazon S3**: [Amazon S3 Data Consistency
  Model](../../../AmazonS3/latest/userguide/Welcome.md#ConsistencyModel "../../../AmazonS3/latest/userguide/Welcome.md#ConsistencyModel") in the _Amazon Simple Storage Service User Guide_

## I am not authorized to

perform: iam:DeleteVirtualMFADevice

You might receive the following error when you attempt to assign or remove a virtual MFA
device for yourself or others:

```
User: arn:aws:iam::123456789012:user/Diego is not authorized to perform: `iam:DeleteVirtualMFADevice` on resource: arn:aws:iam::123456789012:mfa/Diego with an explicit deny
```

This could happen if someone previously began assigning a virtual MFA device to a user in
the IAM console and then cancelled the process. This creates a virtual MFA device for the
user in IAM but never assigns it to the user. Delete the existing virtual MFA device before
you create a new virtual MFA device with the same device name.

To fix this issue, an administrator should **not** edit
policy permissions. Instead, the administrator must use the AWS CLI or AWS API to delete the
existing but unassigned virtual MFA device.

###### To delete an existing but unassigned virtual MFA device

1. View the virtual MFA devices in your account.
   - AWS CLI: [`aws iam
list-virtual-mfa-devices`](../../../cli/latest/reference/iam/list-virtual-mfa-devices.md "../../../cli/latest/reference/iam/list-virtual-mfa-devices.md")
   - AWS API: [`ListVirtualMFADevices`](../APIReference/API_ListVirtualMFADevices.md "../APIReference/API_ListVirtualMFADevices.md")

2. In the response, locate the ARN of the virtual MFA device for the user you are trying
   to fix.
3. Delete the virtual MFA device.
   - AWS CLI: [`aws iam
delete-virtual-mfa-device`](../../../cli/latest/reference/iam/delete-virtual-mfa-device.md "../../../cli/latest/reference/iam/delete-virtual-mfa-device.md")
   - AWS API: [`DeleteVirtualMFADevice`](../APIReference/API_DeleteVirtualMFADevice.md "../APIReference/API_DeleteVirtualMFADevice.md")

## How do I securely create

IAM users?

If you have employees that require access to AWS, you might choose to create IAM users
or [use IAM Identity Center for authentication](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"). If you use
IAM, AWS recommends that you create an IAM user and securely communicate the credentials
to the employee. If you are not physically located next to your employee, use a secure
workflow to communicate credentials to employees.

Use the following secure workflow to create a new user in IAM:

1. [Create a new user](id_users_create.md "id_users_create.md") using the
   AWS Management Console. Choose to grant AWS Management Console access with a generated password. If necessary,
   select the **Users must create a new password at next sign-in** check
   box. Do not add a permissions policy to the user until after they have changed their
   password.
2. After the user is added, copy the sign-in URL, user name, and password for the new
   user. To view the password, choose **Show**.
3. Send the password to your employee using a secure communications method in your
   company, such as email, chat, or a ticketing system. Separately, provide your users with
   the IAM user console link and their user name. Tell the employee to confirm that they
   can sign in successfully before you will grant them permissions.
4. After the employee confirms, add the permissions that they need. As a security best
   practice, add a policy that requires the user to authenticate using MFA to manage their
   credentials. For an example policy, see [AWS: Allows
   MFA-authenticated IAM users to manage their own credentials on the Security
   credentials page](reference_policies_examples_aws_my-sec-creds-self-manage.md "reference_policies_examples_aws_my-sec-creds-self-manage.md").

## Additional resources

The following resources can help you troubleshoot as you work with AWS.

- **[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md")** – Use AWS CloudTrail to track a
  history of API calls made to AWS and store that information in log files. This helps you
  determine which users and accounts accessed resources in your account, when the calls were
  made, what actions were requested, and more. For more information, see [Logging IAM and AWS STS API calls
  with AWS CloudTrail](cloudtrail-integration.md "cloudtrail-integration.md").
- **[AWS Knowledge
  Center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/")** – Find FAQs and links to other resources to help you
  troubleshoot issues.
- **[AWS Support
  Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")** – Get technical support.
- **[AWS Premium Support
  Center](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")** – Get premium technical support.
