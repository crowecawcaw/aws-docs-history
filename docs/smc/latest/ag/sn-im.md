# AWS Systems Manager Incident Manager in ServiceNow

To allow the Connector to synchronize Incidents from AWS Systems Manager Incident Manager for a
specific Region, you must enable Incident Manager in that account and Region.

For more information, see [What is AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/what-is-incident-manager.md "../../../incident-manager/latest/userguide/what-is-incident-manager.md").

## Fields mapped from Incident Manager incident to ServiceNow Incident records

This table shows how AWS Incident Manager Incidents map to ServiceNow Incidents.

| AWS Incident Manager incident | ServiceNow Incident                |
| ----------------------------- | ---------------------------------- |
| Title                         | short_description                  |
| Summary                       | description                        |
| Incident ARN                  | x_126749_aws_sc_awsincidentarn     |
| AWS Account                   | x_126749_aws_sc_awsaccount         |
| AWS Region                    | x_126749_aws_sc_awsregion          |
| Status                        | x_126749_aws_sc_awsstatus          |
| Start time                    | x_126749_aws_sc_awscreationtime    |
| Resolved time                 | x_126749_aws_sc_awsresolvetime     |
| Updated time                  | x_126749_aws_sc_awslastupdatedtime |
| Incident Sync time            | x_126749_aws_sc_awslastsynctime    |
| AWS incident URL              | x_126749_aws_sc_awsincidenturl     |
| Impact                        | impact                             |

**Incident Status** is an integer in ServiceNow. We
map Incident Manager incident status values to ServiceNow status values.

| Incident Manager Incident Status | ServiceNow Incident Status |
| -------------------------------- | -------------------------- |
| Open                             | New                        |
| Resolved                         | Resolved                   |
| Resolved                         | Cancelled                  |

**Priority** - In ServiceNow Incident, you can’t set
the Priority field directly. The values of the **Impact** and **Urgency** fields calculate the
**Priority** field. When synchronizing from AWS,
we set the default priorities as below:

| Incident Manager Incident | ServiceNow Incident |
| ------------------------- | ------------------- | ----------- | ------------------------- |
|                           | **Impact**          | **Urgency** | **Priority (Calculated)** |
| Critical                  | High                | High        | Critical (1)              |
| High                      | High                | High        | Critical (1)              |
| Medium                    | Medium              | High        | High (2)                  |
| Low                       | Low                 | High        | Moderate (3)              |
| No Impact                 | Low                 | High        | Moderate (3)              |
