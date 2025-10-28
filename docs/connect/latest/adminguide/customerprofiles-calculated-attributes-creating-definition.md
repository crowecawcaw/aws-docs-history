# Create

a custom Amazon Connect Customer Profiles calculated attribute definition

Using the Customer Profiles [CreateCalculatedAttributeDefinition](../../../customerprofiles/latest/APIReference/API_CreateCalculatedAttributeDefinition.md "../../../customerprofiles/latest/APIReference/API_CreateCalculatedAttributeDefinition.md") API, you can programmatically
create your own calculated attribute based on a custom object type.

In this topic we show how to create a calculated attribute using a custom JSON
file.

## Step 1: Create a JSON

file

Create a JSON file with the following contents:

```

{
"DomainName": "`your-domain-name`",
   "CalculatedAttributeName": "`your-calculated-attribute-name`",
   "UseHistoricalData": true,
   "DisplayName": "`your-display-name`",
   "Description": "`your-description`",
   "AttributeDetails": {
"Attributes": [
         {
            "Name": "`your-attribute-name`"
         }
       ],
       "Expression": "{`your-object-type.your-attribute-name`}"
   },
    "Statistic": "`your-statistic`",
    "Conditions": {
       "Range": {
        "ValueRange"
        {
            "Start": `your-range-start`
            "End": `your-range-end`
        },
        "TimestampSource": "{`your-object-type.your-timestamp-source`}",
        "Unit": "days"
        },
        "ObjectCount":  `your-object-count`,
        "Threshold": {
           "Value": "`your-threshold-value`",
           "Operator": "`your-threshold-operator`"
        }
   }
}
```

To customize the JSON with your own values, follow these guidelines:

- **Attributes**: This should contain the
  name of the field from your object type that you want to use for the
  calculated attribute. Two attributes being referenced in this list are
  supported.
- **Expression**: Basic math expressions to
  perform between attributes are supported. If you only have one
  attribute, this field should be
  `{ObjectTypeName.AttributeName}`, otherwise if you have a
  math expression in mind this field should contain both
  attributes.
- **Statistic**: This is the operation
  performed when you call one of the calculate APIs that actually performs
  the aggregation operation. Most are self-explanatory, but we have added
  explanations for ones that aren’t.

**Supported statistics**

    + `FIRST_OCCURRENCE` returns the attribute specified
     in the expression of the earliest ingested object.
    + `LAST_OCCURRENCE` returns the attribute specified
     in the expression of the latest ingested object.
    + `COUNT` returns the count from the selected
     data.
    + `SUM` returns the sum from the selected
     data.
    + `MINIMUM` returns minimum from the selected
     data.
    + `MAXIMUM` returns maximum from the selected
     data.
    + `AVERAGE` returns average from the selected
     data.
    + `MAX_OCCURRENCE` returns the most frequently
     occurring value specified in the expression.

- **Range**:
  - Units: Currently supports only DAYS units.
  - ValueRange: Specify positive numbers in ValueRange’s Start or
    End fields to indicate how many days ago to begin from, and
    negative numbers to indicate how many days in the future to
    begin from.
  - TimestampSource: An expression specifying the field in your
    JSON object from which the date should be parsed. The expression
    should follow the structure of \"{ObjectTypeName.<Location of
    timestamp field in JSON pointer format>}\". For example; if your
    object type is MyType and source JSON is `{"generatedAt":
{"timestamp": "1737587945945"}}`, then TimestampSource
    should be `"{MyType.generatedAt.timestamp}"`.

- **ObjectCount**: Indicates how many
  objects the calculated attribute calculation should be based on.
- **Threshold**: If instead of the exact
  calculated attribute value you instead want to know if it’s, for
  example, greater than a certain value, you can use a threshold.

The threshold value can be any string, and the following threshold
operators are supported.

    + `GREATER_THAN`
    + `LESS_THAN`
    + `EQUAL_TO`
    + `NOT_EQUAL_TO`

- UseHistoricalData: Whether historical data ingested before the
  Calculated Attribute was created should be included in
  calculations.

## Step 2: Call the

CreateCalculatedAttributeDefinition API

After you have created and customized the JSON file with your values, call the
[CreateCalculatedAttributeDefinition](../../../customerprofiles/latest/APIReference/API_CreateCalculatedAttributeDefinition.md "../../../customerprofiles/latest/APIReference/API_CreateCalculatedAttributeDefinition.md") API, as shown in the following
example:

```
aws customer-profiles create-calculated-attribute-definition --cli-input-json file:///`custom_calculated_attribute_cli.json` --region `region_name`
```

You can also use the following endpoint:

```
https://profile.`your-region`.amazonaws.com/domains/`your-domain-name`/calculated-attributes
```
