

# How it works
<a name="how-it-works"></a>

Profile explorer offers various widgets to display customer information, layouts are stored as JSON definitions, representing the complete structure and configuration of your dashboard. Each widget and component in your visual layout corresponds to a specific JSON block within this definition.

## Core components
<a name="core-components"></a>

Every component in the layout definition is comprised of five common elements:
+ **Type**
  + Defines the component category
  + Determines how the component renders
  + Examples: BoardItem, Table, KeyValuePair
+ **Id**
  + Unique identifier for each component
  + Used for component tracking and updates
  + Generated automatically when components are created in the builder
+ **Props**
  + Component-specific properties
  + Controls appearance and behavior
  + Contains configuration settings
+ **Children**
  + Nested components or content
  + Defines hierarchical relationships
  + Can contain multiple sub-components
+ **DataSource**
  + Specifies data origin
  + Defines data retrieval parameters
  + Controls data binding for components

## Example layout component definition
<a name="example-layout-component-definition"></a>

The following is a sample JSON structure for a dashboard table component:

```
{
    "Id": "unique-identifier",
    "Type": "BoardItem",
    "Props": {},
    "Children": [
        {
            "Id": "unique-identifier",
            "Type": "Table",
            "Props": {},
            "Children": [
                {
                    "Id": "unique-identifier",
                    "Type": "TextContent",
                    "Props": {},
                    "Children": ["string"]
                }
            ]
        }
    ],
    "DataSource": [
        {
            "Type": "source-type",
            "Params": {}
        }
    ]
}
```

## Dynamic data configuration
<a name="dynamic-data-configuration"></a>

Profile explorer uses template expressions to access and display Customer Profiles data dynamically within your components.

### Single value support
<a name="single-value-support"></a>

For components like Key Value Pairs and Key Metrics, you can access:

#### Standard profile information
<a name="standard-profile-information"></a>

```
{{Customer.<StandardProfileInfo>}}
```

Example usage:
+ `{{Customer.FirstName}}`
+ `{{Customer.LastName}}`
+ `{{Customer.PhoneNumber}}`

#### Calculated Attributes
<a name="calculated-attributes"></a>

```
{{Customer.CalculatedAttributes.<attributeDefinitionName>}}
```

Example usage:
+ `{{Customer.CalculatedAttributes._cases_count}}`
+ `{{Customer.CalculatedAttributes._new_customer}}`

### Tabular data support syntax
<a name="tabular-data-support-syntax"></a>

#### Calculated Attributes
<a name="calculated-attributes-tabular"></a>

```
{{Customer.CalculatedAttributes.DisplayName}}
```

```
{{Customer.CalculatedAttributes.CalculatedAttributeDefinitionName}}
```

#### Segments
<a name="segments"></a>

```
{{Customer.CalculatedAttributes.DisplayName}}
```

```
{{Customer.CalculatedAttributes.SegmentDefinitionName}}
```

#### Profile objects
<a name="profile-objects"></a>

```
{{Customer.ObjectAttributes.<objectTypeName>.<fieldName>}}
```

**Example usage:**
+ `{{Customer.ObjectAttributes.CTR.contactId}}`
+ `{{Customer.ObjectAttributes.Order.orderId}}`

### Implementation examples
<a name="implementation-examples"></a>

#### Single value component
<a name="single-value-component"></a>

```
{
    "Type": "KeyValuePair",
    "Props": {
        "Items": [
            {
                "Label": {
                    "Content": {
                        "Type": "TextContent",
                        "Children": ["Customer Name"]
                    }
                },
                "Value": {
                    "Content": {
                        "Type": "TextContent",
                        "Children": ["{{Customer.FirstName}}"]
                    }
                }
            }
        ]
    }
}
```

#### Tabular component
<a name="tabular-component"></a>

```
{
    "Type": "Table",
    "Props": {
        "ColumnDefinitions": [
            {
                "Cell": {
                    "Content": {
                        "Type": "TextContent",
                        "Children": ["{{Customer.ObjectAttributes.CTR.contactId}}"]
                    }
                },
                "Header": "Contact ID"
            }
        ]
    }
}
```

**Note**  
Make sure that the attributes, objects, and segments you reference exist in your Customer Profiles configuration before using them in your layout.