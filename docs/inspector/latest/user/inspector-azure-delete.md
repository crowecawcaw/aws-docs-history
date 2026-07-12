# Deleting an Azure connector in Amazon Inspector

You can delete an Azure connector when you no longer want Amazon Inspector to scan
resources in that Azure tenant.

###### What happens when you delete a connector

When you delete an Azure connector:

- Amazon Inspector stops scanning all Azure resources associated with
  the connector.
- Existing findings for Azure resources are
  closed.
- Azure resources no longer appear in the Coverage
  view.
- If a service-linked connector exists (created via
  AWS Security Hub CSPM), deleting a customer-managed connector does not affect the
  service-linked connector. Amazon Inspector continues scanning through the
  service-linked connector.
- The Azure app registration, Event Hub infrastructure, and
  permissions configured in your Azure environment are
  _not_ automatically removed. You must clean up Azure
  resources manually if they are no longer needed by other AWS
  services.

###### Note

If you share the Azure app registration with AWS Security Hub CSPM or AWS Security Hub CSPM
CSPM, do not delete the app registration after removing the Amazon Inspector
connector. Other services still depend on it.

###### Deleting a connector

###### To delete an Azure connector

1. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, choose **Integrations**.
3. Select the Azure connector you want to delete.
4. Choose **Delete**.
5. In the confirmation dialog, enter
   `delete` and choose **Delete connector**.
   You can also delete a connector by using the
   `inspector2:DeleteConnector` API operation.

###### Important

If you delete a connector and create a new one within 6 hours, resource
detection may take up to 6 hours. Plan connector deletion and recreation
accordingly.
