AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Update an AWS Mainframe Modernization runtime environment

Use the AWS Mainframe Modernization console to update an AWS Mainframe Modernization runtime environment. You can update the minor
version of the runtime engine or the instance type that hosts the runtime environment. You can
choose whether you want to apply updates immediately or during the preferred maintenance
window.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md").

## Update a runtime environment

###### To update a runtime environment

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the Region where the environment that you want
   to update was created.
3. On the **Environments** page, choose the environment that you want
   to update.
4. On the details page for the environment, choose **Actions**, and
   then choose **Edit environment**.
5. Make any of the following changes:
   - In the **Engine options** section, choose the engine version
     that you want.
   - In the **Resources** section, choose the instance type that you
     want.
   - In the **Maintenance window** section, choose the day, time,
     and duration that you want.

###### Note

The only changes that you can choose to apply during the maintenance window are
changes to the engine version. You must apply all other changes immediately. 6. Choose **Next**. 7. In **When to apply these changes**, choose
**Immediately** or **During the next maintenance
window**. Then choose **Update environment**.

If you choose **Immediately**, you see a message when the environment
has finished updating.

## AWS Mainframe Modernization maintenance window

Every runtime environment has a weekly two-hour maintenance window. Any system changes
are applied during this time. The maintenance window is your chance to control when
modifications, and software and security patching occurs. If a maintenance event is
scheduled for a given week, it begins during that two-hour maintenance window. Most
maintenance events also complete during the two-hour maintenance window, although larger
maintenance events might take more than a couple of hours to complete.

The two-hour maintenance window is selected at random from an 8 hour block of time per
Region. If you don't specify a maintenance window when you create a runtime environment,
AWS Mainframe Modernization assigns a 2 hour maintenance window on a randomly selected day of the week.

AWS Mainframe Modernization consumes some of the resources in your environment instance while maintenance is
being applied. You might observe a minimal effect on performance or some disruptions in
applications during maintenance.
