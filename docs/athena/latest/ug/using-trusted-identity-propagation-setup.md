# Connect Athena to

IAM Identity Center

The following section lists the process of connecting Athena to IAM Identity Center.

## Setup trusted token

issuer

Follow [Setting up a trusted token issuer](../../../IAM/latest/UserGuide/id_roles_providers_create_oidc.md "../../../IAM/latest/UserGuide/id_roles_providers_create_oidc.md") guide to setup trusted token
issuer. This will create an AWS IAM Identity Center.

###### Note

For **Provider type**, choose **OpenID
Connect**. For **Provider URL**, enter the issuer URL from your
Identity provider. For **Audience**, specify the client ID issued by the
Identity provider for your app.

Copy the Application Resource Name (ARN) for AWS IAM Identity provider.
For more information, see [Identity providers and federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md").

## Setup IAM roles

### Setup IAM application role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the left navigation, choose **Roles** and then
   choose **Create role**.
3. For **Trusted entity type**, choose **Custom
   trust policy** as following:
   1. For **Federated Principal**, add the ARN for
      AWS IAM identity provider that you copied during trusted
      token issuer setup.
   2. For policy condition, add the audience from your external
      federated identity provider.

4. Add the following inline policy to grant access to the user for [CreateTokenWithIAM](../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md "../../../singlesignon/latest/OIDCAPIReference/API_CreateTokenWithIAM.md"), [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md"), and [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md") permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:ListTags*",
 "sso:ListTags*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

`CreateTokenWithIam` permissions are given in
customer managed IAM Identity Center application. 5. Copy the ARN for application role.

### Setup

IAM access role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the left navigation, choose **Roles** and then
   choose **Create role**.
3. For **Trusted entity type**, choose **Custom
   trust policy** as following:
   1. For **Federated Principal**, add the ARN for
      AWS IAM Identity Center copied during trusted token issuer setup.
   2. For **AWS Principal**, add the ARN for
      AWS IAM application role copied during IAM application
      role setup.

4. Add the following **inline policy** to grant access
   for driver workflows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:StartQueryExecution",
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "athena:ListWorkGroups",
 "athena:ListDataCatalogs",
 "athena:ListDatabases",
 "athena:ListTableMetadata"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:CreateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:GetTableVersion",
 "glue:GetTableVersions",
 "glue:DeleteTableVersion",
 "glue:BatchDeleteTableVersion",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:UpdatePartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```

5. Copy the ARN for access role.

## Configure AWS IAM Identity Center

customer managed application

To configure a customer managed application, follow the steps in [Set up customer managed OAuth 2.0 applications for trusted identity
propagation](../../../singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md "../../../singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md") with the following considerations for Athena.

- For **Tags**, add the following key-value pair:
  - **Key** – _AthenaDriverOidcAppArn_
  - **Value** – _AccessRoleARN_ that was copied during
    IAM Access Role setup.

- When [specifying application credentials](../../../singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials "../../../singlesignon/latest/userguide/customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2.md#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials"), add the ARN for AWS IAM
  application role that you copied during IAM application role setup.
- For **Applications that can receive requests**, choose
  _AWS-Lake-Formation-AWS-Glue-Data-Catalog-<account-id>_.
- For **Access scopes to apply**, select _lakeformation:query_ for IAM-enabled workgroups, or _lakeformation:query_, _athena:workgroup:read_write_, and _s3:access_grants:read_write_ for Identity Center-enabled workgroups.

## Configure workgroup

association

1. In the Athena console navigation pane, choose
   **Workgroups**.
2. Choose a workgroup from the list and open the **Tags**
   tab.
3. Choose **Manage tags** and enter the following:
   1. **Key** –
      `AthenaDriverOidcAppArn`
   2. **Value** – ARN for AWS IAM Identity Center
      application.

4. Choose **Save**.

Once administrators complete the one-time setup, they can distribute essential connection details to their users. Users need these five mandatory parameters to run SQL workloads:

1. **ApplicationRoleARN** – The ARN of the
   application role
2. **JwtWebIdentityToken** – The JWT token for
   identity verification
3. **WorkgroupARN** – The ARN of the Athena
   workgroup
4. **JwtRoleSessionName** – The session name for JWT
   role
5. **CredentialsProvider** – The credentials provider
   configuration

###### Note

We've simplified the connection string configuration through strategic
tagging. By properly tagging both the Athena workgroup and AWS IAM Identity Center customer
managed application, administrators eliminate the need for users to provide
`AccessRoleArn` and `CustomerIdcApplicationArn`. The
plugin handles this automatically by using the application role to locate
necessary tags and retrieve corresponding ARN values for its workflow.

Administrators can still make users provide `AccessRoleArn` or
`CustomerIdcApplicationArn` in the connection string by adjusting
the application role permissions as needed.

## Run queries using trusted identity propagation

enabled Athena drivers

Download the latest version of driver that you want to use. For more information
on JDBC installation, see [Get started with the JDBC 3.x
driver](jdbc-v3-driver-getting-started.md "jdbc-v3-driver-getting-started.md"). You can choose to install ODBC
drivers based on the supported platform. For more information, see [Get started with the ODBC 2.x
driver](odbc-v2-driver-getting-started.md "odbc-v2-driver-getting-started.md"). Based on the driver that you
want to use, provide the parameters listed in:

- [JDBC auth plugin
  connection parameters](jdbc-v3-driver-jwt-tip-credentials.md "jdbc-v3-driver-jwt-tip-credentials.md")
- [ODBC auth plugin connection
  parameters](odbc-v2-driver-jwt-tip.md "odbc-v2-driver-jwt-tip.md")

###### Note

Trusted identity propagation with drivers is only available after version 3.6.0 in JDBC and version
2.0.5.0 in ODBC.

## Use Athena drivers and trusted identity propagation

with DBeaver

1. Download the latest JDBC jar with dependencies from Athena. For more
   information, see [Athena JDBC 3.x driver](jdbc-v3-driver.md "jdbc-v3-driver.md").
2. Open the DBeaver application on your computer.
3. Navigate to the **Database** menu at the top of the
   screen, and then choose **Driver Manager**.
4. Choose **New** and then
   **Libraries**.
5. Add the latest driver and choose **Find class**. This
   will give you a file path like
   `com.amazon.athena.jdbc.AthenaDriver`.
6. Open **Settings** tab and provide the following
   fields
   1. **Driver name** – Athena JDBC trusted
      identity propagation
   2. **Class name** –
      `com.amazon.athena.jdbc.AthenaDriver`
   3. Select the option **No authentication**.

7. Choose **Connect to a database** and find Athena JDBC
   trusted identity propagation. This will take you to the JDBC URL. For more
   information, see [Configuring the driver](jdbc-v3-driver-getting-started.md#jdbc-v3-driver-configuring-the-driver "jdbc-v3-driver-getting-started.md#jdbc-v3-driver-configuring-the-driver").
8. Provide the following details
   1. **Workgroup** – The workgroup in which you
      want to run queries. For information about workgroups, see [WorkGroup](../APIReference/API_WorkGroup.md "../APIReference/API_WorkGroup.md").
   2. **Region** – The AWS Region where the
      queries will be run. For a list of regions, see [Amazon Athena endpoints and quotas](../../../general/latest/gr/athena.md "../../../general/latest/gr/athena.md").
   3. **OutputLocation** – The location in Amazon S3
      where you want to store the query results. For information about
      output location, see [ResultConfiguration](../APIReference/API_ResultConfiguration.md "../APIReference/API_ResultConfiguration.md").
   4. **CredentialsProvider** – Enter
      `JWT_TIP`.
   5. **ApplicationRoleArn** – The ARN of the
      role to enable `AssumeRoleWithWebIdentity`. For more
      information about ARN roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the AWS Security Token Service API reference.
   6. **WorkgroupArn** – The ARN of the
      workgroup in which queries will run. It must be the same workgroup
      as provided in the **Workgroup** field . For
      information about workgroups, see [WorkGroup](../APIReference/API_WorkGroup.md "../APIReference/API_WorkGroup.md").
   7. **JwtRoleSessionName** – The name of the
      session when you use JWT credentials for authentication. It can be
      any name of your choice.
   8. **JwtWebIdentityToken** – The JWT token
      obtained from an external federated identity provider. This token is
      used to authenticate with Athena.

   ```
   jdbc:athena://Workgroup=`<value>`;Region=`<region>`;OutputLocation=`<location>`;CredentialsProvider=JWT_TIP;ApplicationRoleArn=`<arn>`;WorkgroupArn=`<arn>`;JwtRoleSessionName=JDBC_TIP_SESSION;JwtWebIdentityToken=`<token>`;
   ```

9. Choose **OK** and close the window. DBeaver will start
   loading your metadata after this step and you should start seeing your
   catalogs, databases, and tables getting populated.

###### Note

If JTI claim is present in the token and you choose **Test
connection** before choosing **OK**, it
prevents the same JTI from being reused for token exchanges. For more
information, see [Prerequisites and considerations for trusted token issuers](../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md#trusted-token-issuer-prerequisites "../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md#trusted-token-issuer-prerequisites").
To handle this, JDBC implements an in-memory cache, whose lifecycle is
dependent on the main driver instance. For ODBC, a [file cache](odbc-v2-driver-jwt-tip.md#odbc-v2-driver-jwt-tip-file-cache "odbc-v2-driver-jwt-tip.md#odbc-v2-driver-jwt-tip-file-cache") is
optionally present that enables temporary credentials to be cached and
reused to reduce the number of web identity tokens used during session
lifecycle. 10. Open **SQL query editor** and start running your queries.
See [Cloudtrail logs](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to verify the propagated identity of the
user.
