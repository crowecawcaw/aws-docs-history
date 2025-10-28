AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Editing an IAM role for Amazon Q Developer in chat applications

You can create new IAM roles in the Amazon Q Developer in chat applications console. You associate these roles with your chat channels or Amazon Chime webhooks. The
Amazon Q Developer in chat applications console does not allow editing of IAM roles, including any roles that you've already
created in the Amazon Q Developer in chat applications console.

###### Note

AWS requires that you use the IAM console to edit IAM roles. If you create
roles in the Amazon Q Developer in chat applications console, you must use the IAM console to edit them. This might
happen, for example, when you are using the Amazon Q Developer in chat applications service and a new release comes
out that supports new features.

Use the IAM console to edit Amazon Q Developer in chat applications roles. You can use the entire set of IAM console
features to specify permissions for your Amazon Q Developer in chat applications users.

**To edit roles**

1. Open the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Choose the configured client, and choose the name of the configured channel or webhook.
3. Choose a role to edit:

Channel role

    1. Choose the role you want to edit. When you choose a role, the IAM console opens, automatically showing role configuration page, with the Permissions tab displaying the selected role.


    ###### Note

    You can attach AWS managed policies and customer managed policies. Amazon Q Developer in chat applications
     roles support both types of IAM policies.
    2. Choose **Add permissions** and then select **Attach Policies**.

User roles

    1. Choose the **User role** tab.
    2. Choose **Edit**.


    ###### Note

    You can attach AWS managed policies and customer managed policies. Amazon Q Developer in chat applications
     roles support both types of IAM policies.
    3. Select a role.
    4. Choose **Selected role information**. The IAM console opens automatically showing role configuration page.
    5. Choose **Add permissions** and then select **Attach Policies**.

4.  Choose the name of the policy that you want. You can use the **Search** box to search for the policy by name or by a
    partial string of characters. For example, all IAM policies associated with
    Amazon Q Developer in chat applications include the character string **Chatbot** as
    part of the policy name.
5.  You can attach any of the following AWS managed policies to any role. You can also use
    these policies as templates to create your own policies.

        * **ReadOnlyAccess**
        * **CloudWatchReadOnlyAccess**
        * **AWSSupportAccess**
        * **AmazonQFullAccess**
        * **AIOpsOperator**

    The **ReadOnlyAccess** policy is automatically
    attached to any role that you create in the Amazon Q Developer in chat applications console. In the console, it appears as **Read-only command permissions** policy template.

If you want your users to be able to chat with Amazon Q Developer in natural language, attach the **AmazonQDeveloperAccess** policy. If administrator access is required, use the
**AmazonQFullAccess** policy. In the Amazon Q Developer in chat applications console, the **AmazonQFullAccess** policy appears as the **Amazon Q Permissions** policy template.

You can use these policies to create your own policies that are less permissive and
specify the resources their users can access. You can substitute these custom policies for
the ones listed here. 6. Choose each of the policies that you want to attach to the role and choose
**Attach policy**. If needed, use the Search box to locate
the policies you're looking for.

After you click **Attach policy**, the role's **Permissions** page opens and shows the change in the
**Permissions** list.

###### Note

For more information about the customer managed policies and AWS managed
policies described in this section, see [IAM
Policies for Amazon Q Developer in chat applications](chatbot-iam-policies.md "chatbot-iam-policies.md").

