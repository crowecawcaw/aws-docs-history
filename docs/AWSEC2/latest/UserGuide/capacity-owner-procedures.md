

# Interruptible Capacity Reservations for capacity owners
<a name="capacity-owner-procedures"></a>

The capacity owner is the account that owns the source Capacity Reservation and creates the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.

This section covers how you (the capacity owner) can create, modify, reclaim, and track an interruptible Capacity Reservation.

**Topics**
+ [Creating an interruptible Capacity Reservation](#creating-interruptible-cr)
+ [View your interruptible Capacity Reservation](#view-interruptible-cr)
+ [Modifying your interruptible Capacity Reservation](#modify-interruptible-cr)
+ [Retaining interruptible Capacity Reservation at zero capacity](#retain-interruptible-cr-zero-capacity)
+ [Reclamation process and tracking](#reclamation-process)
+ [Sharing interruptible reservations](#sharing-interruptible-reservations)

## Creating an interruptible Capacity Reservation
<a name="creating-interruptible-cr"></a>

Create an interruptible Capacity Reservation to make unused capacity from your source reservation available for other workloads while maintaining control to reclaim it when needed.

### Prerequisites
<a name="interruptible-cr-prerequisites"></a>

Before creating an interruptible allocation, ensure your source On-Demand Capacity Reservation meets these requirements:
+ Your Capacity Reservation must be in active state with no end date set. You can't create allocations from reservations that are pending, expired, cancelled, or have scheduled end dates.
+ Your Capacity Reservation must have available capacity for allocation. You can only allocate available instances (also called unused capacity).
+ You can create only one interruptible allocation per source Capacity Reservation. If an allocation already exists, you must modify or cancel it before creating a new one.
+ You can allocate a maximum of 1000 instances at once to an interruptible Capacity Reservation.

You can use the console or the AWS CLI to create an interruptible Capacity Reservation.

------
#### [ Console ]

**To create an interruptible Capacity Reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Capacity Reservations**.

1. Select your Capacity Reservation.

1. Choose **Actions**, **Create interruptible reservation**.

1. For **Quantity**, enter the number of instances to allocate.

1. For **Allocation preference when all capacity is reclaimed**, choose **Default** or **Retain**.

1. (Optional) Add tags.

1. Choose **Create interruptible reservation**.

------
#### [ AWS CLI ]

**To create an interruptible Capacity Reservation**  
Use the [create-interruptible-capacity-reservation-allocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-interruptible-capacity-reservation-allocation.html) command:

```
aws ec2 create-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --instance-count {{10}}
```

------

## View your interruptible Capacity Reservation
<a name="view-interruptible-cr"></a>

After creating an interruptible Capacity Reservation, you can view the interruptible reservation in your account or from a specific resource.

### View all interruptible Capacity Reservations in your account
<a name="view-all-interruptible-cr"></a>

Use the following procedure to view the interruptible Capacity Reservations in your account.

------
#### [ Console ]

**To view the interruptible Capacity Reservations in your account**

1. Go to the Capacity Reservations page in the console.

1. In the **Interruptible** column, look for reservations marked **Yes**.

1. Select the interruptible reservation to view details.

------
#### [ AWS CLI ]

**To view the interruptible Capacity Reservations in your account**

```
aws ec2 describe-capacity-reservations \
    --capacity-reservation-id {{cr-interruptible-id}} \
    --filters Name=interruptible,Values=true
```

------

### View interruptible Capacity Reservation from a specific source
<a name="view-interruptible-cr-from-source"></a>

Use the following procedure to view the interruptible Capacity Reservation created from a specific source Capacity Reservation.

```
aws ec2 describe-capacity-reservations \
    --capacity-reservation-id {{cr-source-id}}
```

In the response, you'll find an `interruptibleCapacityAllocation` object that contains the interruptible Capacity Reservation ID and allocation details. For information about the response structure, see [InterruptibleCapacityAllocation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InterruptibleCapacityAllocation.html) in the *Amazon EC2 API Reference*.

## Modifying your interruptible Capacity Reservation
<a name="modify-interruptible-cr"></a>

Use the following procedures to edit or cancel your interruptible Capacity Reservation.

**Note**  
When you reduce the allocation, we first reclaim available instances, then running instances, until we meet the requested count. If we can meet the count entirely with available instances, no termination occurs. All modifications to allocated instance count are done through the source Capacity Reservation, not directly on the interruptible Capacity Reservation.
You can only modify an interruptible Capacity Reservation by a maximum of 1000 instances at once (increase or decrease).

### Edit your interruptible Capacity Reservation
<a name="edit-interruptible-allocation"></a>

Use the following procedure to edit your interruptible Capacity Reservation.

------
#### [ Console ]

1. From the source Capacity Reservation details page, choose the **Edit interruptible allocation** link.

1. For **Quantity**, enter the new number:
   + Add more capacity to share
   + Reclaim capacity to your source Capacity Reservation

1. Choose **Update**.

------
#### [ AWS CLI ]

```
aws ec2 update-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --target-instance-count {{80}}
```

------

### Cancel your interruptible Capacity Reservation
<a name="cancel-interruptible-allocation"></a>

Use the following procedure to permanently remove the allocation and return all capacity.

------
#### [ Console ]

1. From the source Capacity Reservation details page, navigate to the interruptible capacity allocation details.

1. Choose **Edit interruptible allocation**.

1. For **Quantity**, enter `0`.

1. Choose **Update**.

------
#### [ AWS CLI ]

```
aws ec2 update-interruptible-capacity-reservation-allocation \
--capacity-reservation-id {{cr-1234567890abcdef0}} \
--target-instance-count {{0}}
```

------

**Retain zero size preference**  
If you configured `retain` for the zero size preference, the interruptible Capacity Reservation stays active at zero instances. To cancel it, update the zero size preference to `default`, and then reduce the allocation to zero. For more information, see [Retaining interruptible Capacity Reservation at zero capacity](#retain-interruptible-cr-zero-capacity).

## Retaining interruptible Capacity Reservation at zero capacity
<a name="retain-interruptible-cr-zero-capacity"></a>

By default, Amazon EC2 cancels the interruptible reservation when you reduce its allocation to zero instances. The reclaimed capacity returns to your source Capacity Reservation.

If you expect to share capacity again later, you can configure the interruptible reservation to remain active at zero instances. With this option, you can allocate instances to the same reservation later without recreating it.

You control this behavior with the zero size preference. You can set it when you create or edit an interruptible Capacity Reservation allocation, either in the console or with the AWS CLI.

------
#### [ Console ]

On the **Create interruptible reservation** or **Edit interruptible allocation** page, for **Allocation preference when all capacity is reclaimed**, choose one of the following:
+ **Default** – Amazon EC2 cancels the interruptible Capacity Reservation when you reduce its allocation to zero.
+ **Retain** – The interruptible Capacity Reservation remains active at zero capacity when you reduce its allocation to zero. You can then allocate instances to it again later.

After you save the change, the setting appears as the read-only **Zero size preference** field on the interruptible Capacity Reservation details.

------
#### [ AWS CLI ]

To keep the interruptible Capacity Reservation active at zero capacity, specify `--zero-size-preference retain` when you call [create-interruptible-capacity-reservation-allocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-interruptible-capacity-reservation-allocation.html) or [update-interruptible-capacity-reservation-allocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/update-interruptible-capacity-reservation-allocation.html). To cancel the reservation when its allocation reaches zero, specify `default`.

```
aws ec2 update-interruptible-capacity-reservation-allocation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --zero-size-preference retain
```

------

## Reclamation process and tracking
<a name="reclamation-process"></a>

When you reclaim capacity:
+ Running instances receive a 2-minute interruption warning through EventBridge events.
+ After the notice period, running instances in the reclaimed capacity enter a shutting down state and get terminated.
+ When terminated, the reclaimed instances become available in your source Capacity Reservation for immediate use.
+ Your allocation status changes from **updating** to **active** when complete.

Complete reclamation can take a few minutes depending on instance type and shutdown time. For more information about the EventBridge notification you receive when the process is complete, see [Reclamation completion](monitor-interruptible-cr.md#reclamation-completion).

### Track reclamation status
<a name="track-reclamation-status"></a>

Monitor reclamation progress by describing your source reservation:

```
aws ec2 describe-capacity-reservations \
--capacity-reservation-id {{cr-1234567890abcdef0}}
```

The response shows these fields within the `interruptibleCapacityAllocation` object:
+ `instance-count`: Current allocated instances
+ `target-instance-count`: Requested quantity after reclamation
+ `status`: **updating** during reclamation and **active** when complete

## Sharing interruptible reservations
<a name="sharing-interruptible-reservations"></a>

You can share interruptible reservations only within your AWS organization using AWS Resource Access Manager (RAM).

Considerations:
+ If a consumer account leaves your organization, the interruptible reservation is automatically unshared from that account.
+ Any instances running in the unshared reservation are eventually terminated.
+ All other sharing functionality works the same as standard Capacity Reservations.

For complete sharing procedures, see [Sharing Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-sharing.html).