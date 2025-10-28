# Best Practice 10.1 – Agree on SAP

workload availability goals that align with your business requirements

Understanding your availability goals is the first step to help ensure that you focus
on the factors important to your organization. This helps you to define criteria that can
be used to evaluate your architectural patterns.

**Suggestion 10.1.1 – Identify SAP applications in scope and their
interdependencies**

Identify the SAP applications that you have deployed or will deploy in AWS.
Understand any dependencies these applications have regardless of their location.

**Suggestion 10.1.2 – Classify systems based on the impact of
failure**

There is no open standard for system classification aligned with planned availability
and risk of failure. Defining systems using terms such as Mission Critical or Highly
Important can help with defining patterns, identifying application grouping, and
justifying costs. Production applications might be impacted differently by an outage.
Factors to consider might include:

- Revenue generating or revenue reporting
- External or internal facing
- Core business vs. technical support
- Closely coupled vs. loosely coupled with other systems
  Non-production environments can also play an important role in indirectly supporting
  the business. They should also be classified according to project phase and scale, taking
  into account transport paths (such as business as usual and projects) and supporting role
  (such as development, unit test, production copy, and training).

**Suggestion 10.1.3 – Assess the business impact of an
outage**

The impact should be measurable and take into consideration the duration of the
outage. Examples of areas of impact include health and safety, financial, legal,
regulatory, or brand.

**Suggestion 10.1.4 – Understand compliance and regulatory
requirements**

Understand compliance or regulatory requirements for data residency and distance
between locations to help ensure business continuity.

**Suggestion 10.1.5 – Define minimum acceptable percentage
uptime**

For each system, or group of systems, agree and document an acceptable availability
percentage which matches with business requirements. The following terms are used in this
context

- MTTR – Mean Time to Recovery
- RTO – Recovery Time Objective
- RPO – Recovery Point Objective
  A full explanation of the terms can be found in the Well-Architected Framework
  [Reliability]: [Availability](../reliability-pillar/availability.md "../reliability-pillar/availability.md"). Additional information on reliability in SAP can be found in the
  whitepaper:

- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md "../../../sap/latest/general/architecture-guidance-of-sap-on-aws.md")
