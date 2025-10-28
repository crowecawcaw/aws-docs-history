# Scenarios

This section explores common data residency scenarios, framing out
best practices and implementation guidance within the context of the
Well-Architected pillars. These scenarios serve as foundational
experiences shaping the guidance offered in the lens. By exploring
each case, we provide actionable guidance tailored to the
complexities of data residency requirements.

###### Note

While the following
presented guidelines for data residency, you should consult
internally with legal and security teams for specific organizational
requirements.

Before exploring the scenarios detailed in this section, it is
essential to make an informed design choice to meet your specific
legal and compliance requirements using AWS building blocks.

While AWS provides a wide range of tools and resources to help
support your infrastructure, it is ultimately your responsibility to
comply with local laws and regulations. As described in the
[AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model "https://aws.amazon.com/compliance/shared-responsibility-model"), we encourage you to engage with
your legal and compliance teams to thoroughly assess your needs. To
support these discussions and help you make informed decisions that
account for potential trade-offs, consider the following key points:

**Application summary information**

- Provide a brief description of the application.
- List the countries and industries the application will serve.
- Describe the application's main functions and the key data types
  it handles. Detail the data classification conducted for
  individual fields in the datasets handled by the application
- Specify your Recovery Time Objective (RTO) and Recovery Point
  Objective (RPO).
- Outline any significant timelines for deployment or compliance.

**Data residency considerations**

- Identify the acceptable use policies (AUP) for the data managed
  by the application. If these policies are not yet established,
  consider creating them. This should involve:
  - Conducting data classification exercises.
  - Aligning the data with relevant data privacy laws and
    industry-specific regulations.
  - Thoroughly detailing the use-cases that need support, such as
    data and analytics model building, digital forensics, or law
    enforcement. Additionally, clarify the permissible locations for
    storing and processing this data, and explore the possibilities
    for encryption, masking, or tokenization to anonymize data.

- Once sensitive data is identified and the use-cases are clearly
  defined, determine how the application separates the storage and
  processing of sensitive data from non-sensitive data.

###### Note

Some regulators require
additional guarantees that the same person would never have access
to both the regulated and non-regulated data points.

**System design requirements**

- Evaluate the requirement for low-latency access, identifying
  specific latency targets, and determine whether the data needs
  to be accessible on-premises or by external applications. To
  provide maximum resilience, test your application flows that
  transit the AWS network between Regions and Local Zones or
  Outposts against the maximum latency expected for your
  applications.
- Is there a need for data to be shared across borders or exported
  from its primary storage location? If so, identify the parties
  involved, detail how the data transport is secured, and describe
  any adequacy or reciprocal agreements that are in place.

**Compliance and monitoring**

- Determine the necessary level of logging and whether logs can be
  centralized in an AWS Region.
- Identify required audit information for system events, access
  control, and configuration management.

**Backup and recovery**

- Establish the backup and recovery strategies required for your
  business needs, and specify the retention period for stored
  data.
- Assess if these can be stored centrally in an AWS Region.

###### Note

Outposts and Local Zones
(LZs) act as an extension to an AWS Availability Zone (AZ). However,
for disaster recovery (DR) purposes, store backups across multiple
Availability Zones and, where possible, in multiple Regions. The
Availability Zone that connects to the Outposts or Local Zone should
not be used as a backup, which provides greater resilience and
protection against failures in the primary Availability Zone.

**Data access and security**

- Assess if there are any geographical or logical data viewing
  restrictions.
- Address data privacy concerns by asking if the data going to be
  shared internally. If so, please list the use cases.

**Reporting and data management**

- Detail the reporting requirements involving in-scope data,
  including whether aggregated in-scope data can be used for
  reporting purposes. Assess if these reporting activities can be
  managed from outside the jurisdiction.
- Determine if in-scope data is used for business logic or solely
  for reporting purposes.

## Summary

The scenarios outlined in this section demonstrate that data
residency architectures are not one-size-fits-all. Data residency
encompasses a spectrum of considerations. Each scenario is
presented to encourage customers to think beyond conventional
solutions and help them navigate the complex landscape of
regulatory compliance. By exploring these diverse scenarios,
customers can use the full spectrum of AWS services within their
Region and its continuum, aligning with regulatory demands while
maximizing the benefits of AWS offerings.
