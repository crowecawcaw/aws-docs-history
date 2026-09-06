

# View notification errors
<a name="v9-alerting-viewnotificationerrors"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

View notification errors and understand why they failed to be sent or were not received.

**Note**  
This feature is only supported for Grafana Alertmanager.

**To view notification errors**

1. In the Grafana menu, click the **Alerting** (bell) icon to open the Alerting page listing existing alerts.

1. Choose **Contact points** to see a list of the existing contact points.

   If any contact points are failing, a message at the right-hand corner of the screen alerts the user to the fact that there are errors and how many.

1. Click on a contact point to view the details of errors for that contact point.

   Error details are displayed if you hover over the Error icon.

   If a contact point has more than one integration, you see all errors for each of the integrations listed.

1. In the Health column, check the status of the notification.

   This can be either OK, No attempts, or Error.