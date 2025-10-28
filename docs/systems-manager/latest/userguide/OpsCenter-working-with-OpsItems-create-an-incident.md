# Creating an

incident for an OpsItem

Use the following procedure to manually create an incident for an OpsItem to track
and manage it in AWS Systems Manager Incident Manager, which is a tool in AWS Systems Manager. An _incident_ is any unplanned interruption or reduction in
quality of services. For more information about Incident Manager, see [Integrate OpsCenter with other
AWS services](OpsCenter-applications-that-integrate.md "OpsCenter-applications-that-integrate.md").

###### To manually create an incident for an OpsItem

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **OpsCenter**.
3. If Incident Manager created an OpsItem for you, choose it and go to step 5. If
   not, choose **Create OpsItem** and complete the form. If you
   don't see this button, choose the **OpsItems** tab, and then
   choose **Create OpsItem**.
4. If you created an OpsItem, open it.
5. Choose **Start Incident**.
6. For **Response plan**, choose the Incident Manager response
   plan that you want to assign to this incident.
7. (Optional) For **Title**, enter a descriptive name to
   help other team members understand the nature of the incident. If you don't
   enter a new title, OpsCenter creates the OpsItem and the corresponding incident
   in Incident Manager using the title in the response plan.
8. (Optional) For **Incident impact**, choose an impact
   level for this incident. If you don't choose an impact level, OpsCenter
   creates the OpsItem and the corresponding incident in Incident Manager using the
   impact level in the response plan.
9. Choose **Start**.
