# Validating AWS Security Hub integration in

ServiceNow

This section describes how to validate AWS Security Hub integration in ServiceNow.

###### To view Findings from AWS Security Hub

To view AWS Security Hub Findings, you must have the role, **x_126749_aws_sc.finding_manager**, from the Connector scope app.

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulfiller view (standard user interface view).
2. In the navigator, enter `AWS Service
Management`.
3. Choose **AWS Security Hub**.
4. Choose **Findings** to show a list of all synced
   Findings.
5. Choose a Finding to open the record.
6. The **Incident and Problem** fields show the
   Incident and Problem related to the Finding if these exist.
7. Choose the ⓘ symbol to the right of the field to preview the Incident or
   Problem.
8. Choose **Open Record** on the preview form to
   open the Incident or Problem.
9. If the Connector does not automatically create a ServiceNow Incident or
   Problem when a new Finding syncs, choose the link at the bottom of the form to
   create one manually.
   This table shows how fields map from ServiceNow Findings records to ServiceNow as
   Incident or Problem records.

| Finding                                                             | Incident          | Problem           |
| ------------------------------------------------------------------- | ----------------- | ----------------- |
| Created at                                                          | Opened at         | Opened at         |
| Company Name                                                        | Company           | Company           |
| Description                                                         | Description       | Description       |
| Criticality                                                         | Impact            | Impact            |
| Severity                                                            | Urgency           | Urgency           |
| Hardcoded to _software_                                             | Category          | Category          |
| Id of record in _cmdb_ci_service_<br>with name **AWS Security Hub** | Business service  | Business service  |
| Description                                                         | Short description | Short description |
| Reference to related Problem if it exists                           | problem_id        | n/a               |

This table shows how fields synchronize between AWS Security Findings and ServiceNow
Incidents or Problems.

| AWS Security Hub value | ServiceNow Incident | ServiceNow Problem |
| ---------------------- | ------------------- | ------------------ |
| Severity Label         | Urgency             | Urgency            |
| Criticality            | Impact              | Impact             |

**Fields synchronized between AWS Security Findings, Incidents,
and Problems in ServiceNow**

- Finding severity label → Problem/Incident urgency
  - INFORMATIONAL or LOW → LOW
  - MEDIUM → MEDIUM
  - HIGH or CRITICAL → HIGH

- Finding criticality → Problem/Incident impact

      + 0 - 29 → LOW
      + 30 - 69 → MEDIUM
      + 70 - 100 → HIGH

  **Fields synchronized from Findings to AWS Security Hub**

- Severity (Label and Normalized)
- WorkflowStatus
