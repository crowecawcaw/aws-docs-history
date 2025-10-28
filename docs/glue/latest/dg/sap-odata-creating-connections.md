# Create connections

To configure an SAP OData connection:

1. Sign in to the AWS Management Console and open the [AWS Glue console](https://console.aws.amazon.com/glue "https://console.aws.amazon.com/glue"). In the AWS Glue Studio, create a connection by following the steps below:
   1. Click Data connections on the left panel.
   2. Click on Create connection.
   3. Select **SAP OData** in **Choose data source**
   4. Provide the **Application host URL** of the SAP OData instance you want to connect to. This application host url must be accessible over public internet for non VPC connection.
   5. Provide the **Application service path** of the SAP OData instance you want to connect to. This is the same as the catalog service path. For example: `/sap/opu/odata/iwfnd/catalogservice;v=2`. AWS Glue doesn’t accept specific object path.
   6. Provide the **Client number** of the SAP OData instance you want to connect to. Acceptable values are [001-999]. Example: 010
   7. Provide the **Port number** of the SAP OData instance you want to connect to. Example: 443
   8. Provide the **Logon language** of the SAP OData instance you want to connect to. Example: EN
   9. Select the AWS IAM role which AWS Glue can assume and has permissions as outlined in the [IAM policies](sap-odata-configuring-iam-permissions.md "sap-odata-configuring-iam-permissions.md") section.
   10. Select the **Authentication Type** which you want to use for this connection in AWS Glue from the dropdown list: OAUTH2 or CUSTOM
       1. CUSTOM - Select the secret you created as specified in the [AWS Secrets Manager to store your Auth secret](sap-odata-aws-secret-manager-auth-secret.md "sap-odata-aws-secret-manager-auth-secret.md") section.
       2. OAUTH 2.0 - enter the following inputs only in case of OAuth 2.0:
          1. Under **User Managed Client Application ClientId**, enter your client id.
          2. `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` (your client secret) in the AWS Secrets Manager that you created in the [AWS Secrets Manager to store your Auth secret](sap-odata-aws-secret-manager-auth-secret.md "sap-odata-aws-secret-manager-auth-secret.md") section.
          3. Under **Authorization Code URL**, enter your authorization code URL.
          4. Under **Authorization Tokens URL**, enter your authorization token URL.
          5. Under **OAuth Scopes**, enter your OAuth scopes separated by space. Example: `/IWFND/SG_MED_CATALOG_0002 ZAPI_SALES_ORDER_SRV_0001`

   11. Select the network options if you want to use your network. For more details, see [Connectivity / VPC Connection](sap-odata-connectivity-vpc-connection.md "sap-odata-connectivity-vpc-connection.md").

2. Grant the IAM role associated with your AWS Glue job permission to read `secretName`. For more details, see the [IAM policies](sap-odata-configuring-iam-permissions.md "sap-odata-configuring-iam-permissions.md").
3. Choose **Test connection** and test your connection. If the connection test passes, click next, enter your connection name and save your connection. Test connection functionality is not available if you have chosen Network options (VPC).
