# Flow triggers

A _trigger_ determines how a flow runs. The following are the supported
flow trigger types:

- **Run on demand** — Users manually run the flow as needed.
- **Run on event** — Amazon AppFlow runs the flow in response to an event
  from an SaaS application.
- **Run on schedule** — Amazon AppFlow runs the flow on a recurring
  schedule.

## On demand flows

You can manually run on-demand flows as needed. You must run this type of flow each time you
want to transfer the data. For more information, see [Managing Amazon AppFlow flows](flows-manage.md "flows-manage.md").

## Event-triggered flows

Amazon AppFlow runs event-triggered flows based on a specified change event in the source application.

This option is available only for SaaS applications that provide change events. You must
choose the event when you choose the source.

## Schedule-triggered flows

Amazon AppFlow runs schedule-triggered flows based on the schedule that you specify during flow setup. The scheduling
frequency depends on the frequency supported by the source application.

You can choose either full or incremental data transfer for schedule-triggered
flows.

### Full transfer

When you select full transfer, Amazon AppFlow transfers a snapshot of all records at the time of
the flow run from the source to the destination.

### Incremental transfer

When you select incremental transfer, Amazon AppFlow transfers only the records that have been
added or changed since the last successful flow run. You can also select a source timestamp
field to specify how Amazon AppFlow identifies new or changed records. For example, if you have a
_Created Date_ timestamp field, choose this to instruct
Amazon AppFlow to transfer only newly-created records (and not changed records) since the last
successful flow run. The first schedule-triggered flow will pull 30 days of past records at the time of the first
flow run.

###### Tip

To transfer records created or modified over a different time range other than the past 30 days at the time of the first flow run, set up the flow
to be triggered on demand. You can then use the filter option to pull records over the desired
time range. After the on-demand flow runs and pulls the initial set of records, edit the flow to
be triggered on schedule so that subsequent flow runs transfer incremental data.

###### Offset option

Optionally, you can add a time offset (_t_) to the time
range for the incremental transfer. The flow run will import records that were created or
changed between the previous flow run and the specified offset prior to the current flow run.
This feature can be used to accommodate any latencies in the source systems in timestamping
changes to records. By choosing a sufficiently large offset, you can avoid missing records that
changed in the source application close to the run time of the scheduled flow.

If a schedule-triggered flow runs at time instances _T0_,
_T1_, _T2_, and so on, then
records that are new or have changed between _T0 minus t_ and
_T1 minus t_ will be imported from the source at _T1_, and those that have changed between _T1
minus t_ and _T2 minus t_ will be imported from the
source at _T2_.

The total offset value can be longer than the schedule interval (for example, _t_ can be longer than _T1 minus T0_),
but it must be less than 10 hours. The default value is 0.

![Timeline showing flow run times T0 to T3 and corresponding timestamps used for change detection.](images/time_offset.png)

- The flow run at _T0_ transfers records that changed
  between _T0 minus 30 days_ and _T0
  minus t_ in the source application.
- The flow run at _T1_ transfers records that changed between
  _T0 minus t_ and _T1 minus
  t_ in the source application.
- The flow run at _T2_ transfers records that changed between
  _T1 minus t_ and _T2 minus
  t_ in the source application.
- The flow run at _T3_ transfers records that changed between
  _T2 minus t_ and _T3 minus
  t_ in the source application.
