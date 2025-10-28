# Siloed data

Siloed data is a major challenge faced by many companies' supply
chain operations. Data exists separately and is not accessible by
other departments or business unit. As a result, decision making
is made at each local level while lacking upstream and downstream
indicators that would drive improved supply chain execution and
risk mitigation.

A _data fabric_ alleviates the frustration of
hunting through data across multiple systems by creating a unified
data architecture that supply chain teams can quickly access and
trust. End users from procurement specialists to logistics
managers can find, analyze, and act on real-time information
through intuitive interfaces, replacing manual data gathering with
automated insights. Further, by combining data across areas of the
supply chain, leading indicators and downstream results can be
correlated for greater performance management and risk avoidance.

Implementing a data fabric in the supply chain using the AWS
Well-Architected Framework delivers self-service access to
reliable data while maintaining enterprise-grade security and
performance. Business analysts can directly connect to data from
IoT devices, ERP systems, and external feeds through AWS services
including Amazon S3 for storage, AWS Glue for ETL processing, and
AWS DataSync for data movement and synchronization.

The Well-Architected Framework pillars provide users confidence as
they follow efficient standards. Security controls protect
sensitive data while allowing appropriate access. Reliability
features help prevent disruptions to daily operations. Cost
optimization keeps data storage and processing economical.
Operational excellence means systems run smoothly without IT
intervention. Performance efficiency delivers fast query responses
and real-time analytics capabilities.

Supply chain teams gain powerful analytics capabilities through
the data fabric. Business analysts run complex queries in Amazon Redshift. Planners and managers create their own visualizations
and reports in Quick Suite without waiting for IT support.
These self-service tools enable predictive analytics, process
optimization, and data-driven decisions across roles. The result
is greater productivity, faster response times, and better
outcomes through accessible, trusted data and analytics.

## Reference architecture

![Reference architecture displaying an AWS architecture that addresses siloed data.](images/image3.png)

## Architecture description

1. Ingest data from external and internal systems into Amazon S3.
2. AWS Glue provides integration data flows. AWS DataSync to
   migrate data from on premises to AWS Cloud. Amazon DataZone
   to catalog and provide fine grained control of the data
   being integrated.
3. Amazon Redshift provides the structured data store.
4. For the application layer, Amazon Quicksight provides
   dashboards, reporting, and analytics.

## Architecture objectives

- Data accessibility and unification
- Operational analytics
- Business user empowerment
- Supply chain performance enhancement
- Operational efficiency
- Data quality and trust

## Metrics

Based on the given data fabric and AWS Well-Architected
Framework scenario, the relevant metrics that provide valuable
insights for measuring success and performance are:

- Data accuracy:
  - **Metric**: Percentage of
    accurate data transfers.
  - **Rationale**: Critical
    for supply chain operations where data quality directly
    impacts decision-making.
  - **Well-Architected
    pillar**: Reliability.
  - Aligns with the need for trusted data.

- System downtime:
  - **Metric**: System uptime
    percentage.
  - **Rationale**: Essential
    for maintaining continuous access to real-time supply
    chain data.
  - **Well-Architected
    pillar**: Reliability.
  - Critical for supporting uninterrupted supply chain
    operations.

- Response time:
  - **Metric**: Average
    response time.
  - **Rationale**: Crucial
    for real-time analytics and quick decision-making.
  - **Well-Architected
    pillar**: Performance efficiency.
  - Important for self-service analytics mentioned in the
    scenario.

- Security:
  - **Metric**: Number of
    security incidents and compliance adherence.
  - **Rationale**: Essential
    for protecting sensitive supply chain data.
  - **Well-Architected
    pillar**: Security.
  - Critical for maintaining enterprise-grade security
    mentioned in the scenario.
