# Split off capacity from an existing

Capacity Reservation

You can split off capacity from an existing Capacity Reservation to create a new reservation. By
splitting capacity, you allocate a portion of the original reservation to a specific
workload or share it with another AWS account. For example, to partially share a Capacity Reservation
with another account, you can split off some of the capacity to create a smaller sized
Capacity Reservation. The smaller sized Capacity Reservation can then be shared with the other accounts using [AWS Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

When you split capacity from an existing Capacity Reservation, a new Capacity Reservation is automatically created.
The existing reservation will be unchanged, except for the reduced total capacity from
the number of instances split off. Instances that are running in the existing Capacity Reservation are
not affected. You can split the existing reservation into only one new Capacity Reservation.

The new Capacity Reservation will have the same configuration as the existing Capacity Reservation except for tags. By
default, the new Capacity Reservation doesn't have any tags. You can specify new tags during the split
operation. The new Capacity Reservation can also be modified after it is created, if necessary.

When you specify the quantity of instances to be split, by default, any available
capacity is split first, followed by any eligible running instances (the used capacity
in your reservation). For example: if you split 4 instances from a Capacity Reservation with 5 used
instances and 3 available instances, then the 3 available instances and 1 used instance
will be split into a new reservation.

## Prerequisites for splitting

capacity

As a prerequisite, your Capacity Reservation must meet the following requirements:

- The source reservation must be in the active state.
- The source reservation must be owned by your AWS account.

###### Note

When you split used capacity from your reservation by specifying a **Quantity to split** that's greater than the available
capacity, only the instances that were launched with their **Capacity Reservation Specification** as `open` will be
split.

## Considerations

The following considerations apply when splitting off capacity from one
reservation to a new one:

- The used capacity can only be split for Capacity Reservations with “open” instance
  eligibility that are not shared with any account.
- When you split the used capacity, the eligible instances are randomly
  selected. You cannot specify which running instances are split. If a
  sufficient number of eligible instances are not found to fulfill the split
  quantity, the split operation will fail.
- The maximum quantity of instances to split from an existing reservation is
  the size of the reservation minus one. For example, if your reservation’s
  total capacity is 5 instances, you can split a maximum of 4 instances into a
  new reservation.
- **Future-dated Capacity Reservations** – You can't
  split capacity for a future-dated Capacity Reservation during the commitment period.
- **Resource groups** – If the existing
  Capacity Reservation belongs to a resource group, the new Capacity Reservation will not be automatically
  added to the resource group. You can add the new Capacity Reservation to a resource group
  after it is created, if necessary.
- **Sharing** – If the existing Capacity Reservation is
  shared with a consumer account, the new Capacity Reservation will not be automatically
  shared with the consumer account. You can share the new Capacity Reservation after it is
  created, if necessary.
- **Cluster placement group** – If the
  existing Capacity Reservation is part of a cluster placement group, the new Capacity Reservation will be
  created in the same cluster placement group.

###### Note

Splitting capacity from a Capacity Block isn't supported.

## Control access for

splitting Capacity Reservations using tags

You can use tags to control access to Amazon EC2 resources, including splitting
capacity from an existing Capacity Reservation to create a new Capacity Reservation. For more information, see
[Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the
_IAM User Guide_.

To control access for splitting a Capacity Reservation using tags, make sure that you specify both
resource and request tags in the policy statement because IAM policies are
evaluated against both the source Capacity Reservation and the newly created Capacity Reservation. The following
example policy includes the `ec2:ResourceTag` condition key with the tag
`Owner=ExampleDepartment1` for the source Capacity Reservation and the
`ec2:RequestTag` condition key with the tag
`stack=production` for the newly created Capacity Reservation.

```

{
  "Statement": [
    {
      "Sid": "AllowSourceCapacityReservation",
      "Effect": "Allow",
      "Action": "ec2:CreateCapacityReservationBySplitting",
      "Resource": "arn:aws:ec2:us-east-1:111122223333:capacity-reservation/cr-1234567890abcdef0",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Owner": "ExampleDepartment1"
        }
      }
    },
    {
      "Sid": "AllowNewlyCreatedCapacityReservation",
      "Effect": "Allow",
      "Action": ["ec2:CreateCapacityReservationBySplitting", "ec2:CreateTags"],
      "Resource": "arn:aws:ec2:us-east-1:111122223333:capacity-reservation/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/stack": "production"
        }
      }
    }
  ]
}
```

## Split off capacity

You can split off capacity from an existing Capacity Reservation to create a new Capacity Reservation.

Console

###### To split off capacity

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Capacity Reservations**.
3. Select an On-Demand Capacity Reservation ID that has capacity to split.
4. Under **Actions**, **Manage
   capacity**, choose
   **Split**.
5. On the **Split Capacity Reservation** page, under
   **Quantity to split**, use the slider or
   type the number of instances to split from the current
   reservation.
6. (Optional) Add tags for the new Capacity Reservation.
7. Review the summary, and when you're ready, choose
   **Split**.

AWS CLI

###### To split off capacity

Use the `create-capacity-reservation-by-splitting`
command. The following example creates a new Capacity Reservation by splitting off
10 instances from the specified Capacity Reservation.

```
aws ec2 create-capacity-reservation-by-splitting \
    --source-capacity-reservation-id `cr-1234567890abdef0` \
    --instance-count `10`
```

PowerShell

###### To split off capacity

Use the [New-EC2CapacityReservationBySplitting](../../../powershell/latest/reference/items/New-EC2CapacityReservationBySplitting.md "../../../powershell/latest/reference/items/New-EC2CapacityReservationBySplitting.md")
cmdlet. The following example creates a new Capacity Reservation by splitting off
10 instances from the specified Capacity Reservation.

```
New-EC2CapacityReservationBySplitting `
    -SourceCapacityReservationId `cr-1234567890abdef0` `
    -InstanceCount `10`
```
