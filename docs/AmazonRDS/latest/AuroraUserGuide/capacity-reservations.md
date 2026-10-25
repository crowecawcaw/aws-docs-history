

# Amazon Aurora On-Demand Capacity Reservations
<a name="capacity-reservations"></a>

On-Demand Capacity Reservations for Amazon Aurora let you reserve compute capacity for your Aurora DB instances in one or more Availability Zones in an AWS Region. By creating a Capacity Reservation, you help make sure that you have access to Aurora compute capacity when you need it, for as long as you need it. Then DB instance create and compute scaling operations don't fail because of insufficient capacity.

You can reserve capacity for immediate use, or schedule a reservation to begin on a future date so that capacity is reserved ahead of a planned event such as a migration, a product launch, or a seasonal peak.

Immediately active reservations require no commitment, and you can cancel them at any time. Future-dated reservations require a minimum commitment duration.

A Capacity Reservation applies to individual DB instances, not to a DB cluster. You specify the reservation for each DB instance that you want to place in reserved capacity.

**Topics**
+ [Getting started with On-Demand Capacity Reservations](capacity-reservations.getting-started.md)
+ [Capacity Reservation pricing and billing](capacity-reservations.pricing-billing.md)
+ [Creating a Capacity Reservation](capacity-reservations.creating.md)
+ [Viewing and modifying your Capacity Reservations](capacity-reservations.viewing-modifying.md)
+ [Canceling a Capacity Reservation](capacity-reservations.canceling.md)
+ [Using a Capacity Reservation with an Aurora DB instance](capacity-reservations.using.md)
+ [Stopping and starting a DB cluster in a reservation](capacity-reservations.stopstart.md)