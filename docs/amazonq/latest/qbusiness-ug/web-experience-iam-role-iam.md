# IAM role for an Amazon Q Business web experience using IAM Federation

###### Important

This page only applies to Amazon Q Business web experiences connected to
IAM Federated Amazon Q Business applications.

**Policy history**

- **Latest policy update:** — December 3,
  2024
  The following table list and describes the changes to this policy over time.

| Change                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Date       |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Amazon Q Business now supports deleting<br>attachments | To enable delete attachments support on chats, modify your<br>\*Web experience IAM role<br>• by adding the<br>permission `qbusiness:DeleteAttachment`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, users can remove attached files in<br>conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 2/27/2025  |
| Amazon Q Business plugin actions<br>support            | To allow Amazon Q Business to list plugin actions and to<br>allow end users to discover plugins in their web experience, modify<br>the existing \*Web experience IAM role<br>• by adding<br>the following permissions: `qbusiness:ListPluginActions`,<br>`qbusiness:ListPluginTypeMetadata`, and<br>`qbusiness:ListPluginTypeActions`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, Amazon Q Business can list plugin actions and web<br>experience users can discover plugins in their web experience. For<br>more information, see [Prerequisites for configuring Amazon Q Business built-in plugins](basic-plugins-prereqs.md "basic-plugins-prereqs.md").                                                                                           | 12/03/2024 |
| Embedded visual content support                        | To enable extracting semantic meaning from embedded visual<br>content, modify the existing \*Web experience IAM<br>role<br>• by adding the permission<br>`qbusiness:GetMedia`. The scoping for this new<br>permission should be similar to other `qbusiness:`<br>conversation permissions.<br>With this change, if you enable content extraction for a data<br>source, web experience users can ask questions and get answers<br>related to the images. When an end user asks a question, Amazon Q Business<br>retrieves relevant answers from the text and the images. Answers<br>include the images and links for the documents that contain them.<br>For more information, see [Extracting semantic meaning from embedded visual content with Amazon Q Business](extracting-meaning-from-images.md "extracting-meaning-from-images.md"). | 12/01/2024 |
| Recent files support                                   | To enable recent files support on web experiences, modify the<br>existing \*Web experience IAM role<br>• by adding the<br>permission `qbusiness:ListAttachments`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, users can find and reuse any recently attached<br>files in new conversations without uploading the files again.<br>Additionally, users can now drag and drop files they want to upload<br>directly into any conversation inside their Amazon Q web<br>experience.                                                                                                                                                                                                                                                                        | 11/21/2024 |

###### Note

To find the IAM role ARN for your web experience you can go to \***\*Amazon Q Business** →
**Applications** → _choose your
application_
**Name** → **Web experience
settings\*\*** in the Amazon Q Business console.

The following IAM policies allow you to invoke the API operations
required for an application environment using Identity Federation through IAM (IAM Federation)
to manage user access or deploy a web experience using an external IdP.

###### Note

You must create and update an IAM policy for your Amazon Q Business
application (both console and API) before you begin creating it. Amazon Q Business doesn't auto-create IAM roles for your IAM Federation
application if you use the console.

To allow an Amazon Q Business web experience to invoke the API operations
required to integrate your application environment and deploy your web experience with
an AWS Identity and Access Management instance, use the following policy:

###### Note

To make use of the Clickable URL feature, add the following permissions to the IAM role for your Amazon Q web experience.

