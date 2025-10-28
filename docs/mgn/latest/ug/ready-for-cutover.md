NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Ready for cutover indicators

Prior to launching a cutover instance, ensure that your source servers are ready for
cutover by looking for the following indicators on the **Source
servers** page:

1. Under the **Migration lifecycle** column, the server should
   show **Ready for cutover** .
2. Under the **Data replication status** column, the server
   should show the **Healthy** status.
3. Under the **Next step** column, the server should show
   **Terminate launched instance; Launch cutover instance** if you
   have not terminated your latest launched test instance.
4. Alternatively, the Next step column shows **Launch cutover
   instance** if you have terminated your latest launched test instance.
