

# Permissions reference for the AWS assistant
<a name="permissions-reference"></a>

You can use the following permissions as a reference when you write identity-based policies for the AWS assistant. The permissions use the `q` service prefix.

**Important**  
To chat with the AWS assistant, an IAM identity needs permissions for the following actions:  
`q:StartConversation`
`q:SendMessage`
`q:GetConversation` (AWS Management Console only)
`q:ListConversations` (AWS Management Console only)
If one of these actions isn't explicitly allowed by an attached policy, an IAM permissions error is returned when you try to chat with the AWS assistant.


**AWS assistant permissions**  
<a name="assistant-permissions-ref"></a>
<table>
<thead>
  <tr><th>Name</th><th>Description of permission granted</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>User permissions</b></td></tr>
  <tr><td><code>q:StartConversation</code></td><td>Start a conversation with the AWS assistant</td></tr>
  <tr><td><code>q:SendMessage</code></td><td>Send a message to the AWS assistant</td></tr>
  <tr><td><code>q:GetConversation</code></td><td>Get individual messages associated with a specific conversation with the AWS assistant (AWS Management Console only)</td></tr>
  <tr><td><code>q:ListConversations</code></td><td>List individual conversations associated with a specific AWS assistant user (AWS Management Console only)</td></tr>
  <tr><td><code>q:UpdateConversation</code></td><td>Update a conversation with the AWS assistant</td></tr>
  <tr><td><code>q:DeleteConversation</code></td><td>Delete a conversation with the AWS assistant</td></tr>
  <tr><td><code>q:GetIdentityMetaData</code></td><td>Allow the AWS assistant to fetch application identity-related metadata</td></tr>
  <tr><td><code>q:PassRequest</code></td><td>Allow the AWS assistant to perform actions that an IAM identity has permission to perform</td></tr>
  <tr><td><code>q:StartTroubleshootingAnalysis</code></td><td>Start a troubleshooting analysis with the AWS assistant</td></tr>
  <tr><td><code>q:GetTroubleshootingResults</code></td><td>Get troubleshooting results with the AWS assistant</td></tr>
  <tr><td><code>q:StartTroubleshootingResolutionExplanation</code></td><td>Start a troubleshooting resolution explanation with the AWS assistant</td></tr>
  <tr><td><code>q:UpdateTroubleshootingCommandResult</code></td><td>Allow the AWS assistant to analyze resources to troubleshoot a console error</td></tr>
  <tr><td><code>q:UsePlugin</code></td><td>Access plugins from the AWS assistant</td></tr>
  <tr><td colspan="2"><b>Administrator permissions for plugins</b></td></tr>
  <tr><td><code>q:CreatePlugin</code></td><td>Create and configure a third-party plugin for the AWS assistant</td></tr>
  <tr><td><code>q:GetPlugin</code></td><td>View information about a specific plugin</td></tr>
  <tr><td><code>q:DeletePlugin</code></td><td>Delete a configured plugin</td></tr>
  <tr><td><code>q:ListPlugins</code></td><td>View configured plugins</td></tr>
  <tr><td><code>q:ListPluginProviders</code></td><td>View available plugins</td></tr>
  <tr><td><code>q:UpdatePlugin</code></td><td>Update feature enablement controls for a third-party integration plugin</td></tr>
  <tr><td><code>q:CreateAuthGrant</code></td><td>Register a third-party application user</td></tr>
  <tr><td><code>q:UpdateAuthGrant</code></td><td>Update a third-party application user</td></tr>
  <tr><td><code>q:CreateOAuthAppConnection</code></td><td>Register a third-party OAuth application</td></tr>
  <tr><td><code>q:UpdateOAuthAppConnection</code></td><td>Update a third-party OAuth application</td></tr>
  <tr><td><code>q:SendEvent</code></td><td>Send events from a third-party application for processing</td></tr>
</tbody>
</table>


For example policies, see [Identity-based policy examples for the AWS assistant](security-iam-examples.md). For all actions that use the `q` service prefix, see [Actions, resources, and condition keys for Amazon Q](https://docs.aws.amazon.com/service-authorization/latest/reference/list_q.html) in the *Service Authorization Reference*.

## Using `q:PassRequest`
<a name="passrequest"></a>

`q:PassRequest` is a permission that allows the AWS assistant to call AWS APIs on your behalf. When you add the `q:PassRequest` permission to an IAM identity, the AWS assistant gains permission to call any API that the IAM identity has permission to call. For example, if an IAM role has the `s3:ListAllMyBuckets` permission and the `q:PassRequest` permission, the AWS assistant can call the `ListAllMyBuckets` API when a user who assumes that role asks the AWS assistant to list their Amazon S3 buckets.

You can create IAM policies that restrict the scope of the `q:PassRequest` permission. For example, you can prevent the AWS assistant from performing a specific action, or permit it to perform only a subset of actions for a service. You can also specify which Regions the AWS assistant can make calls to when it performs actions on your behalf.

For example policies that control the use of `q:PassRequest`, see the following:
+ [Allow the AWS assistant to perform actions on your behalf](security-iam-examples.md#iam-example-actions)
+ [Deny the AWS assistant permission to perform specific actions](security-iam-examples.md#iam-example-deny-some-actions)
+ [Allow the AWS assistant permission to perform specific actions](security-iam-examples.md#iam-example-allow-some-actions)
+ [Allow the AWS assistant to perform actions in specific Regions](security-iam-examples.md#iam-example-some-regions)
+ [Deny the AWS assistant permission to perform actions on your behalf](security-iam-examples.md#iam-example-deny-actions)