# MIDASEC09-BP03 Automate patch management for ICS and connected data

infrastructure

Patch known vulnerabilities in a timely manner across industrial control systems (ICS),
gateways, and cloud services by automating patch management processes.

**Desired outcome:** Patches are deployed consistently and
timely, minimizing exposure to known exploits.

**Benefits of establishing this best practice:** Reduces manual
overhead, enhances system stability, and supports compliance with vulnerability remediation
SLAs.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely
with OT vendors for ICS-specific patch cycles.

### Implementation steps

- Inventory all patchable assets across OT and IT systems.
- Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed
  nodes.
- Align maintenance windows with production downtime cycles.
- Monitor patch compliance using AWS Config and AWS Systems Manager reports.

## Resources

- [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md")
- [Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/ "https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/")
