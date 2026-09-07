

# MIDASEC09-BP03 Automate patch management for ICS and connected data infrastructure
<a name="midasec09-bp03"></a>

 Patch known vulnerabilities in a timely manner across industrial control systems (ICS), gateways, and cloud services by automating patch management processes. 

 **Desired outcome:** Patches are deployed consistently and timely, minimizing exposure to known exploits. 

 **Benefits of establishing this best practice:** Reduces manual overhead, enhances system stability, and supports compliance with vulnerability remediation SLAs. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-32"></a>

 Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely with OT vendors for ICS-specific patch cycles. 

### Implementation steps
<a name="implementation-steps-33"></a>
+  Inventory all patchable assets across OT and IT systems. 
+  Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed nodes. 
+  Align maintenance windows with production downtime cycles. 
+  Monitor patch compliance using AWS Config and AWS Systems Manager reports. 

## Resources
<a name="resources-33"></a>
+  [AWS Systems Manager Patch Manager ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) 
+  [ Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/) 