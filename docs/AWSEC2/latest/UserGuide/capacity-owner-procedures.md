# Interruptible Capacity Reservations for capacity owners

The capacity owner is the account that owns the source Capacity Reservation and creates the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.

This section covers how you (the capacity owner) can create, modify, reclaim, and track an interruptible Capacity Reservation.

###### Topics

- [Creating an interruptible Capacity Reservation](#creating-interruptible-cr "#creating-interruptible-cr")
- [View your interruptible Capacity Reservation](#view-interruptible-cr "#view-interruptible-cr")
- [Modifying your interruptible Capacity Reservation](#modify-interruptible-cr "#modify-interruptible-cr")
- [Reclamation process and tracking](#reclamation-process "#reclamation-process")

## Creating an interruptible Capacity Reservation

Create an interruptible Capacity Reservation to make unused capacity from your source reservation available for other workloads while maintaining control to reclaim it when needed.

### Prerequisites

Before creating an interruptible allocation, ensure your source On-Demand Capacity Reservation meets these requirements:

- Your Capacity Reservation must be in active state with no end date set. You can't create allocations from reservations that are pending, expired, cancelled, or have scheduled end dates.
- Your Capacity Reservation must have available capacity for allocation. You can only allocate available instances (also called unused capacity).
- You can create only one interruptible allocation per source Capacity Reservation. If an allocation already exists, you must modify or cancel it before creating a new one.
- You can allocate a maximum of 1000 instances at once to an interruptible Capacity Reservation.

Use can use the console or the AWS CLI to create an interruptible Capacity Reservation.

Console

###### To create an interruptible Capacity Reservation

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations**.
3. Select your Capacity Reservation.
4. Choose **Actions**, **Create interruptible allocation**.
5. For **Instances to allocate**, enter the number of instances to allocate.
6. (Optional) Add tags.
7. Choose **Create interruptible capacity allocation**.

AWS CLI

###### To create an interruptible Capacity Reservation

Use the [create-interruptible-capacity-reservation-allocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-interruptible-capacity-reservation-allocation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-interruptible-capacity-reservation-allocation.html") command:

```
aws ec2 create-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id `cr-1234567890abcdef0` \
    --instance-count `10`
```

## View your interruptible Capacity Reservation

After creating an interruptible Capacity Reservation, you can view the interruptible reservation in your account or from a specific resource.

### View all interruptible Capacity Reservations in your account

Use the following procedure to view the interruptible Capacity Reservations in your account.

Console

###### To view the interruptible Capacity Reservations in your account

1. Go to the Capacity Reservations page in the console.
2. Look for reservations with **Interruptible** in the type column.
3. Select the interruptible reservation to view details.

AWS CLI
**To view the interruptible Capacity Reservations in your account**

```
aws ec2 describe-capacity-reservations \
    --capacity-reservation-id `cr-interruptible-id` \
    --filters Name=interruptible,Values=true
```

### View interruptible Capacity Reservation from a specific source

Use the following procedure to view the interruptible Capacity Reservation created from a specific source Capacity Reservation.

```
aws ec2 describe-capacity-reservations \
    --capacity-reservation-id `cr-source-id`
```

In the response, you'll find an `interruptibleCapacityAllocations` object that contains the interruptible
Capacity Reservation ID and allocation details. For information about the response structure, see
[InterruptibleCapacityAllocation](../APIReference/API_InterruptibleCapacityAllocation.md "../APIReference/API_InterruptibleCapacityAllocation.md") in
the _Amazon EC2 API Reference_.

## Modifying your interruptible Capacity Reservation

Use the following procedures to edit or cancel your interruptible Capacity Reservation.

###### Note

- When you reduce the allocation, we first reclaim available instances, then running instances, until we meet the requested count.
  If we can meet the count entirely with available instances, no termination occurs. All modifications to allocated instance count are
  done through the source Capacity Reservation, not directly on the interruptible Capacity Reservation.
- You can only modify an interruptible Capacity Reservation by a maximum of 1000 instances at once (increase or decrease).

### Edit your interruptible Capacity Reservation

Use the following procedure to edit your interruptible Capacity Reservation.

Console

1. From the source Capacity Reservation details page, choose **Actions**. Then, **Edit
   interruptible Capacity Reservation**.
2. For **Instances to allocate**, enter the new number:
   - Add more capacity to share
   - Reclaim capacity to your source Capacity Reservation

3. Choose **Update**.

AWS CLI

```
aws ec2 update-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id `cr-1234567890abcdef0` \
    --target-instance-count `80`
```

### Cancel your interruptible Capacity Reservation

Use the following procedure to permanently remove the allocation and return all capacity.

Console

1. From the source Capacity Reservation details page, navigate to the interruptible capacity allocation details.
2. Choose **Edit interruptible allocation**.
3. For Instance count, enter **0**.
4. Choose **Update**.

AWS CLI

```
aws ec2 update-interruptible-capacity-reservation-allocation \
--capacity-reservation-id `cr-1234567890abcdef0` \
--target-instance-count `0`
```

## Reclamation process and tracking

When you reclaim capacity:

- Running instances receive a 2-minute interruption warning through EventBridge events.
- After the notice period, running instances in the reclaimed capacity enter a shutting down state and get terminated.
- When terminated, the reclaimed instances become available in your source Capacity Reservation for immediate use.
- Your allocation status changes from **updating** to **active** when complete.

Complete reclamation can take a few minutes depending on instance type and shutdown time. For more information about the EventBridge notification you
receive when the process is complete, see [Reclamation completion](monitor-interruptible-cr.md#reclamation-completion "monitor-interruptible-cr.md#reclamation-completion").

### Track reclamation status

Monitor reclamation progress by describing your source reservation:

```
aws ec2 describe-capacity-reservations \
--capacity-reservation-id `cr-1234567890abcdef0`
```

The response shows these fields within the `interruptibleCapacityAllocation` object:

- `instance-count`: Current allocated instances
- `target-instance-count`: Requested quantity after reclamation
- `status`: **updating** during reclamation and **active** when complete

### Sharing interruptible reservations

You can share interruptible reservations only within your AWS organization using AWS Resource Access Manager (RAM).

Considerations:

- If a consumer account leaves your organization, the interruptible reservation is automatically unshared from that account.
- Any instances running in the unshared reservation are eventually terminated.
- All other sharing functionality works the same as standard Capacity Reservations.

For complete sharing procedures, see [Sharing Capacity Reservations](capacity-reservation-sharing.md "capacity-reservation-sharing.md").
