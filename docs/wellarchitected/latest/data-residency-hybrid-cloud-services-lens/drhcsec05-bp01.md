# DRHCSEC05-BP01 Implement detective controls that notify a security operations team when resources are found in unauthorized locations

Automate the detection and notification to security operations
teams if data is stored is locations out of compliance with your
data residency compliance requirements.

**Desired outcome:** Security
operations teams are automatically notified when detective
controls find resources in noncompliant locations.

**Common anti-patterns:**

- Lack of automated mechanisms to detect data in unauthorized
  locations
- No one follows up on notifications that no one follows up on

**Benefits of establishing this best
practice:** Security operations teams are alerted to data
in unauthorized locations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- Create detective controls, such as
  [AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") or open source solutions like
  [Cloud
  Custodian](https://cloudcustodian.io/ "https://cloudcustodian.io/") rules, and configure them to detect and
  notify when resources are found in unapproved locations.
  1.  For EC2 instances, subnets, EBS volumes, and snapshots
      (like EBS, Amazon RDS, and Amazon ElastiCache):
      - **Outposts**:
        Implement rules that detect resources where value of
        OutpostArn attribute is null, which means that the
        resource is located in a Region. Alternatively,
        create a strict implementation that checks if the
        actual value is not in a specific allowlist of
        OutpostArns.
      - **Local Zones**:
        Implement rules that detect resources where the
        value of AvailabilityZone is not the expected Local
        Zone.

  2.  Implement rules for EC2 instances, Auto Scaling groups
      (ASGs), NetworkInterfaces, RDS instances, and
      Application Load Balancers (ALB) to detect when the
      value of the SubnetId attribute value is not present in
      an allowlist.

- Automate remediation of findings in scenarios where precise
  rules without exceptions can be enforced. One example would
  be to automatically end an instance launched in an in-Region
  subnet when data residency requirements prohibit data
  storage in that Region. Another example would be to turn on
  default encryption for S3 buckets and EBS volumes.
  1.  Automated remediation is an example of a control.
      Automated remediation can be implement using
      [AWS Security Hub CSPM custom actions](../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md "../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md"), AWS Config
      integration with
      [Systems
      Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") documents, and
      [Cloud
      Custodian](https://cloudcustodian.io/docs/actions.html "https://cloudcustodian.io/docs/actions.html") actions.

## Resources

**Related documentation:**

- Evaluating Resources with
  [AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
- AWS
  [Systems
  Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [AWS Security Hub CSPM custom actions](../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md "../../../securityhub/latest/userguide/securityhub-cloudwatch-events.md")

**Related partner solutions:**

- [Cloud
  Custodian](https://cloudcustodian.io/docs/actions.html "https://cloudcustodian.io/docs/actions.html") actions
