

# Account scope and billing views

The account you create the dataset in decides which accounts it covers. A dataset created in the management account covers every account in the organization, including accounts that join later. A dataset created in a member account covers that account alone. Public preview has no billing view selector.

A dataset uses the primary billing view of the account that creates the dataset. If that account is in an AWS Billing Conductor billing group, or uses billing transfer to send its bills to another account, the primary billing view shows pro forma costs. The dataset then holds the same pro forma costs, at the rates that the account managing your billing sets.