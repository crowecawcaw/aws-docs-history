# Create a flow using the AWS CLI

You may also use the [CLI](../../../cli/latest/reference/appflow/index.md "../../../cli/latest/reference/appflow/index.md") to create a
connector profile and configure a flow using the AWS CLI commands for
**create-connector-profile** and **create-flow**. Due to the
varying methods of authentication across each target application, the specific information
provided for connection creation will vary. Two examples are provided here as a comparison —
Salesforce and ServiceNow.

Run the **create-connector-profile** command to create the connector profile
for your flow. The following example creates a new Amazon AppFlow connection to Salesforce. Note that
this leverages a Salesforce Connected App, which itself requires several steps to configure across
AWS and Salesforce. See [Salesforce global connected app](salesforce.md#salesforce-global-connected-app "salesforce.md#salesforce-global-connected-app") for details.

Create Salesforce connection:

```
aws appflow create-connector-profile \
    --connector-profile-name MySalesforceConnection \
    --connector-type Salesforce \
    --connection-mode Public \
    --connector-profile-config ' {
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
            }'


```

Run the **create-connector-profile** command to begin creating your flow. The
following example creates a new Amazon AppFlow connection to ServiceNow. Note that, unlike Salesforce,
there is no prerequisite configuration for either AWS or ServiceNow.

Create ServiceNow connection:

```
aws appflow create-connector-profile \
    --connector-profile-name MyServiceNowConnection \
    --connector-type Servicenow \
    --connection-mode Public \
    --connector-profile-config ' {
                "connectorProfileProperties": {
                    "ServiceNow": {
                        "instanceUrl": "https://<instance-name>.service-now.com"
                    }
                },
                "connectorProfileCredentials": {
                    "ServiceNow": {
                        "username": "<username-value>",
                        "password": "<password-value>"
                    }
                }
            }'
```

Run the **create-flow** command to begin creating your flow. The following
implements a flow from Salesforce to S3 using a previously created Salesforce connection and S3
bucket, delivering the data in CSV format with all Salesforce source fields mapped
directly.

Create Salesforce to S3 flow:

```
aws appflow create-flow \
    --flow-name MySalesforceToS3Flow \
    --trigger-config '{
                "triggerType": "OnDemand"
            }' \
    --source-flow-config '{
                  "connectorType": "Salesforce",
                  "connectorProfileName": "MySalesforceConnection",
                  "sourceConnectorProperties": {
                      "Salesforce": {
                          "object": "Account"
                    }
                }
            }' \
    --destination-flow-config '[{
                "connectorType": "S3",
                "destinationConnectorProperties": {
                    "S3": {
                        "bucketName": "<s3-bucket-name>",
                        "s3OutputFormatConfig": {
                            "fileType": "CSV"
                        }
                    }
                }
           }]' \
    --tasks '[
                {
                    "sourceFields": [],
                    "taskType": "Map_all",
                    "taskProperties": {}
                }
            ]'
```

Run the **start-flow** command to start your flow. For on-demand flows, this
operation runs the flow immediately. For schedule and event-triggered flows, this operation
activates the flow. The following starts the flow `MySalesforceToS3Flow` which was
created in the previous step.

```
aws appflow start-flow --flow-name MySalesforceToS3Flow


```

The describe-flow command is helpful for understanding how previously created flows,
including flows created through the Console, are structured.

Describe a flow:

```
aws appflow describe-flow --flow-name MySalesforceToS3Flow
```

Refer to the [AWS
CLI Command Reference for Amazon AppFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html") for additional details about the complete list of
commands available for Amazon AppFlow.
