# Concepts for Amazon EC2 Capacity Reservations

The following key concepts apply to Capacity Reservations.

###### Topics

- [Start date and time](#cr-start-date "#cr-start-date")
- [End date and time](#cr-end-date "#cr-end-date")
- [Commitment duration](#cr-commitment-duration "#cr-commitment-duration")
- [Future-dated Capacity Reservation assessment](#cr-future-dated-assessment "#cr-future-dated-assessment")
- [Capacity Reservation attributes](#cr-attributes "#cr-attributes")
- [Instance matching criteria](#cr-instance-eligibility "#cr-instance-eligibility")

## Start date and time

The start date and time defines when the Capacity Reservation becomes available for use. A Capacity Reservation
can start **immediately**, or it can start at a
**future date**.

- If you choose to start a Capacity Reservation immediately, the reserved capacity becomes
  available for use immediately after you create it, and billing starts as
  soon as the Capacity Reservation enters the active state. You do not need to enter into any
  term commitments. You can modify the Capacity Reservation as needed at any time to meet your
  needs, and you can cancel it at any time to release the capacity and to stop
  incurring charges.
- If you choose to start a Capacity Reservation at a future date, you specify a
  _future date and time_ at which you will need the
  reserved capacity, and a _commitment duration_, which is
  the minimum duration for which you commit to keeping the requested Capacity Reservation in
  your account after it has been provisioned. At the specified future date,
  the Capacity Reservation becomes available for use and billing starts at that time, once the
  Capacity Reservation enters the active state. The commit duration starts as soon as the Capacity Reservation
  is provisioned in your account. During this time, you can't decrease the
  instance count below the committed instance count, choose an end date that
  is before the commitment duration, or cancel the Capacity Reservation. However, after the
  commitment duration lapses, you are free to modify the Capacity Reservation in any way, or
  cancel it to release the reserved capacity and to stop incurring
  charges.

## End date and time

The end date and time defines when the Capacity Reservation ends and the reserved capacity is
released from your account. You can configure a Capacity Reservation to **end
automatically** at a specific date and time, or you can configure it to
stay active indefinitely until you **manually cancel
it**.

If you configure a Capacity Reservation to end automatically, the Capacity Reservation expires within an hour of the
specified time. For example, if you specify `5/31/2019, 13:30:55`, the
Capacity Reservation is guaranteed to end between `13:30:55` and `14:30:55` on
`5/31/2019`.

After a reservation ends, the reserved capacity is released from your account and
you can no longer target instances to the Capacity Reservation. Instances running in the reserved
capacity continue to run uninterrupted. If instances targeting a Capacity Reservation are stopped,
you can't restart them until you remove their Capacity Reservation targeting preference or configure
them to target a different Capacity Reservation. For more information, see [Modify the Capacity Reservation settings of your
instance](capacity-reservations-modify-instance.md "capacity-reservations-modify-instance.md").

## Commitment duration

The commitment duration applies to future-dated Capacity Reservations only.

The commitment duration is a minimum duration for which you commit to having the
future-dated Capacity Reservation in the active state in your account after it has been provisioned.
You can keep a future-dated Capacity Reservation for longer than the commitment duration, but not
shorter. The following apply during the commitment duration:

- You can't cancel a Capacity Reservation during the commitment duration.
- You can't decrease the instance count below the committed instance count,
  but you can increase it.
- You can't configure a Capacity Reservation to automatically end at a date or time that is
  within the commitment duration. You can extend the end date and time during
  the commitment period.

Amazon EC2 uses the commitment duration that you specify to assess whether the request
can be supported. The minimum commitment duration is 14 days. While assessing a
request, Amazon EC2 might determine that it can support a shorter commitment duration. In
that case, Amazon EC2 will schedule the future-dated Capacity Reservation with the shorter commitment
duration. This means that you are committed to keeping the Capacity Reservation in your account for
a shorter period than you initially requested.

## Future-dated Capacity Reservation assessment

When you request a future-dated Capacity Reservation, Amazon EC2 assesses the request to determine
whether it can be supported based on capacity availability and the commitment
duration you specify. The assessment is typically completed within 5 days. Amazon EC2
considers multiple factors when evaluating a request, including:

- Forecasted capacity supply
- The commitment duration
- How early you request the Capacity Reservation relative to your start date
- The size of your request

You can request a future-dated Capacity Reservation between 5 and 120 days in
advance. We recommend that you make the request at least 56 days (8 weeks) in
advance to improve our ability to support your request. The minimum commitment
duration is 14 days and the minimum instance count is 32 vCPUs.

The Capacity Reservation remains in the `assessing` state while the request is being
assessed.

If the request can be supported, the Capacity Reservation enters the `scheduled` state
and it is scheduled for delivery on the requested date and time. The total instance
count remains 0 during while the Capacity Reservation is in the `scheduled` state. A
scheduled Capacity Reservation will become `active` and available for use at the
requested date.

If a request can't be supported, the Capacity Reservation enters the `unsupported`
state. Unsupported Capacity Reservations are not delivered.

You can cancel a future-dated Capacity Reservation while it is in the `assessing`
state.

For more information, see [Create a future-dated Capacity Reservation](capacity-reservations-create.md#create-future-cr "capacity-reservations-create.md#create-future-cr").

## Capacity Reservation attributes

When you create a Capacity Reservation, you must specify the following attributes:

- Availability Zone
- Instance type
- Platform (operating system type)
- Tenancy (`default` or `dedicated`)

Only instances that match these attributes can launch or run in the Capacity Reservation.

## Instance matching criteria

Instance matching criteria, or instance eligibility, determines which instances
are allowed to launch and run in the Capacity Reservation. A Capacity Reservation can have one of the following
matching criteria:

- **Open** — The Capacity Reservation automatically
  matches all instances that have matching attributes (instance type,
  platform, and Availability Zone). New and existing instances that have
  matching attributes automatically run in the Capacity Reservation without any additional
  configuration.
- **Targeted** — The Capacity Reservation accepts only
  instances that have matching attributes (instance type, platform, and
  Availability Zone), and that explicitly target the Capacity Reservation. The instance must
  specifically target the Capacity Reservation to launch or run in its reserved capacity. This
  allows you to explicitly control which instances are allowed to run in the
  reserved capacity and helps you avoid unintentional reserved capacity
  usage.

When you request a future-dated Capacity Reservation, you can specify only targeted matching
criteria. This ensures that the capacity delivered by the Capacity Reservation is incremental, or
additional, to any running instances or reserved capacity that you have at the time
of delivery. After the Capacity Reservation becomes active in your account, you can change the
instance matching criteria to open if needed. However, keep in mind that any
matching instances will automatically run in the Capacity Reservation, which could lead to
unintentional capacity usage and prevent you from launching new instances for the
full requested instance count.
