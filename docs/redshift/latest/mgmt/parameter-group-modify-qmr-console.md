

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating a query monitoring rule
<a name="parameter-group-modify-qmr-console"></a>

You can use the Amazon Redshift console to create and modify WLM query monitoring rules. Query monitoring rules are part of the WLM configuration parameter for a parameter group. If you modify a query monitoring rule (QMR), the change happens automatically without the need to modify the cluster. For more information, see [WLM query monitoring rules](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html). 

When you create a rule, you define the rule name, one or more predicates, and an action. 

When you save WLM configuration that includes a rule, you can view the JSON code for the rule definition as part of the JSON for the WLM configuration parameter. 



**To create a query monitoring rule**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Configurations**, then choose **Workload management** to display the **Workload management** page. 

1. Choose the parameter group that you want to modify to display the details page with tabs for **Parameters** and **Workload management**. 

1. Choose the **Workload management** tab, and choose **Edit workload queues** to edit the WLM configuration.

1. Add a new rule either by using a predefined template or from scratch. 

   To use a predefined template, do the following: 

   1. Choose **Add rule from template** in the **Query monitoring rules** group. The list of rule templates is displayed. 

   1. Choose one or more rule templates. When you choose **Save**, WLM creates one rule for each template that you choose. 

   1. Enter or confirm values for the rule, including **Rule names**, **Predicates** and **Actions**. 

   1. Choose **Save**. 

   To add a new rule from scratch, do the following:

   1. To add additional predicates, choose **Add predicate**. You can have up to three predicates for each rule. If all of the predicates are met, WLM triggers the associated action. 

   1. Choose an **Action**. Each rule has one action.

   1. Choose **Save**.

Amazon Redshift generates your WLM configuration parameter in JSON format and displays it in the **JSON** section. 