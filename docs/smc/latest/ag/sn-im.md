End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# AWS Systems Manager Incident Manager in ServiceNow

To allow the Connector to synchronize Incidents from AWS Systems Manager Incident Manager for a
specific Region, you must enable Incident Manager in that account and Region.

For more information, see [What is AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/what-is-incident-manager.md "../../../incident-manager/latest/userguide/what-is-incident-manager.md").

## Fields mapped from Incident Manager incident to ServiceNow Incident records

This table shows how AWS Incident Manager Incidents map to ServiceNow Incidents.

| AWS Incident Manager incident | ServiceNow Incident                    |
| ----------------------------- | -------------------------------------- |
| Title                         | short\_description                     |
| Summary                       | description                            |
| Incident ARN                  | x\_126749\_aws\_sc\_awsincidentarn     |
| AWS Account                   | x\_126749\_aws\_sc\_awsaccount         |
| AWS Region                    | x\_126749\_aws\_sc\_awsregion          |
| Status                        | x\_126749\_aws\_sc\_awsstatus          |
| Start time                    | x\_126749\_aws\_sc\_awscreationtime    |
| Resolved time                 | x\_126749\_aws\_sc\_awsresolvetime     |
| Updated time                  | x\_126749\_aws\_sc\_awslastupdatedtime |
| Incident Sync time            | x\_126749\_aws\_sc\_awslastsynctime    |
| AWS incident URL              | x\_126749\_aws\_sc\_awsincidenturl     |
| Impact                        | impact                                 |

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
| ------------------------- | ------------------- |
|                           | **Impact**          | **Urgency** | **Priority (Calculated)** |
| Critical                  | High                | High        | Critical (1)              |
| High                      | High                | High        | Critical (1)              |
| Medium                    | Medium              | High        | High (2)                  |
| Low                       | Low                 | High        | Moderate (3)              |
| No Impact                 | Low                 | High        | Moderate (3)              |
