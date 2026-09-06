# Understanding Amazon Quick user billing

Your charges for a Quick user follow the user's lifecycle in your account,
from the moment you provision the user through the period after you remove the user. The
following sections explain when billing begins, how your first billing period is
prorated, how ongoing monthly charges apply, and how removing a user affects your
charges.

###### Topics

- [When billing begins](#billing-when-provisioned "#billing-when-provisioned")
- [Your first billing period](#billing-first-period "#billing-first-period")
- [Ongoing monthly billing](#billing-ongoing "#billing-ongoing")
- [Billing when you remove a user](#billing-user-removal "#billing-user-removal")
- [Billing examples](#billing-examples "#billing-examples")

## When billing begins

Billing for a Quick user begins when you provision the user in your
account, not when the user first signs in. This is independent of user activity. If
you provision a user who never signs in during a billing period, you are still
billed for that user for that period.

The exact moment billing begins depends on how you provision the user:

- For users you provision through the API, such as by registering a user or
  creating an account subscription, billing begins when the API call creates
  the user, whether or not the user has signed in.
- For users who self-provision, billing begins the first time the user opens
  Amazon Quick.
- For users you map from a group in IAM Identity Center or Active
  Directory, billing begins when Amazon Quick detects the user
  through group synchronization.

## Your first billing period

When you provision a user partway through a billing period, your charge for that
first period is prorated. The proration is based on the portion of the period that
remains after the provisioning date. In the next full billing period, you pay the
standard rate for the user's role.

## Ongoing monthly billing

For each billing period a user remains in your account, you pay the monthly rate
for that user's role. These subscription charges are separate from usage-based
charges such as SPICE capacity or reader session usage. For a full
comparison of the capabilities included with each subscription and current per-user
pricing, see [Amazon Quick
pricing](https://aws.amazon.com/quick/pricing/ "https://aws.amazon.com/quick/pricing/").

## Billing when you remove a user

When you remove a user partway through a billing period, you still pay for the
full billing period in which the removal occurs. You are not charged for the user in
any later billing period. This differs from provisioning. Your first billing period
is prorated, but your final billing period is not.

To avoid charges for a user you no longer need, remove the user before the next
billing period begins.

## Billing examples

The following examples show how your charges apply across a user's lifecycle:

- For a user you provision partway through a billing period, your charge for
  that period covers the provisioning date through the end of the period, and
  the full rate applies in the next period.
- For a user you remove partway through a billing period, you pay for the
  full period, and no charge applies in the following period.
- For a user you provision and remove within the same billing period, you
  pay for that full period, and no charge applies afterward.
- For a user who never signs in, you pay each billing period the user
  remains in your account, the same as an active user, until you remove the
  user.

This billing behavior applies to all Amazon Quick user roles across editions and
in all AWS Regions where Amazon Quick is available.
