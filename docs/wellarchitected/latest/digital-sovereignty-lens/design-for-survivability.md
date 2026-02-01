# Design for survivability

Organizations exposed to geopolitical risks and large-scale infrastructure disruptions
want to be able to maintain business continuity by deploying their digital infrastructure to
other regions, countries or jurisdictions.

**Key challenges:**

- In large organizations, applications have specific Recovery Time Objective (RTO) and
  Recovery Point Objective (RPO) targets that may conflict with broader business continuity
  goals. Technology teams and business stakeholders frequently develop separate definitions
  of _minimum restorable service_ and activation timelines, creating
  disconnected recovery plans. This misalignment becomes particularly problematic when
  multiple technology systems and engineering teams support a single business function.
- Restoring workloads and entire systems from backups may take hours or even days. This
  may require several manual steps and many post-restoration validations before the system
  can serve live traffic again. Many systems are not designed to be restored using automated
  scripts. This is especially true for legacy non-idempotent systems that rely on remote
  procedure call (RPC) style synchronous interactions. When in-flight transactions fail,
  engineers must perform manual rollbacks and complex data cleanups to restore system
  integrity.
- Organizations neglect full disaster recovery (DR) testing due to its complexity and
  resource demands. DR testing requires cross-team coordination, third-party service
  integration, data synchronization, and legacy systems availability. Even when DR tests are
  conducted and teams log discovered issues in a risk register, they may not be prioritized
  and addressed. This can lead to fragile systems and hidden vulnerabilities.

**Key practices:**

Consider the following key practices to meet the challenges outlined above.

- **Align with business continuity goals:** Adopt a defined
  disaster recovery strategy, aligning with organizational business continuity goals. Define
  what a minimum restorable service is. Define timelines for full service restoration.
- **Design systems with DR as a stated goal:** Understand
  system dependencies and fault isolation boundaries, and document your recovery path. Test
  for disaster recovery. Prioritize and test critical paths of recovery. Record outcomes of
  DR testing. Use root cause analysis to identify causes of failure and develop mitigations.
  Develop a roadmap to sunset legacy systems that pose risks to your recovery objectives.
- **Prepare for DR:** Identify key stakeholders. In addition to
  stakeholders involved in performing the actual recovery from a disaster (such as
  engineers, technical support, and executives), you should also have a list of key internal
  stakeholders, a list of critical vendors, third-party suppliers, and even key customers
  who might be most affected.
- **Report irregularities:** Incorporate regulatory
  requirements for incident response, and breach notification into your disaster recovery
  and business continuity plans.
- **Plan for contingencies:** Develop business continuity
  strategies for system failures. Implement offline and semi-offline operation modes to
  maintain critical functions during severe disruptions like undersea cable outages. Create
  procedures to restore workloads after offline periods of operation.
