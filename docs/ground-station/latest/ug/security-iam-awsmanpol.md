# AWS managed policies for AWS Ground Station

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy: AWSGroundStationAgentInstancePolicy

You can attach the `AWSGroundStationAgentInstancePolicy` policy to your IAM identities.

This policy grants AWS Ground Station Agent permissions to your Amazon EC2 instance that
allows the instance to send and receive data during Ground Station contacts. All
permissions in this policy are from the Ground Station service.

**Permissions details**

This policy includes the following permissions.

- `groundstation` – Allows dataflow endpoint instances to call the Ground Station Agent APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "groundstation:RegisterAgent",
 "groundstation:UpdateAgentStatus",
 "groundstation:GetAgentConfiguration"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS

managed policy: AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy

You can not attach AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy to your IAM entities. This policy is attached to a
service-linked role that allows AWS Ground Station to perform actions on your behalf. For more
information, see [Using service linked roles](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants EC2 permissions that allow AWS Ground Station to find public IPv4 addresses.

**Permissions details**

This policy includes the following permissions.

- `ec2:DescribeAddresses` – Allows AWS Ground Station to list all IPs associated with EIPs on
  your behalf.
- `ec2:DescribeNetworkInterfaces` – Allows AWS Ground Station to get information on the network
  interfaces associated with EC2 instances on your behalf.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAddresses",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS Ground Station updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Ground Station since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Ground Station Document history page.

| Change                                                                                                                                                                                                                                             | Description                                                                                                                                                                                               | Date              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSGroundStationAgentInstancePolicy](#security-iam-awsmanpol-AWSGroundStationAgentInstancePolicy "#security-iam-awsmanpol-AWSGroundStationAgentInstancePolicy") –<br>New policy                                                                   | AWS Ground Station added a new policy to provide the dataflow endpoint instance permissions to use the AWS Ground Station Agent.                                                                          | April 12, 2023    |
| [AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy](#security-iam-awsmanpol-AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy "#security-iam-awsmanpol-AWSServiceRoleForGroundStationDataflowEndpointGroupPolicy") –<br>New policy | AWS Ground Station added a new policy that grants EC2 permissions to allow AWS Ground Station to find public IPv4 addresses associated with EIPs and network interfaces<br>associated with EC2 instances. | November 02, 2022 |
| AWS Ground Station started tracking changes                                                                                                                                                                                                        | AWS Ground Station started tracking changes for AWS managed policies.                                                                                                                                     | March 01, 2021    |
