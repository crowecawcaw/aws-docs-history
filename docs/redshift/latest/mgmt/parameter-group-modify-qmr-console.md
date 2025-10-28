Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a query monitoring

rule

You can use the Amazon Redshift console to create and modify WLM query monitoring rules. Query
monitoring rules are part of the WLM configuration parameter for a parameter group. If
you modify a query monitoring rule (QMR), the change happens automatically without the
need to modify the cluster. For more information, see [WLM query monitoring
rules](../dg/cm-c-wlm-query-monitoring-rules.md "../dg/cm-c-wlm-query-monitoring-rules.md").

When you create a rule, you define the rule name, one or more predicates, and an
action.

When you save WLM configuration that includes a rule, you can view the JSON code for
the rule definition as part of the JSON for the WLM configuration parameter.

###### To create a query monitoring rule

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Workload management** to display the
   **Workload management** page.
3. Choose the parameter group that you want to modify to display the details page
   with tabs for **Parameters** and **Workload
   management**.
4. Choose the **Workload management** tab, and choose
   **Edit workload queues** to edit the WLM
   configuration.
5. Add a new rule either by using a predefined template or from scratch.

To use a predefined template, do the following:

    1. Choose **Add rule from template** in the
     **Query monitoring rules** group. The list of rule
     templates is displayed.
    2. Choose one or more rule templates. When you choose
     **Save**, WLM creates one rule for each template
     that you choose.
    3. Enter or confirm values for the rule, including **Rule
     names**, **Predicates** and
     **Actions**.
    4. Choose **Save**.

To add a new rule from scratch, do the following:

    1. To add additional predicates, choose **Add
     predicate**. You can have up to three predicates for each
     rule. If all of the predicates are met, WLM triggers the associated
     action.
    2. Choose an **Action**. Each rule has one
     action.
    3. Choose **Save**.

Amazon Redshift generates your WLM configuration parameter in JSON format and displays it in the
**JSON** section.
