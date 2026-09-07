

# MSFTSEC01-BP01 Protect the operating system
<a name="msftsec01-bp01"></a>

 Securing the operating system that hosts your Microsoft application is crucial in blocking unauthorized access, securing software availability, and maintaining the stability of your critical systems. By following Microsoft and AWS recommendations for Windows Server environments, you can reduce the risk of malicious attacks. 

 This is particularly important when using unmanaged or non-serverless services. Implementing these best practices creates a robust foundation for your Microsoft workload, enhancing overall security and resilience. Remember that a well-protected operating system forms a critical layer in your defense strategy, safeguarding your application and data from potential threats. 

 **Desired outcome:** Establish a hardened Windows Server environment that follows security best practices, implements proper access controls, and maintains up-to-date security configurations to protect your Microsoft workload from operating system-level threats and vulnerabilities. 

 **Common anti-patterns:** 
+  Using default Windows Server configurations without implementing security hardening measures, leaving systems vulnerable to common attack vectors and exploitation techniques. 
+  Failing to implement proper user account management and access controls, allowing excessive privileges or shared accounts that increase security risks and make it difficult to track user activities. 
+  Neglecting to configure Windows Firewall and network security settings appropriately, potentially exposing unnecessary services or ports to network-based attacks. 

 **Benefits of establishing this best practice:** 
+  Reduced attack surface through proper system hardening, disabling unnecessary services, and implementing security configurations that minimize potential entry points for malicious actors. 
+  Enhanced access control and accountability through proper user account management, role-based access controls, and audit logging that tracks system access and changes. 
+  Improved regulatory posture by implementing security baselines and configurations that align with industry standards and regulatory requirements for Windows Server environments. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Protecting the Windows Server operating system requires a systematic approach to security hardening that addresses user accounts, services, network configuration, and system monitoring. Start by implementing Microsoft security baselines and AWS-recommended configurations, then customize these settings based on your specific workload requirements. This comprehensive approach verifies that your Windows Server instances provide a secure foundation for your Microsoft applications while maintaining operational functionality. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Apply Microsoft Security Baselines for Windows Server using Group Policy or local security policies to establish fundamental security configurations. 

1.  Configure Windows Firewall with appropriate rules that allow only necessary network traffic and block potentially malicious connections. 

1.  Implement proper user account management with strong password policies, account lockout settings, and regular review of user privileges. 

1.  Disable unnecessary Windows services and features that are not required for your Microsoft workload to reduce the attack surface. 

1.  Configure Windows Event Logging to capture security events, system changes, and access attempts for monitoring and audit purposes. 

1.  Enable Microsoft Windows Defender on your EC2 instances running Windows Server for local anti-malware protection. 

1.  Implement regular security assessments using AWS Systems Manager Compliance or third-party security scanning tools. 

1.  Establish automated patch management processes using AWS Systems Manager Patch Manager to keep the operating system current with security updates. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Security best practices for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-security-best-practices.html) 
+  [Add optional Windows Server components to Amazon EC2 Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-optional-components.html) 
+  [Security baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines) 

 **Related tools:** 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [AWS Systems Manager Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-compliance.html) 
+  [Windows Security Baseline](https://www.microsoft.com/en-us/download/details.aspx?id=55319) 