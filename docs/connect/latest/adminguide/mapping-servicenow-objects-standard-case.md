# Mapping

ServiceNow objects to the standard case in Amazon Connect Customer Profiles

This topic lists which fields in ServiceNow objects map to fields in the
standard case in Amazon Connect Customer Profiles.

## Servicenow-task object

Following is list of all the fields in a Servicenow-task object.

- sys_id
- active
- activity_due
- additional_assignee_list
- approval
- approval_history
- approval_set
- assigned_to
- assignment_group
- business_duration
- business_service
- calendar_duration
- closed_at
- closed_by
- cmdb_ci.display_value
- cmdb_ci.link
- comments
- comments_and_work_notes
- company
- contact_type
- contract
- correlation_display
- active
- correlation_id
- delivery_plan
- delivery_task
- description
- due_date
- escalation
- expected_start
- follow_up
- group_list
- impact
- knowledge
- location
- made_sla
- number
- opened_at
- opened_by.display_value
- order
- parent
- priority
- reassignment_count
- service_offering
- short_description
- sla_due
- state
- sys_class_name
- sys_created_by
- sys_created_on
- active
- sys_domain.global
- sys_domain.link
- sys_domain_path
- sys_mod_count
- sys_updated_by
- sys_updated_on
- time_worked
- upon_approval
- upon_reject
- urgency
- user_input
- watch_list
- work_end
- work_notes
- work_notes_list
- work_start

## Mapping Servicenow-task

to a standard case

A subset of the fields in the Servicenow-task object map to the
standard case in Customer Profiles.

The following table lists which fields can be mapped from the
Servicenow-task object to the standard case.

| Servicenow-task source field     | Standard case target field        |
| -------------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sys_id                           | Attributes.ServiceNowTaskId       |
| opened_by.link                   | Attributes.ServiceNowSystemUserId |
| short_description                | Title                             |
| description                      | Summary                           |
| status                           | Status                            |
| sys_created_by                   | CreatedBy                         |
| sys_created_on                   | CreatedDate                       |
| sys_updated_on                   | UpdatedDate                       | The Servicenow-task customer data from Servicenow is associated with an Amazon Connect standard case using the indexes in the following table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Standard Index Name              | Servicenow-task source field      |
| ---                              | ---                               |
| \_serviceNowTaskId               | sys_id                            |
| \_serviceNowSystemId             | open_by.link                      | For example, you can use `_serviceNowTaskId` and `_serviceNowSystemId` as an `ObjectFilter.KeyName` with the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard case. You can find the Servicenow-task objects associated with a specific profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and `ObjectTypeName` set to `Servicenow-task`. ## Servicenow-incident object Following is a list of all the fields in a Servicenow-incident object. <br>• sys_id <br>• business_stc <br>• calendar_stc <br>• caller_id.link <br>• caller_id.value <br>• category <br>• caused_by <br>• child_incidents <br>• close_code <br>• hold_reason <br>• incident_state <br>• notify <br>• parent_incident <br>• problem_id <br>• reopened_by <br>• reopened_time <br>• reopen_count <br>• resolved_at <br>• resolved_by.link <br>• resolved_by.value <br>• rfc <br>• severity <br>• subcategory ## Mapping Servicenow-incident to a standard case A subset of the fields in the Servicenow-incident object map to the standard case in Customer Profiles. The following table lists which fields can be mapped from the Servicenow-incident object to the standard case. |
| Servicenow-Incident source field | Standard case target field        |
| ---                              | ---                               |
| sys_id                           | Attributes_ServiceNowIncidentId   |
| caller_id.link                   | Attributes_ServiceNowSystemUserId |
| incident_status                  | Status                            |
| caller_id.link                   | CreatedBy                         |
| resolved_at                      | ClosedDate                        |
| category                         | Reason                            | The Servicenow-incident customer data from the Servicenow object is associated with an Amazon Connect standard case using the indexes in the following table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Standard Index Name              | Servicenow source field           |
| ---                              | ---                               |
| \_serviceNowIncidentId           | sys_id                            |
| \_serviceNowSystemId             | caller_id.link                    | For example, you can use `_serviceNowIncidentId` and `_serviceNowSystemId` as a ObjectFilter.KeyName with the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard case. You can find the Servicenow-incident objects associated with a specific profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and `ObjectTypeName` set to `Servicenow-incident`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
