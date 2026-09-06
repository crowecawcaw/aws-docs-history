

# View notification errors
<a name="v10-alerting-manage-viewnotificationerrors"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 10.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

View notification errors and understand why they failed to be sent or were not received.

**Note**  
This feature is only supported for Grafana Alertmanager.

**To view notification errors**

1. From the left menu, choose **Alerting** then **Contact points**.

   If any contact points are failing, a message at the right-hand corner of the workspace tells you that there are errors, and how many.

1. Select a contact point to view the details of errors for that contact point.

   Error details are displayed if you hover over the Error icon.

   If a contact point has more than one integration, you see all errors for each of the integrations listed.

1. In the Health column, check the status of the notification.

   This can be either OK, No attempts, or Error.