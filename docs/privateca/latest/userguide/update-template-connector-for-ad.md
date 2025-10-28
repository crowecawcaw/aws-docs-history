# Update a template for Active Directory

Use the following procedures to update a template using the console, command line, or API
for AWS Private CA Connector for Active Directory.

Console

###### To update a template using the console

Sign in to your AWS account and open the AWS Private CA Connector for Active Directory console at
`https://console.aws.amazon.com/pca-connector-ad/home`.

1. On the list of your **Connectors for Active
   Directory**, select the connector whose template that you'd like to update. Choose **Edit** to view and modify the connector's templates.
2. In your connector's template details page, choose **Edit**. Follow the prompts to make your updates. When you're done editing an area, choose **Save** to save your changes.

API
**To update a template using the API**

To update a template for Active Directory with the API, use the [UpdateTemplate](../../../pca-connector-ad/latest/APIReference/API_UpdateTemplate.md "../../../pca-connector-ad/latest/APIReference/API_UpdateTemplate.md") action in the AWS Private CA Connector for Active Directory API.

CLI
**To update a template using the AWS CLI**

To update a connector for Active Directory with the CLI, use the [update-template](../../../cli/latest/reference/pca-connector-ad/update-template.md "../../../cli/latest/reference/pca-connector-ad/update-template.md") command in the AWS Private CA Connector for Active Directory section of the
AWS CLI.

## How Connector for Active Directory propagates your template changes

AWS Private CA applies template to your policy when your client refreshes the policy cache, which is every
eight hours. This includes changes to template group access control entries. When your client refreshes the cache, it queries the connector for available templates. In the case of auto-enrollment refresh, the client issues certificates that match either or both of the following conditions:

- The certificate is within the renewal period.
- The certificate isn't present on the client device.

For _manual refresh_, the client will query the connector, and you must set the template to issue.

If you're debugging, you can manually clear the policy cache to immediately see the template changes. To do so, run the following Powershell command on your client.

```
certutil -f -user -policyserver * -policycache delete
```
