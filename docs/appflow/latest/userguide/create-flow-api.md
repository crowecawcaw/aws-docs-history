# Create a flow using the Amazon AppFlow APIs

You may also use the APIs to create a connector profile and configure a flow using the
`CreateConnectorProfile` and `CreateFlow` APIs. Due to the varying methods
of authentication across each target application, the specific information provided for connection
creation will vary. Two examples are provided below as a comparison — Salesforce and
ServiceNow.

Program the `CreateConnectorProfile` API to create a connector profile associated
with your AWS account. There is a soft quota of 100 connector profiles per AWS account. If you
need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow
team through the Amazon AppFlow support channel. The following examples creates a new Amazon AppFlow
connection to Salesforce. Note that this leverages a Salesforce Connected App, which itself
requires several steps to configure across AWS and Salesforce. See [Salesforce global connected app](salesforce.md#salesforce-global-connected-app "salesforce.md#salesforce-global-connected-app") for details.

Create Salesforce connection:

```
POST /create-connector-profile HTTP/1.1
Content-type: application/json

{
    "connectorProfileName": "MySalesforceConnection",
    "connectorType": "Salesforce",
    "connectionMode": "Public",
    "connectorProfileConfig": {
        "connectorProfileProperties": {
            "Salesforce": {
                "instanceUrl": "https://<instance-name>.my.salesforce.com",
                "isSandboxEnvironment": false
            }
        },
        "connectorProfileCredentials": {
            "Salesforce": {
                "accessToken": "<access-token-value>",
                "refreshToken": "<refresh-token-value>",
                "oAuthRequest": {
                    "authCode": "<auth-code-value>",
                    "redirectUri": "https://login.salesforce.com/"
                },
                "clientCredentialsArn": "<secret-arn-value>"
            }
        }
    }
}


```

The following examples creates a new Amazon AppFlow connection to ServiceNow. Note that, unlike
Salesforce, there is no pre-requisite configuration for either AWS or ServiceNow.

Create ServiceNow connection

```
POST /create-connector-profile HTTP/1.1
Content-type: application/json

{
    "connectorProfileName": "MyServiceNowConnection",
    "connectorType": "Servicenow",
    "connectionMode": "Public",
    "connectorProfileConfig": {
        "connectorProfileProperties": {
            "ServiceNow": {
                "instanceUrl": "https://<instance-name>.service-now.com",
                "isSandboxEnvironment": false
            }
        },
        "connectorProfileCredentials": {
            "ServiceNow": {
                "username": "<username-value>",
                "password": "<password-value>"
            }
        }
    }
}
```

The following implements a flow from Salesforce to S3 using a previously created Salesforce
connection and S3 bucket, delivering the data in CSV format with all Salesforce source fields
mapped directly.

Create Salesforce to S3 flow

```
POST /create-flow HTTP/1.1
Content-type: application/json

{
    "flowName": "MySalesforceToS3Flow",
    "triggerConfig": {
        "triggerType": "OnDemand"
    },
    "sourceFlowConfig": {
          "connectorType": "Salesforce",
          "connectorProfileName": "MySalesforceConnection",
          "sourceConnectorProperties": {
              "Salesforce": {
                  "object": "Account"
            }
        }
    },
    "destinationFlowConfigList": [{
        "connectorType": "S3",
        "destinationConnectorProperties": {
            "S3": {
                "bucketName": "appflow-demo-destination",
                "s3OutputFormatConfig": {
                    "fileType": "CSV"
                }
            }
        }
    }],
    "tasks": [
        {
            "sourceFields": [],
            "taskType": "Map_all",
            "taskProperties": {}
        }
    ]
}

```

The following starts the flow `MySalesforceToS3Flow` which was created in the
previous step.

Start a flow:

```
POST /start-flow HTTP/1.1
Content-type: application/json

{
   "flowName": "MySalesforceToS3Flow"
}


```

Refer to the [Amazon AppFlow API Reference](../../1.0/APIReference/API_CreateConnectorProfile.md "../../1.0/APIReference/API_CreateConnectorProfile.md") for details about the complete set of Amazon AppFlow APIs.
