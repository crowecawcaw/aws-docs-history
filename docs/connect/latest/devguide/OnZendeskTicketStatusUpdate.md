# OnZendeskTicketStatusUpdate

## Type condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  one of "question", "incident", "problem", "task"
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Type"
- Negate - true or false. If set to true, it means _If ticket
  type does not equal to the type specified in the
  Operands_.

## Priority condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  one of "low", "normal", "high", "urgent"
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Priority"
- Negate - true or false. If set to true, it means _If ticket
  priority does not equal to the priority specified in the
  Operands_.

## Status condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is
  one of "open", "pending", "solved", "close", "hold"
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Status"
- Negate - true or false. If set to true, it means _If ticket
  status does not equal to the status specified in the
  Operands._.

## RequesterId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is a
  requester id.
- ComparisonValue –
  "$.ThirdParty.Zendesk.StatusUpdate.RequesterId"
- Negate - true or false. If set to true, it means _If
  requester id does not equal to the requester id specified in the
  Operands._.

## SubmitterId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is a
  submitter id.
- ComparisonValue –
  "$.ThirdParty.Zendesk.StatusUpdate.SubmitterId"
- Negate - true or false. If set to true, it means _If
  submitter id does not equal to the submitter id specified in the
  Operands._.

## AssigneeId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is an
  assignee id.
- ComparisonValue –
  "$.ThirdParty.Zendesk.StatusUpdate.AssigneeId"
- Negate - true or false. If set to true, it means _If assignee
  id does not equal to the assignee id specified in the
  Operands._.

## OrganizationId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is an
  organization id.
- ComparisonValue –
  "$.ThirdParty.Zendesk.StatusUpdate.OrganizationId"
- Negate - true or false. If set to true, it means _If
  organization id does not equal to the organization id specified in
  the Operands._.

## BrandId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is a
  brand id.
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.BrandId"
- Negate - true or false. If set to true, it means _If brand id
  does not equal to the brand id specified in the
  Operands_.

## FormId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is a
  form id.
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.FormId"
- Negate - true or false. If set to true, it means _If form id
  does not equal to the form id specified in the
  Operands_.

## ExternalId condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is an
  external id.
- ComparisonValue –
  "$.ThirdParty.Zendesk.StatusUpdate.ExternalId"
- Negate - true or false. If set to true, it means _If external
  id does not equal to the external id specified in the
  Operands_.

## Channel condition

###### Parameters

- Operator - "EQUALS"
- Operands – An array of string, array length can only be 1. Value is a
  channel string.
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Channel"
- Negate - true or false. If set to true, it means _If channel
  value does not equal to the channel string specified in the
  Operands_.

## Tags condition

###### Parameters

- Operator - "CONTAINS"
- Operands – An array of string, array length can only be 1. Value is a
  tag string.
- ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Tags"
- Negate - true or false. If set to true, it means _If tag
  value does not equal to the tag string specified in the
  Operands_.
