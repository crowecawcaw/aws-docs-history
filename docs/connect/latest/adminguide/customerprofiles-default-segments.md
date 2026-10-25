

# Default segments in Connect Customer
<a name="customerprofiles-default-segments"></a>

With Connect Customer, you have access to out-of-the-box default segments on every domain. You can use these segments immediately without any configuration. Connect Customer builds default segments from the default calculated attributes it provides. For more information about the calculated attributes that these segments reference, see [Default calculated attributes in Connect Customer Customer Profiles](customerprofiles-default-calculated-attributes.md).

Default segment names begin with the reserved `_default_` prefix. You cannot create a segment definition that uses this prefix, and you cannot delete a default segment.

Connect Customer evaluates default segments at contact disconnected time. As the contact ends, Connect Customer resolves each profile's membership in these segments. Connect Customer then sends the segment memberships to Connect Customer Customer Analytics. You can use the segment memberships to filter and group data in dashboards.

## Default lifetime value segments
<a name="customerprofiles-default-lifetime-value-segments"></a>

The lifetime value segments classify profiles into high, medium, and low tiers based on the profile's total order value. These segments reference the `_lifetime_value_high` and `_lifetime_value_low` default calculated attributes, which track the order object.

To change which profiles fall into each tier, update the thresholds on the underlying `_lifetime_value_high` and `_lifetime_value_low` calculated attributes. The segments use the updated thresholds on subsequent evaluations.

**Note**  
Important: Always configure the high threshold to be greater than the low threshold (`_lifetime_value_high > _lifetime_value_low`). If the high threshold is less than or equal to the low threshold, the tier boundaries overlap and profiles can be classified incorrectly.

The following example shows the High lifetime value default segment definition:

```
{
   "SegmentDefinitionName": "_default_lifetime_value_high",
   "DisplayName": "High lifetime value",
   "Description": "Customers whose total order value meets or exceeds the high lifetime value threshold.",
   "SegmentType": "CLASSIC",
   "SegmentGroups": {
      "Groups": [
         {
            "Type": "ALL",
            "Dimensions": [
               {
                  "CalculatedAttributes": {
                     "_lifetime_value_high": {
                        "DimensionType": "INCLUSIVE",
                        "Values": ["true"]
                     }
                  }
               }
            ]
         }
      ],
      "Include": "ALL"
   },
   "Tags": {
   }
}
```

The following example shows the Medium lifetime value default segment definition:

```
{
   "SegmentDefinitionName": "_default_lifetime_value_medium",
   "DisplayName": "Medium lifetime value",
   "Description": "Customers whose total order value falls between the high and low lifetime value thresholds.",
   "SegmentType": "CLASSIC",
   "SegmentGroups": {
      "Groups": [
         {
            "Type": "ALL",
            "Dimensions": [
               {
                  "CalculatedAttributes": {
                     "_lifetime_value_high": {
                        "DimensionType": "INCLUSIVE",
                        "Values": ["false"]
                     }
                  }
               },
               {
                  "CalculatedAttributes": {
                     "_lifetime_value_low": {
                        "DimensionType": "INCLUSIVE",
                        "Values": ["false"]
                     }
                  }
               }
            ]
         }
      ],
      "Include": "ALL"
   },
   "Tags": {
   }
}
```

The following example shows the Low lifetime value default segment definition:

```
{
   "SegmentDefinitionName": "_default_lifetime_value_low",
   "DisplayName": "Low lifetime value",
   "Description": "Customers whose total order value is at or below the low lifetime value threshold.",
   "SegmentType": "CLASSIC",
   "SegmentGroups": {
      "Groups": [
         {
            "Type": "ALL",
            "Dimensions": [
               {
                  "CalculatedAttributes": {
                     "_lifetime_value_low": {
                        "DimensionType": "INCLUSIVE",
                        "Values": ["true"]
                     }
                  }
               }
            ]
         }
      ],
      "Include": "ALL"
   },
   "Tags": {
   }
}
```

## Default repeat caller segments
<a name="customerprofiles-default-repeat-caller-segments"></a>

The repeat caller segment identifies profiles that have had more than one contact in the last 7 days (inbound or outbound). It references the `_call_count` default calculated attribute, which tracks the number of distinct inbound and outbound contacts a customer has had in the last 7 days.

To change how many contacts qualify a profile as a repeat caller, update the threshold on the `_call_count` calculated attribute. The segment uses the updated threshold on subsequent evaluations.

The following example shows the Repeat caller default segment definition:

```
{
   "SegmentDefinitionName": "_default_repeat_caller",
   "DisplayName": "Repeat caller",
   "Description": "Customers who have called multiple times.",
   "SegmentType": "CLASSIC",
   "SegmentGroups": {
      "Groups": [
         {
            "Type": "ALL",
            "Dimensions": [
               {
                  "CalculatedAttributes": {
                     "_call_count": {
                        "DimensionType": "GREATER_THAN",
                        "Values": ["1"]
                     }
                  }
               }
            ]
         }
      ],
      "Include": "ALL"
   },
   "Tags": {
   }
}
```

## Use default segments in dashboards
<a name="customerprofiles-default-segments-analytics"></a>

You can filter and group data by default segment memberships in Connect Customer Analytics dashboards. For the full list of available dashboards and the data they report, see [Dashboards in Connect Customer for getting contact center performance data](dashboards.md).