# Create and manage Grafana alerting rules

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

An alerting rule is a set of evaluation criteria that determines whether an alert is
initiated. The rule consists of one or more queries and expressions, a condition, the
frequency of evaluation, and optionally the duration over which the condition is
met.

While queries and expressions select the dataset to evaluate, a condition sets the
threshold that an alert must meet, or exceed to create an alert. An interval specifies
how frequently an alerting rule is evaluated. Duration, when configured, indicates how
long a condition must be met. The rules can also define alerting behavior in the absence
of data.

The following sections describe creating and managing different kinds of Grafana alert
rules.

###### Topics

- [Creating Cortex or Loki managed alert
  rules](#create-alert-rule "#create-alert-rule")
- [Creating Cortex or Loki managed
  recording rules](#create-alert-recording-rule "#create-alert-recording-rule")
- [Creating Grafana managed alert
  rules](#create-grafana-alert-rule "#create-grafana-alert-rule")
- [Annotations and labels for alerting
  rules](#alert-rule-labels "#alert-rule-labels")
- [Managing alerting rules](#manage-alert-rules "#manage-alert-rules")
- [Cortex or Loki rule groups and
  namespaces](#alert-rule-groups "#alert-rule-groups")

## Creating Cortex or Loki managed alert

rules

Using Grafana, you can create alerting rules for an external Cortex or Loki
instance.

###### Note

Cortex is the time series database used by Amazon Managed Service for Prometheus and Prometheus data
sources.

**Prerequisites**

- Verify that you have write permissions to the Prometheus data source.
  Otherwise, you are not able to create or update Cortex managed alerting
  rules.
- For Cortex and Loki data sources, enable the ruler API by configuring
  their respective services.
  - **Loki** – The
    `local` rule storage type, default for the Loki data
    source, supports only viewing of rules. To edit rules, configure one
    of the other storage types.
  - **Cortex** – Use the legacy
    `/api/prom` prefix, not `/prometheus`. The
    Prometheus data source supports both Cortex and Prometheus, and
    Grafana expects that both the Query API and Ruler API are under the
    same URL. You cannot provide a separate URL for the Ruler
    API.

###### Note

If you do not want to manage alerting rules for a particular Loki or
Prometheus data source, go to its settings and clear the **Manage alerts
via Alerting UI** checkbox.

###### To add a Cortex or Loki managed alerting rule

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page listing existing alerts.
2. Choose **New alert rule**.
3. In **Step 1**, add the rule name, type and storage
   location, as follows:
   - In **Rule name**, add a descriptive name. This
     name is displayed in the alert rules list. It is also the
     `alertname` label for every alert instance that is
     created from this rule.
   - From the **Rule type** dropdown, select
     **Cortex/Loki managed alert**.
   - From the **Select data source** dropdown, select
     a Prometheus, or Loki data source.
   - From the **Namespace** dropdown, select an
     existing rule namespace. Otherwise, choose **Add
     new** and enter a name to create one. Namespaces can
     contain one or more rule groups and only have an organizational
     purpose. For more information, see [Cortex or Loki rule groups and
     namespaces](#alert-rule-groups "#alert-rule-groups").
   - From the **Group** dropdown, select an existing
     group within the selected namespace. Otherwise, choose **Add
     new** and enter a name to create one. Newly created
     rules are appended to the end of the group. Rules within a group run
     sequentially at a regular interval, with the same evaluation
     time.

4. In **Step 2**, add the query to evaluate.

The value can be a PromQL or LogQL expression. The rule initiates an alert
if the evaluation result has at least one series with a value that is
greater than 0. An alert is created for each series. 5. In **Step 3**, add conditions.

In the For text box of the condition, specify the duration for which the
condition must be true before the alert is initiated. If you specify
`5m`, the conditions must be true for five minutes before the
alert is initiated.

###### Note

After a condition is met, the alert goes into `Pending`
state. If the condition remains active for the duration specified, the
alert transitions to the `Firing` state. If it is no longer
met, it reverts to the `Normal` state. 6. In **Step 4**, add additional metadata associated with
the rule.

    * Add a description and summary to customize alert messages. Use the
     guidelines in [Annotations and labels for alerting
     rules](#alert-rule-labels "#alert-rule-labels").
    * Add Runbook URL, panel, dashboard, and alert IDs.
    * Add custom labels.

7. Choose **Preview alerts** to evaluate the rule and see
   what alerts it would produce. It displays a list of alerts with state and
   value of each one.
8. Choose **Save** to save the rule or **Save and
   exit** to save the rule and go back to the
   **Alerting** page.

## Creating Cortex or Loki managed

recording rules

You can create and manage recording rules for an external Cortex or Loki instance.
Recording rules calculate frequently needed expressions or computationally expensive
expressions in advance and save the result as a new set of time series. Querying
this new time series is faster, especially for dashboards since they query the same
expression every time the dashboards refresh.

**Prerequisites**

For Cortex and Loki data sources, enable the ruler API by configuring their
respective services.

- **Loki** – The `local` rule
  storage type, default for the Loki data source, supports only viewing of
  rules. To edit rules, configure one of the other storage types.
- **Cortex** – When configuring a
  Grafana Prometheus data source to point to Cortex, use the legacy
  `/api/prom` prefix, not `/prometheus`. The
  Prometheus data source supports both Cortex and Prometheus, and Grafana
  expects that both the Query API and Ruler API are under the same URL. You
  cannot provide a separate URL for the Ruler API.

###### Note

If you do not want to manage alerting rules for a particular Loki or
Prometheus data source, go to its settings and clear the **Manage alerts
via Alerting UI** check box.

###### To add a Cortex or Loki managed recording rule

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page listing existing alerts.
2. Choose **New alert rule**.
3. In **Step 1**, add the rule name, type and storage
   location, as follows.
   - In **Rule name**, add a descriptive name. This
     name is displayed in the alert rules list. It is also the
     `alertname` label for every alert instance that is
     created from this rule.
   - From the **Rule type** dropdown, select
     **Cortex/Loki managed alert**.
   - From the **Select data source** dropdown, select
     a Prometheus, or Loki data source.
   - From the **Namespace** dropdown, select an
     existing rule namespace. Otherwise, choose **Add
     new** and enter a name to create one. Namespaces can
     contain one or more rule groups and only have an organizational
     purpose. For more information, see [Cortex or Loki rule groups and
     namespaces](#alert-rule-groups "#alert-rule-groups").
   - From the **Group** dropdown, select an existing
     group within the selected namespace. Otherwise, choose **Add
     new** and enter a name to create one. Newly created
     rules are appended to the end of the group. Rules within a group run
     sequentially at a regular interval, with the same evaluation
     time.

4. In **Step 2**, add the query to evaluate.

The value can be a PromQL or LogQL expression. The rule initiates an alert
if the evaluation result has at least one series with a value that is
greater than 0. An alert is created for each series. 5. In **Step 3**, add additional metadata associated with
the rule.

    * Add a description and summary to customize alert messages. Use the
     guidelines in [Annotations and labels for alerting
     rules](#alert-rule-labels "#alert-rule-labels").
    * Add Runbook URL, panel, dashboard, and alert IDs.
    * Add custom labels.

6. Choose **Save** to save the rule or **Save and
   exit** to save the rule and go back to the
   **Alerting** page.

## Creating Grafana managed alert

rules

Grafana allows you to create alerting rules that query one or more data sources,
reduce or transform the results and compare them to each other or to fix thresholds.
When these are processed, Grafana sends notifications to the contact point.

###### Note

Creating Grafana managed alert rules while using Grafana alerting causes
multiple notifications to be sent when the rule is matched. Some contact point
providers might have configurable options to de-duplicate the
notifications.

###### To add a Grafana managed rule

1. From your Grafana console, in the Grafana menu, choose the
   **Alerting** (bell) icon to open the
   **Alerting** page listing existing alerts.
2. Choose **New alert rule**.
3. In **Step 1**, add the rule name, type and storage
   location, as follows:
   - In **Rule name**, add a descriptive name. This
     name is displayed in the alert rules list. It is also the
     `alertname` label for every alert instance that is
     created from this rule.
   - From the **Rule type** dropdown, select
     **Grafana managed alert**.
   - From the **Folder** dropdown, select the folder
     where you want to store the rule. If you do not select a folder, the
     rule is stored in the `General` folder. To create a
     folder, select the dropdown and enter a new folder name.

4. In **Step 2**, add the queries and expressions to
   evaluate.
   - Keep the default name or hover over and choose the edit icon to
     change the name.
   - For queries, select a data source from the dropdown.
   - Add one or more [queries](panel-queries.md "panel-queries.md") or
     expressions (for details on expressions, see [Expressions](https://grafana.com/docs/grafana/next/panels/query-a-data-source/ "https://grafana.com/docs/grafana/next/panels/query-a-data-source/") in the _Grafana
     documentation_).
   - For each expression, select either **Classic
     condition** to create a single alert rule, or choose
     from **Math**, **Reduce**,
     **Resample** options to generate separate
     alerts for each series. For details on these options, see [Single and multidimensional rules](#single-multi-rule "#single-multi-rule").
   - Choose **Run queries** to verify that the query
     is successful.

5. In **Step 3**, add conditions.
   - From the **Condition** dropdown, select the query
     or expression to initiate the alert rule.
   - For **Evaluate every**, specify the frequency of
     evaluation. Must be a multiple of 10 seconds. For example,
     `1m`, `30s`.
   - For **Evaluate for**, specify the duration for
     which the condition must be true before an alert is
     initiated.

   ###### Note

   After a condition is breached, the alert goes into
   `Pending` state. If the condition remains
   breached for the duration specified, the alert transitions to
   the `Firing` state. If it is no longer met, it
   reverts to the `Normal` state.
   - In **Configure no data and error handling**,
     configure alerting behavior in the absence of data. use the
     guidelines in [Handling no data or error cases](#rule-no-data-error "#rule-no-data-error").
   - Choose **Preview alerts** to check the result of
     running the query at this moment. Preview excludes no data and error
     handling conditions.

6. In **Step 4**, add additional metadata associated with
   the rule.
   - Add a description and summary to customize alert messages. Use the
     guidelines in [Annotations and labels for alerting
     rules](#alert-rule-labels "#alert-rule-labels").
   - Add Runbook URL, panel, dashboard, and alert IDs.
   - Add custom labels.

7. Choose **Save** to save the rule or **Save and
   exit** to save the rule and go back to the
   **Alerting** page.

### Single and multidimensional rules

For Grafana managed alert rules, you can create a rule with a classic
condition or you can create a multidimensional rule.

**Single dimensional rule (classic
condition)**

Use a classic condition expression to create a rule that initiates a single
alert when its condition is met. For a query that returns multiple series,
Grafana does not track the alert state of each series. As a result, Grafana
sends only a single alert even when alert conditions are met for multiple
series.

For more information about how to format expressions, see [Expressions](https://grafana.com/docs/grafana/next/panels/query-a-data-source/ "https://grafana.com/docs/grafana/next/panels/query-a-data-source/") in the _Grafana
documentation_.

**Multidimensional rule**

To generate a separate alert instance for each series returned in the query,
create a multidimensional rule.

###### Note

Each alert instance generated by a multi-dimensional rule counts toward
your total quota of alerts. Rules are not evaluated when you reach your
quota of alerts. For more information about quotas for multi-dimensional
rules, see [Quota reached errors](#rule-quota-reached "#rule-quota-reached").

To create multiple instances from a single rule, use `Math`,
`Reduce`, or `Resample` expressions to create a
multidimensional rule. For example, you can:

- Add a `Reduce` expression for each query to aggregate
  values in the selected time range into a single value. (Not needed for
  [rules using numeric
  data](alert-fundamentals.md#alert-numeric "alert-fundamentals.md#alert-numeric")).
- Add a `Math` expression with the condition for the rule.
  This is not needed in case a query or a reduce expression already
  returns 0 if rule should not initiate an alert, or a positive number if
  it should initiate an alert.

Some examples:

    + `$B > 70` if it should initiate an alert in case
     value of B query/expression is more than 70.
    + `$B < $C * 100` in case it should initiate an
     alert if value of B is less than value of C multiplied by 100.
     If queries being compared have multiple series in their results,
     series from different queries are matched if they have the same
     labels, or one is a subset of the other.

###### Note

Grafana does not support alert queries with template variables. More
information is available at the community page [Template variables are not supported in alert queries while setting up
Alert](https://community.grafana.com/t/template-variables-are-not-supported-in-alert-queries-while-setting-up-alert/2514 "https://community.grafana.com/t/template-variables-are-not-supported-in-alert-queries-while-setting-up-alert/2514").

**Performance considerations for multidimensional
rules**

Each alert instance counts toward the alert quota. Multidimensional rules that
create more instances than can be accommodated within the alert quota are not
evaluated and return a quota error. For more information, see [Quota reached errors](#rule-quota-reached "#rule-quota-reached").

Multidimensional alerts can have a high impact on the performance of your
Grafana workspace, as well as on the performance of your data sources as Grafana
queries them to evaluate your alert rules. The following considerations can be
helpful as you are trying to optimize the performance of your monitoring
system.

- **Frequency of rule evaluation** –
  The **Evaluate Every** property of an alert rule
  controls the frequency of rule evaluation. We recommend using the lowest
  acceptable evaluation frequency.
- **Result set cardinality** – The
  number of alert instances you create with a rule affects its
  performance. Suppose you are monitoring API response errors for every
  API path, on every VM in your fleet. This set has a cardinality of the
  number of paths multiplied by the number of VMs. You can reduce the
  cardinality of the result set, for example, by monitoring total errors
  per VM instead of per path per VM.
- **Complexity of the query** –
  Queries that data sources can process and respond to quickly consume
  fewer resources. Although this consideration is less important than the
  other considerations listed above, if you have reduced those as much as
  possible, looking at individual query performance could make a
  difference. You should also be aware of the performance impact that
  evaluating these rules has on your data sources. Alerting queries are
  often the vast majority of queries handled by monitoring databases, so
  the same load factors that affect the Grafana instance affect them as
  well.

### Quota reached errors

There is a quota for the number of alert instances you can have within a
single workspace. When you reach that number, you can no longer create new alert
rules in that workspace. With multidimensional alerts, the number of alert
instances can vary over time.

The following are important to remember when working with alert
instances.

- If you create only single-dimensional rules, each rule is a
  single alert instance. You can create the same number of rules in a
  single workspace as your alert-instance quota, and no more.
- Multidimensional rules create multiple alert instances, however, the
  number is not known until they are evaluated. For example, if you create
  an alert rule that tracks the CPU usage of your Amazon EC2 instances, there
  might be 50 EC2 instances when you create it (and therefore 50 alert
  instances), but if you add 10 more EC2 instances a week later, the next
  evaluation has 60 alert instances.

The number of alert instances is evaluated when you create a
multidimensional alert, and you can't create one that immediately
puts you over your alert instance quota. Because the number of alert
instances can change, your quota is checked each time that your
rules are evaluated.

- At rule evaluation time, if a rule causes you to go beyond your quota
  for alert instances, that rule is not evaluated until an update is
  made to the alert rule that brings the total count of alert instances
  below the service quota. When this happens, you receive an alert
  notification letting you know that your quota has been reached (the
  notification uses the notification policy for the rule being
  evaluated). The notification includes an `Error`
  annotation with the value `QuotaReachedError`.
- A rule that causes a `QuotaReachedError` stops being
  evaluated. Evaluation is only resumed when an update is made and
  the evaluation after the update does not itself cause a
  `QuotaReachedError`. A rule that is not being evaluated
  shows the **Quota reached** error in the Grafana
  console.
- You can lower the number of alert instances by removing alert rules,
  or by editing multidimensional alerts to have fewer alert instances (for
  example, by having one alert on errors per VM, rather than one alert on
  error per API in a VM).
- To resume evaluations, update the alert and save it. You can update it
  to lower the number of alert instances, or if you have made other
  changes to lower the number of alert instances, you can save it
  with no changes. If it can be resumed, it is. If it causes another
  `QuotaReachedError`, you are not able to save
  it.
- When an alert is saved and resumes evaluation without going over the
  alerts quota, the **Quota reached** error can continue
  to show in the Grafana console for some time (up to its evaluation
  interval), however, the alert rule evaluation does start and alerts are
  sent if the rule threshold is met.
- For details on the alerts quota, as well as other quotas, see [Amazon Managed Grafana service quotas](AMG_quotas.md "AMG_quotas.md").

### Handling no data or error cases

Choose options for how to handle alerting behavior in the absence of data or
when there are errors.

The options for handling no data are listed in the following table.

| No Data option          | Behavior                                                                                                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No Data                 | Create an alert `DatasourceNoData` with the name and UID of the alert rule, and UID of the data source that returned no data as labels.                                                                                                                                            |
| Alerting                | Set alert rule state to `Alerting`.                                                                                                                                                                                                                                                |
| OK                      | Set alert rule state to `Normal`.                                                                                                                                                                                                                                                  | The options for handling error cases are listed in the following table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Error or timeout option | Behavior                                                                                                                                                                                                                                                                           |
| ---                     | ---                                                                                                                                                                                                                                                                                |
| Alerting                | Set alert rule state to `Alerting`                                                                                                                                                                                                                                                 |
| OK                      | Set alert rule state to `Normal`                                                                                                                                                                                                                                                   |
| Error                   | Create an alert `DatasourceError` with the name and UID of the alert rule, and UID of the data source that returned no data as labels.                                                                                                                                             | ## Annotations and labels for alerting rules Annotations and labels are key-value pairs associated with alerts originating from the alerting rule, datasource response, and as a result of alerting rule evaluation. They can be used in alert notifications directly or in [templates](alert-message-templates.md "alert-message-templates.md") and [template functions](alert-message-templates.md#alert-template-functions "alert-message-templates.md#alert-template-functions") to create notification contact dynamically. **Annotations** Annotations are key-value pairs that provide additional information about an alert. You can use the following annotations: `description`, `summary`, `runbook_url`, `alertId`, `dashboardUid`, and `panelId`. These are displayed in rule and alert details in the UI and can be used in contact point message templates. **Labels** Labels are key-value pairs that contain information about an alert. The label set for an alert is generated and added to throughout the alerting evaluation and notification process. They are used in the following ways. <br>• The complete set of labels for an alert uniquely identifies that alert within Grafana Alerts. <br>• The Alertmanager uses labels to match alerts for [silences](alert-silences.md "alert-silences.md") and [alert groups](alert-groups.md "alert-groups.md") in [notification policies](alert-notifications.md "alert-notifications.md"). <br>• The alerting UI displays labels for every alert instance generated by the evaluation of that rule. <br>• Contact points can access labels to dynamically generate notifications that contain information specific to the alert that is resulting in a notification. <br>• Labels can be added to an [alerting rule](alert-rules.md "alert-rules.md"). These manually configured labels are able to use template functions and reference other labels. Labels added to an alerting rule here take precedence in the event of a collision between labels. The following template variables are available when expanding annotations and labels.                                                                                                                                                                                  |
| Name                    | Description                                                                                                                                                                                                                                                                        |
| ---                     | ---                                                                                                                                                                                                                                                                                |
| `$labels`               | The labels from the query or condition. For example, `{{ $labels.instance }}` and `{{ $labels.job }}`. This is unavailable when the rule uses a classic condition.                                                                                                                 |
| `$values`               | The values of all reduce and math expressions that were evaluated for this alert rule. For example, `{{ $values.A }}`, `{{ $values.A.Labels }}` and `{{ $values.A.Value }}` where `A` is the `refID` of the expression. This is unavailable when the rule uses a classic condition |
| `$value`                | The value string of the alert instance. For example, `[ var='A' labels={instance=foo} value=10 ]`.                                                                                                                                                                                 | ## Managing alerting rules The **Alerting** page lists alerting rules. By default, rules are grouped by types of data sources. The **Grafana** section lists rules managed by Grafana, and the **Cortex/Loki** section lists rules for Prometheus compatible data sources. You can view alerting rules for Prometheus compatible data sources but you cannot edit them. ### View alerting rules Using Grafana alerts, you can view all of your alerts in one page. ###### To view alerting details 1. From your Grafana console, in the Grafana menu, choose the **Alerting** (bell) icon to open the **Alerting** page. By default, rules are displayed in groups by data source type. You can also view by the current state of each alert (these are described in more detail in the following text). 2. In **View as**, you can toggle between the group and state views by choosing the option you prefer. 3. Choose the arrow next to a row to view more details for that row. The details for a rule include the rule labels, annotations, data sources, and queries, as well as a list of alert instances resulting from the rule. **Group view** Group view shows Grafana alert rules grouped by folder and Loki or Prometheus alert rules grouped by `namespace` + `group`. This is the default rule list view, intended for managing rules. You can expand each group to view a list of rules in this group. Expand a rule further to view its details. You can also expand action buttons and alerts resulting from the rule to view their details. **State view** State view shows alert rules grouped by state. Use this view to get an overview of which rules are in what state. Each rule can be expanded to view its details. Action buttons and any alerts generated by this rule, and each alert can be further expanded to view its details. **Filter alerting rules** You can filter the alerting rules that appear on the **Alerting** page in several ways. <br>• You can filter to display the rules that query a specific data source by choosing **Select data sources**, then selecting a data source to filter to. <br>• You can filter by labels by choosing search criteria in **Search by label**. Some sample criteria include `environment=production`, `region=~US | EU`, `severity!=warning`. <br>• You can filter to display the rules in a specific state by choosing **Filter alerts by state**, and then selecting the state you want to view. ### Edit or delete alerting rules Grafana managed alerting rules can only be edited or deleted by users with Edit permissions for the folder storing the rules. Alerting rules for an external Cortex or Loki instance can be edited or deleted by users with Editor or Admin roles. ###### To edit or delete a rule 1. Expand a rule until you can see the rule controls for **View**, **Edit**, and **Delete**. 2. Choose **Edit** to open the create rule page. Make updates in the same way that you create a rule. For details, see the instructions in [Creating Grafana managed alert rules](#create-grafana-alert-rule "#create-grafana-alert-rule") or [Creating Cortex or Loki managed alert rules](#create-alert-rule "#create-alert-rule"). 3. Optionally, choose **Delete** to delete a rule. ## Cortex or Loki rule groups and namespaces You can organize your rules. Rules are created within rule groups, and rule groups are organized into namespaces. The rules within a rule group are run sequentially at a regular interval. The default interval is one minute. You can rename Cortex or Loki namespaces and rule groups, and edit rule group evaluation intervals. ###### To edit a rule group or namespace 1. From your Grafana console, in the Grafana menu, choose the **Alerting** (bell) icon to open the **Alerting** page. 2. Navigate to a rule within the rule group or namespace you want to edit. 3. Choose the **Edit** (pen) icon. 4. Make changes to the rule group or namespace. ###### Note For namespaces, you can only edit the name. For rule groups, you change the name, or the evaluation interval for rules in the group. For example, you can choose `1m`to have the rules be evaluated once per minute, or`30s` to evaluate once every 30 seconds. 5. Choose **Save changes**. |
