# LSREL09-BP02 Implement safe deployment strategies (like

blue/green or canary)

Adopt deployment patterns that minimize blast radius and allow rapid
diversion to the last known good state. Phased rollouts provide
early detection of issues and enable quick rollback without
impacting users or downstream regulatory workflows.

**Desired outcome:** Failed releases
can be quickly rolled back or diverted with minimal disruption to
end users and regulatory processes.

**Common anti-patterns:**

- Performing deployments at once without a rollback path.
- No traffic segmentation or user impact analysis during rollouts.
- Failing to gather metrics and health signals during phased
  deployments.

**Benefits of establishing this best
practice:**

- Limits impact to a subset of experiments or studies rather than
  the entire user base and workflows.
- Enables rapid return to a validated state, protecting study
  timelines.
- Improves stakeholder confidence in release safety and stability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Choose a rollout strategy based on risk and verification needs:
blue/green for fast switchovers to fully validated environments,
canary for incremental exposure and metric observation, or
feature-flag driven rollouts for business-level segmentation.
Instrument deployments with health metrics, business KPIs, and
signals so an automated or manual rollback decision can be made
quickly. Validate the traffic-shift and rollback procedures during
staging exercises and include them in release approvals.

### Implementation steps

1. Use blue/green deployment patterns available in AWS Elastic Beanstalk or by provisioning parallel stacks using AWS CloudFormation and switching traffic with Amazon Route 53 or
   load balancer reconfiguration.
2. Use Amazon ECS or Amazon EKS with traffic shifting
   configured (for example, using AWS App Mesh or AWS CodeDeploy integration) to implement canary releases.
3. Implement automated traffic shifting and rollback policies
   in AWS CodeDeploy so that failing canaries automatically
   trigger rollbacks or traffic diversion.

## Resources

**Related best practices:**

- Continuity of workflows and data availability during downtime
- Resilient environment provisioning and lifecycle management
- Automated validation in deployments
