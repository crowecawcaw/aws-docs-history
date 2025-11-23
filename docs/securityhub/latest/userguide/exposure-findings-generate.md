# Generating exposure findings

###### Note

AWS Security Hub is in preview release and is subject to change.

Security Hub generates exposure findings in near real-time.
As new security findings are ingested and existing findings are updated, Security Hub generates or updates exposure findings in near real time.
Security Hub generates one exposure finding per resource ID.

If a resource doesn't have any exposure traits or has insufficient traits, Security Hub
doesn't generate an exposure finding for that resource. Security Hub doesn't publish
exposure findings for resource types not supported by exposure findings. When a resource
has a significant number and combination of traits, Security Hub generates an exposure
finding. The number and combination of traits also determine the severity level of the
exposure finding.
