Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting query limits

Under the **Limits** tab for a workgroup, you can add a limit to
monitor performance and limits. For more information about query monitoring limits,
see [WLM query
monitoring rules](../dg/cm-c-wlm-query-monitoring-rules.md "../dg/cm-c-wlm-query-monitoring-rules.md").

1. Choose **Manage query limits**. Choose **Add
   new limit** on the **Manage query limits**
   dialogue.
2. Choose the limit type you want to set and enter a value for its
   corresponding limit.
3. Choose **Save changes** to save the limit.
   When you change your query limit and configuration parameters, your database will
   restart.
