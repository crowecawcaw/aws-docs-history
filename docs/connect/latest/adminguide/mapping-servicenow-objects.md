# Mapping ServiceNow objects to

the standard profile object in Amazon Connect Customer Profiles

This topic lists which fields in ServiceNow objects map to fields in the
standard profile object in Amazon Connect Customer Profiles.

## Servicenow-sys_user

object

Following is a list of all the fields in a Servicenow-sys_user
object

- sys_id
- active
- building
- calendar_integration
- city
- company
- cost_center
- country
- date_format
- default_perspective
- department
- edu_status
- email
- employee_number
- enable_multifactor_authn
- failed_attempts
- first_name
- gender
- home_phone
- internal_integration_user
- introduction
- last_login
- last_login_device
- last_login_time
- last_name
- last_password
- ldap_server
- location
- locked_out
- manager
- middle_name
- mobile_phone
- name
- notification
- password_needs_reset
- phone
- photo
- preferred_language
- roles
- schedule
- source
- state
- street
- sys_class_name
- sys_created_by
- sys_created_on
- sys_domain.link
- sys_domain.value
- sys_domain_path
- sys_id
- sys_mod_count
- sys_updated_by
- sys_udpated_on
- time_format
- time_zone
- title
- user_name
- user_password
- web_service_access_only
- zip

## Mapping

Servicenow-sys_users to a standard profile object

A subset of the fields in the Servicenow-sys_users object map to the
standard profile object in Customer Profiles.

The following table lists which fields can be mapped from the
Servicenow-sys_users object to the standard profile.

| Servicenow-sys_users source field | Customer profiles target field |
| --------------------------------- | ------------------------------ |
| sys_id                            | Attributes.ServiceNowSystemId  |
| first_name                        | FirstName                      |
| last_name                         | LastName                       |
| middle_name                       | MiddleName                     |
| gender                            | Gender                         |
| email                             | EmailAddress                   |
| phone                             | PhoneNumber                    |
| home_phone                        | HomePhoneNumber                |
| mobile_phone                      | MobilePhoneNumber              |
| street                            | Address.Address1               |
| city                              | Address.City                   |
| state                             | Address.State                  |
| country                           | Address.Country                |
| zip                               | Address.PostalCode             |

The Servicenow-sys_user customer data from Servicenow object is
associated with an Amazon Connect customer profile using the indexes in the
following table.

| Standard Index Name  | Servicenow-sys_user source field |
| -------------------- | -------------------------------- |
| \_serviceNowSystemId | sys_id                           |

For example, you can use `_serviceNowSystemId` and
`_serviceNowIncidentId` as a key name with the [SearchProfiles](../../../customerprofiles/latest/APIReference/API_SearchProfiles.md "../../../customerprofiles/latest/APIReference/API_SearchProfiles.md") API to find an Amazon Connect customer profile. You
can find the Servicenow-sys_user objects associated with a specific
profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and
`ObjectTypeName` set to
`Servicenow-sys_user`.
