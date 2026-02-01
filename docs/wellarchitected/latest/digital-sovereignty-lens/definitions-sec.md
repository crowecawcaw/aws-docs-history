# Definitions

The following are security-specific definitions.

- **Artificial intelligence/machine learning (AI/ML):**
  Technologies for automated analysis and decision-making. In sovereign security contexts,
  AI/ML can automate threat detection, and anomaly identification. However, organizations
  must consider data sovereignty implications when using AI services, including where
  training data is processed, where models are hosted, and whether inference operations
  remain within approved jurisdictions.
- **Application performance management (APM):** Tools and
  practices for monitoring application performance, availability, and user experience. For
  sovereign workloads, APM solutions must operate within approved regions, store telemetry
  data according to residency requirements, and provide visibility into cross-region data
  flows that might violate sovereignty constraints.
- **Automated reasoning:** Mathematical analysis of security
  configurations to prove properties about access policies and network reachability. Tools
  like AWS IAM Access Analyzer use automated reasoning to verify that IAM policies grant only
  intended access and to identify potential unintended information exposure. Critical for
  sovereign workloads to mathematically prove that data access policies enforce
  jurisdictional boundaries.
- **Cyber incident response team (CIRT):** Dedicated team
  responsible for handling security incidents, including detection, analysis, containment,
  eradication, and recovery. For sovereign workloads, CIRT members must be located in
  approved jurisdictions, have appropriate security clearances, and follow incident response
  procedures that maintain data residency during forensic investigation and remediation.
- **Cyber threat intelligence (CTI):** Information about
  potential cybersecurity threats, including threat actor tactics, vulnerabilities, and
  indicators of compromise. Enables organizations to proactively defend against emerging
  threats. For sovereign environments, CTI feeds must be relevant to the region for them to
  be valuable.
- **Indicator of compromise (IoC):** Forensic evidence that a
  security breach has occurred or is occurring. Examples include suspicious IP addresses,
  malware signatures, unusual file hashes, or anomalous user behavior patterns. In sovereign
  contexts, IoC detection and analysis must occur within approved regions, and sharing IoCs
  with external threat intelligence solutions must comply with data export restrictions.
- **Just-in-time access:** Security practice of granting
  temporary, time-limited access only when needed, rather than permanent standing
  privileges. Reduces attack surface by minimizing the window of opportunity for credential
  compromise. For sovereign workloads, JIT access systems must verify that requesting users
  are in approved locations and maintain audit trails of all access grants and usage.
- **Large language model (LLM):** AI model trained on vast
  amounts of text data, capable of understanding and generating human-like text. Used in
  security for analyzing logs, generating security policies, and assisting with threat
  analysis. Organizations must consider where LLM processing occurs and whether prompts
  containing sensitive data remain within sovereign boundaries.
- **Mean Time to Detect (MTTD):** Average time required to
  identify a security incident from when it first occurs. Critical metric for security
  operations effectiveness. Sovereign constraints may impact MTTD if detection tools must
  operate within specific regions or if security analysts must be located in approved
  jurisdictions, potentially limiting 24/7 coverage.
- **Network reachability:** The ability to establish network
  connections between resources, determined by security groups, network ACLs, routing
  tables, and firewall rules. For sovereign architectures, network reachability analysis
  verifies that resources in approved regions cannot be accessed from unauthorized locations
  and that data cannot flow across jurisdictional boundaries.
- **Policy validation:** Process of verifying that access
  policies block unintended access and enforce intended security boundaries. Uses techniques
  like automated reasoning, policy simulation, and access analysis. Essential for sovereign
  workloads to prove that IAM policies, resource policies, and SCPs enforce data residency
  and jurisdictional access requirements.
- **Root cause analysis (RCA):** Systematic investigation to
  identify the underlying causes of security incidents or operational failures. Goes beyond
  symptoms to find root issues. For sovereign workloads, RCA must be conducted by authorized
  personnel in approved locations, and forensic data must remain within jurisdictional
  boundaries throughout the investigation.
- **Session recording:** Capturing and storing all activities
  performed by operators during privileged access sessions, including commands run, files
  accessed, and configuration changes made. Provides audit trail for compliance and forensic
  investigation. For sovereign environments, session recordings must be stored in approved
  regions and protected with appropriate encryption and access controls.
- **Security information and event management (SIEM):**
  Centralized system for collecting, aggregating, analyzing, and correlating security logs
  and events from across the infrastructure. Provides real-time threat detection and
  compliance reporting. For sovereign workloads, SIEM infrastructure must operate within
  approved regions, and log data must not be transmitted outside jurisdictional boundaries
  for analysis.
- **Threat modeling:** Systematic approach to identifying
  security threats by analyzing system architecture, data flows, trust boundaries, and
  potential attack vectors. Assists in prioritizing security controls based on risk. For
  sovereign architectures, threat modeling must consider jurisdiction-specific threats such
  as foreign government access requests, cross-border data transfer risks, and geopolitical
  factors.
- **Tactics, techniques, and procedures (TTP):** Patterns of
  activities and methods used by threat actors to compromise systems and achieve their
  objectives. Understanding TTPs allows organizations to detect and defend against specific
  threat groups. Sovereign organizations must consider TTPs specific to nation-state actors
  and threats targeting regulated industries in their jurisdiction.
- **Tabletop exercise (TTX):** Simulated incident response
  scenario where team members discuss their roles and responses to a hypothetical security
  incident without actually performing the actions. Used to test incident response plans and
  identify gaps. For sovereign workloads, TTX scenarios should include jurisdiction-specific
  incidents like data sovereignty violations or unauthorized cross-border access.
- **User and entity behavior analytics (UEBA):** Technology
  that uses machine learning to establish baseline behavior patterns for users and entities
  (such as applications or devices), then detects anomalies that may indicate compromised
  accounts or insider threats. For sovereign environments, UEBA systems must process
  behavioral data within approved regions and alert on activities that violate
  jurisdictional access policies.
