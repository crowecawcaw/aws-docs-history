# Best Practice 6.2 – Build and protect

the operating system

Protecting the operating system underlying your SAP software reduces the possibility
that a malicious actor could gain unauthorized access to data within the SAP application,
impact software availability, or otherwise destabilize your mission-critical
implementation. Follow recommendations from SAP, the operating system vendor, the database
vendor, and AWS to help secure the operating system. Depending on your chosen SAP
solution and operating system, you may need to enable/disable services, set specific
kernel parameters, and apply different combinations of security patches. Consider how SAP
requirements align with those of your organization, and identify any conflicts.

**Suggestion 6.2.1 – Determine an approach for provisioning a secure
operating system**

An Amazon Machine Image (AMI) provides the information required to launch an EC2
instance. You should be confident that your AMIs are secure at the operating system level;
otherwise, security holes could be propagated to any number of instances as AMIs are
reused and updated over time.

AMIs can be either standard images from the operating system vendor or custom images
that you build yourself. In both cases, you need to have a consistent approach for ensuring
the operating system is secure at launch and maintained in an on-going basis. Using
infrastructure as code (IaC) tools such as [CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") can assist with achieving image
security consistency. For HANA-based SAP solutions, the [AWS Launch Wizard](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/") for SAP simplifies
the installation process, including pre- and post-installation scripts that can be
customized to automate the installation of security components.

Refer to the AWS Well-Architected Framework [Security Pillar] guidance on
protecting compute resources, specifically the information on performing vulnerability
management and reducing the attack surface, for additional details.

- Well-Architected Framework [Security]: [Protecting Compute](../security-pillar/protecting-compute.md "../security-pillar/protecting-compute.md")

**Suggestion 6.2.2 – Determine an approach for building and patching a
secure operating system**

As mentioned in the Well-Architected Framework [Security Pillar] discussion on
protecting compute, if your chosen operating system is supported by the EC2 Image Builder,
it can simplify the building, testing, and deployment of your SAP-specific AMIs and their
ongoing patch management. AWS Systems Manager Patch Manager should also be investigated
for maintaining the security posture of your operating system by automating security patch
application.

- Well-Architected Framework [Security]: [Protecting Compute](../security-pillar/protecting-compute.md "../security-pillar/protecting-compute.md")
- AWS Documentation: [EC2 Image
  Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/")
- AWS Documentation: [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md")

**Suggestion 6.2.3 – Review additional security recommendations
applicable to your operating system**

Determine the complete list of items that are required to harden the operating system
underlying the SAP software. For example, file system permissions on Linux-based systems
should be set according to SAP guidelines, while limiting Administrator group access is a
best practice on Windows-based systems.

The following SAP-specific recommendations might be relevant to your environment:

- SAP Documentation: [SAP NetWeaver Security Guide - Operating System Security](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a6e3d96f90472dde10000000a42189b.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a6e3d96f90472dde10000000a42189b.html")
- SAP Note: 2808515 - [Installing security software on SAP servers running on Linux](https://launchpad.support.sap.com/#/notes/2808515 "https://launchpad.support.sap.com/#/notes/2808515")

| Operating System                           | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| All Supported UNIX/Linux Operating Systems | • SAP Documentation: [SAP System Security Under UNIX/LINUX](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d3da980d936391ee10000000a15822b.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d3da980d936391ee10000000a15822b.html")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SUSE Linux Enterprise Server               | • SAP Note: [2684254 - SAP HANA<br>DB: Recommended OS settings for SLES 15 / SLES for SAP Applications<br>15](https://launchpad.support.sap.com/#/notes/2684254 "https://launchpad.support.sap.com/#/notes/2684254") [Requires SAP Portal Access]<br>• SAP Note: [2578899 - SUSE<br>Linux Enterprise Server 15: Installation Note](https://launchpad.support.sap.com/#/notes/2578899 "https://launchpad.support.sap.com/#/notes/2578899") [Requires SAP Portal<br>Access]<br>• Operating system-specific Documentation: [SUSE Hardening Guide](https://documentation.suse.com/sbp/all/html/OS_Security_Hardening_Guide_for_SAP_HANA_SLES15/ "https://documentation.suse.com/sbp/all/html/OS_Security_Hardening_Guide_for_SAP_HANA_SLES15/")                                                                                                                                                                  |
| Red Hat Enterprise Linux                   | • SAP Note: [2777782 - SAP HANA DB: Recommended OS Settings for RHEL 8](https://launchpad.support.sap.com/#/notes/2777782 "https://launchpad.support.sap.com/#/notes/2777782") [Requires<br>SAP Portal Access]<br>• SAP Note: [2772999 - Red Hat Enterprise Linux 8.x: Installation and<br>Configuration](https://launchpad.support.sap.com/#/notes/2772999 "https://launchpad.support.sap.com/#/notes/2772999") (with particular mention of SELinux support) [Requires<br>SAP Portal Access]<br>• Red Hat Documentation: [Red Hat Enterprise Linux<br>Security Hardening Guide for SAP HANA 2.0](https://access.redhat.com/articles/6892601 "https://access.redhat.com/articles/6892601")<br>• Red Hat Blog: [Security recommendations for SAP HANA on RHEL](https://www.redhat.com/en/blog/security-recommendations-sap-hana-rhel "https://www.redhat.com/en/blog/security-recommendations-sap-hana-rhel") |
| Microsoft Windows                          | • SAP Documentation: [SAP System Security on Windows](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d6b747d7f961fbbe10000000a15822b.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d6b747d7f961fbbe10000000a15822b.html")<br>• SAP Note: [1837765 - Security<br>policies for <SID>adm and SAPService<SID> on Windows](https://launchpad.support.sap.com/#/notes/1837765 "https://launchpad.support.sap.com/#/notes/1837765")<br>[Requires SAP Portal Access]                                                                                                                                                                                                                                                                                                                                                                                  |
| Oracle Enterprise Linux                    | • (Consult SAP or Vendor documentation for guidance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Suggestion 6.2.4 – Validate the security posture of the operating
system**

After the operating system has been securely deployed and patched, validating the
operating system security posture ensures that the operating system maintains an ongoing
high level of security without violation. Consider automating this validation using
third-party host intrusion protection, intrusion detection, antivirus, and operating system
firewall software.

Consider the following services:

- [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/") is an automated
  vulnerability management service that continually scans AWS workloads for software
  vulnerabilities and unintended network exposure.
- [Amazon GuardDuty Malware Protection](../../../guardduty/latest/ug/malware-protection.md "../../../guardduty/latest/ug/malware-protection.md") is a continuous security monitoring service to
  analyze and process threats from multiple data sources. Use it to highlight activity
  that may indicate an instance compromise, such as cryptocurrency mining, denial of
  service activity, EC2 credential compromise, or data exfiltration using DNS.
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") and [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") can be used for aggregation and
  assessment of operating system based alerts and configuration, along with other AWS
  services.
  For more details, refer to the following information:

- Well-Architected Framework [Security]: [Secure Operation](../security-pillar/operating-your-workload-securely.md "../security-pillar/operating-your-workload-securely.md")
- Well-Architected Framework [Security]: [Detection](../security-pillar/detection.md "../security-pillar/detection.md")
- Well-Architected Framework [Security]: [Protecting Compute](../security-pillar/protecting-compute.md "../security-pillar/protecting-compute.md")
