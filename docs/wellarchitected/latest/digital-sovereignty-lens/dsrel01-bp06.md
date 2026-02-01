# DSREL01-BP06 Train team members on recovery procedures

In regulated industries, training on recovery procedures is
essential for maintaining regulatory adherence, minimizing incident
impact, and protecting against financial and reputational damage.
Well-trained teams can run recovery plans effectively under
time-pressure, maintaining both regulatory adherence and swift
system restoration while reducing human error.

**Desired outcome:** Team members can
run recovery procedures efficiently, meeting regulatory requirements
and minimizing business disruption.

**Common anti-patterns:**

- Training only specific individuals creates single points of
  failure and knowledge bottlenecks.
- Using content that doesn't reflect current infrastructure,
  procedures, or regulatory requirements.
- Relying on theoretical training without regular drills in
  realistic environments.
- Conducting training too infrequently and failing to measure
  effectiveness or competency.
- Not incorporating industry-specific regulatory requirements into
  training programs and recovery steps.
- Failing to properly document procedures, leading to
  inconsistency and knowledge gaps.

**Benefits of establishing this best
practice:**

- Well-trained teams run procedures quickly and decisively,
  minimizing business impact through practiced workflows.
- Structured training programs demonstrate due diligence and
  maintain regulatory alignment.
- Regular practice builds confidence, reduces stress, and enhances
  cross-functional collaboration during incidents.
- Systematic training minimizes human error and knowledge loss
  while lowering incident-related costs.
- Training sessions identify optimization opportunities while
  building confidence among customers, partners, and regulators.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish a task-based training program that combines theoretical
knowledge with hands-on practice through simulation exercises and
game days.

Key implementation elements:

- Develop role-specific recovery runbooks
- Use AWS services to simulate failures (for example, chaos
  engineering)
- Schedule quarterly recovery drills
- Automate compliance validation during recovery

### Implementation steps

1. Define a training program structure with role and product
   domain based curricula and learning objectives using
   [AWS Skill
   Builder](https://skillbuilder.aws/ "https://skillbuilder.aws/"). Establish assessment criteria and
   certification paths to validate team member competency.
   Create a training schedule and document training
   requirements.
2. Define what each role needs to do during recovery, including
   operations procedures and step-by-step actions. Add
   validation checks so teams can verify that they're on track
   at each stage. Include compliance controls so that
   regulatory requirements are met during recovery. Set up
   version control to track changes and schedule quarterly
   reviews to keep runbooks current.
3. Set up a simulation environment using
   [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/") and
   [AWS Fault Injection Service](https://aws.amazon.com/fis/ "https://aws.amazon.com/fis/").

## Resources

**Related best practices:**

- [OPS07-BP01
  Ensure personnel capability](../operational-excellence-pillar/ops_ready_to_support_personnel_capability.md "../operational-excellence-pillar/ops_ready_to_support_personnel_capability.md")
- [OPS03-BP07
  Resource teams appropriately](../operational-excellence-pillar/ops_org_culture_team_res_appro.md "../operational-excellence-pillar/ops_org_culture_team_res_appro.md")
- [ADVREL05-BP01
  Perform routine evaluation of your workload's fault tolerance
  capabilities](../video-streaming-advertising-lens/advrel05-bp01.md "../video-streaming-advertising-lens/advrel05-bp01.md")
- [OPS07-BP03
  Use runbooks to perform procedures](../operational-excellence-pillar/ops_ready_to_support_use_runbooks.md "../operational-excellence-pillar/ops_ready_to_support_use_runbooks.md")
- [SEC10-BP04
  Develop and test security incident response playbooks](../security-pillar/sec_incident_response_playbooks.md "../security-pillar/sec_incident_response_playbooks.md")

**Related documents:**

- [Creating
  your own runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md")

**Related videos:**

- [AWS GameDay -
  Learn by doing](https://youtu.be/mNkf-Sjw3Kk "https://youtu.be/mNkf-Sjw3Kk")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Fault Injection Service](https://aws.amazon.com/fis/ "https://aws.amazon.com/fis/")
- [AWS GameDay](https://aws.amazon.com/gameday/ "https://aws.amazon.com/gameday/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/")
