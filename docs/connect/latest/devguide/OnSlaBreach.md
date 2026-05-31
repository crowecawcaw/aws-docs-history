# OnSlaBreach

## Cases SLA name condition

###### Parameters

- Operator - “CONTAINS_ANY”
- Operands – A list of SLA names.
- ComparisonValue – "$.RelatedItem.SlaConfiguration.Name"
- Negate - false

```
{
"Operator": "CONTAINS_ANY",
"Operands": ["highPrioritySla"],
"ComparisonValue": "$.RelatedItem.SlaConfiguration.Name",
"Negate": false
}

```
