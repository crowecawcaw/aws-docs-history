# Re-scanning previously scanned Amazon EC2

instance

Whether a scan is GuardDuty-initiated or started on-demand, you can start a new on-demand malware scan on
the same Amazon EC2 instance after 1 hour from the start time of the previous malware scan. If the new
malware scan gets started within 1 hour of initiation of the previous malware scan, your request
will result in the following error, and no scan ID will get generated for this request.

`A scan was started on this resource recently. You can request a scan on the same
 resource one hour after the previous scan start time.`

The steps to re-scan the instance remain the same as starting an on-demand malware scan
for the first time. For information about the steps, see [Start On-demand malware scan](malware-protection-getting-started-on-demand-scan.md#malware-protection-initiate-on-demand-malware-scan "malware-protection-getting-started-on-demand-scan.md#malware-protection-initiate-on-demand-malware-scan").

To track the status of the malware scans, see [Monitoring scan statuses and results in
Malware Protection for EC2](malware-protection-scans.md "malware-protection-scans.md").
