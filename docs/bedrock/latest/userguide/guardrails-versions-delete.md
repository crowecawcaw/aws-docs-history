# Delete a version of a guardrail

To learn how to delete a version of a guardrail, select one of the tabs below and follow the steps indicated:

Console
If you no longer need a version, you can delete it with the following steps.

###### To delete a version

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
   [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. Choose **Guardrails** from the left navigation pane. Then, select a guardrail in the **Guardrails** section.
3. In the **Versions** section, select the version you want to delete and choose **Delete**.
4. A modal appears to warn you about resources that are dependent on this version of the guardrail. Disassociate the version from the resources before you delete to avoid errors.
5. Enter `delete` in the user input field and
   choose **Delete** to delete the guardrail version.

API
To delete a version of a guardrail, send a [DeleteGuardrail](../APIReference/API_DeleteGuardrail.md "../APIReference/API_DeleteGuardrail.md") request. Specify the ARN of the guardrail in the `guardrailIdentifier` field and the version in the `guardrailVersion` field.

The following is the request format:

```
DELETE /guardrails/`guardrailIdentifier`?guardrailVersion=`guardrailVersion` HTTP/1.1
```

If the deletion is successful, the response returns an HTTP 200 status code.
