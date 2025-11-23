# About control relationships

Certain controls stand in specified relationships to each other. These relationships are
defined as follows:

- **Alternative**: One control can replace or substitute the other. Example: An AWS Config
  rule and a Security Hub control using the same underlying Config rule.
- **Complementary**: The related controls work together to strengthen governance, each
  covering different aspects of security and compliance and enhancing the
  effectiveness of the other. Example: A Security Hub control and a proactive control that
  both check that an Amazon S3 bucket should have **Block public access** settings
  configured.
- **Mutually Exclusive**: Controls cannot be enabled together on the same target or else
  either control fails in achieving the desired outcome. Example: Two proactive
  controls that enforce two incompatible features.
  You can discover the control relationships in the AWS Control Tower console, or by calling the `ListControlMappings` API in Control Catalog. Here are some examples.

Find all related controls, request:

```
{
    "Filter": {
        "ControlArns": ["arn:aws:controlcatalog:::control/CONTROL_A_ARN"],
        "MappingTypes": ["RELATED_CONTROL"]
    }
}
```

Find all related controls, response:

```
{
    "ControlMappings": [
        {
            "ControlArn": "arn:aws:controlcatalog:::control/CONTROL_A_ARN",
            "MappingType": "RELATED_CONTROL",
            "Mapping": {
                "RelatedControl": {
                    "ControlArn": "arn:aws:controlcatalog:::control/CONTROL_B_ARN",
                    "RelationType": "ALTERNATIVE"
                }
            }
        }, {
            "ControlArn": "arn:aws:controlcatalog:::control/CONTROL_A_ARN",
            "MappingType": "RELATED_CONTROL"
            "Mapping": {
                "RelatedControl": {
                    "ControlArn": "arn:aws:controlcatalog:::control/CONTROL_C_ARN",
                    "RelationType": "COMPLEMENTARY"
                }
            }
        }
        ...
    ],
    "NextToken": "..."
}
```

For more information, see [ListControlMappings](../../../index.md "../../../index.md").
