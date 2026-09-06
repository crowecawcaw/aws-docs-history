# Delete a consent portal

When you no longer need a consent portal, you can delete it from the AgentCore console or with the AWS CLI. Deleting a consent portal permanently removes it: its consent portal URL no longer serves end users, and any agent flows that depend on it can no longer obtain user consent through the portal. When you delete a consent portal, it transitions to the `DELETING` status and is then permanently removed.

## Delete a consent portal with the console

**To delete a consent portal**

1. Open the [AgentCore](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#") console.
2. From the left navigation pane, choose **Identity**.
3. Select the consent portal that you want to delete.
4. On the consent portal page, choose **Delete**.
5. In the confirmation dialog, type `confirm` to confirm the deletion.
6. Choose **Delete**.

## Delete a consent portal with the AWS CLI

Delete a consent portal with the `delete-consent-portal` command. Identify the consent portal with the required `--consent-portal-identifier` parameter, which accepts either the consent portal ID or its full ARN.

The following command deletes a consent portal. Replace `<consent-portal-id>` with your value.

```
aws bedrock-agentcore-control delete-consent-portal \
    --consent-portal-identifier "<consent-portal-id>"
```
