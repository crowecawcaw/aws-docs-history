# Amazon GameLift Servers pricing and cost planning

Understanding the Amazon GameLift Servers pricing structure and implementing cost-effective strategies
in your game hosting solution is essential for optimizing your gaming infrastructure budget.
For detailed service information, including example pricing scenarios and pricing tools, see
[Amazon GameLift Servers Pricing](https://aws.amazon.com/gamelift/pricing/ "https://aws.amazon.com/gamelift/pricing/").

New AWS customers can use Amazon GameLift Servers without incurring charges under the Free Tier for up to
12 months. Stay within Free Tier usage limits to avoid charges.

## Pricing models

Amazon GameLift Servers offers several pricing models designed to accommodate different usage scenarios
and business needs. Each model has a different cost basis. You can control costs by
adjusting the cost factors in each model.

**Managed hosting**

Managed EC2 and managed container fleets use Amazon EC2 instances that Amazon GameLift Servers
manage. When you set up game hosting, you choose the type of Amazon EC2 instance to
use.

- **Compute costs** – Pay for hourly EC2
  instance usage for hosting game sessions. Cost factors for instances
  include:
  - AWS Region
  - Instance family, type, and size
  - Use of Spot versus On-Demand instances
  - Operating system (managed container fleets run on Linux only)

- **Data transfer** – Pay for traffic between game clients and hosted game servers

**Anywhere hosting**

Anywhere hosting runs on game hosting resources that you supply and manage, so there
are no compute costs. Instead costs are based on:

- **Game sessions** – Pay based on the number of game sessions placed on Anywhere computes
- **Connection minutes** – Pay for server process connection minutes

Use the **Pricing calculator for Amazon GameLift Servers** to estimate
costs for different Amazon GameLift Servers configurations. Use the calculator when designing your game
hosting solution or to forecast costs for configuration changes. See [Generate Amazon GameLift Servers pricing estimates](gamelift-calculator.md "gamelift-calculator.md").
