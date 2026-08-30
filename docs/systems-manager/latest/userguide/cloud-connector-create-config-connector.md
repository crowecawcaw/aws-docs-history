# Step 1: Create an AWS Config connector

The AWS Config connector sets up the credential exchange between AWS and
Azure and enables AWS Config to record Azure resource state. You must create this
before creating the Systems Manager Cloud Connector.

###### Note

The AWS Config connector automatically creates a service-linked role
for federation. You do not need to create a separate IAM role for this
step.

###### To create an AWS Config connector for Azure

1. Create the AWS Config connector. Replace
   `TENANT_ID` with your Azure tenant ID and
   `CLIENT_ID` with the **Config
   Application (Client) ID** — the application (client) ID of the
   AWS Config Azure AD app that you noted in the Azure prerequisites (Step
   6).

```
aws configservice put-connector \
    --connector-configuration '{
        "azure": {
            "tenantIdentifier": "`TENANT_ID`",
            "clientIdentifier": "`CLIENT_ID`"
        }
    }'
```

Note the `Arn` from the response — you need it in the
next step. 2. Confirm the connector was created:

```
aws configservice list-connectors
```
