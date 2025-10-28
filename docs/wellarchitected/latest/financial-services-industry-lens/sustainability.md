# Sustainability

The sustainability pillar provides you with the discipline to address the
long-term environmental, economic, and societal impact of your
business activities. You can find extensive prescriptive guidance on
your implementation's sustainability in the
[Well-Architected Sustainability Pillar whitepaper](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md").

Financial institutions must focus on sustainability within their
cloud operating model to reduce their impact on the environment and
to encourage sustainable practices. Focusing on these areas helps financial institutions adapt their workloads to financial
services industry sustainability best practices, to adopt new
environmentally friendly technology trends, and to plan for the
business impacts of potential future regulatory requirements.

## Sustainability topics

The sustainability pillar includes the following topics on AWS cloud-based
architectures. Keep these topics in mind when developing your workload and also
when assessing the sustainability performance of your workloads.

- **Cloud sustainability:** Compare cloud capabilities against
  on-premises or hosted sustainability performance.
- **Shared responsibility model:** You _and_
  AWS are responsible for your cloud sustainability performance. AWS is responsible for
  providing the most sustainable infrastructure possible while you are responsible for
  judiciously developing workloads that take advantage of the most sustainable options
  provided by AWS.
  - **Sustainability of the cloud**: AWS' responsibility
    to you
  - **Sustainability in the cloud**: Your responsibility

- **Design principles for sustainability in the cloud:** This
  lens pillar and the sustainability whitepaper offer an extensive set of design principles
  and best practices for achieving the best possible outcomes.
- **Improvement processes:** After performing a
  Well-Architected Framework review, a number of improvement recommendations are provided by
  the AWS Well-Architected Tool. You can use this process to implement sustainability improvements to your
  workloads.
- **Best practices for sustainability:** The sustainability pillar and this lens pillar provide recommendations for sustainable practices across six
  areas of your critical workload infrastructure.

## Design principles

The following section defines a set of design principles for
financial services sustainability best practices. Typically, some
areas of financial services workload performance must be very low
latency (for example, trading and investing where microseconds can
cost $1MMs) while other areas have no concerns about speed. In
many areas of financial services, data retention for at least
seven years is critical. However, maintaining low latency storage
strategies for six-year-old insurance data is very wasteful.

- **Implement low-latency workloads only
  for time-critical performance.** Trading generally
  requires high-performance compute, networks, and storage,
  while banking and insurance typically do not.
- **Use tiered storage for data requiring long-term archive
  storage.** Financial records typically must be stored for at least seven years.
  Amazon S3 storage classes can better align resource usage to retrieval needs. Amazon S3 Standard is not recommended for long-term storage without any requirement for timely data retrieval. Amazon Glacier storage classes offer long-term, secure, durable storage classes for data archiving.
- **Region selection is a complex factor for implementing financial
  workloads.** While selection of low-carbon Regions is generally recommended for
  processing of financial data, sometimes data residency requirements stipulate the use of
  higher carbon storage. Also, some financial data's low latency requirements drive the
  choice of Regions with a higher carbon footprint due to greater network latency
  requirements. The selection of the best Region might be driven by taking into account a
  variety of reasons.
- **Back up data only when it's difficult
  to recreate.** Too often data is backed up in
  multiple locations and in the wrong tiers of storage. Use
  smart backup and storage disciplines to reduce your workload's
  overall carbon footprint.

## Definitions

- [Region
  selection](../sustainability-pillar/region-selection.md "../sustainability-pillar/region-selection.md")
- [Alignment
  to demand](../sustainability-pillar/alignment-to-demand.md "../sustainability-pillar/alignment-to-demand.md")
- [Software
  and architecture](../sustainability-pillar/software-and-architecture.md "../sustainability-pillar/software-and-architecture.md")
- [Data](../sustainability-pillar/data.md "../sustainability-pillar/data.md")
- [Hardware
  and services](../sustainability-pillar/hardware-and-services.md "../sustainability-pillar/hardware-and-services.md")
- [Process
  and culture](../sustainability-pillar/process-and-culture.md "../sustainability-pillar/process-and-culture.md")
