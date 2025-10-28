# Configuring the Amazon Q Developer CloudZero plugin

CloudZero is a cloud cost optimization platform that evaluates costs to improve cloud efficiency. If
you use CloudZero to monitor your AWS costs, you can use the CloudZero plugin in
Amazon Q Developer chat to access cost insights without leaving the AWS Management Console.

You can use the CloudZero plugin to understand your AWS costs, get cost optimization
insights, and track billing. After you receive a response, you can ask follow up
questions, such as the status or cost impact of CloudZero insights.

To configure the plugin, you provide authentication credentials from your CloudZero
account to enable a connection between Amazon Q and CloudZero. After you configure the
plugin, you can access CloudZero data by adding
`@cloudzero` to the beginning of your
question in Amazon Q chat.

###### Warning

CloudZero user permissions are not detected by the CloudZero plugin in Amazon Q. When an
administrator configures the CloudZero plugin in an AWS account, users with plugin
permissions in that account have access to any resources in the CloudZero account
retrievable by the plugin.

You can configure IAM policies to restrict which plugins users have access to. For
more information, see
[Configure user permissions](#cloudzero-configure-user-permissions "#cloudzero-configure-user-permissions").

## Prerequisites

### Add permissions

To configure plugins, the following administrator level permissions are required:

- Permissions to access the Amazon Q Developer console. For an example IAM policy
  that grants needed permissions, see [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").
- Permissions to configure plugins. For an example IAM policy that grants
  the needed permissions, see [Allow administrators to configure
  plugins](id-based-policy-examples-admins.md#id-based-policy-examples-admin-plugins "id-based-policy-examples-admins.md#id-based-policy-examples-admin-plugins").

### Acquire credentials

Before you begin, note the following information from your CloudZero account. These
authentication credentials will be stored in an AWS Secrets Manager secret when you
configure the plugin.

- **API key** – An access key that allows
  Amazon Q to call the CloudZero API to access your organization’s cost insights and billing
  information. You can find the API key in your CloudZero account settings. For more information, see the
  [Authorization](https://docs.cloudzero.com/reference/authorization "https://docs.cloudzero.com/reference/authorization") in the CloudZero documentation.

For more information on acquiring credentials from your CloudZero account, see
the [CloudZero
documentation](https://docs.cloudzero.com/docs/amazon-q-integration "https://docs.cloudzero.com/docs/amazon-q-integration").

## Secrets and service roles

### AWS Secrets Manager secret

When you configure the plugin, Amazon Q creates a new AWS Secrets Manager secret for you to store
CloudZero authentication credentials. Alternatively, you can use an existing secret
that you create yourself.

If you create a secret yourself, enter the API key as plaintext:

```
`your-api-key`
```

For more information about creating secrets, see
[Create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the
_AWS Secrets Manager User Guide_.

### Service roles

To configure the CloudZero plugin in Amazon Q Developer, you need to create a service
role that gives Amazon Q permission to access your Secrets Manager secret. Amazon Q
assumes this role to access the secret where your CloudZero credentials are stored.

When you configure the plugin in the AWS console, you have the option to create
a new secret or use an existing one. If you create a new secret, the associated
service role is created for you. If you use an existing secret and an existing
service role, make sure your service role contains the following permissions, and
has the following trust policy attached. The service role required depends on your
secret encryption method.

If your secret is encrypted with an AWS
managed KMS key, the following IAM service role is required:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-id`"
 ]
 }
 ]
}`

```

[Show moreShow less](# "#")
If your secret is encrypted with a customer
managed AWS KMS key, the following IAM service role is required:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-id`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "secretsmanager.`us-east-1`.amazonaws.com"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")
To allow Amazon Q to assume the service role, the service role needs the following
trust policy:

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "q.amazonaws.com"
 },
 "Action": ["sts:AssumeRole", "sts:SetContext"],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333",
 "aws:SourceArn": "arn:aws:codewhisperer:us-east-1:111122223333:profile/`profile-id`"
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")
For more information about service roles, see [Create a role to
delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _AWS Identity and Access Management User
Guide_.

## Configure the CloudZero plugin

You configure plugins in the Amazon Q Developer console. Amazon Q uses credentials stored in
AWS Secrets Manager to enable interactions with CloudZero.

To configure the CloudZero plugin, complete the following procedure:

1. Open the Amazon Q Developer console at [https://console.aws.amazon.com/amazonq/developer/home](https://console.aws.amazon.com/amazonq/developer/home "https://console.aws.amazon.com/amazonq/developer/home")
2. On the Amazon Q Developer console home page, choose **Settings**.
3. In the navigation bar, choose **Plugins**.
4. On the plugins page, choose the plus sign on the
   **CloudZero** panel. The plugin configuration page opens.
5. For **Configure AWS Secrets Manager**, choose either
   **Create a new secret** or **Use an
   existing secret**. The Secrets Manager secret is where your CloudZero authentication
   credentials will be stored.

If you create a new secret, enter the following information:

    1. For **CloudZero API key**, enter the API key for your CloudZero organization.
    2. A service role will be created that Amazon Q will use to access the
     secret where your CloudZero credentials are stored. Do not edit the
     service role that is created for you.If you use an existing secret, choose a secret from the **AWS Secrets Manager

secret\*\* dropdown menu. The secret should include the CloudZero authentication
credentials specified in the previous step.

For more information about the required credentials, see
[Acquire credentials](#acquire-cloudzero-credentials "#acquire-cloudzero-credentials"). 6. For **Configure AWS IAM service role**, choose either **Create new service role** or
**Use existing service role**.

###### Note

If you chose **Create a new secret** for step 6, you can’t use an existing
service role. A new role will be created for you.

If you create a new service role, a service role will be created that
Amazon Q will use to access the secret where your CloudZero credentials
are stored. Do not edit the service role that is created for you.

If you use an existing service role, choose a role from the dropdown
menu that appears. Make sure your service role has the permissions and
trust policy defined in [Service roles](#cloudzero-service-role "#cloudzero-service-role"). 7. Choose **Save configuration**. 8. After the CloudZero plugin panel appears in the **Configured plugins** section on the Plugins
page, users will have access to the plugin.

If you want to update the credentials for a plugin, you must delete your current
plugin and configure a new one. Deleting a plugin removes all previous
specifications. Any time you configure a new plugin, a new plugin ARN is generated.

## Configure user permissions

To use plugins, the following permissions are required:

- Permissions to chat with Amazon Q in the console. For an example IAM
  policy that grants permissions needed to chat, see
  [Allow users to chat with
  Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").
- The `q:UsePlugin` permission.

When you grant an IAM identity access to a configured CloudZero plugin, the identity
gains access to any resources in the CloudZero account retrievable by the plugin. CloudZero
user permissions are not detected by the plugin. If you want to control access to a
plugin, you can do so by specifying the plugin ARN in an IAM policy.

Each time you create or delete and re-configure a plugin, it is assigned a new ARN. If
you use a plugin ARN in a policy, it will need to be updated if you want to grant access
to the newly configured plugin.

To locate the CloudZero plugin ARN, go to the **Plugins** page in the Amazon Q Developer
console and choose the configured CloudZero plugin. On the plugin details page, copy the
plugin ARN. You can add this ARN to a policy to allow or deny access to the CloudZero
plugin.

If you create a policy to control access to CloudZero plugins, specify
`CloudZero` for the plugin provider in the policy.

For examples of IAM policies that control plugin access, see
[Allow users to chat with
plugins from one provider](id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type "id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type").

## Chat with the CloudZero plugin

To use the CloudZero plugin, enter `@cloudzero` at the beginning of a
question about CloudZero or your AWS application monitors and cases. Follow up questions
or responses to questions from Amazon Q must also include `@cloudzero`.

Following are some example use cases and associated questions you can ask to get the
most of out of the Amazon Q CloudZero plugin:

- **Learn about using CloudZero with AWS**
  – Ask about how CloudZero features work.
  Amazon Q might ask you for more information about what you’re trying to do to
  provide the best answer.
  - `@cloudzero how do I use CloudZero?`
  - `@cloudzero how do I get started with CloudZero?`

- **List cost insights**
  – Get a list of cost insights or find out more about a specific insight.
  - `@cloudzero list my top cost insights`
  - `@cloudzero tell me more about insight <insight
ID>`

- **Get billing information**
  – Ask the Amazon Q CloudZero plugin about your AWS billing information.
  - `@cloudzero what were my AWS costs for December 2024?`
