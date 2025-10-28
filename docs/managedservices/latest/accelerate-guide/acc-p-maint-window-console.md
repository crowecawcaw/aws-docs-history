# Create a maintenance window from the Systems Manager console for AMS Accelerate

To create an AMS Accelerate maintenance window from the Systems Manager console, follow these steps:

1. In the left navigation bar in the **Change management** area, click **Maintenance Windows**, and then
   click **Create Maintenance Window** at the top right of the screen. Fill in the form. For details on any of the options, see
   [Create a maintenance window (console)](../../../systems-manager/latest/userguide/sysman-maintenance-create-mw.md "../../../systems-manager/latest/userguide/sysman-maintenance-create-mw.md"). When
   finished, click **Create maintenance window**.

The maintenance windows list page opens. 2. Select the newly created maintenance window.

The maintenance window details page opens. 3. Go to the **Targets** tab and choose **Register target**.

The **Register target** page opens. 4. Add your Accelerate target. For information on targets, see
[Assign targets to a maintenance window (console)](../../../systems-manager/latest/userguide/sysman-maintenance-assign-targets.md "../../../systems-manager/latest/userguide/sysman-maintenance-assign-targets.md").
When finished, click **Register target**. Make note of the target as you need it later.

The maintenance windows details page reopens on the **Targets** tab with a list including the new target. 5. On the **Tasks** tab of the maintenance window details page, choose **Register Task**, and then pick
**Register Automation task** from the drop-down list. Fill in the form. Accelerate notes:

    * Provide a meaningful task name. For example: AcceleratePatch.
    * In the **Automation document** area click in the search box, choose **Owner**, then **Shared documents**.
    * Select the automation document by clicking in the search box and choosing **Document name prefix** -->  **Equals**
     and then typing: **AWSManagedServices-PatchInstance**. Then select the **AWSManagedServices-PatchInstance** document by
     selecting its radio button.
    * Under document version, choose **Default version at runtime**.
    * In the **Targets** section:




    	+ Set **Target by:** to **Selecting registered target groups**.
    	+ In the list of targets, select the target you registered in the **Targets** tab.
    * In the **Input parameters** section, fill in the form.




    	+ **InstanceId**: `{{`TARGET_ID`}}`
    	+ **StartInactiveInstances**: `True` to start the instances if they are stopped during the patch maintenance window.


    	###### Note

    	The **InstanceId** parameter value is case sensitive and the **StartInactiveInstances** parameter value
    	 can be either True or False.

    	Stopped instances cannot be started when targeted by tags. For more information, see
    	 [No Invocations to Execute](https://aws.amazon.com/premiumsupport/knowledge-center/ssm-no-invocations-automation "https://aws.amazon.com/premiumsupport/knowledge-center/ssm-no-invocations-automation").
    * In the **Rate control** section, choose percentages. AMS Accelerate recommends **100%** for
     **Concurrency** and **100%** for **Error threshold** to attempt to patch all instances
     simultaneously, regardless of automation errors. If you wish to patch half your targets at a time, for example, to keep a half of the target instances
     behind a load balance running, set **Concurrency** to 50%.
    * In the **IAM service role** section,choose **Use a custom service role**, then choose the
     **ams\_ssm\_automation\_role**.

Click **Register Automation task**.

The patching maintenance window is created. Under the **Description** tab, you can see the **Next execution time**.
