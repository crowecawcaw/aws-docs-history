# Decision guide: Choose a hosting option

Amazon GameLift Servers offers several hosting options, each designed for different hosting scenarios
and requirements. This guide helps you choose the type of fleet based on your game's
technical needs, operational preferences, and business constraints. For high-level
descriptions, see [Amazon GameLift Servers game hosting options](gamelift-intro-flavors.md "gamelift-intro-flavors.md").

## Fleet comparison

The following table compares the key characteristics of each hosting option:

| Hosting option     | Best For                                           | Management Level | Key Benefits                                                    |
| ------------------ | -------------------------------------------------- | ---------------- | --------------------------------------------------------------- |
| Managed EC2        | Production hosting with full AWS management        | Fully managed    | Auto-scaling, global reach, minimal operational overhead        |
| Managed containers | Containerized applications requiring orchestration | Fully managed    | Container orchestration, resource efficiency, modern deployment |
| Anywhere           | On-premises, hybrid, or development environments   | Self-managed     | Hardware control, compliance requirements, cost optimization    |

## Key decision factors

Consider these factors when choosing your hosting option:

Operational complexity

How much infrastructure management do you want to handle? Managed fleets require minimal operational overhead, while Anywhere fleets give you full control but require more management.

Scalability requirements

Do you need automatic scaling based on player demand? Managed fleets provide built-in auto-scaling, while Anywhere fleets require manual capacity management.

Geographic distribution

Where are your players located? Managed fleets can be deployed across multiple AWS Regions globally, while Anywhere fleets depend on your own infrastructure locations.

Compliance and security

Do you have specific compliance requirements or need to keep data on-premises? Anywhere fleets allow you to maintain full control over your infrastructure and data location.

Cost considerations

What's your budget and cost optimization strategy? Consider both infrastructure costs and operational overhead when comparing options.

## Hybrid solutions

You don't have to choose just one type of fleet for your game hosting solution. Many
games use a hybrid approach that combines multiple fleet types to optimize for different
scenarios:

- **Development and testing**: Use Anywhere fleets for development and testing, then deploy to managed fleets for production.
- **Regional optimization**: Use managed fleets in AWS Regions with high player density and Anywhere fleets in regions where you have existing infrastructure.
- **Cost optimization**: Use managed fleets for baseline capacity and Anywhere fleets for overflow or specific workloads.