```


{
    "Sid": "QBusinessGetDocumentContentPermission",
    "Effect": "Allow",
    "Action": ["qbusiness:GetDocumentContent"],
    "Resource": [
        "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}",
        "arn:aws:qbusiness:{{region}}:{{source_account}}:application/{{application_id}}/index/*"
    ]
}

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessConversationPermissions",
 "Effect": "Allow",
 "Action": [
 "qbusiness:Chat",
 "qbusiness:ChatSync",
 "qbusiness:ListMessages",
 "qbusiness:ListConversations",
 "qbusiness:PutFeedback",
 "qbusiness:DeleteConversation",
 "qbusiness:GetWebExperience",
 "qbusiness:GetApplication",
 "qbusiness:ListPlugins",
 "qbusiness:GetChatControlsConfiguration",
 "qbusiness:ListRetrievers",
 "qbusiness:ListPluginActions",
 "qbusiness:ListAttachments",
 "qbusiness:GetMedia",
 "qbusiness:DeleteAttachment"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 },
 {
 "Sid": "QBusinessPluginDiscoveryPermissions",
 "Effect": "Allow",
 "Action": [
 "qbusiness:ListPluginTypeMetadata",
 "qbusiness:ListPluginTypeActions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "QBusinessRetrieverPermission",
 "Effect": "Allow",
 "Action": [
 "qbusiness:GetRetriever"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/retriever/*"
 ]
 },
 {
 "Sid": "QBusinessAutoSubscriptionPermission",
 "Effect": "Allow",
 "Action": [
 "user-subscriptions:CreateClaim"
 ],
 "Condition": {
 "Bool": {
 "user-subscriptions:CreateForSelf": "true"
 },
 "StringEquals": {
 "aws:CalledViaLast": "qbusiness.amazonaws.com"
 }
 },
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "QBusinessKMSDecryptPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "qbusiness.us-east-1.amazonaws.com",
 "qapps.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "QAppsResourceAgnosticPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:CreateQApp",
 "qapps:PredictQApp",
 "qapps:PredictProblemStatementFromConversation",
 "qapps:PredictQAppFromProblemStatement",
 "qapps:ListQApps",
 "qapps:ListLibraryItems",
 "qapps:CreateSubscriptionToken"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 },
 {
 "Sid": "QAppsAppUniversalPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:DisassociateQAppFromUser"
 ],
 "Resource": "arn:aws:qapps:us-east-1:111122223333:application/`application-id`/qapp/*"
 },
 {
 "Sid": "QAppsAppOwnerPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:GetQApp",
 "qapps:CopyQApp",
 "qapps:UpdateQApp",
 "qapps:DeleteQApp",
 "qapps:ImportDocument",
 "qapps:CreateLibraryItem",
 "qapps:UpdateLibraryItem",
 "qapps:StartQAppSession"
 ],
 "Resource": "arn:aws:qapps:us-east-1:111122223333:application/`application-id`/qapp/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "qapps:UserIsAppOwner": "true"
 }
 }
 },
 {
 "Sid": "QAppsPublishedAppPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:GetQApp",
 "qapps:CopyQApp",
 "qapps:AssociateQAppWithUser",
 "qapps:GetLibraryItem",
 "qapps:CreateLibraryItemReview",
 "qapps:AssociateLibraryItemReview",
 "qapps:DisassociateLibraryItemReview",
 "qapps:StartQAppSession"
 ],
 "Resource": "arn:aws:qapps:us-east-1:111122223333:application/`application-id`/qapp/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "qapps:AppIsPublished": "true"
 }
 }
 },
 {
 "Sid": "QAppsAppSessionModeratorPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:ImportDocument",
 "qapps:GetQAppSession",
 "qapps:GetQAppSessionMetadata",
 "qapps:UpdateQAppSession",
 "qapps:UpdateQAppSessionMetadata",
 "qapps:StopQAppSession"
 ],
 "Resource": "arn:aws:qapps:us-east-1:111122223333:application/`application-id`/qapp/*/session/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "qapps:UserIsSessionModerator": "true"
 }
 }
 },
 {
 "Sid": "QAppsSharedAppSessionPermissions",
 "Effect": "Allow",
 "Action": [
 "qapps:ImportDocument",
 "qapps:GetQAppSession",
 "qapps:GetQAppSessionMetadata",
 "qapps:UpdateQAppSession"
 ],
 "Resource": "arn:aws:qapps:us-east-1:111122223333:application/`application-id`/qapp/*/session/*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "qapps:SessionIsShared": "true"
 }
 }
 }
 ]
}`

```

**To allow Amazon Q to assume this role for a web
experience using SAML-compliant identity provider for user management, use the
following trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "sts:AssumeRoleWithSAML",
 "Sid": "SAMLAssumeRoleAccess",
 "Effect": "Allow",
 "Condition": {
 "StringEquals": {
 "SAML:aud": "https://`q-web-experience-domain`/saml"
 }
 },
 "Principal": {
 "Federated": "arn:aws:iam::111122223333:saml-provider/[[`saml_provider`]]"
 }
 },
 {
 "Action": "sts:TagSession",
 "Sid": "SAMLTagSessionAccess",
 "Effect": "Allow",
 "Condition": {
 "StringLike": {
 "aws:RequestTag/Email": "*"
 }
 },
 "Principal": {
 "Federated": "arn:aws:iam::111122223333:saml-provider/[[`saml_provider`]]"
 }
 }
 ]
}`

```

**To allow Amazon Q to assume this role for a web
experience using an OIDC-compliant identity provider for user management, use the
following trust policy:**

**To allow an Amazon Q Business web experience to access
AWS KMS to decrypt an OIDC client secret stored in Secrets Manager for an OIDC-based identity
provider:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToGetSecret",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secret-id`"
 ]
 },
 {
 "Sid": "AllowsAmazonQToDecryptSecret",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "secretsmanager.*.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

**To allow Amazon Q to assume the role to decrypt an
OIDC client secret stored in Secrets Manager, use the following trust
policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowsAmazonQToAssumeRoleForServicePrincipal",
 "Effect": "Allow",
 "Principal": {
 "Service": "application.qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```
