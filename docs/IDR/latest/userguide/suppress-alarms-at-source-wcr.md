# Submit a workload change request to suppress alarms

If you can’t suppress alarms at the source as described in the previous section, then submit a Workload Change Request to instruct Incident Detection and Response to manually suppress monitoring of some or all of your workload’s alarms.

For detailed instructions on how to create a Workload Change Request, see [Request changes to an onboarded workload in Incident Detection and Response](idr-workloads-change-request.md "idr-workloads-change-request.md"). When raising a Workload Change Request to request suppression of your alarms, make sure that you provide the following required information

- **Workload name:** Your workload name.
- **Account ID(s):** ID1, ID2, ID3, and so on.
- **Change details:** Alarm Suppression
- **Suppression start time:** Date, time, and time zone.
- **Suppression end time:** Date, time, and time zone.
- **Alarms to suppress:** A list of CloudWatch alarm ARNs or third party APM event identifiers to suppress.
  After you create the alarm suppression Workload Change Request, you receive the following notifications from Incident Detection and Response:

- Acknowledgement of your Workload Change Request.
- Notification when alarms are suppressed.
- Notification when alarms are re-enabled for monitoring.
