# MSFTOPS02-BP03 Implement operating system image control

AWS has developed a set of Amazon Machine Images (AMIs) for popular
Microsoft solutions with License Included software, enabling
standardized and automated deployments of Windows Server instances
in Amazon EC2. You can either use the latest images that are built
by AWS or create your own. You can subscribe to AWS Windows AMI
notifications or create custom AMIs of your own to apply the
standards required by your environment, such as regional settings,
agents, base patches, and general tools. EC2 Image Builder is a
fully managed AWS service that helps you to automate the creation,
management, and deployment of customized, secure, and up-to-date
server images.

**Desired outcome:** Establish
standardized, secure, and consistently configured Windows Server
images for your Microsoft workloads through automated AMI
management, ensuring rapid deployment capabilities, security
compliance, and operational consistency across all Windows instances
in your environment.

**Common anti-patterns:**

- Using outdated or unpatched base AMIs without regular updates,
  leading to security vulnerabilities and inconsistent
  configurations across Windows instances in your Microsoft
  workload environment.
- Creating custom AMIs manually without automation or version
  control, resulting in configuration drift, difficulty in
  reproducing images, and challenges in maintaining security and
  compliance standards.
- Deploying Windows instances without standardized configurations,
  leading to operational inconsistencies, increased
  troubleshooting time, and potential security gaps across your
  Microsoft workload infrastructure.

**Benefits of establishing this best
practice:**

- Faster deployment and improved consistency through standardized
  Windows Server images that include all necessary configurations,
  patches, and tools, reducing instance launch time and ensuring
  uniform environments.
- Enhanced security posture through automated image updates and
  patch management, ensuring all Windows instances are deployed
  with the latest security updates and compliance configurations.
- Reduced operational overhead through automated AMI creation and
  management processes that eliminate manual image preparation
  tasks and ensure consistent, repeatable deployments across
  environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing operating system image control for Microsoft
workloads requires a systematic approach to AMI management and
automation. Begin by establishing your image requirements and
standards, then implement EC2 Image Builder to automate the
creation and maintenance of custom Windows AMIs. This approach
ensures consistent, secure, and up-to-date images for your
Microsoft workload deployments.

### Implementation steps

1. Define your Windows Server image requirements including base
   configurations, security settings, required software, and
   organizational standards.
2. Set up EC2 Image Builder with appropriate IAM roles and
   permissions to automate AMI creation and management
   processes.
3. Create Image Builder recipes that include your required
   Windows configurations, software installations, and security
   hardening steps.
4. Configure automated testing pipelines to validate AMI
   functionality and security compliance before distribution.
5. Implement automated AMI distribution to multiple AWS regions
   and accounts as needed for your Microsoft workload
   deployment strategy.
6. Set up AMI lifecycle management policies to automatically
   deprecate and delete outdated images while maintaining
   required retention periods.
7. Subscribe to AWS Windows AMI notifications to stay informed
   about security updates and new releases for base Windows
   Server images.
8. Establish regular AMI update schedules to incorporate
   security patches, software updates, and configuration
   changes into your custom images.

## Resources

**Related documents:**

- [What
  is EC2 Image Builder?](../../../imagebuilder/latest/userguide/how-image-builder-works.md "../../../imagebuilder/latest/userguide/how-image-builder-works.md")
- [How
  Amazon creates AWS Windows AMIs](../../../ec2/latest/windows-ami-reference/windows-ami-versions.md "../../../ec2/latest/windows-ami-reference/windows-ami-versions.md")

**Related tools:**

- [Amazon EC2 AMIs](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md")
- [EC2 Image Builder](../../../imagebuilder.md "../../../imagebuilder.md")
