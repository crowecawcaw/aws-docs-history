# Using Quick action connectors in

dashboard visuals

## Prerequisites

Before you begin, make sure to
[create at least one action connector](builtin-services-integration.md "builtin-services-integration.md").

The connector must meet these requirements:

- Uses the **User Auth** authentication method
- Uses one of the following integrations:
  - Atlassian Jira Cloud
  - Microsoft Outlook
  - Microsoft Teams
  - Salesforce
  - ServiceNow
  - Slack

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

## Use action connectors on a visual

###### To use action connectors on a visual

1. Open a dashboard with the **Enable Quick actions**
   publishing option turned on.
2. Hover over a visual.
3. Choose the lightening bolt icon.
4. A menu appears with a list of all supported action connectors and actions.
5. Choose the desired action from the list.
6. If you have not used the connector before, or if your previous login credentials
   have expired, an authentication modal will appear. Log in with appropriate credentials
   for your organization.
7. An **Action** form appears in the right pane.
8. Enter all the information you need to include with the action.
9. Some fields allow the inclusion of autofill values. Choose **Autofill**
   to open the menu. Choose the values you need and they will be added to your entered text.
   - **Today’s date**: Injects today’s date
   - **Visual name**: Injects visual name
   - **All**: Injects both of the above

10. Some actions support the ability to include an attachment. You can optionally attach an
    image of the visual with these actions by selecting the **Visual image** checkbox.
11. Select the action button at the bottom of the form to invoke the action.

## Security and customizations

**Custom Permissions/Capability Customization**

- **Actions** capability: You cannot see or use
  actions if your user or role is restricted the permission to use the Actions capability

To learn more about custom permissions, see
[Creating a custom permissions profile in Amazon Quick](create-custom-permisions-profile.md "create-custom-permisions-profile.md").

**Row Level Security (RLS) / Column Level Security (CLS)**

- You cannot see or use actions on visuals that are based on datasets
  that use RLS or CLS.

To learn more about RLS, see
[Using row-level security in Amazon Quick](row-level-security.md "row-level-security.md").

To learn more about CLS, see
[Using column-level security to restrict access to a dataset](row-level-security.md "row-level-security.md").

**Dashboard publishing options**

- Enable Quick actions
  - You cannot see or use actions on any visuals of a dashboard that was published
    with the **Enable Quick actions** publishing option disabled.

To learn more about dashboard publishing options, see
[Publishing dashboards](creating-a-dashboard.md "creating-a-dashboard.md").

## Limitations

**Visual Image attachment support**

The following visual types do not support image attachments:

- High charts (when HTML is used)
- ML Insights (when HTML is used)
- Textbox and insights (when HTML is used)
- Custom content

###### Note

For these visuals, the **Visual image** checkbox will not appear on the UI.
