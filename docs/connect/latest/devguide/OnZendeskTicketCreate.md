

# OnZendeskTicketCreate
<a name="OnZendeskTicketCreate"></a>

## Type condition
<a name="type-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "question", "incident", "problem", "task"
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.Type"
+ Negate - true or false. If set to true, it means *If ticket type does not equal to the type specified in the Operands*.

## Priority condition
<a name="priority-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "low", "normal", "high", "urgent"
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.Priority"
+ Negate - true or false. If set to true, it means *If ticket priority does not equal to the priority specified in the Operands*.

## Status condition
<a name="status-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "open", "pending", "solved", "close", "hold"
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.Status"
+ Negate - true or false. If set to true, it means *If ticket status does not equal to the status specified in the Operands.*.

## RequesterId condition
<a name="requesterid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a requester id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.RequesterId"
+ Negate - true or false. If set to true, it means *If requester id does not equal to the requester id specified in the Operands.*.

## SubmitterId condition
<a name="submitterid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a submitter id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.SubmitterId"
+ Negate - true or false. If set to true, it means *If submitter id does not equal to the submitter id specified in the Operands.*.

## AssigneeId condition
<a name="assigneeid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an assignee id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.AssigneeId"
+ Negate - true or false. If set to true, it means *If assignee id does not equal to the assignee id specified in the Operands.*.

## OrganizationId condition
<a name="organizationid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an organization id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.OrganizationId"
+ Negate - true or false. If set to true, it means *If organization id does not equal to the organization id specified in the Operands.*.

## BrandId condition
<a name="brandid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a brand id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.BrandId"
+ Negate - true or false. If set to true, it means *If brand id does not equal to the brand id specified in the Operands*.

## FormId condition
<a name="formid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a form id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.FormId"
+ Negate - true or false. If set to true, it means *If form id does not equal to the form id specified in the Operands*.

## ExternalId condition
<a name="externalid-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an external id.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.ExternalId"
+ Negate - true or false. If set to true, it means *If external id does not equal to the external id specified in the Operands*.

## Channel condition
<a name="channel-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a channel string.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.Channel"
+ Negate - true or false. If set to true, it means *If channel value does not equal to the channel string specified in the Operands*.

## Tags condition
<a name="tags-condition"></a>

**Parameters**
+ Operator - "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a tag string.
+ ComparisonValue – "$.ThirdParty.Zendesk.TicketCreate.Tags"
+ Negate - true or false. If set to true, it means *If tag value does not equal to the tag string specified in the Operands*.