

# Managing Amazon AppFlow connections
<a name="connections"></a>

To enable data flows in Amazon AppFlow, you provide access to your source and destination applications by creating *connections*. Connections store the configuration details and credentials that Amazon AppFlow requires to transfer data with applications on your behalf. For example, these details include your user names, passwords, secret keys, and API access tokens. After you create a connection, you can assign it to new or existing flows without manually entering the configuration details anew.

Use the following sections to work with your connections by using the Amazon AppFlow console, AWS CLI, or the Amazon AppFlow API. Connections are also called *connector profiles* in the AWS CLI and Amazon AppFlow API.

## Amazon AppFlow console
<a name="connections-"></a>

Complete the following steps to manage your connections by using the Amazon AppFlow console.

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).
**Note**  
 If **multi-session support** is enabled, disable the **multi-session support** feature in the AWS Management Console to enable the 3-leg OAuth process during connection setup. For more information, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html). 

1. In the navigation pane, select **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose the application that your connection accesses. For example, if your connection enables data to flow to Amazon Redshift, you would choose **Amazon Redshift**.

1. After you choose a connector, you can do any of the following:
   + To create a connection, choose **Create connection**, and provide the required details. These details vary for each type of connector application. For application-specific instructions, find your application under [Supported source and destination applications](app-specific.md).
   + To view the details for a connection, choose its name in the **Connection name** column.
   + To edit a connection, select it and choose **Edit**.
   + To copy a connection, select it and choose **Copy to new connection**. The console shows a window where you configure a new connection, and it copies the initial settings from the connection that you selected. You can modify these settings before you create the new connection.

     Amazon AppFlow doesn't copy OAuth credentials, such as client secret and client ID. For connections that require those credentials, you must provide them anew.
   + To delete a connection, select it and choose **Delete**.

## AWS CLI
<a name="connections-"></a>

You can manage your connections in Amazon AppFlow by running commands with the AWS CLI.

**To create a connection**
+ Run the [`create-connector-profile`](https://docs.aws.amazon.com/cli/latest/reference/appflow/create-connector-profile.html) command. In this command, you provide configuration details and credentials for the `--connector-profile-config` parameter. The required details vary for each type of connector application.

  The following example creates a connection for SAP OData, and it provides the configuration details in a JSON file:

  ```
  $ aws appflow create-connector-profile \
  > --connector-profile-name {{sap-odata-connection}} \
  > --connector-type {{SAPOData}} \
  > --connection-mode {{Public}} \
  > --connector-profile-config {{file://sap-odata-connector-profile-config.json}}
  ```

  The `sap-odata-connector-profile-config.json` file contains the following configuration details: 

  ```
  {
    "connectorProfileProperties":
    {
      "SAPOData":
      {
        "applicationHostUrl": "https://example.connection.url",
        "applicationServicePath": "/sap/opu/odata/example/path;v=2",
        "portNumber": 443,
        "clientNumber": "100",
        "logonLanguage": "EN"
      }
    },
    "connectorProfileCredentials":
    {
      "SAPOData":
      {
        "basicAuthCredentials":
        {
          "username": "username",
          "password": "password"
        }
      }
    }
  }
  ```

  The command response provides the Amazon Resource Name (ARN) of the new connection:

  ```
  {
      "connectorProfileArn": "arn:aws:appflow:us-east-1:111122223333:connectorprofile/sap-odata-connection"
  }
  ```

**To view the details for all of your connections**
+ Run the [`describe-connector-profiles`](https://docs.aws.amazon.com/cli/latest/reference/appflow/describe-connector-profiles.html) command:

  ```
  $ aws appflow describe-connector-profiles
  ```

  The command response is a JSON body with details for each of your connections. The following example response shows the details for an SAP OData connection:

  ```
  {
      "connectorProfileDetails": [
          {
              "connectorProfileArn": "arn:aws:appflow:regionus-east-1:111122223333:connectorprofile/sap-odata-connection",
              "connectorProfileName": "sap-odata-connection",
              "connectorType": "SAPOData",
              "connectionMode": "Public",
              "credentialsArn": "arn:aws:secretsmanager:us-east-1:111122223333:secret:appflow!111122223333-sap-odata-connection",
              "connectorProfileProperties": {
                  "SAPOData": {
                      "applicationHostUrl": "https://example.connection.url",
                      "applicationServicePath": "/sap/opu/odata/example/path;v=2",
                      "portNumber": 443,
                      "clientNumber": "100",
                      "logonLanguage": "EN"
                  }
              },
              "createdAt": "2022-02-22T15:31:41.467000-08:00",
              "lastUpdatedAt": "2022-02-22T15:31:41.467000-08:00"
          }
      ]
  }
  ```

**To view the details for specific connections**
+ Run the `describe-connector-profiles` command, and filter the results by using the `--connector-profile-names` or `--connector-type` parameters. The following example gets the details for a single connection:

  ```
  $ aws appflow describe-connector-profiles --connector-profile-names {{sap-odata-connection}}
  ```

**To edit a connection**
+ Run the [`update-connector-profile`](https://docs.aws.amazon.com/cli/latest/reference/appflow/update-connector-profile.html) command. For this command, you provide the updated configuration details for the `--connector-profile-config` parameter. The following example provides the updated configuration in a JSON file:

  ```
  $ aws appflow update-connector-profile \
  > --connector-profile-name {{sap-odata-connection}} \
  > --connection-mode {{Public}} \
  > --connector-profile-config {{file://sap-odata-connector-profile-config.json}}
  ```

**To delete a connection**
+ Run the [`delete-connector-profile`](https://docs.aws.amazon.com/cli/latest/reference/appflow/delete-connector-profile.html) command.

  ```
  $ aws appflow delete-connector-profile --connector-profile-name {{sap-odata-connection}}
  ```

## Amazon AppFlow API
<a name="connections-"></a>

You can manage your connections by using the following actions in the Amazon AppFlow API:
+ [CreateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_CreateConnectorProfile.html) – Creates a connection.
+ [DescribeConnectorProfiles](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DescribeConnectorProfiles.html) – Provides details about your connections.
+ [UpdateConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpdateConnectorProfile.html) – Edits a connection.
+ [DeleteConnectorProfile](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DeleteConnectorProfile.html) – Deletes a connection.