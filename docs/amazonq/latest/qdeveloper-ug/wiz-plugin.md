# Configuring the Amazon Q Developer Wiz plugin

Wiz is a cloud security platform that provides security posture management, risk
assessment and prioritization, and vulnerability management. If you use Wiz to evaluate and
monitor your AWS applications, you can use the plugin in Amazon Q chat to access insights
from Wiz without leaving the AWS Management Console.

You can use the plugin to identify and retrieve Wiz issues, assess your riskiest assets,
and understand vulnerabilities or exposures. After you receive a response, you can ask
follow up questions, including how to remediate an issue.

To configure the plugin, you provide authentication credentials from your Wiz account to
enable a connection between Amazon Q and Wiz. After you configure the plugin, you can
access Wiz metrics by adding `@wiz` to the beginning of your question in Amazon Q
chat.

###### Warning

Wiz user permissions are not detected by the Wiz plugin in Amazon Q. When an
administrator configures the Wiz plugin in an AWS account, users with plugin
permissions in that account have access to any resources in the Wiz account retrievable
by the plugin.

You can configure IAM policies to restrict which plugins users have access to. For
more information, see
[Configure user permissions](#wiz-configure-user-permissions "#wiz-configure-user-permissions").

## Prerequisites

### Add permissions

To configure plugins, the following administrator level permissions are required:

- Permissions to access the Amazon Q Developer console. For an example IAM policy
  that grants needed permissions, see [Allow administrators to use the Amazon Q Developer console](id-based-policy-examples-admins.md#q-admin-setup-admin-users "id-based-policy-examples-admins.md#q-admin-setup-admin-users").
- Permissions to configure plugins. For an example IAM policy that grants
  the needed permissions, see [Allow administrators to configure
  plugins](id-based-policy-examples-admins.md#id-based-policy-examples-admin-plugins "id-based-policy-examples-admins.md#id-based-policy-examples-admin-plugins").

### Acquire credentials

Before you begin, note the following information from your Wiz account. These
authentication credentials will be stored in an AWS Secrets Manager secret when you
configure the plugin.

- **API endpoint URL** – The URL where
  you access Wiz. For example, `https://api.us1.app.Wiz.io/graphql`. For
  more information, see
  [API
  endpoint URL](https://win.wiz.io/reference/prerequisites#api-endpoint-url "https://win.wiz.io/reference/prerequisites#api-endpoint-url") in the Wiz documentation.
- **Client ID and Client secret** –
  Credentials that allow Amazon Q to call Wiz APIs to access your application.
  For more information, see
  [Client ID and Client secret](https://win.wiz.io/reference/prerequisites#client-id-and-client-secret "https://win.wiz.io/reference/prerequisites#client-id-and-client-secret") in the Wiz
  documentation.

## Secrets and service roles

### AWS Secrets Manager secret

When you configure the plugin, Amazon Q creates a new AWS Secrets Manager secret for you to store
Wiz authentication credentials. Alternatively, you can use an existing secret
that you create yourself.

If you create a secret yourself, make sure it includes the following credentials
and uses the following JSON format:

```
{
   "ClientId": "`<your-client-id>`",
   "ClientSecret": "`<your-client-secret>`"
}
```

For more information about creating secrets, see
[Create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the
_AWS Secrets Manager User Guide_.

### Service roles

To configure the Wiz plugin in Amazon Q Developer, you need to create a service
role that gives Amazon Q permission to access your Secrets Manager secret. Amazon Q
assumes this role to access the secret where your Wiz credentials are stored.

When you configure the plugin in the AWS console, you have the option to create a new
secret or use an existing one. If you create a new secret, the associated service role
is created for you. If you use an existing secret and an existing service role, make
sure your service role contains these permissions, and has the following trust policy attached. The service role required depends on your
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

## Configure the Wiz plugin

You configure plugins in the Amazon Q Developer console. Amazon Q uses credentials stored in
AWS Secrets Manager to enable interactions with Wiz.

To configure the Wiz plugin, complete the following procedure:

1. Open the Amazon Q Developer console at [https://console.aws.amazon.com/amazonq/developer/home](https://console.aws.amazon.com/amazonq/developer/home "https://console.aws.amazon.com/amazonq/developer/home")
2. On the Amazon Q Developer console home page, choose **Settings**.
3. In the navigation bar, choose **Plugins**.
4. On the plugins page, choose the plus sign on the **Wiz** panel. The plugin configuration page
   opens.
5. For **API endpoint URL**, enter the URL of API endpoint where you access Wiz.
6. For **Configure AWS Secrets Manager**, choose either
   **Create a new secret** or **Use an
   existing secret**. The Secrets Manager secret is where your Wiz authentication
   credentials will be stored.

If you create a new secret, enter the following information:

    1. For **Client ID**, enter the Client ID for your Wiz account.
    2. For **Client Secret**, enter the Client Secret for your Wiz account.
    3. A service role will be created that Amazon Q will use to access the
     secret where your Wiz credentials are stored. Do not edit the
     service role that is created for you.If you use an existing secret, choose a secret from the **AWS Secrets Manager

secret\*\* dropdown menu. The secret should include the Wiz authentication
credentials specified in the previous step.

For more information about the required credentials, see
[Acquire credentials](#acquire-wiz-credentials "#acquire-wiz-credentials") . 7. For **Configure AWS IAM service role**, choose either **Create new service role** or
**Use existing service role**.

###### Note

If you chose **Create a new secret** for step 6, you can’t use an existing
service role. A new role will be created for you.

If you create a new service role, a service role will be created that
Amazon Q will use to access the secret where your Wiz credentials
are stored. Do not edit the service role that is created for you.

If you use an existing service role, choose a role from the dropdown
menu that appears. Make sure your service role has the permissions and
trust policy defined in [Service roles](#wiz-service-role "#wiz-service-role"). 8. Choose **Save configuration**. 9. After the Wiz plugin panel appears in the **Configured plugins** section on the Plugins
page, users will have access to the plugin.

If you want to update the credentials for a plugin, you must delete your current
plugin and configure a new one. Deleting a plugin removes all previous specifications.
Any time you configure a new plugin, a new plugin ARN is generated.

## Configure user permissions

To use plugins, the following permissions are required:

- Permissions to chat with Amazon Q in the console. For an example IAM
  policy that grants permissions needed to chat, see
  [Allow users to chat with
  Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").
- The `q:UsePlugin` permission.

When you grant an IAM identity access to a configured Wiz plugin, the identity
gains access to any resources in the Wiz account retrievable by the plugin. Wiz
user permissions are not detected by the plugin. If you want to control access to a
plugin, you can do so by specifying the plugin ARN in an IAM policy.

Each time you create or delete and re-configure a plugin, it is assigned a new ARN. If
you use a plugin ARN in a policy, it will need to be updated if you want to grant access
to the newly configured plugin.

To locate the Wiz plugin ARN, go to the **Plugins** page in the Amazon Q Developer
console and choose the configured Wiz plugin. On the plugin details page, copy the
plugin ARN. You can add this ARN to a policy to allow or deny access to the Wiz
plugin.

If you create a policy to control access to Wiz plugins, specify
`Wiz` for the plugin provider in the policy.

For examples of IAM policies that control plugin access, see
[Allow users to chat with
plugins from one provider](id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type "id-based-policy-examples-users.md#id-based-policy-examples-allow-plugin-type").

## Chat with the Wiz plugin

To use the Amazon Q Wiz plugin, enter `@Wiz` at the beginning of a
question about your Wiz issues. Follow up questions or responses to questions from
Amazon Q must also include `@Wiz`.

Following are some example use cases and associated questions you can ask to get the
most of out of the Amazon Q Wiz plugin:

- **View issues with critical severity** – Ask
  the Amazon Q Wiz plugin to list your issues with critical or high severity. The
  plugin can return up to 10 issues. You can also ask to list up to the top 10
  most severe issues.
  - `@wiz what are my critical severity issues?`
  - `@wiz can you specify the top 5?`

- **List issues based on date or status** –
  Ask to list issues based on create date, due date, or resolved date. You can
  also specify issues based on properties like status, severity, and type.
  - `@wiz which issues are due before <date>?`
  - `@wiz what are my issues that have been resolved since
<date>?`

- **Assess issues with security vulnerabilities** –
  Ask about the vulnerabilities or exposures that are posing security threats in your issues.
  - `@wiz which issues are associated with vulnerabilities or external exposures?`
