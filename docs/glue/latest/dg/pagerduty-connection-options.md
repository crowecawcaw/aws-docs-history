

# PagerDuty connection options

The following are connection options for PagerDuty:
+ `ENTITY_NAME` – (Required) Used for Read. The entity path of the PagerDuty object to read. Use the nested forms described in [Reading from PagerDuty entities](pagerduty-reading-from-entities.md) for `alerts`, `incident_notes`, and `team_members`.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate in Spark SQL format.

PagerDuty supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| audit\_records | execution\_time | greater than or equal to, less than or equal to, and between | 
| change\_events | timestamp | greater than or equal to, less than or equal to, and between | 
| incidents | status | equals only | 
| incidents | created\_at | greater than or equal to, less than or equal to, and between | 
| log\_entries | created\_at | greater than or equal to, less than or equal to, and between | 
| oncalls | start | greater than or equal to, less than or equal to, and between | 

AWS Glue applies filters on any other PagerDuty entity after it reads records, through the Spark DataFrame filters.