# Using Quick action connectors in

threshold alerts

## Prerequisites

Before you begin, make sure to
[create at least one action connector](builtin-services-integration.md "builtin-services-integration.md").

The connector must meet these requirements:

- Uses the **Service Auth** authentication method
- Uses one of the following integrations:
  - Atlassian Jira Cloud
  - Microsoft Outlook
  - Salesforce
  - ServiceNow

## Enable Quick actions on a dashboard

to use action connectors

###### To enable Quick actions on a dashboard to use action connectors

1. If a dashboard exists, go to the source analysis of the dashboard. Otherwise,
   [create a new analysis](quickstart-createanalysis.md "quickstart-createanalysis.md").
2. Choose **Publish**.
3. Choose between **New Dashboard** or
   **Replace existing dashboard**.
4. Choose the **Enable Quick actions** checkbox
   under **Dashboard options**.
5. Choose **Publish dashboard**.

## Use action connectors in a threshold alert

###### To use action connectors in a threshold alert

1. Open a dashboard with the **Enable Quick actions**
   publishing option turned on.
2. Hover over a visual that supports threshold alerts. The types of visuals that support alerts
   can be found [here](threshold-alerts.md "threshold-alerts.md").
3. Choose the bell icon.
4. The **Create alert** pane opens at right.
5. Choose **Add Action**.
6. A menu appears with a list of all supported action connectors and actions.
7. Choose the desired action from the list.
8. An **Action** form appears in the right pane.
9. Enter all the information you need to include with the action.
10. Some fields allow the inclusion of autofill values. Choose **Autofill**
    to open the menu. Choose the values you need and they will be added to your entered text.
    - **Value**: Injects the current value that was used by the
      alert to evaluate the alert condition
    - **Alert name**: Injects the alert name
    - **Condition**: Injects the alert condition
    - **Threshold**: Injects the threshold value
    - **All**: Injects all of the above

11. Some actions support the ability to include an attachment. You can optionally attach a
    PDF of the current dashboard sheet with these actions by selecting the
    **Include this sheet as PDF** checkbox.
12. Choose **Add action** to add the action to the alert.
13. Back at the **Create alert** pane, the configured action is added to
    the alert at the bottom.
14. Configure all the other desired fields of the alert and choose **Save**.
15. When your configured threshold is breached, this action should get invoked. To learn more about when
    a threshold alert is evaluated, see [Alert Scheduling](threshold-alerts-scheduling.md "threshold-alerts-scheduling.md").

## Security and customizations

**Custom Permissions/Capability Customization**

- **Actions** capability: You cannot see or use
  actions if your user or role is restricted the permission to use the Actions capability
- **Export To PDF** capability:
  - New actions on alerts: You will not see the option to attach a PDF of the sheet while
    adding a new action to an alert if your user or role is restricted the permission to use
    the **Export To PDF** capability.
  - Existing actions on alerts: If you have existing alerts with actions containing PDF
    attachments then those actions will be sent out without the PDF attachments when your
    user or role gets restricted from using the **Export To PDF** capability.

To learn more about custom permissions, see
[Creating a custom permissions profile in Amazon Quick](create-custom-permisions-profile.md "create-custom-permisions-profile.md").

**Row Level Security (RLS) / Column Level Security (CLS)**

- New actions on alerts: If your dashboard contains a dataset with RLS or CLS, then
  - You cannot add actions to new alerts that track the dataset with RLS or CLS
  - You can add actions to new alerts that track a different dataset without RLS or CLS,
    but you cannot include PDF attachments in these actions

- Existing actions on alerts: If you add RLS or CLS to a dataset after creating alerts with actions, then
  - Existing actions on alerts tracking that dataset will stop working completely
  - Existing actions on alerts tracking a different dataset on the same dashboard
    will be sent out without any PDF attachments

To learn more about RLS, see
[Using row-level security in Amazon Quick](row-level-security.md "row-level-security.md").

To learn more about CLS, see
[Using column-level security to restrict access to a dataset](row-level-security.md "row-level-security.md").

**Dashboard publishing options**

- Enable PDF generation for interactive sheets
  - New actions on alerts: You will not see the option to attach a PDF of the sheet while
    adding a new action on alert if your dashboard has the
    **Enable PDF generation for interactive sheets** publishing option disabled.
  - Existing actions on alerts: If you have existing alerts with actions containing PDF
    attachments, then those actions will be sent out without the PDF attachments when the
    **Enable PDF generation for interactive sheets** publishing option gets
    disabled on your dashboard.

- Enable Quick actions
  - New actions on alerts: You will not see the option to add an action to the alert if
    your dashboard has the **Enable Quick actions** publishing option
    turned off.
  - Existing actions on alerts: Your existing actions on alerts will stop working
    completely when the **Enable Quick actions** publishing option
    gets disabled on your dashboard.

To learn more about dashboard publishing options, see
[Publishing dashboards](creating-a-dashboard.md "creating-a-dashboard.md").
