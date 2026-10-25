

# Getting started with On-Demand Capacity Reservations
<a name="capacity-reservations.getting-started"></a>

An Amazon RDS Capacity Reservation holds compute capacity for a specific combination of DB instance class, database engine, and Availability Zones, and reports a state that reflects where it is in its lifecycle. Before you create a reservation, review what it holds, how it's identified, when to use one, and the states it can report.

A reservation holds compute capacity for a specific combination of:
+ **DB instance class** (for example, db.r7g.large)
+ **Database engine** (for example, RDS for PostgreSQL or RDS for MySQL)
+ **One or more Availability Zones** in a single AWS Region
+ **Reserved capacity per Availability Zone** – the number of DB instances to reserve in each zone
+ **License model**, for engines that offer more than one – for example, `license-included` or `bring-your-own-license`. Engines with a single license option don't use it.

A reservation holds the same capacity in every Availability Zone you specify. To reserve capacity for Multi-AZ DB instances, specify two or more Availability Zones.

To use reserved capacity, you explicitly reference the reservation by either the name you gave it or the ID that Amazon RDS assigns to it when you create, restore, or modify a DB instance (see [Using a Capacity Reservation with a DB instance](capacity-reservations.using.md)). Amazon RDS Capacity Reservations are targeted – a DB instance draws from a reservation only when you specify that reservation's identifier or name. Creating a reservation on its own does not change how other DB instances in your account are placed.

A Capacity Reservation is identified by an ID with the prefix `dbcr-` (for example, `dbcr-abc123example`) and by a name that you assign when you create it.

Use a Capacity Reservation in the following cases:
+ Reserving capacity for a planned migration into Amazon RDS.
+ Reserving capacity ahead of a launch or a seasonal peak (for example, a fourth-quarter sales event).
+ Reserving capacity for a specific future date so it's in place before you need it.

**Topics**
+ [Differences between Capacity Reservations, reserved DB instances, and Savings Plans](#capacity-reservations.comparison)
+ [Quotas for Capacity Reservations](#capacity-reservations.quotas)
+ [Considerations and limitations](#capacity-reservations.limitations)
+ [Capacity Reservation states](#capacity-reservations.states)

## Differences between Capacity Reservations, reserved DB instances, and Savings Plans
<a name="capacity-reservations.comparison"></a>

The following table shows the key differences between Capacity Reservations, reserved DB instances, and Database Savings Plans.


| Feature | Capacity Reservations | Reserved DB instances | Database Savings Plans | 
| --- | --- | --- | --- | 
| Term | No commitment required for immediate-use Capacity Reservations. You can create, modify, and cancel them as needed.<br />With future-dated Capacity Reservations, you specify a commitment duration for which you commit to keeping the capacity in your account. | Requires a fixed one-year or three-year commitment. | Requires a fixed one-year commitment. | 
| Capacity benefit | Capacity reserved in a specific Availability Zone. | No capacity reserved. | No capacity reserved. | 
| Billing discount | No billing discount. You can combine Capacity Reservations with Database Savings Plans or Reserved DB instances to receive a discount. | Provides a billing discount. | Provides a billing discount. | 
| Instance limits | Your On-Demand DB instance quota for each Region applies. | Asia Pacific (Mumbai) (ap-south-1): 20. Each of the other supported Regions: 40. | No limit. | 

For more information, see [Reserved DB instances for Amazon RDS ](USER_WorkingWithReservedDBInstances.md) and [Database Savings Plans](https://aws.amazon.com/savingsplans/database-pricing/).

## Quotas for Capacity Reservations
<a name="capacity-reservations.quotas"></a>

The number of DB instances that you can reserve capacity for is based on your account's On-Demand DB instance quota. The quota covers your existing DB instances plus any unused reserved capacity. The capacity you can newly reserve is your quota, minus the DB instances you already have, minus the unused capacity in your other reservations. Reserved capacity is counted as the capacity per Availability Zone multiplied by the number of Availability Zones, so reserving 3 DB instances across 3 Availability Zones uses 9 of your quota.

## Considerations and limitations
<a name="capacity-reservations.limitations"></a>
+ Capacity Reservations are scoped to a single AWS Region, and within that Region to the specific Availability Zones you specify. Reserved capacity can be used only in those Availability Zones – a DB instance in any other zone can't draw on the reservation, even in the same Region. Create separate reservations in each Region and Availability Zone where you need reserved capacity.
+ A reservation covers one DB instance class and one engine, plus one license model for engines that offer more than one, across one or more Availability Zones. To reserve different combinations, create multiple reservations.
+ A reservation reserves the same capacity in each Availability Zone you specify, up to the number of Availability Zones in the Region. To place Multi-AZ DB instances, reserve capacity in at least two Availability Zones so that both the primary and the standby can be placed.
+ Reserved capacity applies to matching DB instances in the same account.
+ Capacity Reservations don't support Amazon RDS Custom DB instances (the `custom-oracle-*` and `custom-sqlserver-*` engines).
+ Future-dated reservations:
  + Can be scheduled between 5 and 120 days ahead of the current date.
  + Require a minimum commitment duration of 14 days. For the X family, the minimum commitment duration is 12 weeks.
  + Support only DB instance classes in the C, M, R, T, and X families.
  + Require M and R DB instance classes of generation 7 or later. For example, you can use db.m7g and db.r7g, but not db.m6g or db.r6i.
  + Require at least 32 vCPUs in each Availability Zone of the reservation. For example, a db.r7g.large reservation (2 vCPUs for each unit) must reserve at least 16 units of DB capacity in each Availability Zone.
+ Capacity Reservations don't reserve storage, I/O, or any resource other than compute capacity for the specified DB instance class.

## Capacity Reservation states
<a name="capacity-reservations.states"></a>

A Capacity Reservation reports a state that reflects where it is in its lifecycle.


| State | Description | 
| --- | --- | 
| `pending` | Amazon RDS is provisioning the reserved capacity. | 
| `active` | Capacity is reserved and available for your DB instances. Billing is in effect. | 
| `expired` | The reservation reached its end date and capacity has been released. | 
| `cancelled` | You canceled the reservation and capacity has been released. | 
| `failed` | The reservation couldn't be provisioned. | 

For future-dated reservations, the following additional states apply while the reservation is scheduled ahead of its start date.


| State | Description | 
| --- | --- | 
| `assessing` | Amazon RDS is evaluating whether the requested future capacity can be delivered. | 
| `scheduled` | The request was accepted. Amazon RDS delivers the capacity on the start date. No charges apply yet. | 
| `delayed` | Amazon RDS couldn't deliver capacity on the requested start date and is still working to fulfill it. Amazon RDS doesn't provide a revised delivery date. The reservation reports `CommitmentEndDate` equal to `StartDate`.<br />The commitment is partly waived. You can cancel the reservation immediately, while it is in the `delayed` state, and you can set an end date earlier than the original commitment end date. But until the original commitment end date, you can't reduce the capacity below the committed capacity. | 
| `unsupported` | The requested configuration can't be scheduled for the future date. | 

A future-dated reservation moves from `assessing` to `scheduled`, and then to `active` on the start date.