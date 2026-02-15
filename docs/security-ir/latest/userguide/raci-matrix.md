# RACI Matrix

The following RACI matrix defines roles and responsibilities across the Security Incident Response implementation process. RACI stands for Responsible (R), Accountable (A), Consulted (C), and Informed (I).

| Activity                                                                                                                                             | Customer | AWS Account Team | SIR Team |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | -------- |
| **Pre-Onboarding**                                                                                                                                   |
| Identify Key Stakeholders                                                                                                                            | R        |                  | I        |
| Validate Finding Sources                                                                                                                             | R        | C                | I        |
| [3rd Party EDR integration] Security Hub CSPM                                                                                                        | R        | C                | I        |
| GuardDuty Validation/Health Check                                                                                                                    | C        | R                | I        |
| Determine Account Scope                                                                                                                              | R        |                  |          |
| Establish Escalation Protocols                                                                                                                       | R        | I                | C        |
| Enable AWS Organizations                                                                                                                             | R        | C                |          |
| Associate accounts with AWS Organizations                                                                                                            | R        | I                |          |
| Select Delegated Administrator / Security Tooling Account                                                                                            | R        | I                |          |
| **Onboarding**                                                                                                                                       |
| Setup membership details                                                                                                                             | R        | I                |          |
| Walkthrough (Setup proactive response and alert triaging workflows; Deploy service-linked role to management account; Authorize containment actions) | R        | C                | I        |
| **Post-Deployment Configuration**                                                                                                                    |
| Review operational integration capabilities                                                                                                          | R        | C                | I        |
| Submit Security Incident Response Reactive Cases                                                                                                     | R        |                  |          |
| Configure Amazon EventBridge integrations                                                                                                            | R        | C                | C        |
| Connect 3rd party tooling (Jira, ServiceNow, PagerDuty, Teams, etc.)                                                                                 | R        | I                | C        |
| Service deep dive and demo                                                                                                                           | A        | R                | C        |

**RACI Definitions:**

- **Responsible (R)** - The party who performs the work to complete the task
- **Accountable (A)** - The party ultimately answerable for the correct completion of the task
- **Consulted (C)** - The party whose opinions are sought and with whom there is two-way communication
- **Informed (I)** - The party who is kept up-to-date on progress and with whom there is one-way communication
