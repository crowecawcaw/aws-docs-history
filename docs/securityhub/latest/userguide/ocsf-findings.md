# OCSF findings in Security Hub

###### Note

Security Hub is in preview release and is subject to change.

Security Hub considers findings with `activity_name != Close` as active findings.
Active findings are automatically deleted if they aren’t updated in 90 days.
Security Hub considers findings with `Activity_name = Close` as closed findings.
Closed findings are automatically deleted if they aren’t updated in 14 days.
Security Hub determines when a finding is updated using the most recent value of the finding `modified_time_dt`.
At the end of a finding’s retention period, Security Hub permanently deletes the finding.
Finding providers can change the value of the `finding.info.modified_time_dt` field when they update a finding.
For information about other `Activity_name` values, see [Vulnerability Finding](https://schema.ocsf.io/1.5.0/classes/vulnerability_finding "https://schema.ocsf.io/1.5.0/classes/vulnerability_finding") in the OCSF schema.
