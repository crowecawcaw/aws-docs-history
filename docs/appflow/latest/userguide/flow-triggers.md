

# Flow triggers
<a name="flow-triggers"></a>

A *trigger* determines how a flow runs. The following are the supported flow trigger types:
+ **Run on demand** — Users manually run the flow as needed.
+ **Run on event** — Amazon AppFlow runs the flow in response to an event from an SaaS application.
+ **Run on schedule** — Amazon AppFlow runs the flow on a recurring schedule.

## On demand flows
<a name="flow-triggers-demand"></a>

You can manually run on-demand flows as needed. You must run this type of flow each time you want to transfer the data. For more information, see [Managing Amazon AppFlow flows](flows-manage.md).

## Event-triggered flows
<a name="flow-triggers-event"></a>

Amazon AppFlow runs event-triggered flows based on a specified change event in the source application.

This option is available only for SaaS applications that provide change events. You must choose the event when you choose the source.

## Schedule-triggered flows
<a name="flow-triggers-schedule"></a>

Amazon AppFlow runs schedule-triggered flows based on the schedule that you specify during flow setup. The scheduling frequency depends on the frequency supported by the source application.

You can choose either full or incremental data transfer for schedule-triggered flows.

### Full transfer
<a name="flow-triggers-schedule-full"></a>

When you select full transfer, Amazon AppFlow transfers a snapshot of all records at the time of the flow run from the source to the destination.

### Incremental transfer
<a name="flow-triggers-schedule-incremental"></a>

When you select incremental transfer, Amazon AppFlow transfers only the records that have been added or changed since the last successful flow run. You can also select a source timestamp field to specify how Amazon AppFlow identifies new or changed records. For example, if you have a *Created Date* timestamp field, choose this to instruct Amazon AppFlow to transfer only newly-created records (and not changed records) since the last successful flow run. The first schedule-triggered flow will pull 30 days of past records at the time of the first flow run.

**Tip**  
To transfer records created or modified over a different time range other than the past 30 days at the time of the first flow run, set up the flow to be triggered on demand. You can then use the filter option to pull records over the desired time range. After the on-demand flow runs and pulls the initial set of records, edit the flow to be triggered on schedule so that subsequent flow runs transfer incremental data.

**Offset option**  
Optionally, you can add a time offset (*t*) to the time range for the incremental transfer. The flow run will import records that were created or changed between the previous flow run and the specified offset prior to the current flow run. This feature can be used to accommodate any latencies in the source systems in timestamping changes to records. By choosing a sufficiently large offset, you can avoid missing records that changed in the source application close to the run time of the scheduled flow.

If a schedule-triggered flow runs at time instances *T0*, *T1*, *T2*, and so on, then records that are new or have changed between *T0 minus t* and *T1 minus t* will be imported from the source at *T1*, and those that have changed between *T1 minus t* and *T2 minus t* will be imported from the source at *T2*.

The total offset value can be longer than the schedule interval (for example,* t* can be longer than *T1 minus T0*), but it must be less than 10 hours. The default value is 0.

![Timeline showing flow run times at T0 through T3, with timestamps T0-t through T3-t used to query source records.](http://docs.aws.amazon.com/appflow/latest/userguide/images/time_offset.png)

+ The flow run at *T0* transfers records that changed between *T0 minus 30 days* and *T0 minus t* in the source application.
+ The flow run at *T1* transfers records that changed between *T0 minus t* and *T1 minus t* in the source application.
+ The flow run at *T2* transfers records that changed between *T1 minus t* and *T2 minus t* in the source application.
+ The flow run at *T3* transfers records that changed between *T2 minus t* and *T3 minus t* in the source application.