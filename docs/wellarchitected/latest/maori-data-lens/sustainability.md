# Sustainability

The Sustainability Pillar provides design principles, operational guidance, best-practices,
potential trade-offs, and improvement plans you can use to meet sustainability targets for your
AWS workloads. If relevant, you can find prescriptive guidance on implementation in the [Sustainability
Pillar whitepaper](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md").

Apply these design principles when architecting your cloud workloads to maximise
sustainability and minimise impact.

###### Design principles

- **Understand your impact:** Measure the impact of your cloud
  workload and model the future impact of your workload. Include all sources of impact,
  including impacts resulting from customer use of your products, and impacts resulting from
  their eventual decommissioning and retirement. Compare the productive output with the total
  impact of your cloud workloads by reviewing the resources and emissions required per unit of
  work. Use this data to establish key performance indicators (KPIs), evaluate ways to improve
  productivity while reducing impact, and estimate the impact of proposed changes over time.
- **Establish sustainability goals:** For each cloud workload,
  establish long-term sustainability goals such as reducing the compute and storage resources
  required per transaction. Model the return on investment of sustainability improvements for
  existing workloads, and give owners the resources they need to invest in sustainability
  goals. Plan for growth, and architect your workloads so that growth results in reduced
  impact intensity measured against an appropriate unit, such as per user or per transaction.
  Goals help you support the wider sustainability goals of your business or organisation,
  identify regressions, and prioritise areas of potential improvement.
- **Maximise utilisation:** Right-size workloads and implement
  efficient design to ensure high utilisation and maximise the energy efficiency of the
  underlying hardware. Two hosts running at 30% utilisation are less efficient than one host
  running at 60% due to baseline power consumption per host. At the same time, eliminate or
  minimise idle resources, processing, and storage to reduce the total energy required to
  power your workload.
- **Anticipate and adopt new, more efficient hardware and software
  offerings:** Support the upstream improvements your partners and suppliers make
  to help you reduce the impact of your cloud workloads. Continually monitor and evaluate new,
  more efficient hardware and software offerings. Design for flexibility to allow for the
  rapid adoption of new efficient technologies.
- **Use managed services:** Sharing services across a broad
  customer base helps maximise resource utilisation, which reduces the amount of
  infrastructure needed to support cloud workloads. For example, customers can share the
  impact of common data centre components like power and networking by migrating workloads to
  the AWS Cloud and adopting managed services, such as AWS Fargate for serverless
  containers, where AWS operates at scale and is responsible for their efficient operation.
  Use managed services that can help minimise your impact, such as automatically moving
  infrequently accessed data to cold storage with Amazon S3 Lifecycle configurations or Amazon EC2 Auto Scaling to
  adjust capacity to meet demand.
- **Reduce the downstream impact of your cloud workloads:**
  Reduce the amount of energy or resources required to use your services. Reduce or eliminate
  the need for customers to upgrade their devices to use your services. Test using device
  farms to understand expected impact and test with customers to understand the actual impact
  from using your services.
  Māori have deep connections to the land and the natural world. The land can act as a
  foundation for whakapapa, and as such can be an integral part of a person or community's
  identity. The natural world also provides resources, food, and shelter for Māori. This
  connection with the natural world means that it needs to be cherished and protected. Having a
  deeper understanding of this can inform your organisation's approach to reducing or minimising
  the impact of your technology decisions on the environment. Specifically, aim to incorporate the
  design principles, guidance, and best practices in the Sustainability Pillar into your
  organisation's approach to sustainability. The following specific questions and good practices
  could be considered along with the best practices in the Well-Architected Sustainability Pillar
  whitepaper.

###### Topics

- [MD_SUS 1 How do you design and operate systems to minimise potential impacts on the
  environment?](md_sus-1-how-do-you-design-and-operate-systems-to-minimise-potential-impacts-on-the-environment.md "md_sus-1-how-do-you-design-and-operate-systems-to-minimise-potential-impacts-on-the-environment.md")
- [Resources](md_sus-resources.md "md_sus-resources.md")
