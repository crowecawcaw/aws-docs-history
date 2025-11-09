Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# WLM dynamic and static configuration

properties

The WLM configuration properties are either dynamic or static. You can apply dynamic
properties to the database without a cluster reboot, but static properties require a
cluster reboot for changes to take effect. However, if you change dynamic and static
properties at the same time, then you must reboot the cluster for all the property changes
to take effect. This is true whether the changed properties are dynamic or static.

While dynamic properties are being applied, your cluster status is
`modifying`. Switching between automatic WLM and manual WLM is a static
change and requires a cluster reboot to take effect.

The following table indicates which WLM properties are dynamic or static when
using automatic WLM or manual WLM.

| WLM Property                      | Automatic WLM  | Manual WLM     |
| --------------------------------- | -------------- | -------------- |
| Query groups                      | Dynamic        | Static         |
| Query group wildcard              | Dynamic        | Static         |
| User groups                       | Dynamic        | Static         |
| User group wildcard               | Dynamic        | Static         |
| User roles                        | Dynamic        | Static         |
| User role wildcard                | Dynamic        | Static         |
| Concurrency on main               | Not applicable | Dynamic        |
| Concurrency Scaling mode          | Dynamic        | Dynamic        |
| Enable short query acceleration   | Not applicable | Dynamic        |
| Maximum runtime for short queries | Dynamic        | Dynamic        |
| Percent of memory to use          | Not applicable | Dynamic        |
| Timeout                           | Not applicable | Dynamic        |
| Priority                          | Dynamic        | Not applicable |
| Adding or removing queues         | Dynamic        | Static         |

If you add a query monitoring rule (QMR), or modify or delete an existing QMR, the change happens
automatically without the need to restart the cluster.

###### Note

When using manual WLM, if the timeout value is changed, the new value is applied to any query
that begins running after the value is changed. If the concurrency or percent of memory
to use are changed, Amazon Redshift changes to the new configuration dynamically. Thus,
currently running queries aren't affected by the change. For more information, see
[WLM Dynamic Memory
Allocation.](cm-c-wlm-dynamic-memory-allocation.md "cm-c-wlm-dynamic-memory-allocation.md")

###### Topics

- [WLM dynamic memory
  allocation](cm-c-wlm-dynamic-memory-allocation.md "cm-c-wlm-dynamic-memory-allocation.md")
- [Dynamic WLM example](cm-c-wlm-dynamic-example.md "cm-c-wlm-dynamic-example.md")
