

# OnCaseUpdate
<a name="OnCaseUpdate"></a>

## Assigned queue condition
<a name="OnCaseUpdate-aq-condition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue ids
+ ComparisonValue – "$.Case.Fields.assigned\_queue"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["queueId"], 
    "ComparisonValue": "$.Case.Fields.assigned_queue",
    "Negate": false
}
```

## Assigned user condition
<a name="OnCaseUpdate-au-condition"></a>

**Parameters**
+ Operator - "CONTAINS\_ANY"
+ Operands – A list of queue ids
+ ComparisonValue – "$.Case.Fields.assigned\_user"
+ Negate - false

```
{
    "Operator": "CONTAINS_ANY",
    "Operands": ["userId1, userId2"], 
    "ComparisonValue": "$.Case.Fields.assigned_user",
    "Negate": false
}
```

## Case reason condition
<a name="OnCaseUpdate-cr-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of strings in which the array length can only be 1. The value is a case reason.
+ ComparisonValue – "$.Case.Fields.case\_reason"
+ Negate - true/false

```
{
    "Operator": "EQUALS",
    "Operands": ["Refund"], 
    "ComparisonValue": "$.Case.Fields.case_reason",
    "Negate": false
}
```

## Case status condition
<a name="OnCaseUpdate-cs-condition"></a>

**Parameters**
+ Operator - "EQUALS"
+ Operands – An array of strings in which the array length can only be 1. The value is a case status.
+ ComparisonValue – "$.Case.Fields.status"
+ Negate - false

```
{
    "Operator": "EQUALS",
    "Operands": ["open"], 
    "ComparisonValue": "$.Case.Fields.status",
    "Negate": false
}
```

## Case summary condition
<a name="OnCaseUpdate-csu-condition"></a>

**Parameters**
+ Operator - “CONTAINS” \| “EQUALS”
+ Operands – An array of strings in which the array length can only be 1. The value is a case summary.
+ ComparisonValue – "$.Case.Fields.summary"
+ Negate - false

```
{
    "Operator": "EQUALS",
    "Operands": ["open"], 
    "ComparisonValue": "$.Case.Fields.summary",
    "Negate": false
}
```

## Case date/time last closed condition
<a name="OnCaseUpdate-cdtlc-condition"></a>

**Parameters**
+ Operator - “NumberLessOrEqualTo” \| “NumberGreaterOrEqualTo”
+ Operands – An array of strings in which the array length can only be 1. The value is interpreted as a numeric value.
+ ComparisonValue – "$.Case.Fields.last\_closed\_datetime"
+ Negate - false

```
{
    "Operator": "NumberLessOrEqualTo",
    "Operands": ["2023-11-11T11:11:11.111111Z"], 
    "ComparisonValue": "$.Case.Fields.last_closed_datetime",
    "Negate": false
}
```

## Case date/time updated condition
<a name="OnCaseUpdate-cdtu-condition"></a>

**Parameters**
+ Operator - “NumberLessOrEqualTo” \| “NumberGreaterOrEqualTo”
+ Operands – An array of strings in which the array length can only be 1. The value is interpreted as a numeric value.
+ ComparisonValue – "$.Case.Fields.last\_updated\_datetime"
+ Negate - false

```
{
    "Operator": "NumberLessOrEqualTo",
    "Operands": ["2023-11-11T11:11:11.111111Z"], 
    "ComparisonValue": "$.Case.Fields.last_updated_datetime",
    "Negate": false
}
```

## Case date/time opened condition
<a name="OnCaseUpdate-cdto-condition"></a>

**Parameters**
+ Operator - “NumberLessOrEqualTo” \| “NumberGreaterOrEqualTo”
+ Operands – An array of strings in which the array length can only be 1. The value is interpreted as a numeric value.
+ ComparisonValue – "$.Case.Fields.created\_datetime"
+ Negate - true/false

```
{
    "Operator": "NumberLessOrEqualTo",
    "Operands": ["2023-11-11T11:11:11.111111Z"], 
    "ComparisonValue": "$.Case.Fields.created_datetime",
    "Negate": false
}
```

## Case reference number condition
<a name="OnCaseUpdate-rn-condition"></a>

**Parameters**
+ Operator - “CONTAINS” \| “EQUALS”
+ Operands – An array of strings in which the array length can only be 1. The value is interpreted as a numeric value.
+ ComparisonValue – "$.Case.Fields.reference\_number"
+ Negate - true

```
{
    "Operator": "CONTAINS",
    "Operands": ["11111111"], 
    "ComparisonValue": "$.Case.Fields.reference_number",
    "Negate": false
}
```

## Case customer fields condition
<a name="OnCaseUpdate-cf-condition"></a>

**Parameters**
+ Operator - “CONTAINS” \| “EQUALS”
+ Operands – An array of strings in which the array length can only be 1.
+ ComparisonValue – "$.Case.Fields.custom\_case\_field\_id"
+ Negate - true/false

```
{
    "Operator": "EQUALS",
    "Operands": ["vip"], 
    "ComparisonValue": "$.Case.Fields.custom_case_field_id",
    "Negate": false
}
```

## Case template condition
<a name="OnCaseCreate-ctcu-condition"></a>

**Parameters**
+ Operator - “CONTAINS\_ANY”
+ Operands – A list of template ids.
+ ComparisonValue – "$.Case.TemplateId"
+ Negate - true/false

```
{
"Operator": "CONTAINS_ANY",
"Operands": ["templateId"],
"ComparisonValue": "$.Case.TemplateId",
"Negate": false
}
```