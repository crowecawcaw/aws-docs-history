

# Capacity Reservation pricing and billing
<a name="capacity-reservations.pricing-billing"></a>

The following topics give an overview of pricing and billing for Capacity Reservations.

**Topics**
+ [Pricing](#capacity-reservations.pricing-billing.pricing)
+ [Billing](#capacity-reservations.pricing-billing.billing)
+ [Billing discounts](#capacity-reservations.pricing-billing.discounts)
+ [Viewing your bill](#capacity-reservations.pricing-billing.viewing-bill)

## Pricing
<a name="capacity-reservations.pricing-billing.pricing"></a>

Capacity Reservations are charged at the equivalent On-Demand rate whether you run instances in reserved capacity or not. When you run a matching DB instance that matches the attributes of a reservation, you just pay for the DB instance and the capacity that it uses has no separate charge. Reserved capacity that has no DB instance usage appears as unused reservation on your bill. There are no upfront charges.

For example, you create a Capacity Reservation for 20 db.r7g.large DB instances in one Availability Zone, and you run 15 matching DB instances in that Availability Zone. You will be charged for the 15 DB instances and for 5 units of unused reserved capacity.

A Capacity Reservation reserves only compute capacity. Storage, I/O, backup storage, and other resources of your DB instances are billed as usual.

For more information, see [Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/).

## Billing
<a name="capacity-reservations.pricing-billing.billing"></a>

Billing for a Capacity Reservation starts as soon as the Capacity Reservation is provisioned in your account, and it continues while the Capacity Reservation remains provisioned in your account. For future-dated Capacity Reservations, this means that billing starts only after the Capacity Reservation is provisioned in your account at the requested future date.

Capacity Reservations are billed at per-second granularity, with a minimum of 60 seconds. This means that you are charged for partial hours. For example, if a Capacity Reservation remains provisioned in your account for 24 hours and 15 minutes, you are billed for 24.25 reservation hours.

The following example shows how a Capacity Reservation is billed. The Capacity Reservation is created for one db.r7g.large Aurora PostgreSQL DB instance in the US East (Ohio) Region. For this example, assume that the On-Demand rate of the db.r7g.large DB instance class is USD $0.276 per usage hour. In this example, the Capacity Reservation is provisioned in the account for five hours. The Capacity Reservation is unused for the first hour, so it is billed for one unused hour at the standard On-Demand rate of the db.r7g.large DB instance class. In hours two through five, the Capacity Reservation is occupied by a db.r7g.large Aurora PostgreSQL DB instance. During this time, the Capacity Reservation accrues no charges, and the account is instead billed for the db.r7g.large DB instance that occupies it. In the sixth hour, the Capacity Reservation is canceled and the db.r7g.large DB instance runs normally outside of the reserved capacity. For that hour, it is charged at the On-Demand rate of the db.r7g.large DB instance class.


| Hour | Capacity Reservation | DB instance | Charge in this example | 
| --- | --- | --- | --- | 
| 1 | Active, unused | None | USD $0.276 for one hour of unused reserved capacity | 
| 2–5 | Active, used by one db.r7g.large DB instance | Runs in the reserved capacity | USD $0.276 per hour for the DB instance. No charge for the Capacity Reservation. | 
| 6 | Canceled | Runs outside the reserved capacity | USD $0.276 for the On-Demand DB instance | 

In this example, the total charge for the six hours would be 6 × USD $0.276 = USD $1.656. The Capacity Reservation adds no charge for the hours that a DB instance uses it.

The following also applies to billing:
+ Billing stops when you cancel the Capacity Reservation, or when it reaches its end date.
+ When you increase the reserved capacity or set a later end date, the additional charges apply immediately. When you decrease the reserved capacity or set an earlier end date, you don't get a refund for time that has already passed.
+ Stopping a DB cluster doesn't change the cost of the reservations that its DB instances use. The capacity that the stopped DB instances used appears as unused reservation.

## Billing discounts
<a name="capacity-reservations.pricing-billing.discounts"></a>

A Capacity Reservation doesn't give a billing discount. To get a discount, use Capacity Reservations together with reserved DB instances or Database Savings Plans. AWS applies these discounts automatically to matching usage. When a DB instance uses the reserved capacity, the discount applies to the DB instance.

For more information, see [ Reserved DB instances for Amazon Aurora](USER_WorkingWithReservedDBInstances.md) and [Database Savings Plans](https://aws.amazon.com/savingsplans/database-pricing/).

## Viewing your bill
<a name="capacity-reservations.pricing-billing.viewing-bill"></a>

You can review the charges for your Capacity Reservations on the AWS Billing and Cost Management console. On the **Bills** page, under **Details**, expand the **Relational Database Service** section and the Region.