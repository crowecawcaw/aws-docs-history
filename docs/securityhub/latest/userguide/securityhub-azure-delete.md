# Deleting a Microsoft Azure connector in Security Hub CSPM

After you create a Microsoft Azure connector in AWS Security Hub CSPM, you can delete it at any time. If you
delete a connector, Security Hub CSPM stops performing posture management checks and vulnerability
monitoring for your Azure environment. Security Hub CSPM also stops generating new findings about your
environment. Your existing findings are retained for 90 days. Resource inventory remains as it
was when the connector was deleted and is removed after 90 days.

When you delete a connector, note the following:

- Security Hub CSPM doesn't delete the Azure application registration and Event Hub infrastructure in
  your Azure environment. You must delete these manually, directly in Microsoft Azure. To learn how,
  see [Remove an application](https://learn.microsoft.com/en-us/entra/identity-platform/howto-remove-app "https://learn.microsoft.com/en-us/entra/identity-platform/howto-remove-app") in the Microsoft Azure documentation.
- If the connector is a customer-managed connector and a service-linked connector also
  exists, deleting the customer-managed connector does not affect the service-linked connector.
  Security Hub CSPM continues to receive posture management findings through the service-linked
  connector.
- Existing findings transition to an archived state within 3-5 days and are deleted after
  the 90-day retention period.

###### To delete an Azure connector

1. Open the Security Hub CSPM console.
2. In the navigation pane, choose **Integrations**.
3. Select your connector.
4. Choose **Delete**.
5. When prompted, confirm that you want to delete the connector.
   After deletion, you can optionally clean up the Azure resources that were created during
   setup:

- Delete the app registration in Microsoft Entra ID.
- Delete the Event Hub namespace and resource group.
- Remove the diagnostic settings that export Activity Logs and Entra ID Audit Logs.
