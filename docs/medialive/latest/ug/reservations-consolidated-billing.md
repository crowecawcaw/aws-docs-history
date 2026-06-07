# Reservations and AWS Organizations

MediaLive reservations work with AWS Organizations consolidated billing. If
you purchase a reservation in the management (payer) account, the reservation
applies to MediaLive usage across all member accounts in the organization. AWS
applies the reservation to unreserved usage in the management account first, then
to remaining unreserved usage in member accounts.

If you purchase a reservation in a member account, the reservation applies
only to MediaLive usage in that member account.

For more information about how reservations work with consolidated billing, see
[Reserved Instances](../../../awsaccountbilling/latest/aboutv2/ri-behavior.md "../../../awsaccountbilling/latest/aboutv2/ri-behavior.md")
in the _AWS Billing User Guide_.
