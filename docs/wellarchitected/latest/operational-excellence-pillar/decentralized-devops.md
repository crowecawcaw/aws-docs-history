# Decentralized DevOps

The decentralized DevOps model is a variation of the _you build it, you run it_ methodology where operations are primarily under the ownership of workload teams.

Your application engineers perform both the engineering and the operations of their workloads. Similarly, your infrastructure engineers perform both the engineering and operations of the platforms they use to support application teams.

![Decentralized DevOps diagram](images/decentralized-devops.en.png)
_Decentralized DevOps_

For this example, we treat governance as decentralized. Standards are still distributed, provided, or shared to application teams by the platform team, but application teams are free to engineer and operate new platform capabilities in support of their workload.

In this model, there are fewer constraints on the application team, but that comes with a significant increase in responsibilities. Additional skills (and potentially team members) must be present to support the additional platform capabilities. The risk of significant rework is increased if skill sets are inadequate and defects are not recognized early.

Enforce policies that are not specifically delegated to application teams. Use tools or services that help you to centrally govern your environments across accounts, such as [AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/"). Services like [AWS Control Tower](https://aws.amazon.com/controltower/features/ "https://aws.amazon.com/controltower/features/") expand this management capability by helping you define blueprints (supporting your operating models) for the setup of accounts, apply ongoing governance using AWS Organizations, and automate provisioning of new accounts.

It’s beneficial to have mechanisms for the application team to request additions and changes to standards. They can contribute new standards that can provide benefit to other application teams. The platform teams may decide that providing direct support for these additional capabilities is an effective support for business outcomes.

This model limits constraints on innovation with significant skill and team member requirements. It addresses many of the bottlenecks and delays created by transition of tasks between teams, while still promoting the development of effective relationships between teams and customers.
