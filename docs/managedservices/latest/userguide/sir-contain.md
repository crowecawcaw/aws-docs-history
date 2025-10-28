# Contain

AMS's approach to containment is partnership with you. You understand your business and the workload impacts that might occur
from containment activities, such as network isolation, IAM user or role de-provisioning, instance re-building, and so forth.

An essential part of containment is decision-making. For example, shut down a system, isolate a resource from the network, or turn off
access or end sessions. These decisions are easier to make if there are predetermined strategies and procedures to
contain the incident. AMS provides the containment strategy and then implements the solution after you have
considered the risk involved with implementing the containment actions.

There are different containment options depending on the resources under analysis. AMS expects multiple types of
containment to be simultaneously deployed during an incident investigation. Some of these examples include:

- Apply protection rules to block unauthorized traffic (Security group, NACL, WAF Rules, SCP rules, Deny listing,
  setting signature action to quarantine or block)
- Resource Isolation
- Network Isolation
- Disabling IAM users, roles and policies
- Modifying/Reducing IAM user, role privilege
- Terminating / Suspending / Deleting compute resources
- Restricting public access from affected resource
- Rotating access keys, API keys, and passwords
- Scrubbing disclosed credentials and sensitive information
  AMS encourages you to consider the type of containment strategies for each major incident type that is within their
  risk appetite, with criteria clearly documented to help with decision making in the event of an incident. Criteria to
  determine the appropriate strategy include:

- Potential damage to resources
- Preservation of evidence
- Service unavailability (for example, network connectivity, services provided to external parties)
- Time and resources needed to implement the strategy
- Effectiveness of the strategy (For example, partial containment, full containment)
- Permanence of the solution (For example, one-way door vs two-way door decisions)
- Duration of the solution (For example, emergency workaround to be removed in four hours, temporary workaround to be removed in
  two weeks, permanent solution).
- Apply security controls that you can turn on to lower the risk and allow time to define and implement a
  more effective containment.
  The speed of containment is critical, AMS advises a staged approach to achieve efficient and effective containment by
  strategizing short-term and long-term approaches.

Use this guide to consider your containment strategy that involves different techniques based on the resource type.

- Containment Strategy
  - Can AMS identify the scope of the security incident?
    - If yes, identify all the resources (users, systems, resources).
    - If no, investigate in parallel with executing the next step on identified resources.

  - Can the resource be isolated?
    - If yes, then proceed to isolate the affected resources.
    - If no, then work with system owners and managers to determine further actions necessary to contain the problem.

  - Are all affected resources isolated from non-affected resources?
    - If yes, then continue to the next step.
    - If no, then continue to isolate affected resources until short-term containment is accomplished to prevent the incident from
      escalating further.

- System Backup
  - Were backup copies of affected systems created for further analysis?
  - Are the forensic copies encrypted and stored in a secure location?
    - If yes, then continue to the next step.
    - If no, encrypt the forensic images, then store them in a secure location to prevent accidental usage, damage, and
      tampering.
