For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Setting up IAM Identity Provider and roles in AWS

Complete each section below to set up IAM for Timestream for LiveAnalytics JDBC single sign-on
authentication with Microsoft Azure AD:

###### Topics

- [Create a SAML Identity Provider](#JDBC.withAzureAD.IAM.SAML "#JDBC.withAzureAD.IAM.SAML")
- [Create an IAM role](#JDBC.withAzureAD.IAM.roleForIAM "#JDBC.withAzureAD.IAM.roleForIAM")
- [Create an IAM policy](#JDBC.withAzureAD.IAM.policyForIAM "#JDBC.withAzureAD.IAM.policyForIAM")
- [Provisioning](#JDBC.withAzureAD.IAM.provisioning "#JDBC.withAzureAD.IAM.provisioning")

## Create a SAML Identity Provider

To create a SAML Identity Provider for the Timestream for LiveAnalytics JDBC single sign-on
authentication with Microsoft Azure AD, complete the following steps:

1. Sign in to the AWS Management Console
2. Choose **Services** and select
   **IAM** under Security, Identity, &
   Compliance
3. Choose **Identity providers** under Access
   management
4. Choose **Create Provider** and choose
   **SAML** as the provider type. Enter the
   **Provider Name**. This example will use
   AzureADProvider.
5. Upload the previously downloaded Federation Metadata XML file
6. Choose **Next**, then choose
   **Create**.
7. Upon completion, the page will be redirected back to the Identity
   providers page

## Create an IAM role

To create an IAM role for the Timestream for LiveAnalytics JDBC single sign-on authentication
with Microsoft Azure AD, complete the following steps:

1. On the sidebar select **Roles** under Access
   management
2. Choose Create role
3. Choose **SAML 2.0 federation** as the trusted
   entity
4. Choose the **Azure AD provider**
5. Choose **Allow programmatic and AWS Management Console
   access**
6. Choose **Next: Permissions**
7. Attach permissions policies or continue to Next:Tags
8. Add optional tags or continue to Next:Review
9. Enter a Role name. This example will use AzureSAMLRole
10. Provide a role description
11. Choose **Create Role** to complete

## Create an IAM policy

To create an IAM policy for the Timestream for LiveAnalytics JDBC single sign-on authentication
with Microsoft Azure AD complete the following steps:

1. On the sidebar, choose **Policies** under Access
   management
2. Choose **Create policy** and select the
   **JSON** tab
3. Add the following policy

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:ListAccountAliases"
 ],
 "Resource": "*"
 }
]
}`

```

4. Choose **Create policy**
5. Enter a policy name. This example will use
   TimestreamAccessPolicy.
6. Choose **Create Policy**
7. On the sidebar, choose **Roles** under Access
   management.
8. Choose the previously created **Azure AD role** and
   choose **Attach policies** under Permissions.
9. Select the previously created access policy.

## Provisioning

To provision the identity provider for Timestream for LiveAnalytics JDBC single sign-on
authentication with Microsoft Azure AD, complete the following steps:

1. Go back to Azure Portal
2. Choose **Azure Active Directory** in the list of
   Azure services. This will redirect to the Default Directory page
3. Choose **Enterprise Applications** under the Manage
   section on the sidebar
4. Choose **Provisioning**
5. Choose **Automatic mode** for the Provisioning
   Method
6. Under Admin Credentials, enter your
   **AwsAccessKeyID** for clientsecret, and
   **SecretAccessKey** for Secret Token
7. Set the **Provisioning Status** to
   **On**
8. Choose **save**. This allows Azure AD to load the
   necessary IAM Roles
9. Once the Current cycle status is completed, choose **Users and
   groups** on the sidebar
10. Choose **+ Add user**
11. Choose the Azure AD user to provide access to Timestream for LiveAnalytics
12. Choose the IAM Azure AD role and the corresponding Azure Identity
    Provider created in AWS
13. Choose **Assign**
