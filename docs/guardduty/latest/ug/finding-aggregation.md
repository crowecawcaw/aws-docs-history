# GuardDuty finding aggregation

GuardDuty updates the generated findings dynamically. If GuardDuty detects a new activity related to the
same security issue, then instead of creating a new finding, GuardDuty will update the original finding
with the latest details. This behavior allows you to identify any ongoing
issues, without the need to look through multiple similar reports, and reduces the
overall volume of findings for known security issues.

For example, for UnauthorizedAccess:EC2/SSHBruteForce
finding, multiple access attempts against your instance will be aggregated to the same
finding ID, increasing the **Count** number in the finding's details. This is because that
finding represents a single security issue with the instance indicating that the SSH
port on the instance is not properly secured against this type of activity. However, if
GuardDuty detects SSH access activity targeting a new instance in your environment, it will
create a new finding with a unique finding ID to alert you to the fact that there is a
security issue associated with the new resource.

When a finding is aggregated, it is updated with information from the latest occurrence
of that activity. This means that in the above example, if your instance is the target
of a brute force attempt from a new actor, the finding details will be updated to
reflect the remote IP of the most recent source and older information will be replaced.
Complete information about individual activity attempts will still be available in your CloudTrail
logs or VPC Flow Logs.

The criteria that alert GuardDuty to generate a new finding instead of aggregating an
existing one is dependent on the finding type. The aggregation criteria for each finding
type is determined by our security engineers to provide an overview of distinct
security issues within your account.

When GuardDuty generates an attack sequence finding type in your account, the finding will be
aggregated only when you GuardDuty identifies the similar signals in the same sequence in your account. Otherwise,
GuardDuty will generate another attack sequence.
