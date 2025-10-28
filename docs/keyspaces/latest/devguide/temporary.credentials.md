# Create temporary credentials to connect to Amazon Keyspaces using an IAM role and the SigV4 plugin

The recommended way to access Amazon Keyspaces programmatically is by using [temporary credentials](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") to authenticate with the SigV4 plugin.
In many scenarios, you don't need long-term access keys that never expire (as you have with an IAM user). Instead, you can create an IAM role and generate
temporary security credentials. Temporary security credentials consist of an access key ID and a secret access key, but they also include a security token that
indicates when the credentials expire. To learn more about how to use IAM roles instead of long-term access keys, see [Switching to an IAM role (AWS API)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md").

To get started with temporary credentials, you first need to create an IAM role.

###### Create an IAM role that grants read-only access to Amazon Keyspaces

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, then **Create
   role**.
3. On the **Create role** page, under **Select type of trusted
   entity**, choose **AWS service**. Under
   **Choose a use case**, choose **Amazon EC2**,
   then choose **Next**.
4. On the **Add permissions** page, under **Permissions
   policies**, choose **Amazon Keyspaces Read Only
   Access** from the policy list, then choose
   **Next**.
5. On the **Name, review, and create** page, enter a name for the role, and review the **Select trusted entities** and
   **Add permissions** sections.
   You can also add optional tags for the role on this page. When you are done,
   select **Create role**. Remember this name because you’ll need
   it when you launch your Amazon EC2 instance.
   To use temporary security credentials in code, you programmatically call an AWS Security Token Service API like `AssumeRole` and extract the resulting credentials
   and session token from your IAM role that you created in the previous step. You then use those values as credentials for subsequent calls to AWS.
   The following example shows pseudocode for how to use
   temporary security credentials:

```
assumeRoleResult = AssumeRole(role-arn);
tempCredentials = new SessionAWSCredentials(
   assumeRoleResult.AccessKeyId,
   assumeRoleResult.SecretAccessKey,
   assumeRoleResult.SessionToken);
cassandraRequest = CreateAmazoncassandraClient(tempCredentials);
```

For an example that implements temporary credentials using the Python driver to access
Amazon Keyspaces, see [Connect to Amazon Keyspaces using the DataStax
Python driver for Apache Cassandra and the SigV4 authentication plugin](using_python_driver.md#python_SigV4 "using_python_driver.md#python_SigV4").

For details about how to call `AssumeRole`, `GetFederationToken`,
and other API operations, see
the [AWS Security Token Service API Reference](../../../STS/latest/APIReference.md "../../../STS/latest/APIReference.md").
For information on getting the temporary security credentials and
session token from the result, see the documentation for the SDK that you're working with. You
can find the documentation for all the AWS SDKs on the main [AWS documentation page](http://aws.amazon.com/documentation "http://aws.amazon.com/documentation"), in the
**SDKs and Toolkits** section.
