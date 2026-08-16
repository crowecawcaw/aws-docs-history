# Deleting a Microsoft Azure connector in Security Hub

After you create a Microsoft Azure connector in AWS Security Hub, you can delete it at any time. If you
delete a connector, Security Hub stops performing posture management checks and vulnerability
monitoring for your Azure environment. Security Hub also stops generating new findings and other data
about your environment. Your existing findings are retained for 90 days. Resource inventory
remains as it was when the connector was deleted and is removed after 90 days.

When you delete a connector, Security Hub automatically deletes the associated
service-linked connectors in AWS Security Hub CSPM and Amazon Inspector. Security Hub does not delete the Azure
application registration and Event Hub infrastructure in your Azure environment. You must delete
these manually, directly in Microsoft Azure. To learn how, see [Remove an
application](https://learn.microsoft.com/en-us/entra/identity-platform/howto-remove-app "https://learn.microsoft.com/en-us/entra/identity-platform/howto-remove-app") in the Microsoft Azure documentation.

###### To delete an Azure connector

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1. "https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.").
2. In the navigation pane, choose **Integrations**.
3. Select the connector that you want to delete.
4. Choose **Delete**.
5. When prompted, confirm that you want to delete the connector.

###### Important

If you delete a connector and create a new one within 6 hours, resource detection
may take up to 6 hours. Plan connector deletion and recreation accordingly.
