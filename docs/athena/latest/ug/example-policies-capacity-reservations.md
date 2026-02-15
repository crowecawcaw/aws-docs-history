# Example capacity reservation

policies

This section includes example policies you can use to enable various actions on capacity
reservations. Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

A capacity reservation is an IAM resource managed by Athena. Therefore, if your capacity
reservation policy uses actions that take `capacity-reservation` as an input, you
must specify the capacity reservation's ARN as follows:

```
"Resource": [arn:aws:athena:`<region>`:`<user-account>`:capacity-reservation/`<capacity-reservation-name>`]
```

Where `<capacity-reservation-name>` is the name
of your capacity reservation. For example, for a capacity reservation named
`test_capacity_reservation`, specify it as a resource as follows:

```
"Resource": ["arn:aws:athena:`us-east-1`:`123456789012`:capacity-reservation/test_capacity_reservation"]
```

For a complete list of Amazon Athena actions, see the API action names in the [Amazon Athena API Reference](../APIReference.md "../APIReference.md"). For more information about IAM policies,
see [Creating policies with the visual editor](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-visual-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-visual-editor") in the
_IAM User Guide_.

###### Example policy to list capacity reservations

The following policy allows all users to list all capacity reservations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:ListCapacityReservations"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example policy for management operations

The following policy allows a user to create, cancel, obtain details, and update the
capacity reservation `test_capacity_reservation`. The policy also allows a
user to assign `workgroupA` and `workgroupB` to
`test_capacity_reservation`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect": "Allow",
 "Action": [
 "athena:CreateCapacityReservation",
 "athena:GetCapacityReservation",
 "athena:CancelCapacityReservation",
 "athena:UpdateCapacityReservation",
 "athena:GetCapacityAssignmentConfiguration",
 "athena:PutCapacityAssignmentConfiguration"
 ],
 "Resource": [
 "arn:aws:athena:`us-east-1`:`123456789012`:capacity-reservation/`test_capacity_reservation`",
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/`workgroupA`",
 "arn:aws:athena:`us-east-1`:`123456789012`:workgroup/`workgroupB`"
 ]
 }
 ]
}`

```
