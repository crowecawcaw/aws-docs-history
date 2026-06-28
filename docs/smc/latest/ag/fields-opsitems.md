End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Fields mapped from OpsCenter OpsItem records to ServiceNow Incident records

This table shows how AWS OpsItems map to ServiceNow Incidents.

| AWS Ops Center   | ServiceNow Incident |
| ---------------- | ------------------- |
| Title            | short\_description  |
| Description      | description         |
| CreatedTime      | opened\_at          |
| Status           | incident\_state     |
| Severity         | impact/urgency      |
| Priority         | priority            |
| CreatedBy        | Not synced          |
| LastModifiedTime | Not synced          |
| LastModifiedBy   | Not synced          |
| Source           | Not synced          |
| OpsItemId        | Not synced          |
| OperationalData  | Not synced          |
| Category         | Software            |

**Incident Status** is an integer in ServiceNow. We
map OpsItem status values to values.

| ServiceNow Incident Status | OpsCenter Status |
| -------------------------- | ---------------- |
| New (primary)              | Open             |
| On Hold                    | Open             |
| In Progress                | In Progress      |
| Resolved (primary)         | Resolved         |
| Closed                     | Resolved         |
| Cancelled                  | Resolved         |

In this type of subjective mapping, we only change the target value if it is
incompatible. An example of subjective mapping would be if _New_ and _On Hold_ in ServiceNow
both map to _Open_ in AWS. An
example of an incompatible target would be if the Incident is _On Hold_, while we're synchronizing from AWS an OpsItem that is _Open_, and we
don't change _On Hold_.

**Priority** - In Incident, you can’t set the
Priority field directly. The values of the **Impact**
and **Urgency** fields calculate the **Priority** field. When synchronizing from AWS, we set by default the fields shown in the table below:

| OpsItem Priority | ServiceNow Incident |
| ---------------- | ------------------- |
|                  | **Impact**          | **Urgency** | **Priority (Calculated)** |
| 1                | High                | High        | Critical (1)              |
| 2                | Medium              | High        | High (2)                  |
| 3                | Medium              | Medium      | Moderate (3)              |
| 4                | Low                 | Medium      | Low (4)                   |
| 5                | Low                 | Low         | Planning (5)              |

You can find these mappings in a ServiceNow table _Priority
Data Lookup_. While we can use this table to find the required values
of **Impact** and **Urgency**, note that you can customize the mappings and also define
new priority values. Additionally, you might want a specific priority in AWS to map to an entirely different priority in an Incident or Problem.
