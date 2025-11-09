# Mapping Zendesk objects to

the standard case in Amazon Connect Customer Profiles

This topic lists which fields in Zendesk objects map to fields in the
standard case in Customer Profiles.

## Zendesk-tickets object

Following is a list of all the fields in a Zendesk-tickets
object.

- id
- url
- type
- subject
- raw_subject
- description
- priority
- status
- recipient
- requester_id
- submitter_id
- assignee_id
- organization_id
- group_id
- collaborator_ids
- email_cc_ids
- follower_ids
- forum_topic_id
- problem_id
- has_incidents
- due_at
- tags
- via.channel
- custom_fields
- satisfaction_rating
- sharing_agreement_ids
- followup_ids
- ticket_form_id
- brand_id
- allow_channelback
- allow_attachments
- is_public
- created_at
- updated_at

## Mapping

Zendesk-tickets object to a standard case

A subset of the fields in the Zendesk-tickets object map to the
standard case in Customer Profiles. The following table lists which
fields can be mapped from the Zendesk-tickets object to the standard
case.

| Zendesk-tickets source field | Standard case target field |
| ---------------------------- | -------------------------- |
| requester_id                 | Attributes.ZendeskUserId   |
| id                           | Attributes.ZendeskTicketId |
| subject                      | Title                      |
| description                  | Summary                    |
| status                       | Status                     |
| requester_id                 | CreatedBy                  |
| created_at                   | CreatedDate                |
| updated_at                   | UpdatedDate                |

The Zendesk-tickets customer data from the Zendesk object is associated
with a Amazon Connect standard case using the following indexes.

| Standard Index Name | Zendesk-tickets source field |
| ------------------- | ---------------------------- |
| \_zendeskUserId     | requester_id                 |
| \_zendeskTicketId   | id                           |

For example, you can use `_zendeskUserId` and
`_zendeskTicketId` as an `ObjectFilter.KeyName`
with the [ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API to find a standard case. You can find
the Zendesk-tickets objects associated with a specific profile by using the
[ListProfileObjects](../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md "../../../customerprofiles/latest/APIReference/API_ListProfileObjects.md") API with the `ProfileId` and
`ObjectTypeName` set to `Zendesk-tickets`.
