# OPS10-BP04 Define escalation paths

Establish clear escalation paths within your incident response protocols to facilitate timely and effective action. This includes specifying prompts for escalation, detailing the escalation process, and pre-approving actions to expedite decision-making and reduce mean time to resolution (MTTR).

**Desired outcome:** A structured and efficient process that escalates incidents to the appropriate personnel, minimizing response times and impact.

**Common anti-patterns:**

- Lack of clarity on recovery procedures leads to makeshift responses during critical incidents.
- Absence of defined permissions and ownership results in delays when urgent action is needed.
- Stakeholders and customers are not informed in line with expectations.
- Important decisions are delayed.

**Benefits of establishing this best
practice:**

- Streamlined incident response through predefined escalation procedures.
- Reduced downtime with pre-approved actions and clear ownership.
- Improved resource allocation and support-level adjustments according to incident severity.
- Improved communication to stakeholders and customers.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Properly defined escalation paths are crucial for rapid incident response. AWS Systems Manager Incident Manager supports the setup of structured escalation plans and on-call schedules, which alert the right personnel so that they are ready to act when incidents occur.

### Implementation steps

1. **Set up escalation prompts:** Set up [CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md#alarms-and-actions") to create an incident in [AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md").
2. **Set up on-call schedules:** Create [on-call schedules](../../../incident-manager/latest/userguide/incident-manager-on-call-schedule-create.md "../../../incident-manager/latest/userguide/incident-manager-on-call-schedule-create.md") in Incident Manager that align with your escalation paths. Equip on-call personnel with the necessary permissions and tools to act swiftly.
3. **Detail escalation procedures:**
   - Determine specific conditions under which an incident should be escalated.
   - Create [escalation plans](../../../incident-manager/latest/userguide/escalation.md "../../../incident-manager/latest/userguide/escalation.md") in Incident Manager.
   - Escalation channels should consist of a contact or an on-call schedule.
   - Define the roles and responsibilities of the team at each escalation level.

4. **Pre-approve mitigation actions:** Collaborate with decision-makers to pre-approve actions for anticipated scenarios. Use [Systems Manager Automation runbooks](../../../incident-manager/latest/userguide/tutorials-runbooks.md "../../../incident-manager/latest/userguide/tutorials-runbooks.md") integrated with Incident Manager to speed up incident resolution.
5. **Specify ownership:** Clearly identify internal owners for each step of the escalation path.
6. **Detail third-party escalations:**
   - Document third-party service-level agreements (SLAs), and align them with internal goals.
   - Set clear protocols for vendor communication during incidents.
   - Integrate vendor contacts into incident management tools for direct access.
   - Conduct regular drills that include third-party response scenarios.
   - Keep vendor escalation information well-documented and easily accessible.

7. **Train and rehearse escalation plans:** Train your team on the escalation process and conduct regular incident response drills or game days. Enterprise Support customers can request an [Incident Management Workshop](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/ "https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/").
8. **Continue to improve:** Review the effectiveness of your escalation paths regularly. Update your processes based on lessons learned from incident post-mortems and continuous feedback.

**Level of effort for the implementation plan:** Moderate

## Resources

**Related best practices:**

- [OPS08-BP04 Create actionable alerts](ops_workload_observability_create_alerts.md "ops_workload_observability_create_alerts.md")
- [OPS10-BP02 Have a process per alert](ops_event_response_process_per_alert.md "ops_event_response_process_per_alert.md")
- [OPS11-BP02 Perform post-incident analysis](ops_evolve_ops_perform_rca_process.md "ops_evolve_ops_perform_rca_process.md")

**Related documents:**

- [AWS Systems Manager Incident Manager Escalation Plans](../../../incident-manager/latest/userguide/escalation.md "../../../incident-manager/latest/userguide/escalation.md")
- [Working with on-call schedules in Incident Manager](../../../incident-manager/latest/userguide/incident-manager-on-call-schedule.md "../../../incident-manager/latest/userguide/incident-manager-on-call-schedule.md")
- [Creating and Managing Runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md")
- [Temporary elevated access management with AWS IAM Identity Center](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/ "https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/")
- [Atlassian - Escalation policies for effective incident management](https://www.atlassian.com/incident-management/on-call/escalation-policies "https://www.atlassian.com/incident-management/on-call/escalation-policies")
