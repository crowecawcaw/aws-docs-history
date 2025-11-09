# Compute Savings Plans and Reserved Instances

Compute Savings Plans are a flexible pricing model that offers low prices, just like
Amazon EC2 Reserved Instances (RI), but with added flexibility. With Savings Plans, you can reduce your bill
by committing to a consistent amount of compute usage (measured in $/hour), instead of specific
instance configurations. Savings Plans give you the flexibility to use the compute option that best suits
your needs at low prices, without having to perform exchanges or modifications.

Compute Savings Plans provide savings up to 66 percent off On-Demand, similar to
Convertible RIs. Compute Savings Plans automatically reduce your cost on EC2 instance usage, Fargate,
and Lambda. EC2 Instance Savings Plans offer savings up to 72 percent off of On-Demand, similar to
Standard RIs. They also automatically save you money on any instance usage within a given EC2
instance family in your Region of choice. For more information, see [Savings Plans types](plan-types.md "plan-types.md").

| Comparing Savings Plans and RIs                                  |                  | Compute Savings Plans | EC2 Instance Savings Plans | Convertible RIs\* | Standard RIs |
| ---------------------------------------------------------------- | ---------------- | --------------------- | -------------------------- | ----------------- | ------------ |
| Savings over On-Demand                                           | Up to 66 percent | Up to 72 percent      | Up to 66 percent           | Up to 72 percent  |
| Lower price in exchange for monetary commitment                  | ✓                | ✓                     | —                          | —                 |
| Automatically applies pricing to any instance family             | ✓                | —                     | —                          | —                 |
| Automatically applies pricing to any instance size               | ✓                | ✓                     | —\*\*                      | —\*\*             |
| Automatically applies pricing to any Tenancy or OS               | ✓                | ✓                     | —                          | —                 |
| Automatically applies to Amazon ECS and Amazon EKS using Fargate | ✓                | —                     | —                          | —                 |
| Automatically applies to Lambda                                  | ✓                | —                     | —                          | —                 |
| Automatically applies pricing across AWS Regions                 | ✓                | —                     | —                          | —                 |
| Term length options of 1 or 3 years                              | ✓                | ✓                     | ✓                          | ✓                 |

**\*** Convertible RIs can be changed across instance family,
instance size, OS, and tenancy, but requires you to manually perform exchanges.

**\*\*** Regional convertible RIs and Regional standard RIs
provide instance size flexibility.

###### Note

Savings Plans doesn't provide capacity reservations, but you can allocate On-Demand Capacity
Reservation (ODCR) for your needs and your Savings Plans will apply.

Savings Plans prices for instances running SUSE Linux Enterprise Server (SLES) are different
compared to the corresponding RI price.

Savings Plans prices do not change based on the amount of hourly commitment.

Savings Plans doesn't apply to spot usage or usage covered by RIs.

Savings Plans offer lower prices compared to On-Demand pricing in exchange for a commitment, and
can't be cancelled during the term.
