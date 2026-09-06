

# Using Quick connectors in dashboard visuals
<a name="action-connectors-in-dashboard-visuals"></a>

## Prerequisites
<a name="action-connectors-in-dashboards-prerequisites"></a>

Before you begin, make sure to [create at least one connector](builtin-services-integration.md).

The connector must meet these requirements:
+ Uses the **User Auth** authentication method
+ Uses one of the following integrations:
  + Atlassian Jira Cloud
  + Microsoft Outlook
  + Microsoft Teams
  + Salesforce
  + ServiceNow
  + Slack

## Enable Quick actions on a dashboard to use connectors
<a name="enable-quick-actions-on-dashboards"></a>

**To enable Quick actions on a dashboard to use connectors**

1. If a dashboard exists, go to the source analysis of the dashboard. Otherwise, [create a new analysis](quickstart-createanalysis.md).

1. Choose **Publish**.

1. Choose between **New Dashboard** or **Replace existing dashboard**.

1. Choose the **Enable Quick actions** checkbox under **Dashboard options**.

1. Choose **Publish dashboard**.

## Use connectors on a visual
<a name="use-action-connectors-on-visuals"></a>

**To use connectors on a visual**

1. Open a dashboard with the **Enable Quick actions** publishing option turned on.

1. Hover over a visual.

1. Choose the lightening bolt icon.

1. A menu appears with a list of all supported connectors and actions.

1. Choose the desired action from the list.

1. If you have not used the connector before, or if your previous login credentials have expired, an authentication modal will appear. Log in with appropriate credentials for your organization.

1. An **Action** form appears in the right pane.

1. Enter all the information you need to include with the action.

1. Some fields allow the inclusion of autofill values. Choose **Autofill** to open the menu. Choose the values you need and they will be added to your entered text.
   + **Today’s date**: Injects today’s date
   + **Visual name**: Injects visual name
   + **All**: Injects both of the above

1. Some actions support the ability to include an attachment. You can optionally attach an image of the visual with these actions by selecting the **Visual image** checkbox.

1. Select the action button at the bottom of the form to invoke the action.

## Security and customizations
<a name="dashboard-security-and-customizations"></a>

**Custom Permissions/Capability Customization**
+ **Actions** capability: You cannot see or use actions if your user or role is restricted the permission to use the Actions capability

To learn more about custom permissions, see [Custom permissions in Amazon Quick](custom-permissions.md).

**Row Level Security (RLS) / Column Level Security (CLS)**
+ You cannot see or use actions on visuals that are based on datasets that use RLS or CLS.

To learn more about RLS, see [Using row-level security in Amazon Quick](row-level-security.md).

To learn more about CLS, see [Using column-level security to restrict access to a dataset](row-level-security.md).

**Dashboard publishing options**
+ Enable Quick actions
  + You cannot see or use actions on any visuals of a dashboard that was published with the **Enable Quick actions** publishing option disabled.

To learn more about dashboard publishing options, see [Publishing dashboards](creating-a-dashboard.md).

## Limitations
<a name="action-connectors-on-dashboard-limitations"></a>

**Visual Image attachment support**

The following visual types do not support image attachments:
+ High charts (when HTML is used)
+ ML Insights (when HTML is used)
+ Textbox and insights (when HTML is used)
+ Custom content

**Note**  
For these visuals, the **Visual image** checkbox will not appear on the UI.