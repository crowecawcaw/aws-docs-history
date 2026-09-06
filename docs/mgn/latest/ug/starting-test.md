

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Starting a test
<a name="starting-test"></a>

To launch a test instance for a single source server or multiple source servers:

1. Go to the **Source servers** page.

1. Check the box to the left of each server for which you want to launch a test instance.

1. Open the **Test and cutover** menu.

1. Under **Testing**, choose the **Launch test instances** option to launch a test instance for this server.

1. When the **Launch test instances for X servers** dialog appears, choose **Launch** to begin the test. 

The AWS Transform MGN console indicates **Launch job started** when the test has started. 

Choose **View job details** on the dialog to view the specific job for the test launch in the **Launch history** tab. 



## Successful test launch indicators
<a name="successful-test"></a>

You can tell that the test instance launch started successfully through several indicators on the **Source servers** page.

1. The Alerts column shows the **Launched** status, indicating that a Test instance has been launched for this server.

1. The **Migration lifecycle** column shows **Test in progress**.

1. The **Next step** column shows **Complete testing and mark as 'Ready for cutover'**.