# Using Amazon Q Developer with AWS Lambda

This document describes how to set up and activate Amazon Q Developer for the Lambda console.
Once activated, Amazon Q can make code recommendations on demand in the Lambda code editor
as you develop your function.

###### Note

In the Lambda console, Amazon Q only supports functions using the Python and Node.js
runtimes.

## AWS Identity and Access Management permissions for Lambda

For Amazon Q to provide recommendations in the Lambda console, you must enable the correct IAM permissions
for either your IAM user or role. You must add the `codewhisperer:GenerateRecommendations` permission, as outlined
in the sample IAM policy below:

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
 "Sid": "AmazonQDeveloperPermissions",
 "Effect": "Allow",
 "Action": ["codewhisperer:GenerateRecommendations"],
 "Resource": "*"
 }
 ]
}`

```

It is best practice to use IAM policies to grant restrictive permissions to IAM
principals. For details about working with IAM for AWS Lambda, see [Identity and access management in AWS Lambda](../../../lambda/latest/dg/security-iam.md "../../../lambda/latest/dg/security-iam.md") in the _AWS Lambda Developer Guide_.

## Activating Amazon Q Developer with Lambda

To activate Amazon Q in the Lambda console code editor, complete these steps.

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console,
   and choose the function that you want to edit.
2. As you type in the code editor, automatic code suggestions from Amazon Q are enabled by
   default. To pause suggestions, choose **Amazon Q** in the bottom left
   corner of the **Code source** panel. The command palette opens at the top
   of the Code source panel. From there, choose **Pause auto-suggestions**.

For shortcut keys, see [Using shortcut keys](actions-and-shortcuts.md "actions-and-shortcuts.md").
