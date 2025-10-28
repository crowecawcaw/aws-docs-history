# Create a Capacity Reservation

You can create a Capacity Reservation at any time to ensure that you have compute capacity available
in a specific Availability Zone. A Capacity Reservation can start immediately, or it can
start at a future date. The capacity becomes available for use only once the Capacity Reservation enters
the `active` state.

###### Note

If you create a Capacity Reservation with `open` instance matching criteria, and you
have running instances with matching attributes at the time the Capacity Reservation becomes active,
those instances automatically run in the reserved capacity. To avoid this, use
`targeted` instance matching criteria. For more information, see
[Instance matching criteria](cr-concepts.md#cr-instance-eligibility "cr-concepts.md#cr-instance-eligibility").

Your request to create a Capacity Reservation could fail if one of the following is true:

- Amazon EC2 does not have sufficient capacity to fulfill the request. Either try
  again at a later time, try a different Availability Zone, or try a smaller
  request. If your application is flexible across instance types and sizes, try
  different instance attributes.
- The requested quantity exceeds your On-Demand Instance limit for the selected instance
  family. Increase your On-Demand Instance limit for the instance family and try again. For
  more information, see [On-Demand Instance quotas](ec2-on-demand-instances.md#ec2-on-demand-instances-limits "ec2-on-demand-instances.md#ec2-on-demand-instances-limits").

###### Topics

- [Create a Capacity Reservation for immediate use](#create-immediate-cr "#create-immediate-cr")
- [Create a future-dated Capacity Reservation](#create-future-cr "#create-future-cr")

## Create a Capacity Reservation for immediate use

You create a Capacity Reservation for immediate use.

Console

###### To create a Capacity Reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations**, and then choose
   **Create Capacity Reservation**.
3. Configure the following settings in the **Instance
   details** section.
   1. **Instance Type** — The
      instance type for which to reserve capacity.
   2. **Platform** — The operating
      system for your instances. For more information, see
      [Supported platforms](ec2-capacity-reservations.md#capacity-reservations-platforms "ec2-capacity-reservations.md#capacity-reservations-platforms").
   3. **Availability Zone** — The
      Availability Zone in which to reserve the
      capacity.
   4. **Tenancy** — The type of
      tenancy to use for the reserved capacity. Choose Default
      to reserve capacity on shared hardware, or Dedicated to
      reserve capacity on hardware that is dedicated to your
      account.
   5. (_Optional_) **Placement
      group ARN** — The ARN of the cluster
      placement group in which to create the Capacity Reservation. For more
      information, see [Use Capacity Reservations with cluster placement groups](cr-cpg.md "cr-cpg.md").
   6. **Total instance count** — The
      number of instances for which to reserve capacity. If
      you specify a quantity that exceeds your remaining On-Demand Instance
      quota for the selected instance type, the request
      fails.

4. Configure the following settings in the **Reservation
   details** section:
   1. **Capacity Reservation starts** — Choose
      **Immediately**.
   2. **Capacity Reservation ends** — Choose one of
      the following options:
      - **Manually** — Reserve
        the capacity until you explicitly cancel
        it.
      - **Specific time** —
        Cancel the capacity reservation automatically at
        the specified date and time.

   3. **Instance eligibility** —
      Choose one of the following options:
      - **open** — (Default)
        The Capacity Reservation matches any instance that has matching
        attributes (instance type, platform, Availability
        Zone, and tenancy). If you launch an instance with
        matching attributes, it is placed into the
        reserved capacity automatically.
      - **targeted** — The
        Capacity Reservation only accepts instances that have matching
        attributes (instance type, platform, Availability
        Zone, and tenancy), and that explicitly target the
        reservation.

5. Choose **Create**.

AWS CLI

###### To create a Capacity Reservation

Use the [create-capacity-reservation](../../../cli/latest/reference/ec2/create-capacity-reservation.md "../../../cli/latest/reference/ec2/create-capacity-reservation.md") command.

```
aws ec2 create-capacity-reservation \
    --availability-zone `az_name` \
    --instance-type `instance_type` \
    --instance-count `number_of_instances` \
    --instance-platform `operating_system` \
    --instance-match-criteria `open`|`targeted`
```

PowerShell

###### To create a Capacity Reservation

Use the [Add-EC2CapacityReservation](../../../powershell/latest/reference/items/Add-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Add-EC2CapacityReservation.md") cmdlet.

```
Add-EC2CapacityReservation `
    -AvailabilityZone `az_name` `
    -InstanceType `instance_type` `
    -InstanceCount `number_of_instances` `
    -InstancePlatform `operating_system` `
    -InstanceMatchCriterion `open`|`targeted`
```

## Create a future-dated Capacity Reservation

Request a future-dated Capacity Reservation if you need the reserved capacity to become available
at a future date and time.

After you request a future-dated Capacity Reservation, the request undergoes an assessment to
determine whether it can be supported. For more information, see [Future-dated Capacity Reservation assessment](cr-concepts.md#cr-future-dated-assessment "cr-concepts.md#cr-future-dated-assessment").

###### Considerations

- You can request future-dated Capacity Reservations for instance types in the following series:
  C, G, I, M, R, and T.
- You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For
  example, if you request a future-dated Capacity Reservation for `m5.xlarge`
  instances, you must request capacity for at least 8 instances (_8 \*
  m5.xlarge = 32 vCPUs_).
- You can request a future-dated Capacity Reservation between 5 and 120 days in advance.
  However, we recommend that you request it at least 56 days (8 weeks) in
  advance to improve supportability.
- The minimum commitment duration is 14 days.

Console

###### To create a Capacity Reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations**, and then choose
   **Create Capacity Reservation**.
3. Configure the following settings in the **Instance
   details** section.
   1. **Instance Type** — The
      instance type for which to reserve capacity.
   2. **Platform** — The operating
      system for your instances. For more information, see
      [Supported platforms](ec2-capacity-reservations.md#capacity-reservations-platforms "ec2-capacity-reservations.md#capacity-reservations-platforms").
   3. **Availability Zone** — The
      Availability Zone in which to reserve the
      capacity.
   4. **Tenancy** — The type of
      tenancy to use for the reserved capacity. Choose Default
      to reserve capacity on shared hardware, or Dedicated to
      reserve capacity on hardware that is dedicated to your
      account.
   5. **Total instance count** — The
      number of instances for which to reserve capacity. If
      you specify a quantity that exceeds your remaining On-Demand Instance
      quota for the selected instance type, the request
      fails.

4. Configure the following settings in the **Reservation
   details** section:
   1. **Capacity Reservation starts** — Choose
      **At a specific time**.
   2. **Start date** — Specify the
      date and time at which the Capacity Reservation must become available for
      use. For more information, see [Start date and time](cr-concepts.md#cr-start-date "cr-concepts.md#cr-start-date").
   3. **Commitment duration** —
      Specify the minimum duration for which you commit
      keeping the Capacity Reservation after it has been delivered. For more
      information, see [Commitment duration](cr-concepts.md#cr-commitment-duration "cr-concepts.md#cr-commitment-duration").
   4. **Capacity Reservation ends** — Choose one of
      the following options:
      - **When I cancel it** —
        Reserve the capacity until you explicitly cancel
        it.
      - **Specific time** —
        Cancel the capacity reservation automatically at
        the specified date and time.

5. Choose **Create**.

AWS CLI

###### To create a Capacity Reservation

Use the [create-capacity-reservation](../../../cli/latest/reference/ec2/create-capacity-reservation.md "../../../cli/latest/reference/ec2/create-capacity-reservation.md") command.

```
aws ec2 create-capacity-reservation \
    --availability-zone `az_name` \
    --instance-type `instance_type` \
    --instance-count `number_of_instances` \
    --instance-platform `operating_system` \
    --instance-match-criteria targeted \
    --delivery-preference incremental \
    --commitment-duration `commitment_in_seconds` \
    --start-date `YYYY-MMDDThh:mm:ss.sssZ`
```

PowerShell

###### To create a Capacity Reservation

Use the [Add-EC2CapacityReservation](../../../powershell/latest/reference/items/Add-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Add-EC2CapacityReservation.md") cmdlet.

```
Add-EC2CapacityReservation `
    -AvailabilityZone `az_name` `
    -InstanceType `instance_type` `
    -InstanceCount `number_of_instances` `
    -InstancePlatform `operating_system` `
    -InstanceMatchCriterion targeted `
    -DeliveryPreference incremental `
    -CommitmentDuration `commitment_in_seconds` `
    -StartDate  `YYYY-MMDDThh:mm:ss.sssZ`
```
