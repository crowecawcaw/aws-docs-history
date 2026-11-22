

# SEC06-BP05 Automate compute protection

 Manual security operations do not keep pace with the rate at which compute resources change and vulnerabilities appear. Automating scanning, patching, verification, and remediation reduces the chance of a misconfiguration reaching production and shortens the time from detection to remediation. 

 **Desired outcome:** 
+  Your automation performs the scanning and patching of your compute resources. 
+  Your automated verification confirms that images and dependencies come from trusted sources and are unaltered. 
+  Your workloads are checked automatically for current dependencies and are signed to establish trust before they run. 
+  Your automated remediation starts when a non-compliant resource is detected, with a manual override available. 

 **Common anti-patterns:** 
+  Teams adopt immutable infrastructure but have no plan for emergency patching or replacing production systems. 
+  Automation fixes misconfigured resources, but no manual override exists to suspend it while requirements change. 

 **Benefits of establishing this best practice:** 
+  Automation reduces the risk of unauthorized access to and use of your compute resources. 
+  Misconfigurations are caught before they reach production, and corrected quickly when they do occur. 
+  Faster detection and response shrink the overall scope of impact from an issue. 
+  Consistent, automated controls remove the variability of manual security operations. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Hardened images, signature verification, vulnerability scanning, and patching can all drift, lag, or get skipped when performed manually. Automated pipelines and fleet operations run them continuously. A pipeline that builds hardened images, verifies signatures, checks dependencies, and scans for known CVEs lets a workload reach production only when those checks pass. 

 Preventive controls stop a bad state from being created, while detective controls find existing bad states. For example, a pipeline gate that blocks an unsigned image is preventive, and a fleet scan that flags an instance using an outdated metadata service is detective. Pair the scan with automated remediation to resolve the finding without waiting for a person. At design time, choose which risks you want to prevent and which risks you want to detect and correct. 

 Automated remediation introduces its own risk where performs its exact function even after a requirement has changed. If a control automatically reverts a configuration and a legitimate change needs that configuration, the automation will continue to revert the change. Build a manual override or suspension mechanism from the start so an operator can pause a remediation while requirements are updated. 

 [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) offers standards such as [NIST SP 800-53 Rev. 5](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference-nist-800-53.html), which includes a [check that EC2 instances use Instance Metadata Service Version 2 (IMDSv2)](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-8). IMDSv2 requires session-oriented requests, blocks requests that carry an X-Forwarded-For header, and sets a network TTL of 1 to stop external sources from retrieving instance metadata. When Security Hub CSPM detects an instance still using IMDSv1, it can initiate an automated remediation. Around this control, [EC2 Image Builder](https://aws.amazon.com/image-builder/) produces hardened images, [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) and [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/managed-signing.html) verify what runs, [Amazon Inspector](https://aws.amazon.com/inspector/) scans for CVEs, and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) patches or redeploys. [Amazon GuardDuty](https://aws.amazon.com/guardduty/) adds threat and malware detection across the environment, including unusual behavior tied to instances and functions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Automate hardened image creation:** Use [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-compliance-products.html) to produce images that incorporate CIS Benchmark or DISA STIG controls from base AWS and APN partner images. 

1.  **Automate configuration and compliance management:** Enforce and validate secure configurations automatically with [AWS Config](https://aws.amazon.com/config/), and manage your security and compliance posture with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/). 

1.  **Automate patching or replacement:** Use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to patch managed instances with operating system and application updates, and redeploy from fresh images where components are immutable. 

1.  **Automate vulnerability scanning:** Scan compute resources for CVEs with [Amazon Inspector](https://aws.amazon.com/inspector/), and embed [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) in your build pipeline. 

1.  **Automate threat and malware detection:** Use [Amazon GuardDuty](https://aws.amazon.com/guardduty/) to detect malware and threats against your compute resources, including issues raised when an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function is invoked in your environment. 

1.  **Preserve a manual override:** Build a mechanism to suspend automated remediation so an operator can pause it while you update requirements, then re-enable it once the change is complete. 

1.  **Evaluate AWS Partner solutions where they fill gaps:** Consider [AWS Partner infrastructure security products](https://aws.amazon.com/security/partner-solutions/) that complement native controls across your cloud and on-premises environments. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [SEC06-BP02 Provision compute from hardened images](sec06-bp02.md) 
+  [SEC06-BP03 Reduce manual management and interactive access](sec06-bp03.md) 
+  [SEC06-BP04 Validate software integrity](sec06-bp04.md) 
+  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md) 

 **Related documents:** 
+  [AWS Security Hub CSPM NIST SP 800-53 Rev. 5 standard](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference-nist-800-53.html) 
+  [Security Hub CSPM control EC2.8 – EC2 instances should use IMDSv2](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-8) 
+  [Automate hardened image creation with EC2 Image Builder compliance products](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-compliance-products.html) 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) 
+  [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) 
+  [AWS Partner security solutions](https://aws.amazon.com/security/partner-solutions/) 

 **Related videos:** 
+  [AWS Encryption and Authorization for Security](https://www.youtube.com/watch?v=T4_rqwfngfU) 

 **Related examples:** 
+  [Transition to using Instance Metadata Service Version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) 

 **Related services:** 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [Amazon ECR](https://aws.amazon.com/ecr/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 