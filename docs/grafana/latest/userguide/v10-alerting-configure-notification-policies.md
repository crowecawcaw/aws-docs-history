# Configure

notification policies

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Notification policies determine how alerts are routed to contact points.

Policies have a tree structure, where each policy can have one or more nested
policies. Each policy, except for the default policy, can also match specific alert
labels.

Each alert is evaluated by the default policy and subsequently by each nested
policy.

If you enable the `Continue matching subsequent sibling nodes` option
for a nested policy, then evaluation continues even after one or more matches. A
parent policy’s configuration settings and contact point information govern the
behavior of an alert that does not match any of the child policies. A default
policy governs any alert that does not match a nested policy.

For more information on notification policies, see [Notifications](v10-alerting-explore-notifications.md "v10-alerting-explore-notifications.md").

The following procedures show you how to create and manage notification
policies.

###### To edit the default notification policy

1. In the left-side menu, choose **Alerting**.
2. Choose **Notification policies**.
3. From the **Choose Alertmanager** dropdown, select the
   Alertmanager you want to edit.
4. In the **Default policy** section, choose
   **...**, **Edit**.
5. In **Default contact point**, update the contact point
   where notifications should be sent for rules when alert rules do not match
   any specific policy.
6. In **Group by**, choose the labels to group alerts by.
   If multiple alerts are matched for this policy, then they are grouped by
   these labels. A notification is sent per group. If the field is empty
   (the default), then all notifications are sent in a single group. Use a
   special label, `...` to group alerts by all labels (which
   effectively disables grouping).
7. In **Timing options**, select from the following
   options.
   - **Group wait** – Time to wait to buffer
     alerts of the same group before sending an initial notification. The
     default is 30 seconds.
   - **Group interval** – Minimum time interval
     between two notifications for a group. The default is 5
     minutes.
   - **Repeat interval** – Minimum time
     interval before resending a notification if no new alerts were added
     to the group. The default is 4 hours.

8. Choose **Save** to save your changes.
   To create a new notification policy, you need to follow its tree structure. New
   policies created on the trunk of the tree (the default policy), are the tree
   branches. Each branch can have their own nested policies. This is why you will
   always be adding a new **nested** policy, either under the
   default policy, or under an already nested policy.

###### To add a new nested policy

1. In the left-side menu, choose **Alerting**.
2. Choose **Notification policies**.
3. From the **Choose Alertmanager** dropdown, select the
   Alertmanager you want to edit.
4. To add a top level specific policy, go to the Specific routing section
   (eitehr to the default policy, or to antoher existing policy in which you
   would like to add a new nested policy) and choose **+ New nested
   policy**.
5. In the matching labels section, add one or more rules for matching alert
   labels.
6. In the **Contact point** dropdown, select the contact
   point to send notifications to if an alert matches only this specific
   policy and not any of the nested policies.
7. Optionally, enable **Continue matching subsequent sibling
   nodes** to continue matching sibling policies even after the alert
   matched the current policy. When this option is enabled, you can get more
   than one notification for one alert.
8. Optionally, enable **Override grouping** to specify the
   same grouping as the default policy. If the option is not enabled, the
   default policy grouping is used.
9. Optionally, enable **Override general timings** to
   override the timing options configured in the group notification
   policy.
10. Choose **Save policy** to save your changes.

###### To edit a nested policy

1. In the left-side menu, choose **Alerting**.
2. Choose **Notification policies**.
3. Select the policy that you want to edit, then choose
   **...**, **Edit**.
4. Make any changes (as when adding a nested policy).
5. Save your changes.
   **Searching for policies**

You can search within the tree of policies by _Label
matchers_ or _contact points_.

- To search by contact point, enter a partial or full name of a
  contact point in the **Search by contact point**
  field. The policies that use that contact point will be highlighted
  in the user interface.
- To search by label, enter a valid label matcher in the
  **Search by matchers** input field. Multiple matchers can
  be entered, separated by a comma. For example, a valid matcher input
  could be `severity=high, region=~EMEA|NA`.

###### Note

When searching by label, all matched policies will be exact
matches. Partial matches and regex-style matches are not
supported.
