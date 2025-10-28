# Managing Amazon AppFlow flows

After you create one or more flows, you can use the **Flows** page in the
Amazon AppFlow console to manage them.

###### To go to the **Flows** page

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Flows**. The console shows
   the **Flows** page. This page contains a table that summarizes the flows
   that you've created.

###### To view the details for flow

- Select a flow, and choose **View details**. The console shows the flow
  details page.

The **Flow details** section shows details about the flow, its data
source, and its destination. To view additional information, choose any of the following
tabs:

**Data field settings**

Details about how data is mapped between the source and destination.

**Partition and aggregation settings**

Details about how the flow organizes output data into partitions and aggregates it
into files.

**Filters**

Details about the filters that control which data the flow sends to the
destination.

**Tags**

The tag keys and values that you've applied to the flow.

**Run history**

Details about each run that has occurred for the flow, such as the date, transfer
size, and status.

###### To initiate a flow

To initiate a flow, you _activate_ or _run_ it. The action that you take depends on whether you configured
the flow to run on a schedule, based on an event, or on demand.

- Select a flow, and choose **View details**. Then, do one of the
  following:
  - If the flow runs on a schedule or based on an event, choose
    **Activate** to activate the flow. To deactivate the flow, choose
    **Deactivate flow**.
  - If the flow runs on demand, choose **Run flow** whenever you want
    to transfer the data.

###### To update a flow

- Select a flow, and choose **Edit**. The console shows the flow creation
  process, and you can navigate the pages to revise settings such as field mappings, trigger
  type, and filters. You can't change the flow name, source, or destination. The changes apply
  only to flow runs that occur after you save your changes.

###### To copy a flow

- Select a flow, and choose **Copy to new flow**. The console shows the
  flow creation process, and it copies the initial settings from the flow that you copied. You
  can modify these settings before you create the new flow.

###### To cancel a flow

You can cancel any flow that's currently running.

- Select a flow, and choose **View details**. Then, do either of the
  following:

      + If the page shows a banner about your active flow run, choose **Cancel this
       flow run** in the banner. If multiple runs are active at the same time, you
       can cancel all of them.
      + Choose the **Run history** tab and do the following:


      	1. Select the checkbox for the flow run that you want to cancel. You can select
      	 multiple runs.
      	2. Choose **Cancel selected flow run**.

  You cannot resume a run after you cancel it.

###### Note

When you cancel a run, you still incur charges for any data that the run already processed
before the cancellation. If the run had already written some data to the flow destination,
then that data remains in the destination. If you configured the flow to use a batch API (such
as the Salesforce Bulk API 2.0), then the run will finish reading or writing its entire batch
of data after the cancellation. For these operations, the data processing charges for Amazon AppFlow
apply. For the pricing information, see [Amazon AppFlow
pricing](https://aws.amazon.com/appflow/pricing/ "https://aws.amazon.com/appflow/pricing/").

###### To delete a flow

- Select a flow, and choose **Delete**. When the console prompts you to
  confirm the operation, type `delete`, and then choose
  **Delete**.
