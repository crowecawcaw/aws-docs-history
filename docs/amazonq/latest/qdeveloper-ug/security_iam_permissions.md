# Amazon Q Developer permissions reference

Amazon Q Developer uses two types of APIs to provide the service:

- User and administrator permissions, which can be used in policies to control usage of
  Amazon Q
- Other APIs used to provide the service, which can’t be used in policies to control usage of
  Amazon Q
  This section provides information about the APIs used by Amazon Q Developer, and what they do.

###### Topics

- [Amazon Q Developer permissions](#qdev-permissions "#qdev-permissions")
- [Amazon Q User Subscriptions permissions](#subscriptions-permissions "#subscriptions-permissions")
- [Other Amazon Q Developer APIs](#other-permissions "#other-permissions")

## Amazon Q Developer permissions

You can use the following permissions as a reference when you are setting up [Authenticating with identities in Amazon Q](security-iam.md#security-iam-authentication "security-iam.md#security-iam-authentication") and
writing permissions policies that you can attach to an IAM identity (identity-based
policies).

The following table shows the Amazon Q Developer permissions that you can allow or deny access to in
policies.

###### Important

To chat with Amazon Q, an IAM identity needs permissions for the following actions:

- `StartConversation`
- `SendMessage`
- `GetConversation` (console only)
- `ListConversations` (console only)
  If one of these actions isn't explicitly allowed by an attached policy, an IAM permissions
  error is returned when you try to chat with Amazon Q.

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

| Amazon Q Developer permissions                | Name                                                                                | Description of permission granted | Required to chat with Amazon Q? |
| --------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------- | ------------------------------- |
| User permissions                              |
| `q:DeleteConversation`                        | Delete a conversation with Amazon Q                                                 | Yes                               |
| `qdeveloper:ExportArtifact`                   | Export artifacts from Amazon Q                                                      | No                                |
| `codewhisperer:GenerateRecommendations`       | Get code suggestions in Amazon Q for AWS coding environments                        | No                                |
| `q:GenerateCodeFromCommands`                  | Generate code from CLI commands in Amazon Q                                         | No                                |
| `q:GetConversation`                           | Get individual messages associated with a specific conversation with<br>Amazon Q    | Yes (in console only)             |
| `q:GetIdentityMetaData`                       | Allow Amazon Q to fetch application identity-related metadata                       | No                                |
| `q:GetTroubleshootingResults`                 | Get troubleshooting results with Amazon Q                                           | No                                |
| `qdeveloper:ImportArtifact`                   | Import artifacts to Amazon Q                                                        | No                                |
| `q:ListConversations`                         | List individual conversations associated with a specific Amazon Q user              | Yes (in console only)             |
| `q:PassRequest`                               | Allow Amazon Q to perform actions that an IAM identity has permission to<br>perform | No                                |
| `q:SendMessage`                               | Send a message to Amazon Q                                                          | Yes                               |
| `qdeveloper:StartAgentSession`                | Start an agent session with Amazon Q                                                | No                                |
| `q:StartConversation`                         | Start a conversation with Amazon Q                                                  | Yes                               |
| `q:StartTroubleshootingAnalysis`              | Start a troubleshooting analysis with Amazon Q                                      | No                                |
| `q:StartTroubleshootingResolutionExplanation` | Start a troubleshooting resolution explanation with Amazon Q                        | No                                |
| `qdeveloper:TransformCode`                    | Transform code with Amazon Q                                                        | No                                |
| `q:UsePlugin`                                 | Access plugins from Amazon Q chat                                                   | No                                |
| `q:UpdateConversation`                        | Update a conversation with Amazon Q                                                 | Yes                               |
| `q:UpdateTroubleshootingCommandResult`        | Allow Amazon Q to analyze resources to troubleshoot a console error                 | No                                |
| Administrator permissions                     |
| `codewhisperer:CreateCustomization`           | Create an Amazon Q customization from your data source                              | No                                |
| `codewhisperer:DeleteCustomization`           | Delete an Amazon Q customization                                                    | No                                |
| `codewhisperer:GetCustomization`              | Get details about an Amazon Q customization                                         | No                                |
| `codewhisperer:ListCustomizations`            | List Amazon Q customizations based on their state                                   | No                                |
| `codewhisperer:ListProfiles`                  | List Amazon Q Profiles                                                              | No                                |
| `codewhisperer:ListTagsForResource`           | List all tags associated with an Amazon Q resource in the console                   | No                                |
| `codewhisperer:TagResource`                   | Add or create a tag for an Amazon Q resource                                        | No                                |
| `codewhisperer:UnTagResource`                 | Remove a tag from an Amazon Q resource                                              | No                                |
| `codewhisperer:UpdateCustomization`           | Activate or deactivate an Amazon Q customization                                    | No                                |
| `codewhisperer:ListCustomizationVersions`     | List the versions of an Amazon Q customization                                      | No                                |
| `codewhisperer:UpdateProfile`                 | Update an Amazon Q Profile                                                          | No                                |
| `q:CreateAssignment`                          | Create a user or group assignment for an Amazon Q Developer Profile                 | No                                |
| `q:CreateAuthGrant`                           | Register a third-party application user with Amazon Q                               | No                                |
| `q:CreateOAuthAppConnection`                  | Register a third-party OAuth application with Amazon Q                              | No                                |
| `q:CreatePlugin`                              | Create and configure a third party plugin in Amazon Q                               | No                                |
| `q:DeleteAssignment`                          | Delete a user or group assignment for an Amazon Q Developer Profile                 | No                                |
| `q:DeletePlugin`                              | Delete a configured plugin in Amazon Q                                              | No                                |
| `q:GetPlugin`                                 | View information about a specific Amazon Q plugin                                   | No                                |
| `q:ListPlugins`                               | View configured plugins in Amazon Q                                                 | No                                |
| `q:ListPluginProviders`                       | View available plugins in Amazon Q                                                  | No                                |
| `q:ListTagsForResource`                       | List all tags associated with an Amazon Q resource in the console                   | No                                |
| `q:TagResource`                               | Add or create a tag for an Amazon Q resource                                        | No                                |
| `q:SentEvent`                                 | Send events from third-party application to Amazon Q for processing                 | No                                |
| `q:UntagResource`                             | Remove a tag from an Amazon Q resource                                              | No                                |
| `q:UpdateAuthGrant`                           | Update a third-party application user with Amazon Q                                 | No                                |
| `q:UpdateOAuthAppConnection`                  | Update a third-party OAuth application with Amazon Q                                | No                                |
| `q:UpdatePlugin`                              | Update feature enablement controls for third-party integration plugin               | No                                |

### Using q:PassRequest

`q:PassRequest` is an Amazon Q permission that allows Amazon Q to call AWS APIs on
your behalf. When you add the `q:PassRequest` permission to an IAM identity,
Amazon Q gains permission to call any API that the IAM identity has permission to call. For
example, if an IAM role has the `s3:ListAllMyBuckets` permission and the
`q:PassRequest` permission, Amazon Q is able to call the
`ListAllMyBuckets` API when a user assuming that IAM role asks Amazon Q to list
their Amazon S3 buckets.

You can create IAM policies that restrict the scope of the `q:PassRequest`
permission. For example, you can prevent Amazon Q from performing a specific action, or only
permit Amazon Q to perform a subset of actions for a service. You can also specify what regions
Amazon Q can make calls to when performing actions on your behalf.

For examples of IAM policies that control the use of `q:PassRequest`, see the
following identity-based policy examples:

- [Allow Amazon Q to perform actions on
  your behalf in chat](id-based-policy-examples-users.md#id-based-policy-examples-allow-actions "id-based-policy-examples-users.md#id-based-policy-examples-allow-actions")
- [Deny Amazon Q
  permission to perform specific actions on your behalf](id-based-policy-examples-users.md#id-based-policy-examples-deny-some-actions "id-based-policy-examples-users.md#id-based-policy-examples-deny-some-actions")
- [Allow Amazon Q permission to
  perform specific actions on your behalf](id-based-policy-examples-users.md#id-based-policy-examples-allow-some-actions "id-based-policy-examples-users.md#id-based-policy-examples-allow-some-actions")
- [Allow Amazon Q
  permission to perform actions on your behalf in specific regions](id-based-policy-examples-users.md#id-based-policy-examples-allow-actions-some-regions "id-based-policy-examples-users.md#id-based-policy-examples-allow-actions-some-regions")
- [Deny Amazon Q permission to perform
  actions on your behalf](id-based-policy-examples-users.md#id-based-policy-examples-deny-actions "id-based-policy-examples-users.md#id-based-policy-examples-deny-actions")

## Amazon Q User Subscriptions permissions

Amazon Q Developer administrators must have the following permissions to create and manage
subscriptions for users and groups in their organization.

The following terminology is useful in understanding what subscriptions permissions do:

**User**

An individual user, represented within AWS IAM Identity Center by a unique user ID.

**Group**

A collection of users, represented within AWS IAM Identity Center by a unique group ID.

**Subscription**

A subscription is tied to a single Identity Center user, and entitles them to use
Amazon Q features. A subscription does not authorize a user to use Amazon Q features. For
example, if Adam is subscribed to Amazon Q Developer Pro, they are entitled to used Amazon Q Developer
features, but they don't have access to those features until their administrator grants
them the needed permissions.

| Amazon Q User Subscriptions permissions    | Name                                                | Description of action |
| ------------------------------------------ | --------------------------------------------------- | --------------------- |
| `user-subscriptions:CreateClaim`           | Create a user subscription                          |
| `user-subscriptions:DeleteClaim`           | Delete a user subscription                          |
| `user-subscriptions:ListApplicationClaims` | List all user subscriptions for a given application |
| `user-subscriptions:ListClaims`            | List all user subscriptions                         |
| `user-subscriptions:ListUserSubscriptions` | List all user subscriptions for a given user        |
| `user-subscriptions:UpdateClaim`           | Update a user subscription                          |

## Other Amazon Q Developer APIs

The following table shows the APIs that are used by features of Amazon Q in the IDE. These APIs
aren’t used to control access to features of Amazon Q, but they will appear in AWS CloudTrail logs in
management accounts when users access the associated feature.

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

| Amazon Q Developer APIs to provide the service    | Name                                                                                                   | Description of action |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------- |
| `codewhisperer:AllowVendedLogDeliveryForResource` | Enables Amazon Q Developer to publish logs to Amazon CloudWatch asynchronously                         |
| `codewhisperer:CreateTaskAssistConversation`      | Starts a conversation with the Amazon Q Developer Agent for software development                       |
| `codewhisperer:CreateUploadUrl`                   | Creates the URL to upload the code files that will be used for development with<br>Amazon Q in the IDE |
| `codewhisperer:DeleteTaskAssistConversation`      | Deletes a conversation with the Amazon Q Developer Agent for software development                      |
| `codewhisperer:ExportResultArchive`               | Exports an archive of outputs of Amazon Q Developer for download                                       |
| `codewhisperer:GenerateAssistantResponse`         | Returns a response in Amazon Q in chat in the IDE                                                      |
| `codewhisperer:GenerateCompletions`               | Gets inline code suggestions                                                                           |
| `codewhisperer:GenerateTaskAssistPlan`            | Generates an implementation plan from the Amazon Q Developer Agent for software development            |
| `codewhisperer:GetCodeAnalysis`                   | Gets the status of an ongoing security scan                                                            |
| `codewhisperer:GetTaskAssistCodeGeneration`       | Gets code generated by the Amazon Q Developer Agent for software development                           |
| `codewhisperer:GetTransformation`                 | Returns a code transformation from the Amazon Q Developer Agent for code transformation                |
| `codewhisperer:GetTransformationPlan`             | Returns the transformation plan from the Amazon Q Developer Agent for software development             |
| `codewhisperer:ListAvailableCustomizations`       | Returns the list of customizations that have been created and are available for<br>use                 |
| `codewhisperer:ListCodeAnalysisFindings`          | Returns the list of all security issues in the files scanned                                           |
| `codewhisperer:ListFeatureEvaluations`            | Lists relevant configurations for Amazon Q Developer client-side features                              |
| `codewhisperer:SendTelemetryEvent`                | Sends telemetry information to AWS about usage of Amazon Q in the IDE                                  |
| `codewhisperer:StartTaskAssistCodeGeneration`     | Starts code generation with the Amazon Q Developer Agent for software development                      |
| `codewhisperer:StartCodeAnalysis`                 | Starts a security scan                                                                                 |
| `codewhisperer:StartTransformation`               | Starts a transformation with the Amazon Q Developer Agent for code transformation                      |
| `codewhisperer:StopTransformation`                | Stops a transformation with the Amazon Q Developer Agent for code transformation                       |
