# Operational excellence

The Operational Excellence Pillar provides guidance on running and monitoring systems to
deliver customer value and continually improving the supporting processes and procedures. The
pillar also provides an overview of design principles, best practices, and questions. You can
find prescriptive guidance on implementation in the [Operational Excellence
Pillar whitepaper](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md").

At AWS, operational excellence is defined as a commitment to build software correctly
while consistently delivering a great customer experience. It contains best practices for
organising your team, designing your workload, operating it at scale, and evolving it over time.
Operational excellence focuses your team more on building new features that benefit customers
and less on maintenance and firefighting. We look to best practices that result in well-running
systems, a balanced workload for you and your team, and most importantly, a great customer
experience.

The goal of operational excellence is to get new features and bug fixes into customers'
hands quickly and reliably. Organisations that invest in operational excellence consistently
delight customers while building new features, making changes, and dealing with failures. Along
the way, operational excellence drives towards continuous integration and continuous delivery
(CI/CD) by helping developers achieve high quality results consistently.

###### Design principles

- **Perform operations as code**: In the cloud, you can apply the
  same engineering discipline that you use for application code to your entire environment.
  You can define your entire workload (applications, infrastructure, etc.) as code and update
  it with code. You can script your operations procedures and automate their process by
  launching them in response to events. By performing operations as code, you limit human
  error and create consistent responses to events.
- **Make frequent, small, reversible changes**: Design workloads
  that are scalable and loosely coupled to permit components to be updated regularly.
  Automated deployment techniques together with smaller, incremental changes reduces the blast
  radius and allows for faster reversal when failures occur. This increases confidence to
  deliver beneficial changes to your workload while maintaining quality and adapting quickly
  to changes in market conditions.
- **Refine operations procedures frequently**: As you evolve your
  workloads, evolve your operations appropriately. As you use operations procedures, look for
  opportunities to improve them. Hold regular reviews and validate that all procedures are
  effective and that teams are familiar with them. Where gaps are identified, update
  procedures accordingly. Communicate procedural updates to all stakeholders and teams. Gamify
  your operations to share best practices and educate teams.
- **Anticipate failure**: Perform "pre-mortem" exercises to
  identify potential sources of failure so that they can be removed or mitigated. Test your
  failure scenarios and validate your understanding of their impact. Test your response
  procedures to ensure they are effective and that teams are familiar with their process. Set
  up regular game days to test workload and team responses to simulated events.
- **Learn from all operational failures**: Drive improvement
  through lessons learned from all operational events and failures. Share what is learned
  across teams and through the entire organisation.
- **Use managed services:** Reduce operational burden by using
  AWS managed services where possible. Build operational procedures around interactions with
  those services.
- **Implement observability for actionable insights:** Gain a
  comprehensive understanding of workload behavior, performance, reliability, cost, and
  health. Establish key performance indicators (KPIs) and leverage observability telemetry to
  make informed decisions and take prompt action when business outcomes are at risk.
  Proactively improve performance, reliability, and cost based on actionable observability
  data.
  While operational excellence design principles are focused on digital workloads, their
  wider objective is to help an organisation improve its operational capability. The following
  specific questions are intended to identify areas of improvements to an organisation's
  operational practices with respect to Māori data.

###### Topics

- [MD_OPS 1: How do you incorporate Māori views into your technology governance and
  operations?](md_ops-1-how-do-you-incorporate-m%C4%81ori-views-into-your-technology-governance-and-operations.md "md_ops-1-how-do-you-incorporate-m%C4%81ori-views-into-your-technology-governance-and-operations.md")
- [MD_OPS 2: How can you design data collection with your Māori customer(s) in mind?](md_ops-2-how-can-you-design-data-collection-with-your-m%C4%81ori-customers-in-mind.md "md_ops-2-how-can-you-design-data-collection-with-your-m%C4%81ori-customers-in-mind.md")
- [MD_OPS 3: How do you use or
  share Māori data back with Māori?](md_ops-3-how-do-you-use-or-share-m%C4%81ori-data.md "md_ops-3-how-do-you-use-or-share-m%C4%81ori-data.md")
- [Resources](md_ops-resources.md "md_ops-resources.md")
