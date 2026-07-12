# Step 1: Create an Cloud Connector

The Cloud Connector sets up the credential exchange between AWS and
Azure and enables to record Azure resource state. You must create this
before creating the Systems Manager Cloud Connector.

###### Note

The Cloud Connector automatically creates a service-linked role
for federation. You do not need to create a separate IAM role for this
step.

###### To create an Cloud Connector for Azure

1. Create the connector. Replace
   `TENANT_ID` with your Azure tenant ID and
   `CLIENT_ID` with the application (client)
   ID of the Azure AD app you created for .

```
aws configservice put-connector \
    --connector-configuration '{
        "azure": {
            "tenantIdentifier": "`TENANT_ID`",
            "clientIdentifier": "`CLIENT_ID`"
        }
    }'
```

Note the `Arn` from the response — you will need it in the
next step. 2. Confirm the connector was created:

```
aws configservice list-connectors
```
