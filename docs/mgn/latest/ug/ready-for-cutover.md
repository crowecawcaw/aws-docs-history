

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Ready for cutover indicators
<a name="ready-for-cutover"></a>

Before launching a cutover instance, ensure that your source servers are ready for cutover by looking for the following indicators on the **Source servers** page:

1. Under the **Migration lifecycle** column, the server should show **Ready for cutover** .

1. Under the **Data replication status** column, the server should show the **Healthy** status. 

1. Under the **Next step** column, the server should show **Terminate launched instance; Launch cutover instance** if you have not terminated your latest launched test instance.

1. Alternatively, the Next step column shows **Launch cutover instance** if you have terminated your latest launched test instance. 