For more information about editing IAM policies, see [Editing IAM
Policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md"). Exercise caution at all times when editing policies, and avoid
overwriting existing customer managed policies.

## Managing IAM role

permissions for running commands in Amazon Q Developer in chat applications

With AWS Identity and Access Management (IAM), you can use _identity-based
policies_, which are JSON permissions policy documents, and attach them to
an _identity_, such as a user, role, or group.
These policies work with your guardrail policies to control what actions a user can
perform. Amazon Q Developer in chat applications provides the following IAM policies in the Amazon Q Developer in chat applications console that you can use to set up
AWS CLI commands support for chat channels. Those policies include:

- **ReadOnly command permissions**
- **Lambda-Invoke command permissions**
- **AWS Support command permissions**

You can use any or all of these policies, based on your organization's requirements.
To use them, create a new channel role in your channel configuration using the
Amazon Q Developer in chat applications console, and attach the policies there. You can also attach the policies to the Amazon Q Developer in chat applications
IAM roles using the IAM console. The policies simplify Amazon Q Developer in chat applications role configuration and
enable you to set up quickly.

You can use these IAM policies as templates to define your own policies. For
example, all policies described here use a wildcard ("\*") to apply the policy's permissions to
all resources:

```
               "Resource": [
                "*"
            ]
```

You can define custom permissions in a policy to limit actions to specific resources in your
AWS account. These are called _resource-based permissions_.
For more information on defining resources in a policy, see the section [IAM JSON Policy Elements:
Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _IAM User Guide_.

For more information on these policies, see [Configuring
an IAM Role for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md "editing-iam-roles-for-chatbot.md").

### Using the Amazon Q Developer in chat applications read-only command

permissions policy

The Amazon Q Developer in chat applications **ReadOnly Command Permissions** policy
controls access to several important AWS services, including IAM, AWS Security Token Service
(AWS STS), AWS Key Management Service (AWS KMS), and Amazon S3. It disallows all IAM operations when using
AWS commands in Microsoft Teams and Slack. When you use the **ReadOnly Command
Permissions** policy, you allow or deny the following permissions to
users who run commands in chat channels:

- IAM (Deny All)
- AWS KMS (Deny All)
- AWS STS (Deny All)
- Amazon Cognito (allows Read-Only, denies `GetSigningCertificate` commands)
- Amazon EC2 (allows Read-Only, denies `GetPasswordData`
  commands)
- Amazon Elastic Container Registry (Amazon ECR) (allows Read-Only, denies `GetAuthorizationToken` commands)
- Amazon GameLift Servers (allows Read-Only, denies requests for credentials and
  `GetInstanceAccess` commands)
- Amazon Lightsail (allows List, Read, denies several key pair operations and
  `GetInstanceAccess`)
- Amazon Redshift (denies `GetClusterCredentials` commands)
- Amazon S3 (allows Read-Only commands, denies `GetBucketPolicy` commands)
- AWS Storage Gateway (allows Read-Only, denies `DescribeChapCredentials`
  commands)

The **ReadOnly Command Permissions** policy JSON code is shown
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "iam:*",
 "kms:*",
 "sts:*",
 "cognito-idp:GetSigningCertificate",
 "ec2:GetPasswordData",
 "ecr:GetAuthorizationToken",
 "gamelift:RequestUploadCredentials",
 "gamelift:GetInstanceAccess",
 "lightsail:DownloadDefaultKeyPair",
 "lightsail:GetInstanceAccessDetails",
 "lightsail:GetKeyPair",
 "lightsail:GetKeyPairs",
 "redshift:GetClusterCredentials",
 "s3:GetBucketPolicy",
 "storagegateway:DescribeChapCredentials"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Using the Amazon Q Developer in chat applications Lambda-Invoke

policy

The Amazon Q Developer in chat applications **Lambda-Invoke Command Permissions**
policy allows users to invoke AWS Lambda functions in chat channels. This policy is
an AWS managed policy that is not specific to Amazon Q Developer in chat applications, though it appears in the
Amazon Q Developer in chat applications console.

By default, invoked Lambda functions can perform _any
operation_. You might need to define a more restrictive inline IAM policy that
allows permissions to invoke specific Lambda functions, such as functions specifically developed
for your DevOps team that only they should be able to invoke, and deny permissions to invoke
Lambda functions for any other purpose.

The following example shows the **Lambda-Invoke Command
Permissions** policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:invokeAsync",
 "lambda:invokeFunction"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

You can also define resource-based permissions to allow invoking of Lambda functions only
against specific resources, instead of the "\*" wildcard that applies the policy to all
resources. Always follow the IAM practice of granting only the permissions required for your
users to do their jobs.
