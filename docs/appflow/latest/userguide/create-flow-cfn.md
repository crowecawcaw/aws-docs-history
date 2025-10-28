# Create a flow using CloudFormation resources

You may also use CloudFormation to create a connector profile and configure a flow using the
`AWS::AppFlow::ConnectorProfile` and `AWS::AppFlow::Flow` resources. The
following example creates a new Amazon AppFlow connection to Salesforce. Note that this leverages a
Salesforce Connected App, which itself requires several steps to configure across AWS and
Salesforce. See [Salesforce global connected app](salesforce.md#salesforce-global-connected-app "salesforce.md#salesforce-global-connected-app") for details.

Declare the `AWS::AppFlow::ConnectorProfile` entity in your CloudFormation template
with the following JSON syntax:

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources": {
    "MySalesforceConnection": {
      "Type" : "AWS::AppFlow::ConnectorProfile",
      "Properties": {
        "ConnectorProfileName": "MySalesforceConnection",
        "ConnectorType": "Salesforce",
        "ConnectionMode": "Public",
        "ConnectorProfileConfig": {
          "ConnectorProfileProperties": {
            "Salesforce": {
              "InstanceUrl": "https://<instance-name>.my.salesforce.com",
              "IsSandboxEnvironment": false
            }
          },
          "ConnectorProfileCredentials": {
            "Salesforce": {
              "AccessToken": "<access-token-value>",
              "RefreshToken": "<refresh-token-value>",
              "ConnectorOAuthRequest": {
                "AuthCode": "<auth-code-value>",
                "RedirectUri": "https://login.salesforce.com/"
              },
              "ClientCredentialsArn": "<secret-arn-value>"
            }
          }
        }
      }
    }
  }
}


```

Following is an example of YAML syntax:

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MySalesforceConnection:
    Type: AWS::AppFlow::ConnectorProfile
    Properties:
      ConnectorProfileName: MySalesforceConnection
      ConnectorType: Salesforce
      ConnectionMode: Public
      ConnectorProfileConfig:
        ConnectorProfileProperties:
          Salesforce:
            InstanceUrl: https://<instance-name>.my.salesforce.com
            IsSandboxEnvironment: false
        ConnectorProfileCredentials:
          Salesforce:
            AccessToken: <access-token-value>
            RefreshToken: <refresh-token-value>
            ConnectorOAuthRequest:
              AuthCode: <auth-code-value>
              RedirectUri: https://login.salesforce.com/
            ClientCredentialsArn: <secret-arn-value>

```

The following examples creates a new Amazon AppFlow connection to ServiceNow.

Create ServiceNow connection - JSON

```

{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources": {
    "MyServiceNowConnection": {
      "Type" : "AWS::AppFlow::ConnectorProfile",
      "Properties": {
        "ConnectorProfileName": "MyServiceNowConnection",
        "ConnectorType": "Servicenow",
        "ConnectionMode": "Public",
        "ConnectorProfileConfig": {
          "ConnectorProfileProperties": {
            "ServiceNow": {
              "InstanceUrl": "https://<instance-name>.service-now.com",
            }
          },
          "ConnectorProfileCredentials": {
            "ServiceNow": {
              "Username": "<username-value>",
              "Password": "<password-value>"
            }
          }
        }
      }
    }
  }
}

```

The following is an example of YAML syntax that creates a new Amazon AppFlow connection to
ServiceNow.

Create ServiceNow connection - YAML:

```

AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyServiceNowConnection:
    Type: AWS::AppFlow::ConnectorProfile
    Properties:
      ConnectorProfileName: MyServiceNowConnection
      ConnectorType: Servicenow
      ConnectionMode: Public
      ConnectorProfileConfig:
        ConnectorProfileProperties:
          ServiceNow:
            InstanceUrl: https://<instance-name>.service-now.com
        ConnectorProfileCredentials:
          ServiceNow:
            Username: <username-value>
            Password: <password-value>


```

The following implements a flow from Salesforce to S3 using a previously created Salesforce
connection and S3 bucket, delivering the data in CSV format with all Salesforce source fields
mapped directly.

Create Salesforce to S3 flow - JSON:

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources": {
    "MySalesforceToS3Flow": {
      "Type" : "AWS::AppFlow::Flow",
      "Properties": {
        "FlowName": "MySalesforceToS3Flow",
        "TriggerConfig": {
          "TriggerType": "OnDemand"
        },
        "SourceFlowConfig": {
          "ConnectorType": "Salesforce",
          "ConnectorProfileName": "MySalesforceConnection",
          "SourceConnectorProperties": {
            "Salesforce": {
                "Object": "Account"
            }
          }
        },
        "DestinationFlowConfigList" : [{
          "ConnectorType": "S3",
          "DestinationConnectorProperties": {
            "S3": {
              "BucketName": "<s3-bucket-name>",
              "S3OutputFormatConfig": {
                "FileType": "CSV"
              }
            }
          }
        }],
        "Tasks": [
          {
            "TaskType": "Map_all",
            "SourceFields": [],
            "TaskProperties": [{
              "Key": "EXCLUDE_SOURCE_FIELDS_LIST",
              "Value": "[]"
            }],
            "ConnectorOperator": {
              "Salesforce": "NO_OP"
            }
          }
        ]
      }
    }
  }
}
```

The following implements a flow from Salesforce to S3 using a previously created Salesforce
connection and S3 bucket, delivering the data in CSV format with all Salesforce source fields
mapped directly.

Create Salesforce to S3 flow - YAML:

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MySalesforceToS3Flow:
    Type: AWS::AppFlow::Flow
    Properties:
      FlowName: MySalesforceToS3Flow
      TriggerConfig:
        TriggerType: OnDemand
      SourceFlowConfig:
        ConnectorType: Salesforce
        ConnectorProfileName: MySalesforceConnection
        SourceConnectorProperties:
          Salesforce:
            Object: Account
      DestinationFlowConfigList:
        - ConnectorType: S3
          DestinationConnectorProperties:
            S3:
              BucketName: <s3-bucket-name>
              S3OutputFormatConfig:
                FileType: CSV
      Tasks:
        - TaskType: Map_all
          SourceFields: []
          TaskProperties:
          - Key: EXCLUDE_SOURCE_FIELDS_LIST
            Value: '[]'
          ConnectorOperator:
            Salesforce: NO_OP
```

Refer to the [AWS
CloudFormation User Guide Amazon AppFlow chapter](../../../AWSCloudFormation/latest/UserGuide/AWS_AppFlow.md "../../../AWSCloudFormation/latest/UserGuide/AWS_AppFlow.md") for details about the complete set of
resource options for all sources and destinations.
