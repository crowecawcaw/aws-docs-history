# Anti-patterns for everything as code

- **Checking in secrets:** Storing sensitive data, such as
  API keys, passwords, or other secrets, directly in the code base or version control
  system is a critical security vulnerability. Checking in secrets exposes sensitive
  credentials to anyone with access to the repository and, if the repository is public, to
  the world. Instead, use management tools or services to store and retrieve secrets
  securely. These tools can integrate with deployment pipelines and systems during runtime
  to provide secrets only when necessary, ensuring they remain confidential and are not
  inadvertently exposed.
- **Manual modifications to infrastructure:** Making manual
  changes to infrastructure can be time consuming and error prone, leading to
  inconsistencies that can be difficult to troubleshoot and resolve. Actively prevent
  users from making manual changes to environments and workloads to ensure consistent and
  reliable deployments.
- **Outdated or incomplete documentation:** Ignoring
  documentation or treating it as an afterthought can lead to knowledge gaps,
  misunderstandings about system behavior, and misleading users. As the system changes
  over time, documentation needs to be continuously updated to align with the current
  system state.
- **Ignoring configuration drift:** Failing to track and
  manage changes to your system's configuration can result in configuration drift, where
  the actual configuration state deviates from the desired state. Overtime this can lead
  to system instability, security vulnerabilities, and operational inefficiencies. Use
  continuous configuration management practices and automated governance capabilities to
  keep configurations in a known and secure state.
- **Bypassing code review and testing:** Failing to review
  and test IaC changes, including data, documentation, configuration, and networking
  components is an anti-pattern that can lead to data inconsistencies, data loss, and
  system instability. It's important to apply the same quality assurance practices to IaC
  as you would to application code.
- **Inefficient IaC development practices:** Treating IaC
  differently from application code, especially by not using version control, diminishes
  developer experience and increases deployment risk. By not versioning IaC files, teams
  lose the ability to track changes over time, identify when specific changes were made,
  or correlate infrastructure changes with system behavior. Additionally, storing large,
  monolithic IaC files makes development and management of IaC more complex, as
  intertwining components make it challenging to identify specific sections and understand
  changes being made. Mitigate these challenges by segmenting IaC into modular units
  consistent with the system's architecture and maintain them within version control
  systems. Using general-purpose programming languages when developing IaC can further
  simplify managing IaC like other application code.
- **Monolithic network architectures:** Designing a network
  where different components are tightly coupled leads to reduced flexibility and
  increased complexity. This pattern can make troubleshooting and scaling particularly
  challenging, as changes in one component may inadvertently impact others. Instead,
  create a modular network design expressed through multiple, well-organized IaC files
  where components are loosely coupled and can be individually managed, maintained, and
  scaled.
