

# OnZendeskTicketStatusUpdate
<a name="OnZendeskTicketStatusUpdate"></a>

## Type condition
<a name="typeu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "question", "incident", "problem", "task"
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Type"
+ Negate - true or false. If set to true, it means *If ticket type does not equal to the type specified in the Operands*.

## Priority condition
<a name="priorityu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "low", "normal", "high", "urgent"
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Priority"
+ Negate - true or false. If set to true, it means *If ticket priority does not equal to the priority specified in the Operands*.

## Status condition
<a name="statusu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is one of "open", "pending", "solved", "close", "hold"
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Status"
+ Negate - true or false. If set to true, it means *If ticket status does not equal to the status specified in the Operands.*.

## RequesterId condition
<a name="requesteridu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a requester id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.RequesterId"
+ Negate - true or false. If set to true, it means *If requester id does not equal to the requester id specified in the Operands.*.

## SubmitterId condition
<a name="submitteridu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a submitter id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.SubmitterId"
+ Negate - true or false. If set to true, it means *If submitter id does not equal to the submitter id specified in the Operands.*.

## AssigneeId condition
<a name="assigneeidu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an assignee id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.AssigneeId"
+ Negate - true or false. If set to true, it means *If assignee id does not equal to the assignee id specified in the Operands.*.

## OrganizationId condition
<a name="organizationidu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an organization id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.OrganizationId"
+ Negate - true or false. If set to true, it means *If organization id does not equal to the organization id specified in the Operands.*.

## BrandId condition
<a name="brandidu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a brand id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.BrandId"
+ Negate - true or false. If set to true, it means *If brand id does not equal to the brand id specified in the Operands*.

## FormId condition
<a name="formidu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a form id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.FormId"
+ Negate - true or false. If set to true, it means *If form id does not equal to the form id specified in the Operands*.

## ExternalId condition
<a name="externalidu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is an external id.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.ExternalId"
+ Negate - true or false. If set to true, it means *If external id does not equal to the external id specified in the Operands*.

## Channel condition
<a name="channelu-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of string, array length can only be 1. Value is a channel string.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Channel"
+ Negate - true or false. If set to true, it means *If channel value does not equal to the channel string specified in the Operands*.

## Tags condition
<a name="tagsu-condition"></a>

**Parameters**
+ Operator - "CONTAINS"
+ Operands – An array of string, array length can only be 1. Value is a tag string.
+ ComparisonValue – "$.ThirdParty.Zendesk.StatusUpdate.Tags"
+ Negate - true or false. If set to true, it means *If tag value does not equal to the tag string specified in the Operands*.