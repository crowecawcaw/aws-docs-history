# Mapping Zendesk objects to the

standard profile in Amazon Connect Customer Profiles

This topic lists which fields in Zendesk objects map to fields in the
standard profile in Customer Profiles.

## Zendesk-users object

Following is a list of all the fields in a Zendesk-users
object.

- id
- url
- external_id
- email
- active
- chat_only
- customer_role_id
- role_type
- details
- last_login_at
- locale
- locale_id
- moderator
- notes
- only_private_comments
- default_group_id
- phone
- shared_phone_number
- photo
- restricted_agent
- role
- shared
- tags
- signature
- suspended
- ticket_restriction
- time_zone
- two_factor_auth_enabled
- user_fields
- verified
- report_csv
- created_at
- updated_at

## Mapping Zendesk users to a

standard profile

A subset of the fields in the Zendesk-users object map to the standard
profile in Customer Profiles. The following table lists which fields can
be mapped from the Zendesk-users object to the standard profile.

| Zendesk-users source field | Standard profile target field |
| -------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                         | Attributes.ZendeskUserId      |
| external_id                | Attributes.ZendeskExternalId  |
| email                      | EmailAddress                  |
| phone                      | PhoneNumber                   | The Zendesk-users customer data from the Zendesk object is associated with a Amazon Connect customer profile using the following indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Standard Index Name        | Zendesk-user source field     |
| ---                        | ---                           |
| \_zendeskUserId            | Id                            |
| \_zendeskExternalId        | external_id                   | For example, you can use `_zendeskUserId` and `_zendeskExternalId` as a key name with the [SearchProfiles](../../../customerprofiles/latest/APIReference/API_SearchProfiles.md "../../../customerprofiles/latest/APIReference/API_SearchProfiles.md") API to find an Amazon Connect customer profile. You can find the Zendesk-users objects associated with a specific customer profile by using the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and `ObjectTypeName` set to `Zendesk-users`. |
