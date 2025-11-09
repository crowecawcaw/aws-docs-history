AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# `aws:invokeWebhook` – Invoke an

Automation webhook integration

Invokes the specified Automation webhook integration. For information about creating
Automation integrations, see [Creating webhook integrations for
Automation](creating-webhook-integrations.md "creating-webhook-integrations.md").

###### Note

The `aws:invokeWebhook` action supports automatic throttling retry. For
more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

###### Note

To use the `aws:invokeWebhook` action, your user or service role must
allow the following actions:

- ssm:GetParameter
- kms:Decrypt
  Permission for the AWS Key Management Service (AWS KMS) `Decrypt` operation is only
  required if you use a customer managed key to encrypt the parameter for your
  integration.

###### Input

Provide the information for the Automation integration you want to invoke.

YAML

```
action: "aws:invokeWebhook"
inputs:
 IntegrationName: "`exampleIntegration`"
 Body: "`Request body`"
```

JSON

```
{
    "action": "aws:invokeWebhook",
    "inputs": {
        "IntegrationName": "`exampleIntegration`",
        "Body": "`Request body`"
    }
}
```

IntegrationName

The name of the Automation integration. For example,
`exampleIntegration`. The integration you specify must
already exist.

Type: String

Required: Yes

Body

The payload you want to send when your webhook integration is
invoked.

Type: String

Required: No

###### Output

Response

The text received from the webhook provider response.

ResponseCode

The HTTP status code received from the webhook provider response.
