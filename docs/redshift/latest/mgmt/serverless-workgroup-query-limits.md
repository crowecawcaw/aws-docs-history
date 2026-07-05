Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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
