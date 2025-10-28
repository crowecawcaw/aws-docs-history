# List connector templates

You can use the AWS Private CA Connector for Active Directory console or AWS CLI to list templates for connectors
that you own. Connector templates are based on AWS Private CA [BlankEndEntityCertificate_APIPassthrough/V1](UsingTemplates.md#BlankEndEntityCertificate_APIPassthrough "UsingTemplates.md#BlankEndEntityCertificate_APIPassthrough") templates.

Console

###### To list your templates using the console

1. Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
   `https://console.aws.amazon.com/pca-connector-ad/home`.
2. Choose a connector from the **Connectors for Active
   Directory** list and then choose **View
   details**.
3. On the connector details page, review the information in the
   **Templates** section. You can navigate through multiple pages
   of templates using the page numbers at upper-right. Each template occupies a row
   displaying the following columns of information.

- **Template name** – The human-readable name of the
  template.
- **Template status** – Status of the template. Possible
  values are: **Active** |
  **Deleting**.
- **Template ID** – The unique identifier of the
  template.

API
**To list your connectors using the API**

Use the [ListTemplates](../../../pca-connector-ad/latest/APIReference/API_ListTemplates.md "../../../pca-connector-ad/latest/APIReference/API_ListTemplates.md") action in the AWS Private CA Connector for Active Directory API to list templates for the
specified connector.

CLI
**To list your connectors using the AWS CLI**

Use the [list-templates](../../../cli/latest/reference/pca-connector-ad/list-templates.md "../../../cli/latest/reference/pca-connector-ad/list-templates.md") command to list templates for the specified connector.
