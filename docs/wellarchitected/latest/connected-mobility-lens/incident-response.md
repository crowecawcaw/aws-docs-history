# Incident response

| CMSEC_22: Does your team deploy a VSOC? If so, what are the required<br>capabilities of a VSOC? |
| ----------------------------------------------------------------------------------------------- |
|                                                                                                 |

A VSOC has become a compliance requirement for automotive
cybersecurity management systems very recently. An incident
may involve safety implications, making incident response a
critical component of a security program. A VSOC must contain
automotive specific playbooks that are relevant to your
business case, collaboration across IT SOC, cloud SOC, and
VSOC, continuous improvement and lessons learned. A VSOC must
have many of the detection mechanisms we described above
[refer to CM\_SECBP20 for detection] as well as providing
triage, containment, recovery, and lessons learned to your
monitoring and remediation program. A VSOC also requires
trained personnel that are capable of addressing different
vehicle alerts with varying complexity.

**[CMSEC\_BP22.1] Define VSOC capabilities and requirements, then
develop and test your VSOC incident response plan.**

To successfully respond to an incident, you must first define VSOC capabilities and
requirements. This aligns with compliance or risk-based security requirements. You then
prepare your incident response plan and runbooks that are referenced during a potential
security incident. The incident response plan contains several components that span across
an organization, and cover both business and technical steps. AWS provides [Automation runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md") which define the actions that Systems Manager performs on
your managed instances and other AWS resources when an automation runs. runbooks contain
one or more steps in sequential order. You can use runbooks for manual approvals or trigger
a workflow.

The VSOC should include security orchestration automation and response (SOAR) and
ticketing capability to provide timely responses and workflows that can prioritize and
address incidents. Customers can send findings to AWS Security Hub, which integrates with issue
tracking systems like [ServiceNow](../../../smc/latest/ag/sn-config-security-hub.md "../../../smc/latest/ag/sn-config-security-hub.md") and [Jira](../../../smc/latest/ag/jsmcloud-config-security-hub.md "../../../smc/latest/ag/jsmcloud-config-security-hub.md").
The incident response procedure must be consistent, accurate, and updated when necessary.
Running game days and tabletop exercises can provide insight about the ability to handle an
incident in a practice environment. Game days, also known as simulations or exercises, are
internal events that provide a structured opportunity to practice your incident management
plans and procedures during a realistic scenario.

**[CMSEC\_BP22.2] Train or outsource personnel to manage security
incidents at multiple layers of complexity.**

One of the major observed gaps is a lack of expertise in vehicle incident response.
You must determine if your organization has the resources, processes, and skills in place to
address vehicle incidents and events at multiple tiers based on the severity and complexity
of the incident. Organizations might shift responsibility to an AWS Partner or vendor to manage
their VSOC and personnel to identify, prepare, analyze, contain, and recover from a vehicle
security incident. Argus Cyber Security provides consultive and managed VSOC services that
can help address those security needs.

| CMSEC_23: How do you contain, recover, and learn from incidents that can span<br>vehicles, backend systems, APIs, IT, cloud, AWS Partners, and supplier<br>resources? |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                       |

Organizations must be able effectively respond to an incident
and notify the organization of severity and scope. This
involves processes to triage and prioritize, response and
recovery activities, and properly monitoring and closing an
incident after confirming the incident has been fully
resolved. Organizations will then continuously improve by
going through lessons learned and using the process to inform
the next set of service improvements after the incident has
been mitigated and resolved.

**[CMSEC\_BP23.1] Mitigate and respond to potential incidents by
creating and testing policies, procedures, and playbooks**

During a potential vehicle security issue, it is necessary to
attempt to automate and respond to an incident promptly. By
using runbooks, you can automate several workflow tasks like
notifying different stakeholders and creating a ticket. You
must be able to contain the scope of the issue. Depending on
the finding, you can issue APIs to AWS IoT Core where you can
automate changing a certificate status based on the incident.
If a vehicle is compromised, you can build a workflow that
will inactivate or revoke a certificate and block
communications to AWS IoT Core while you investigate the
incident. You should follow your incident response procedure
to then recover the vehicle back to a non-compromised state
which can vary in complexity depending on the incident.
