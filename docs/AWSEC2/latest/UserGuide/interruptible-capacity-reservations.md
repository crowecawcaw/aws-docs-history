# Interruptible Capacity Reservations

Interruptible Capacity Reservations help you make unused capacity temporarily available for other workloads within your account. This gives you control to reclaim capacity when needed. When you reclaim capacity, any instances running inside the interruptible reservation are terminated. After creating an interruptible reservation, you can share it with additional AWS accounts or your AWS organization using AWS Resource Access Manager (RAM).

Use interruptible Capacity Reservations when you have unused reserved capacity during off-peak periods, between deployments, or when workloads scale down. If you know another team that could use this capacity, you can make it available by creating an interruptible Capacity Reservation. When your critical workload needs capacity back, you can reclaim it.

You can use interruptible Capacity Reservations as one of the following:

- **Capacity owner** – You own the source Capacity Reservation and create the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.
- **Capacity consumer** – You launch instances into shared interruptible reservations, understanding that your instances may be terminated when the owner reclaims capacity.

###### Topics

- [How it works](#how-interruptible-cr-works "#how-interruptible-cr-works")
- [Billing](#interruptible-cr-billing "#interruptible-cr-billing")
- [Considerations](#interruptible-cr-considerations "#interruptible-cr-considerations")
- [Interruptible Capacity Reservations for capacity owners](capacity-owner-procedures.md "capacity-owner-procedures.md")
- [Interruptible Capacity Reservations for capacity consumers](capacity-consumer-procedures.md "capacity-consumer-procedures.md")
- [Monitor interruptible Capacity Reservations with EventBridge and CloudTrail](monitor-interruptible-cr.md "monitor-interruptible-cr.md")

## How it works

To make unused capacity available to other teams, create an interruptible reservation by specifying the number of unused instances you want to share from your source reservation. When you create the interruptible reservation, we transfer these instances from your source reservation to the new interruptible reservation within your account.

We retain the association between the source reservation and the interruptible Capacity Reservation. As a result, when you reclaim your capacity, any running consumer instances are terminated, and the capacity is restored to your original source reservation.

Key features:

- Make unused capacity temporarily available while maintaining control to reclaim it
- Reclaim capacity at any time. For more information, see [Reclamation process and tracking](capacity-owner-procedures.md#reclamation-process "capacity-owner-procedures.md#reclamation-process")
- Share with additional accounts or your AWS organization using AWS Resource Access Manager (RAM)

## Billing

When you create an interruptible reservation, you're billed for it as an independent new reservation. This splits your billing:

- Source reservation: You're billed for total capacity minus allocated capacity
- Interruptible reservation: You're billed for the allocated capacity

For more information about On-Demand Capacity Reservation billing, see [Capacity Reservation pricing and billing](capacity-reservations-pricing-billing.md "capacity-reservations-pricing-billing.md").

## Considerations

Before using interruptible Capacity Reservations, review the following limitations and requirements that apply to capacity owners and consumers.

### Capacity owners

- You cannot directly modify or cancel an interruptible Capacity Reservation. To edit it, update the capacity allocated from the source Capacity Reservation.
- You can only view, launch, tag, share, and assign billing for interruptible reservations.
- You can create only one interruptible allocation per source Capacity Reservation.

### Capacity consumers

- Interruptible Capacity Reservations are by default targeted Capacity Reservations, so you need to target them in your instance launch.
- You can't add interruptible Capacity Reservations to capacity reservation groups.
- We recommend that you only use interruptible Capacity Reservations for applications that can be interrupted.
- Your instances will be terminated when the owner reclaims capacity - there is no fallback to On-Demand or Spot. For more information, see [Interruption experience](capacity-consumer-procedures.md#interruption-experience "capacity-consumer-procedures.md#interruption-experience").
