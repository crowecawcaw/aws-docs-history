# Generating exposure findings

###### Note

AWS Security Hub is in preview release and is subject to change.

AWS Security Hub generates exposure findings every 6 hours. During each 6-hour period,
Security Hub considers the available exposure traits for a resource. It produces at most one
exposure finding per resource ID. The uniqueness of a finding is determined by finding
ID, AWS Region, exposure type, and account. This means you can have two resources with
the same ID. However, the resources might have different types of exposures. This
exposure finding aggregates all of the applicable exposure traits that apply to the
resource.

If a resource doesn't have any exposure traits or has insufficient traits, Security Hub
doesn't generate an exposure finding for that resource. Security Hub doesn't publish
exposure findings for resource types not supported by exposure findings. When a resource
has a significant number and combination of traits, Security Hub generates an exposure
finding. The number and combination of traits also determine the severity level of the
exposure finding.
