# IAM role for an Amazon Q Business

web experience using IAM Identity Center

###### Important

This page only applies to Amazon Q Business web experiences connected to
IAM Identity Center-integrated Amazon Q Business applications.

**Policy history**

- **Latest policy update:** — December 3,
  2024
  The following table list and describes the changes to this policy over time.

| Change                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Date       |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Amazon Q Business now supports deleting<br>attachments | To enable delete attachments support on chats, modify your<br>\*Web experience IAM role<br>• by adding the<br>permission `qbusiness:DeleteAttachment`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, users can remove attached files in<br>conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 2/27/2025  |
| Amazon Q Business plugin actions<br>support            | To allow Amazon Q Business to list plugin actions and to<br>allow end users to discover plugins in their web experience, modify<br>the existing \*Web experience IAM role<br>• by adding<br>the following permissions: `qbusiness:ListPluginActions`,<br>`qbusiness:ListPluginTypeMetadata`, and<br>`qbusiness:ListPluginTypeActions`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, Amazon Q Business can list plugin actions and web<br>experience users can discover plugins in their web experience. For<br>more information, see [Prerequisites for configuring Amazon Q Business built-in plugins](basic-plugins-prereqs.md "basic-plugins-prereqs.md").                                                                                              | 12/03/2024 |
| Amazon Quick Suite plugin support                      | To allow the Quick Suite plugin to include visuals from Amazon Quick Suite,<br>modify the existing \*Web experience IAM role<br>• to<br>add permission for<br>`quicksight:GenerateEmbedUrlForRegisteredUserWithIdentity`.<br>With this change, web experience users can view visuals from<br>Quick Suite. For more information about the Quick Suite plugin, see<br>[Using the Quick Suite plugin to get insights from<br>structured data](quicksight-plugin.md "quicksight-plugin.md").                                                                                                                                                                                                                                                                                                                                                       | 12/03/2024 |
| Embedded visual content support                        | To enable extracting semantic meaning from embedded visual<br>content, modify the existing \*Web experience IAM<br>role<br>• by adding the permission<br>`qbusiness:GetMedia`. The scoping for this new<br>permission should be similar to other `qbusiness:`<br>conversation permissions.<br>With this change, if you enable content extraction for a data<br>source, web experience users can ask questions and get answers<br>related to the images. When an end user asks a question, Amazon Q Business<br>retrieves relevant answers from the text and the images. Answers<br>include the images and links for the documents that contain them.<br>For more information, see [Extracting semantic meaning from embedded<br>visual content with Amazon Q Business](extracting-meaning-from-images.md "extracting-meaning-from-images.md"). | 12/01/2024 |
| Recent files support                                   | To enable recent files support on web experiences, modify the<br>existing \*Web experience IAM role<br>• by adding the<br>permission `qbusiness:ListAttachments`. The scoping for<br>this new permission should be similar to other<br>`qbusiness:` conversation permissions.<br>With this change, users can find and reuse any recently attached<br>files in new conversations without uploading the files again.<br>Additionally, users can now drag and drop files they want to upload<br>directly into any conversation inside their Amazon Q web<br>experience.                                                                                                                                                                                                                                                                           | 11/21/2024 |

###### Note

To find the IAM role ARN for your web experience you can go to \***\*Amazon Q Business** →
**Applications** → _choose your
application_
**Name** → **Web experience
settings\*\*** in the Amazon Q Business console.

The following section lists the IAM policies required to allow you to
invoke the API operations required to integrate your application environment with IAM Identity Center.

To allow an Amazon Q Business web experience to invoke the API operations
required to integrate your application environment and deploy your web experience with
an IAM Identity Center instance, use the following policy:

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

To allow Amazon Q to assume this role, use the following trust
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "application.qbusiness.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```
