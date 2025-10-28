# Create a Contributor Insights rule in CloudWatch

You can create rules to analyze log data. Any logs in JSON or Common Log Format (CLF) can
be evaluated. This includes your custom logs that follow one of these formats and logs from
AWS services such as Amazon VPC flow logs, Amazon Route 53 DNS query logs, Amazon ECS container logs, and
logs from AWS CloudTrail, Amazon SageMaker AI, Amazon RDS, AWS AppSync and API Gateway.

In a rule, when you specify field names or values, all matching is case sensitive.

You can use built-in sample rules when you create a rule or you can create your own rule
from scratch. Contributor Insights includes sample rules for the following types of logs:

- Amazon API Gateway logs
- Amazon Route 53 public DNS query logs
- Amazon Route 53 resolver query logs
- CloudWatch Container Insights logs
- VPC flow logs
  If you are signed in to an account that is set up as a monitoring account in CloudWatch cross-account
  observability, you can create Contributor Insights rules for log groups in the source accounts linked
  to this monitoring account,
  in addition to creating rules for log groups in the monitoring account. You can also set up a single rule that
  monitors log groups in different accounts.
  For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

###### Important

When you grant a user the `cloudwatch:PutInsightRule` permission,
by default that user can create a rule that
evaluates any log group in CloudWatch Logs. You can add IAM policy conditions that limit
these permissions
for a user to include and exclude specific log groups. For more information,
see [Using condition keys to
limit Contributor Insights users' access to log groups](iam-cw-condition-keys-contributor.md "iam-cw-condition-keys-contributor.md").

###### To create a rule using a built-in sample rule

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Contributor Insights**.
3. Choose **Create rule**.
4. For **Select log group(s)**,
   select the log group(s)
   that you want your rule
   to monitor.
   You can select
   as many as
   20 log groups. If you are signed in to a monitoring account that is set up for CloudWatch cross-account
   observability, you can select log groups in source accounts, and you can also set up a single rule
   to analyze log groups in different accounts.
   1. (Optional)
      To select all log groups
      that have names beginning
      with a specific string,
      choose the **Select by prefix match** dropdown,
      and then enter the prefix. If this is a monitoring account, you can optionally select the accounts
      to search in, otherwise all accounts are selected.###### Note

You incur charges
for each log event
that matches your rule.
If you choose the **Select by prefix match** dropdown,
be aware
of how many log groups
the prefix can match.
If you search more log groups than you want,
you might incur unexpected charges.
For more information,
see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing"). 5. For **Rule type**, choose **Sample rule**. Then choose **Select sample rule** and
select the rule. 6. For **Log format**, select the format of the logs that the rule will evaluate. 7. For **Transformers**, select **Enable contributor insights on transformers** to have the rule evaluate log events after they are transformed
by [CloudWatch Logs log transformation](../logs/CloudWatch-Logs-Transformation.md "../logs/CloudWatch-Logs-Transformation.md"). If you select to enable this:

    * If the rule evaluates any log groups that have transformers, the rule is applied to the transformed versions of the logs.
    * If the rule evaluates any log groups that don't have transformers, the rule is applied to the original versions of the logs.

If you don't select this, the evaluation happens to original log events in all log groups, even those that use log transformation.

###### Note

If a log group has a transformer, and transformation fails for some log events, those log events won't be evaluated by
Contributor Insights. For information about investigating log transformation failures, see
[Transformation metrics and errors](../logs/Transformation-Errors-Metrics.md "../logs/Transformation-Errors-Metrics.md"). 8. The sample rule you chose has filled out the **Log format**,
**Contribution**, **Filters**, and **Aggregation** fields. You can adjust those values, if you like. 9. Choose **Next**. 10. For **Rule name**, enter a name. Valid characters are A-Z, a-z, 0-9, (hyphen), (underscore), and (period). 11. Choose whether to create the rule in a disabled or enabled state. If you choose to enable it,
the rule immediately starts analyzing your data. You incur costs when you run enabled
rules. For more information, see [Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Contributor Insights analyzes only new log events after a rule is created. A rule cannot process logs events that were previously processed by
CloudWatch Logs. 12. (Optional) For **Tags**, add one or more key-value pairs as tags for this
rule. Tags can help you identify and organize your AWS resources and track your AWS
costs. For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md"). 13. Choose **Create**.

###### To create a rule from scratch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Contributor Insights**.
3. Choose **Create rule**.
4. For **Select log group(s)**,
   select the log group(s)
   that you want your rule
   to monitor.
   You can select
   as many as
   20 log groups. If you are signed in to a monitoring account that is set up for CloudWatch cross-account
   observability, you can select log groups in source accounts, and you can also set up a single rule
   to analyze log groups in different accounts.
   1. (Optional)
      To select all log groups
      that have names beginning
      with a specific string,
      choose the **Select by prefix match** dropdown,
      and then enter the prefix.###### Note

You incur charges
for each log event
that matches your rule.
If you choose the **Select by prefix match** dropdown,
be aware
of how many log groups
the prefix can match.
If you search more log groups than you want,
you might incur unexpected charges.
For more information,
see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing"). 5. For **Rule type**, choose **Custom
rule**. 6. For **Log format**, choose **JSON** or **CLF**. 7. For **Transformers**, select **Enable contributor insights on transformers** to have the rule evaluate log events after they are transformed
by [CloudWatch Logs log transformation](../logs/CloudWatch-Logs-Transformation.md "../logs/CloudWatch-Logs-Transformation.md"). If you select to enable this:

    * If the rule evaluates any log groups that have transformers, the rule is applied to the transformed versions of the logs.
    * If the rule evaluates any log groups that don't have transformers, the rule is applied to the original versions of the logs.

If you don't select this, the evaluation happens to original log events in all log groups, even those that use log transformation.

###### Note

If a log group has a transformer, and transformation fails for some log events, those log events won't be evaluated by
Contributor Insights. For information about investigating log transformation failures, see
[Transformation metrics and errors](../logs/Transformation-Errors-Metrics.md "../logs/Transformation-Errors-Metrics.md"). 8. You can finish creating the rule by using the wizard or by choosing the
**Syntax** tab and specifying your rule syntax manually.

To continue using the wizard, do the following:

    1. For **Contribution**, **Key**, enter a contributor type that
     you want to report on. The report displays the top-N values for this contributor
     type.


    Valid entries are any log field that has values. Examples include `requestId`,
     `sourceIPaddress`, and `containerID`.


    For information about finding the log field names for the logs in a certain log group,
     see [Finding Log Fields](#finding_log_fields "#finding_log_fields").


    Keys larger than 1 KB are truncated to 1KB.
    2. (Optional) Choose **Add new key** to add more keys.
     You can include as many as four keys in a rule. If you enter more than one key, the
     contributors in the report are defined by unique value combinations of the keys. For
     example, if you specify three keys, each unique combination of values for the three
     keys is counted as a unique contributor.
    3. (Optional) If you want
     to add a filter
     that narrows the scope
     of your results,
     choose **Add filter**.
     For **Match**,
     enter the name
     of the log field
     that you want
     to filter on.
     For **Condition**,
     choose a comparison operator,
     and enter a value
     that you want to filter for.



    You can add as many as four filters in a rule. Multiple filters are joined by AND logic,
     so only log events that match all filters are evaluated.


    ###### Note

    Arrays that follow comparison operators,
     such as `In`, `NotIn`, or `StartsWith`,
     can include
     as many as
     10 string values.
     For more information
     about the Contributor Insights rules syntax,
     see [Contributor Insights rule syntax in CloudWatch](ContributorInsights-RuleSyntax.md "ContributorInsights-RuleSyntax.md").
    4. For **Aggregate on**, choose **Count** or
     **Sum**. Choosing **Count** causes the contributor
     ranking to be based on the number of occurrences. Choosing **Sum**
     causes the ranking to be based on the aggregated sum of the values of the field that
     you specify for **Contribution**, **Value**.

9. To enter your rule as a JSON object instead of using the wizard, do the following:
   1. Choose the **Syntax** tab.
   2. In **Rule body**, enter the JSON object for your rule. For information about rule syntax, see
      [Contributor Insights rule syntax in CloudWatch](ContributorInsights-RuleSyntax.md "ContributorInsights-RuleSyntax.md").

10. Choose **Next**.
11. For **Rule name**, enter a name. Valid characters are A-Z, a-z, 0-9, "-",
    "\_', and ".".
12. Choose whether to create the rule in a disabled or enabled state. If you choose to enable it,
    the rule immediately starts analyzing your data. You incur costs when you run enabled
    rules. For more information, see [Amazon CloudWatch
    Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

Contributor Insights analyzes only new log events after a rule is created. A rule cannot process logs events that were previously processed by
CloudWatch Logs. 13. (Optional) For **Tags**, add one or more key-value pairs as tags for this
rule. Tags can help you identify and organize your AWS resources and track your AWS
costs. For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md"). 14. Choose **Next**. 15. Confirm the settings that you entered, and choose **Create rule**.
You can disable, enable, or delete rules that you have created.

###### To enable, disable, or delete a rule in Contributor Insights

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Contributor Insights**.
3. In the list of rules, select the check box next to a single rule.

Built-in rules are created by AWS services and can't be edited, disabled, or deleted. 4. Choose **Actions**, and then choose the option you want.
**Finding log fields**

When you create a rule, you need to know the names of fields in the log entries in a log group.

###### To find the log fields in a log group

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Logs**, choose **Insights**.
3. Above the query editor, select one or more log groups to query.

When you select a log group, CloudWatch Logs Insights automatically detects fields in the data
in the log group and displays them in the right pane in **Discovered
fields**.
