# Excluding functions from Lambda code scanning

You can add tags to Lambda functions, so you can exclude them from Amazon Inspector Lambda code scans.
Excluding functions from scans can prevent unactionable alerts.
When you tag a function for exclusion, the tag must have the following key-value pair.

- Key – `InspectorCodeExclusion`
- Value – `LambdaCodeScanning`

This topic describes how to tag a function for exclusion from code scans.
For more information about adding tags in Lambda, see [Using tags on Lambda functions](../../../lambda/latest/dg/configuration-tags.md "../../../lambda/latest/dg/configuration-tags.md").

###### To exclude a function from code scans

1. Sign in using your credentials, and then open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. From the navigation pane, choose **Functions**.
3. Choose the name of the function you would want to exclude from Amazon Inspector Lambda code scans.
4. Choose **Configuration**, and then choose **Tags**.
5. Choose **Manage tags**, and then **Add new tag**.
   1. For **Key**, enter `InspectorCodeExclusion`.
   2. For **Value**, enter `LambdaCodeScanning`

6. Choose **Save**.
