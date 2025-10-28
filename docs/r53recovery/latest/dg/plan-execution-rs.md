# Execute a Region switch plan to recover an application

To recover an application when an AWS Region is impaired, you execute a Region switch plan in Amazon Application Recovery Controller (ARC).

- If your application is deployed with an active/active approach, the workflows in your plan deactivate
  the Region that is impaired so that your other active Region is appropriately scaled and begins
  to receive all of your application traffic.
- If your application is deployed with an active/passive approach, the workflows in your plan
  deactivate the impaired Region and activate your standby Region, by scaling up your resources there, if
  needed, and redirecting your application traffic to the standby Region.
  To perform application recovery manually, run your Region switch plan by doing the following.

Another option is to trigger an execution automatically with specific Amazon CloudWatch alarms that you specify to
start a plan execution. You can specify triggers for plan execution when you create or update a plan.
For more information, see [Create a trigger for a Region switch plan](working-with-rs-triggers.md "working-with-rs-triggers.md").

# To execute a Region switch plan

1. In the AWS Management Console, navigate to the AWS Region that you want to activate for your application.
2. On the Amazon Application Recovery Controller (ARC) console, choose **Region switch**, and then select the
   plan that you want to run.
3. Choose **Execute plan**.
4. If your plan includes manual approval steps, approve each step when prompted.
   While a plan is executing, you can track its progress on the execution details page, which opens when
   you choose to execute a plan.

You can also view information about in-progress application recovery on the Region switch dashboards. On the Region switch console,
in the left navigation, under **Region switch**,
choose one of the following:

- **Global dashboard**
- **Executions in _Region name_**
  Be aware that, if there are impairments in a Region, the global dashboard might
  not show all your plan data. Because of this, we recommend that you rely only on
  Regional executions dashboard during operational events. The Regional executions dashboard
  is more resilient because it uses the local Region switch data plane.

When plan execution is complete, you can see information about the plan execution, and other plans that Region switch
has run, on the **Plan details** page in the **Plan execution history** tab.
