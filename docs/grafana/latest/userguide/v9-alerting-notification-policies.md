# Working with notification

policies

This documentation topic is designed
for Grafana workspaces that support **Grafana version
9.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Notification policies determine how alerts are routed to contact points. Policies have
a tree structure, where each policy can have one or more child policies. Each policy,
except for the root policy, can also match specific alert labels. Each alert is
evaluated by the root policy and then by each child policy. If you enable the
`Continue matching subsequent sibling nodes` option for a specific
policy, then evaluation continues even after one or more matches. A parent policy’s
configuration settings and contact point information govern the behavior of an alert
that does not match any of the child policies. A root policy governs any alert that does
not match a specific policy.

###### Note

You can create and edit notification policies for Grafana managed alerts.
Notification policies for Alertmanager alerts are read-only.

**Grouping notifications**

Grouping categorizes alert notifications of similar nature into a single funnel. This
allows you to control alert notifications during larger outages when many parts of a
system fail at once causing a high number of alerts to initiate simultaneously.

**Grouping example**

Suppose you have 100 services connected to a database in different environments. These
services are differentiated by the label `env=environmentname`. An alert rule
is in place to monitor whether your services can reach the database. The alert rule
creates alerts named `alertname=DatabaseUnreachable`.

If a network partition occurs, where half of your services can no longer reach the
database, 50 different alerts are initiated. For this situation, you want to receive a
single-page notification (as opposed to 50) with a list of the environments that are
affected.

You can configure grouping to be `group_by: [alertname]` (not using the
`env` label, which is different for each service). With this
configuration in place, Grafana sends a single compact notification that has all the
affected environments for this alert rule.

**Special Groups**

Grafana has two special groups. The default group, `group_by: null` groups
_all_ alerts together into a single group. You can also use a
special label named `...` to group alerts by all labels, effectively
disabling grouping, and sending each alert into its own group.

## Working with

notifications

The following procedures show you how to create and manage notification
policies.

###### To edit the root notification policy

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Choose **Notification policies**.
3. From the **Alertmanager** dropdown, select the
   Alertmanager you want to edit.
4. In the **Root policy** section, choose the
   **Edit** icon (pen).
5. In **Default contact point**, update the contact point
   where notifications should be sent for rules when alert rules do not match
   any specific policy.
6. In **Group by**, choose the labels (or special groups) to
   group alerts by.
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

###### To add a new, top-level specific policy

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page.
2. Choose **Notification policies**.
3. From the **Alertmanager** dropdown, select the
   Alertmanager you want to edit.
4. In the **Specific routing** section, choose **New
   specific policy**.
5. In the **Matching labels** section, add one or more
   matching alert labels. More information about label matching is later in
   this topic.
6. In **Contact point**, add the contact point to send
   notifications to if the alert matches this specific policy. Nested policies
   override this contact point.
7. Optionally, enable **Continue matching subsequent sibling
   nodes** to continue matching sibling policies even after
   the alert matched the current policy. When this policy is enabled, you
   can get more than one notification for the same alert.
8. Optionally select **Override grouping** to specify a
   grouping different from the root policy.
9. Optionally select **Override general timings** to
   override the timing options in the group notification policy.
10. Choose **Save policy** to save your changes.

###### To add a nested policy

1. Expand the specific policy you want to create a nested policy
   under.
2. Choose **Add nested policy**, then add the details (as
   when adding a top-level specific policy).
3. Choose **Save policy** to save your changes.

###### To edit a specific policy

1. From the **Alerting** page, choose
   **Notification policies** to open the page that
   listing existing policies.
2. Select the policy that you want to edit, then choose the
   **Edit** icon (pen).
3. Make any changes (as when adding a top-level specific policy).
4. Choose **Save policy**.

**Searching for policies**

You can search within the tree of policies by _Label
matchers_ or _contact points_.

- To search by contact point, enter a partial or full name of a
  contact point in the **Search by contact point**
  field.
- To search by label, enter a valid label matcher in the
  **Search by label** field. Multiple matchers can
  be entered, separated by a comma. For example, a valid matcher input
  could be `severity=high, region=~EMEA|NA`.

###### Note

When searching by label, all matched policies will be exact
matches. Partial matches and regex-style matches are not
supported.

**How label matching works**

A policy matches an alert if the alert's labels match all the _Matching Labels_ specified on the policy.

- **Label** – The name of the label to
  match. It must exactly match the label name of the alert.
- **Operator** – The operator used to
  compare the label value with the matching label value. The available
  operators are:
  - `=` Select labels whose value exactly matches the
    provided string.
  - `!=` Select labels whose value does not match the
    provided string.
  - `=~` Select labels whose value match the regex
    interpreted value of the provided string (the provided string is
    interpreted as a regular expression.
  - `!=` Select labels that do not match the provided
    regular expression.

- **Value** – The value to match the
  label value to. It can match as a string or as a regular expression,
  depending on the operator chosen.
