# IAM permissions for using Amazon Q Apps

If the users of your deployed web experience want to create lightweight, purpose-built
Amazon Q Apps within your broader Amazon Q Business application environment, you must include
the following policy permissions.

###### Note

This Amazon Q Apps IAM policy released on July 10, 2024 supports the ability for
users to view and specify approved _data sources_ at the
card-level and use other future features. To use these features, you must update all
roles for Amazon Q Apps that have been created prior to this date with this new
policy.

| Change                                                                     | Description                                                                                                                                                                                                                                                                           | Date       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Deprecated some IAM actions related to file upload                         | The `qapps:ImportDocumentToQApp`,<br>`qapps:ImportDocumentToQAppSession`, and<br>`qapps:CreatePresignedUrl` IAM actions are<br>deprecated. The `qapps:ImportDocument` action now serves<br>as the single file upload action.                                                          | 05/22/2025 |
| Added Permission to `CreatePresignedUrl`                                   | This new API allows users to leverage the improved file limits in<br>Amazon Q Apps. You can now upload files with size up to 10MB (per file<br>card).                                                                                                                                 | 11/22/2024 |
| Added Permissions to `DescribeQAppPermissions` and `UpdateQAppPermissions` | These new APIs allows users [privately share Amazon Q Apps](qapps-private-sharing.md "qapps-private-sharing.md") to leverage the improved<br>file limits in Amazon Q Apps. You can now upload files with size up to<br>10MB (per file card).                                          | 11/22/2024 |
| Added permissions related to management of persistent sessions.            | These new APIs allows users to start, manage and terminate long<br>running collaborative [data<br>collection sessions](q-apps-forms.md "q-apps-forms.md") to leverage the improved file limits<br>in Amazon Q Apps. You can now upload files with size up to 10MB (per<br>file card). | 11/22/2024 |

###### Topics

- [Capabilities available with Amazon Q Apps](#q-apps-actions "#q-apps-actions")
- [IAM permissions for users to
  view and specify approved data sources in Amazon Q Apps](#deploy-data-source-iam-permissions "#deploy-data-source-iam-permissions")
  **If you want to use Amazon Q Apps, your web experience IAM role
  needs the following additional permissions:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
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
 "qapps:StartQAppSession",
 "qapps:DescribeQAppPermissions",
 "qapps:UpdateQAppPermissions"
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
 "qapps:StartQAppSession",
 "qapps:DescribeQAppPermissions"
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
 "qapps:StopQAppSession",
 "qapps:ListQAppSessionData",
 "qapps:ExportQAppSessionData"
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
 "qapps:UpdateQAppSession",
 "qapps:ListQAppSessionData"
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

## Capabilities available with Amazon Q Apps

The Amazon Q Apps IAM policy allows your web experience users permissions to do
the following:

- **Amazon Q Apps capabilities:**
  - Create a Q App ([API](../api-reference/API_qapps_CreateQApp.md "../api-reference/API_qapps_CreateQApp.md"))
  - Get the status and other information on a Q App ([API](../api-reference/API_qapps_GetQApp.md "../api-reference/API_qapps_GetQApp.md"))
  - Update a Q App ([API](../api-reference/API_qapps_UpdateQApp.md "../api-reference/API_qapps_UpdateQApp.md"))
  - List all created Q Apps ([API](../api-reference/API_qapps_ListQApps.md "../api-reference/API_qapps_ListQApps.md"))
  - Delete a Q App ([API](../api-reference/API_qapps_DeleteQApp.md "../api-reference/API_qapps_DeleteQApp.md"))
  - Start a Q App run (session) ([API](../api-reference/API_qapps_StartQAppSession.md "../api-reference/API_qapps_StartQAppSession.md"))
  - Stop a Q App run (session) ([API](../api-reference/API_qapps_StopQAppSession.md "../api-reference/API_qapps_StopQAppSession.md"))
  - Upload files to a Q App run (session) ([API](../api-reference/API_qapps_ImportDocument.md "../api-reference/API_qapps_ImportDocument.md"))
  - Converts a conversation into a (_text string_)
    problem statement ([API](../api-reference/API_qapps_PredictQApp.md "../api-reference/API_qapps_PredictQApp.md"))
  - Convert a problem statement into a proposed Q App ([API](../api-reference/API_qapps_PredictQApp.md "../api-reference/API_qapps_PredictQApp.md"))

- **Amazon Q Apps library capabilities:**
  - Publish a Q App by adding items to your Q Apps library ([API](../api-reference/API_qapps_CreateLibraryItem.md "../api-reference/API_qapps_CreateLibraryItem.md"))
  - Get the status and other information on a Q App (item) in your
    Q Apps library ([API](../api-reference/API_qapps_GetLibraryItem.md "../api-reference/API_qapps_GetLibraryItem.md"))
  - Update a published Q App (item) in your Q Apps library ([API](../api-reference/API_qapps_UpdateLibraryItem.md "../api-reference/API_qapps_UpdateLibraryItem.md"))
  - List all Q Apps (items) from your Q Apps library ([API](../api-reference/API_qapps_ListLibraryItems.md "../api-reference/API_qapps_ListLibraryItems.md"))
  - Delete a Q App (item) from your Q Apps library ([API](../api-reference/API_qapps_DeleteLibraryItem.md "../api-reference/API_qapps_DeleteLibraryItem.md"))
  - Like (rate) a Q App item from your Q Apps library ([API](../api-reference/API_qapps_AssociateLibraryItemReview.md "../api-reference/API_qapps_AssociateLibraryItemReview.md"))

## IAM permissions for users to

view and specify approved data sources in Amazon Q Apps

**(Optional) You must add the following permissions to the
Amazon Q Apps policy to allow Q Apps users to view and specify approved data
sources** in their app.

###### Note

If you are using permissions for Amazon Q Apps created prior to July 10, 2024,
you must update your role with the new [Amazon Q Apps](deploy-q-apps-iam-permissions.md "deploy-q-apps-iam-permissions.md") permissions for your users
to have access to use the [permissions
to view and specify approved data sources](deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions "deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions") and other future features in Q Apps.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessIndexPermission",
 "Effect": "Allow",
 "Action": [
 "qbusiness:ListIndices"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 },
 {
 "Sid": "QBusinessDataSourcePermission",
 "Effect": "Allow",
 "Action": [
 "qbusiness:ListDataSources"
 ],
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`",
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/index/*"
 ]
 }
 ]
}`

```

###### Note

If any of these permissions are removed, then you run the risk of your web
experience users not being able to create and run their own Q Apps properly.
