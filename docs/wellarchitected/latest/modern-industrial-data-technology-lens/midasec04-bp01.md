# MIDASEC04-BP01 Segment OT networks from IT systems

Establish clear segmentation between OT networks and IT systems to limit the scope of
impact and reduce risk of lateral movement between environments.

**Desired outcome:** OT systems are logically and physically
isolated from IT networks while enabling secure data flows.

**Benefits of establishing this best practice:** Reduces
propagation of malware, minimizes risk of compromise of safety-critical systems, and supports
compliance with industrial cybersecurity frameworks.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement logical segmentation using VPCs, subnets, routing controls, and edge
gateways. Verify that minimal and controlled data flows between domains.

### Implementation steps

- Design separate network segments for IT and OT environments using VPCs and
  subnets.
- Deploy gateway services like AWS IoT Greengrass or AWS Transit Gateway to manage
  traffic between zones.
- Apply network ACLs and security groups to limit access paths.
- Log and monitor all cross-boundary traffic using VPC Flow Logs and AWS Network Firewall.

## Resources

- [Secure data ingestion from OT to IT using AWS IoT SiteWise and AWS IoT Greengrass](https://aws.amazon.com/blogs/iot/secure-data-ingestion-from-ot-to-it-using-aws-iot-sitewise-and-iot-greengrass/ "https://aws.amazon.com/blogs/iot/secure-data-ingestion-from-ot-to-it-using-aws-iot-sitewise-and-iot-greengrass/")
- [Security in your VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md")
