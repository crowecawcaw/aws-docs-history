

# Reading from PagerDuty entities

**Prerequisites**

A PagerDuty object you want to read from. See the supported entities table below for the available entities.

The `alerts` and `incident_notes` entities belong to an incident, and `team_members` belongs to a team. Use `alerts/{{incidentId}}`, `incident_notes/{{incidentId}}`, or `team_members/{{teamId}}`. AWS Glue discovers the available incident and team IDs for your connection.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| incidents | Yes | Yes | Yes | No | No | 
| log\_entries | Yes | Yes | Yes | No | No | 
| services | No | Yes | Yes | No | No | 
| users | No | Yes | Yes | No | No | 
| teams | No | Yes | Yes | No | No | 
| escalation\_policies | No | Yes | Yes | No | No | 
| schedules | No | Yes | Yes | No | No | 
| oncalls | Yes | Yes | Yes | No | No | 
| maintenance\_windows | No | Yes | Yes | No | No | 
| change\_events | Yes | Yes | Yes | No | No | 
| audit\_records | Yes | Yes | Yes | No | No | 
| priorities | No | No | Yes | No | No | 
| vendors | No | Yes | Yes | No | No | 
| incident\_types | No | No | Yes | No | No | 
| tags | No | Yes | Yes | No | No | 
| alerts | No | Yes | Yes | No | No | 
| team\_members | No | Yes | Yes | No | No | 
| extensions | No | Yes | Yes | No | No | 
| incident\_notes | No | No | Yes | No | No | 
| business\_services | No | Yes | Yes | No | No | 

**Example – Reading from a PagerDuty entity**  
The following example reads from the `incidents` entity. Replace {{connectionName}} with the name of your PagerDuty connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="pagerduty",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "incidents"
    }
)
```