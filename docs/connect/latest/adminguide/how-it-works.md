# How it works

Profile explorer offers various widgets to display customer information, layouts
are stored as JSON definitions, representing the complete structure and
configuration of your dashboard. Each widget and component in your visual layout
corresponds to a specific JSON block within this definition.

## Core components

Every component in the layout definition is comprised of five common
elements:

- **Type**
  - Defines the component category
  - Determines how the component renders
  - Examples: BoardItem, Table, KeyValuePair

- **Id**
  - Unique identifier for each component
  - Used for component tracking and updates
  - Generated automatically when components are created in the
    builder

- **Props**
  - Component-specific properties
  - Controls appearance and behavior
  - Contains configuration settings

- **Children**
  - Nested components or content
  - Defines hierarchical relationships
  - Can contain multiple sub-components

- **DataSource**
  - Specifies data origin
  - Defines data retrieval parameters
  - Controls data binding for components

## Example layout component

definition

The following is a sample JSON structure for a dashboard table
component:

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

Profile explorer uses template expressions to access and display Customer
Profiles data dynamically within your components.

### Single value support

For components like Key Value Pairs and Key Metrics, you can
access:

#### Standard profile

information

```
{{Customer.<StandardProfileInfo>}}
```

Example usage:

- `{{Customer.FirstName}}`
- `{{Customer.LastName}}`
- `{{Customer.PhoneNumber}}`

#### Calculated Attributes

```
{{Customer.CalculatedAttributes.<attributeDefinitionName>}}
```

Example usage:

- `{{Customer.CalculatedAttributes._cases_count}}`
- `{{Customer.CalculatedAttributes._new_customer}}`

### Tabular data support

syntax

#### Calculated

Attributes

```
{{Customer.CalculatedAttributes.DisplayName}}
```

```
{{Customer.CalculatedAttributes.CalculatedAttributeDefinitionName}}
```

#### Segments

```
{{Customer.CalculatedAttributes.DisplayName}}
```

```
{{Customer.CalculatedAttributes.SegmentDefinitionName}}
```

#### Profile objects

```
{{Customer.ObjectAttributes.<objectTypeName>.<fieldName>}}
```

**Example usage:**

- `{{Customer.ObjectAttributes.CTR.contactId}}`
- `{{Customer.ObjectAttributes.Order.orderId}}`

### Implementation examples

#### Single value component

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

###### Note

Ensure that the attributes, objects, and segments you reference exist in
your Customer Profiles configuration before using them in your
layout.
