

# OnSlaBreach
<a name="OnSlaBreach"></a>

## Cases SLA name condition
<a name="OnSlaBreach-csnc-condition"></a>

**Parameters**
+ Operator - “CONTAINS\_ANY”
+ Operands – A list of SLA names.
+ ComparisonValue – "$.RelatedItem.SlaConfiguration.Name"
+ Negate - false

```
{
"Operator": "CONTAINS_ANY",
"Operands": ["highPrioritySla"],
"ComparisonValue": "$.RelatedItem.SlaConfiguration.Name",
"Negate": false
}
```