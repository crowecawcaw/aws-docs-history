# ADVOPS01-BP02 Create RACI matrices that define the roles and

responsibilities for each key advertising process like infrastructure monitoring

When designing advertising workloads, define roles and set clear
expectations for each stakeholder for seamless key advertising
processes. By implementing this best practice, organizations can
leverage RACI (responsible, accountable, consulted, and informed)
matrices to establish a robust framework for accountability and
decision-making.

## Implementation guidance

By creating comprehensive RACI matrices, organizations can
establish accountability, decision-making authority, and
communication requirements for each step of the ad-serving
workflow. This level of clarity assists in blocking confusion,
gaps, or overlaps in responsibilities. This clarity also
verifies that stakeholders understand their roles and how they
contribute to the overall success of the advertising
operations.

For data management specifically, implement the following
approach:

1. Establish data classification and handling processes:
   - Classify advertising data based on criticality and
     latency requirements (real-time bidding data, campaign
     configuration data, historical analytics data)
   - Define data retention policies for each classification
     (for example, bid data retained for 30 days, campaign data
     for one year)
   - Implement data lineage tracking using AWS Glue Data
     Catalog to document data origins, transformations, and
     dependencies across the advertising pipeline

2. Structure teams around data criticality:
   - **Real-time data operations team:** Responsible for
     sub-100ms data like bidding, user profiles, and fraud
     detection
   - **Campaign data management team:** Handles near real-time
     data for configurations, targeting, and budgets
   - **Analytics and reporting team:** Manages batch processing
     for historical data and business intelligence

3. Define data ownership with specific domains:
   - Assign data stewards for specific advertising domains
     such as:
     - Bid management domain (bid requests, responses,
       auction data)
     - User profile domain (demographic data, behavioral
       signals, privacy preferences)
     - Campaign domain (creative assets, targeting
       parameters, budget configurations)
     - Analytics domain (performance metrics, attribution
       data, reporting datasets)

   - Document domain-specific quality standards and
     governance responsibilities in the RACI matrix

4. Implement data governance using AWS services:
   - Use AWS Organizations with service control policies
     (SCPs) to enforce data residency requirements for
     different Regions
   - Configure IAM roles with least-privilege permissions
     aligned to team responsibilities (for example, real-time team
     with write access to bidding data, read-only for
     analytics)
   - Deploy AWS Control Tower guardrails to help block
     unauthorized cross-account or cross-Region data
     transfers
   - Implement AWS Config rules to continuously audit
     compliance with data governance policies

5. Establish data management processes:
   - Data cataloging: Use AWS AWS Glue Data Catalog to maintain
     a comprehensive inventory of advertising datasets with
     metadata, ownership, and classification
   - Quality monitoring: Implement automated data quality
     checks using AWS Glue DataBrew to validate incoming
     data against defined schemas and business rules
   - Workflow automation: Create AWS Step Functions
     workflows for data handoffs between teams, with
     validation checkpoints and approval gates for critical
     data transitions

## Resources

- AWS Organizations for team boundaries: Implement
  multi-account strategies with SCPs to enforce separation
  of duties between data teams as described in
  [AWS Organizations Best Practices](../../../organizations/latest/userguide/orgs_best-practices.md "../../../organizations/latest/userguide/orgs_best-practices.md")
- Data governance implementation: Follow the framework in
  [AWS Data Governance Whitepaper](../../../whitepapers/latest/data-governance-aws.md "../../../whitepapers/latest/data-governance-aws.md")
  to establish controls specific to advertising data domains
- Team collaboration on data assets: Use
  [Amazon DataZone](../../../datazone/latest/userguide.md "../../../datazone/latest/userguide.md")
  to create a data marketplace where teams can discover,
  share, and collaborate on advertising datasets
- Automated operational procedures: Implement
  [AWS Systems Manager](../../../systems-manager/latest/userguide/systems-manager-best-practices.md "../../../systems-manager/latest/userguide/systems-manager-best-practices.md")
  runbooks for standardized data operations tasks across
  teams
- Compliance monitoring: Deploy
  [AWS Config rules](../../../config/latest/developerguide/best-practices.md "../../../config/latest/developerguide/best-practices.md")
  to continuously validate that data handling practices meet
  organizational and regulatory requirements
- [Create a RACI or RASCI matrix for a cloud operating model](../../../prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.md "../../../prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.md")

## Key AWS services

- AWS Organizations
- AWS IAM
- AWS Control Tower
- AWS AWS Glue Data Catalog
- AWS Glue DataBrew
- Amazon DataZone
- AWS Systems Manager
- AWS Config
- AWS Step Functions
