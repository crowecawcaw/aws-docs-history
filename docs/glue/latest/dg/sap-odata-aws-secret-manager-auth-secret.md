# AWS Secrets Manager to store your Auth secret

You will need to store the SAP OData connection secrets in AWS Secrets Manager, configure the necessary permissions for retrieval as specified in the [IAM policies](sap-odata-configuring-iam-permissions.md "sap-odata-configuring-iam-permissions.md") section, and use it while creating a connection.

Use the AWS Management Console for AWS Secrets Manager to create a secret for your SAP source. For more information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). Details in AWS Secrets Manager should include the elements in the following code.

## Custom Authentication Secret

You will need to enter your SAP system username in place of _<your SAP username>_ and its password in place of _<your SAP username password>_ and True or False. In this context, setting `basicAuthDisableSSO` to `true` disables Single Sign-On (SSO) for Basic Authentication requests, requiring explicit user credentials for each request. Conversely, setting it to `false` allows the use of existing SSO sessions if available.

```
{
   "basicAuthUsername": "<your SAP username>",
   "basicAuthPassword": "<your SAP username password>",
   "basicAuthDisableSSO": "<True/False>",
   "customAuthenticationType": "CustomBasicAuth"
}
```

## OAuth 2.0 Secret

In case you are using OAuth 2.0 as your authentication mechanism, the secret in the AWS Secrets Manager should have the **User Managed Client Application ClientId** in the following format. You will need to enter your SAP client secret in place of <your client secret>.

```
{"USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET": "<your client secret>"
}
```
