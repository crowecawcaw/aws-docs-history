# View connector details

Use the following procedures to view the configuration details of a connector in the
console, command line, or API for AWS Private CA Connector for Active Directory.

Console

###### To view details for a connector using the console

1. Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
   `https://console.aws.amazon.com/pca-connector-ad/home`.
2. Choose a connector from the **Connectors for Active
   Directory** list and then choose **View
   details**.
3. On the connector details page, review the information in the Connector
   details, pane, which includes the following:
   - **Connector ID**
   - **Connector status**
   - **Additional status details**
   - **Connector ARN**
   - **Certificate enrollment policy server
     endpoint**
   - **Directory name**
   - **Directory ID**
   - **AWS Private CA subject**
   - **AWS Private CA status**
   - **IP address type**
   - **VPC endpoint and security groups**

4. In the **Templates** pane, you can create or manage templates
   associated with the connector.
5. From the **Service principal name (SPN)** pane, you can view
   the service principle name associated with the connector.
6. From the **Directory Registration** pane, you can view or
   change the directory registration associated with the connector.
7. From the **Tags — _optional_** pane, you can create or manage tags
   associated with the connector.

API
**To list your connectors using the API**

Use the [GetConnector](../../../pca-connector-ad/latest/APIReference/API_GetConnector.md "../../../pca-connector-ad/latest/APIReference/API_GetConnector.md") action in the AWS Private CA Connector for Active Directory API.

CLI
**To list your connectors using the AWS CLI**

Use the [get-connector](../../../cli/latest/reference/pca-connector-ad/get-connector.md "../../../cli/latest/reference/pca-connector-ad/get-connector.md") command in the AWS Private CA Connector for Active Directory section of the AWS CLI.
