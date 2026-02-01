# DSREL01-BP04 Select and operationalize recovery sites

Select and set up recovery sites that meet your data and operational
sovereignty requirements, especially if you operate in regulated
industries. Your recovery plans should maintain data and workloads
in approved locations, meet industry regulations, and follow your
organizational security policies.

**Desired outcome:** Organizations
maintain disaster recovery sites that preserve data sovereignty and
regulatory adherence. Recovery sites enable rapid restoration when
needed and function reliably during normal operations and failover
scenarios. Data and workloads remain within approved jurisdictions
throughout the recovery processes.

**Common anti-patterns:**

- Automatically replicating data to nearest Regions without
  considering data sovereignty implications, treating data
  uniformly regardless of sensitivity levels, and failing to
  document data flows during normal and disaster scenarios.
- Moving data across jurisdictions without proper compliance
  checks or verification that recovery sites meet applicable
  regulations.
- Depending on manual, error-prone recovery procedures instead of
  automated, tested processes that maintain consistent compliance.

**Benefits of establishing this best
practice:**

- Supports quick and reliable disaster recovery through clear,
  consistent, and automated recovery steps that work across each
  scenario.
- Builds customer trust and competitive advantage by demonstrating
  commitment to data sovereignty, compliance requirements, and
  operational excellence.
- Maintains data and workloads within approved jurisdictions
  throughout the recovery processes, fostering regulatory
  adherence even during disruptions.
- Reduces risk of regulatory penalties and improves audit
  readiness.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Select AWS Regions that meet your needs for disaster recovery and
automate your recovery steps. Agree with your business
stakeholders as to what constitutes minimum service levels for a
given workload. Perform validations (for example, data integrity
checks, connectivity checks, data flows, and latency) after
completion of every stage to check if minimum service levels are
achieved.

Your recovery procedure should also document full recovery
timelines, and how stakeholders are to be kept informed during
every stage until full recovery is achieved.

**Digital sovereignty
considerations**: To set up compliant recovery sites,
start by classifying data, including data type and sensitivity
levels. Understand which data privacy legislations and
cybersecurity standards are applicable to you. Check where data
can be stored. Check where your operational recovery teams are
located and what access they have. Work with legal and compliance
teams to establish clear policies for cross-border data movement.

Key implementation elements:

- Assess regulatory requirements (for example, GDPR,
  country-specific data privacy legislations and directives)
- Select AWS Regions that meet residency and compliance needs
- Apply data residency controls (for example
  [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") Service Control Policies,
  [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/") rules,
  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") routes) to manage traffic during
  disaster recovery
- Automate deployment of workloads to recovery sites using
  infrastructure as code (IaC)
- Encrypt data using keys managed in compliant Regions (for
  example, AWS KMS with restricted key policies)
- Regularly test failover to validate adherence and
  functionality

### Implementation steps

1. Assess regulatory requirements:
   1. List data protection and data privacy requirements that
      apply to your business.
   2. Document industry-specific regulations you must follow.
   3. Define recovery timelines for each system.
   4. Map which data types can be stored in which locations.
   5. Get sign-off from legal and compliance teams.

2. Select and validate AWS Regions for recovery:
   1. Review
      [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") to verify service availability
      in your chosen AWS Regions.
   2. Use
      [AWS Artifact](https://aws.amazon.com/artifact/ "https://aws.amazon.com/artifact/") to check compliance certifications and
      attestations for each AWS Region.
   3. Test the network latency between primary and recovery
      sites.

3. Configure encryption and key management using
   [AWS Key Management Service](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") (AWS KMS) and
   [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/"):
   1. Create Region-specific encryption keys.
   2. Set up key policies that enforce data sovereignty.
   3. Document key management procedures.

4. Design and configure the recovery network using
   [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"),
   [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/"), and
   [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/"):
   1. Create isolated network segments with VPC.
   2. Set up security controls and define routing between
      Regions.
   3. Configure Transit Gateway to connect VPCs and
      on-premises networks.
   4. Control cross-Region traffic and enforce network
      security policies.
   5. Set up Direct Connect for dedicated connection to AWS
      with consistent network performance and secure data
      transfer.

5. Automate your recovery infrastructure using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") (CloudFormation) or
   [AWS Cloud Development Kit (AWS CDK) (CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/"):
   1. Create infrastructure templates.
   2. Validate your infrastructure templates with
      CloudFormation cfn-validate and
      cfn-test.
   3. Automate recovery steps. Consider using
      [AWS Elastic Disaster Recovery](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md"),
      [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/"),
      [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/"),
      [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") functions to orchestrate recovery flows.
   4. Run regular recovery drills to test automation.
   5. Validate compliance requirements during tests.
   6. Document test results and update procedures based on
      findings.

## Resources

**Related best practices:**

- [Encryption
  best practices for AWS Key Management Service](../data-residency-hybrid-cloud-services-lens/drhcops03-bp04.md "../data-residency-hybrid-cloud-services-lens/drhcops03-bp04.md")
- [REL13-BP02
  Use defined recovery strategies to meet the recovery
  objectives](../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md "../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md")
- [ADVREL03-BP02
  Choose AWS Regions that meet your legal and disaster recovery
  requirements](../video-streaming-advertising-lens/advrel03-bp02.md "../video-streaming-advertising-lens/advrel03-bp02.md")

**Related documents:**

- [AWS Regions](../../../global-infrastructure/latest/regions/aws-regions.md "../../../global-infrastructure/latest/regions/aws-regions.md")
- [Encryption
  best practices for AWS Key Management Service](../../../prescriptive-guidance/latest/encryption-best-practices/kms.md "../../../prescriptive-guidance/latest/encryption-best-practices/kms.md")

**Related videos:**

- [AWS re:Inforce 2025-Navigating sovereignty requirements:
  Architectures and solutions on AWS (DAP202)](https://www.youtube.com/watch?v=Eq0K0pxRjRk "https://www.youtube.com/watch?v=Eq0K0pxRjRk")

**Related services:**

- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/ "https://aws.amazon.com/cloudhsm/")
- [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/")
- [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [AWS Elastic Disaster Recovery](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md")
