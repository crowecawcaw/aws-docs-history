# Amazon Connect Customer Profiles calculated

attributes APIs

You can use the following Customer Profiles calculated attribute APIs

CreateCalculatedAttributeDefinition
**CreateCalculatedAttributeDefinition**

Create a new calculated attribute. This requires an existing object
type in the domain. You can define attributes that you want to pull from
a single source object and the mathematical operations to apply to them
in aggregate as well as the time range and object count.

After creation, new object data ingested into Customer Profiles will be included in
the calculated attribute, which can be retrieved for a profile using the
`GetCalculatedAttributeForProfile` API. To use historical
data as well, specify `UseHistoricalData` as true. The
`Readiness` and `Status` fields on the API
response will provide information regarding the status of including
historical data in the calculated attribute.

Defining a calculated attribute makes it available for all profiles
within a domain. Each calculated attribute can only reference one
ObjectType and at most two fields from that ObjectType.

**Request**

```
`POST /domains/`DomainName`/calculated-attributes/`CalculatedAttributeName``
```

```

{
    "CalculatedAttributeName": "string",
    "DisplayName": "string",
    "Description": "string",
    "AttributeDetails": {
       "Attributes": [
           {
               "Name": "string"
           }
           ...
       ],
       "Expression": "string",
    },
    "Statistic": "AVERAGE" | "COUNT" | "SUM" | "FIRST_OCCURRENCE" | "LAST_OCCURRENCE" | "MINIMUM" | "MAXIMUM" | "MAX_OCCURRENCE",
    "Conditions": {
        "Range": {
             "Value": "number",
             "Units": "string"
        },
        "ObjectCount": "number",
        "Threshold": {
            "Value": "string",
            "Operator": "EQUAL_TO" | "GREATER_THAN" | "LESS_THAN" | "NOT_EQUAL_TO"
        }
     },
     "Tags": {}
}

```

**Response**

```

{
    "CalculatedAttributeName": "string",
    "DisplayName": "string",
    "Description": "string",
    "AttributeDetails": {
       "Attributes": [
           {
               "Name": "string"
           }
           ...
       ],
       "Expression": "string",
    },
    "Statistic": "AVERAGE" | "COUNT" | "SUM" | "FIRST_OCCURRENCE" | "LAST_OCCURRENCE" | "MINIMUM" | "MAXIMUM" | "MAX_OCCURRENCE"
    "Conditions": {
        "Range": {
             "Value": "number",
             "Units": "string"
        },
        "ObjectCount": "number",
        "Threshold": {
            "Value": "string",
            "Operator": "EQUAL_TO" | "GREATER_THAN" | "LESS_THAN" | "NOT_EQUAL_TO"
        }
    },
    "CreatedAt": number,
    "LastUpdatedAt": number,
    "Tags": {}
}

```

**Request body**

- **CalculatedAttributeName**

The unique (per domain) name of the calculated
attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **DisplayName**

The display name of the calculated attribute.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern:
     `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
    + Required: No

- **Description**

The description of the calculated attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 1000.
    + Required: No

- **UseHistoricalData**

Whether historical data ingested before the Calculated
Attribute was created should be included in calculations.

    + Type : Boolean
    + Required: No

- **AttributeDetails**

Details of the attributes used in the definition and the
mathematical operations involved between the attributes. See the
following components:

    + **Attributes**


    A list of attribute items specified in the
     mathematical expression.




    	- **AttributeItem**


    	The details of a single attribute item
    	 specified in the mathematical expression.




    		* Name




    			+ The name of an attribute defined in a
    			 profile object type.
    			+ Type: String
    + **Expression**


    Mathematical expression that is performed on attribute
     items provided in the attribute list. Each element in
     the expression should follow the structure of
     \"{ObjectTypeName.AttributeName}\".




    	- Example : `{ObjA.AttributeA} -
    	 {ObjA.AttributeB}`
    	- Type : String
    	- We only support the following mathematical
    	 operations: `+ - * /`
    	- You cannot make modifications to the
    	 Expression once a calculated attribute definition
    	 is created

- **Conditions**

Defines the calculated attribute aggregation criteria and
threshold.

    + Type: Conditions object




    	- Range
    	- ObjectCount
    	- Threshold

- **Range**

The relative time period over which data is included in the
aggregation.

    + Type: Range object




    	- Value: The length of time of the specified
    	 units. `ValueRange` overrides
    	 Value.




    		* Type: Integer
    		* Required: No
    	- ValueRange: A structure letting customers
    	 specify a relative time window over which over
    	 which data is included in the Calculated
    	 Attribute. Use positive numbers to indicate that
    	 the endpoint is in the past, and negative numbers
    	 to indicate it is in the future. ValueRange
    	 overrides Value.




    		* Type: ValueRange
    		* Required: No




    			+ Start




    				- The start time of when to include objects.
    				 Use positive numbers to indicate that the
    				 startpoint is in the past, and negative numbers to
    				 indicate it is in the future.
    				- Type: Integer
    				- Required: Yes


    			+ End




    				- The end time of when to include objects. Use
    				 positive numbers to indicate that the startpoint
    				 is in the past, and negative numbers to indicate
    				 it is in the future.
    				- Type: Integer
    				- Required: Yes
    	- TimestampSource: An expression specifying the
    	 field in your JSON object from which the date
    	 should be parsed. The expression should follow the
    	 structure of \"{ObjectTypeName.<Location of
    	 timestamp field in JSON pointer format>}\". For
    	 example, if your object type is MyType and source
    	 JSON is `{"generatedAt": {"timestamp":
    	 "1737587945945"}}`, then TimestampSource
    	 should be
    	 `"{MyType.generatedAt.timestamp}"`.




    		* Length Constraints: Minimum length of 1.
    		 Maximum length of 255.
    		* Required: No
    	- TimestampFormat: The format the timestamp
    	 field in your JSON object is specified. This value
    	 should be one of EPOCHMILLI (for Unix epoch
    	 timestamps with second/millisecond level
    	 precision) or ISO\_8601 (following ISO\_8601 format
    	 with second/millisecond level precision, with an
    	 optional offset of Z or in the format HH:MM or
    	 HHMM.). For example, if your object type is MyType
    	 and source JSON is `{"generatedAt":
    	 {"timestamp":
    	 "2001-07-04T12:08:56.235-0700"}},` then
    	 TimestampFormat should be
    	 `"ISO_8601"`.
    	- Unit: Unit of time




    		* Valid values: Days
    		* Required: Yes
    + Required: Yes
    + Initial scope: Max of 366 days

- **ObjectCount**

The number of profile objects used for the calculated
attribute.

    + Type: Number
    + Range: 1 through 100
    + Required: No

- **Threshold**

The comparison logic to generate a true/false calculated
attribute.

    + Type: Threshold object




    	- Value




    		* The value of the threshold
    		* Type: String
    		* Required: No
    	- Operator




    		* The operator of the threshold
    		* Type: ENUM
    		* Valid Values:




    			+ GREATER\_THAN
    			+ LESS\_THAN
    			+ EQUAL\_TO
    			+ NOT\_EQUAL\_TO
    + Required: No

- **Statistic**

The aggregation operation to perform for the calculated
attribute.

    + Type: ENUM
    + Valid Values:




    	- FIRST\_OCCURRENCE
    	- LAST\_OCCURRENCE
    	- COUNT
    	- SUM
    	- MINIMUM
    	- MAXIMUM
    	- AVERAGE
    	- MAX\_OCCURRENCE

UpdateCalculatedAttributeDefinition
**UpdateCalculatedAttributeDefinition**

Update a calculated attribute definition. Updates are limited to
display name, description, time range, object count, and threshold. This
API supports partial updates, so only the parameters that require
updating need to be included.

###### Note

When updating the Conditions:

- Increasing the date range of a calculated attribute will
  not trigger inclusion of historical data greater than the
  current date range.
- TimestampSource and TimestampFormat cannot be updated
  after a calculated attribute definition has been
  created.

**Request**

```
`PUT /domains/`DomainName`/calculated-attributes/`CalculatedAttributeName``
```

```

{
    "DisplayName": "string",
    "Description": "string",
    "Conditions": {
        "Range": {
             "Value": "number",
             "Units": "string"
        },
        "ObjectCount": "number",
        "Threshold": {
            "Value": "string",
            "Operator": "EQUAL_TO" | "GREATER_THAN" | "LESS_THAN" | "NOT_EQUAL_TO"
        }
   }
}

```

**Response**

```

{
    "CalculatedAttributeName": "string",
    "DisplayName": "string",
    "Description": "string",
    "AttributeDetails": {
       "Attributes": [
           {
               "Name": "string"
           }
           ...
       ],
       "Expression": "string",
    },
    "Statistic": "AVERAGE" | "COUNT" | "SUM" | "FIRST_OCCURRENCE" | "LAST_OCCURRENCE" | "MINIMUM" | "MAXIMUM" | "MAX_OCCURRENCE"
    "Conditions": {
        "Range": {
             "Value": "number",
             "Units": "string"
        },
        "ObjectCount": "number",
        "Threshold": {
            "Value": "string",
            "Operator": "EQUAL_TO" | "GREATER_THAN" | "LESS_THAN" | "NOT_EQUAL_TO"
        }
    },
    "CreatedAt": number,
    "LastUpdatedAt": number,
    "Tags": {}
}

```

**Request body**

- **DisplayName**

The display name of the calculated attribute.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern:
     `^[a-zA-Z_][a-zA-Z_0-9-\s]*$`
    + Required: No

- **Description**

The description of the calculated attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 1000.
    + Required: No

- **Conditions**

Defines the calculated attribute aggregation criteria and
threshold.

    + Type: Conditions object




    	- Range
    	- ObjectCount
    	- Threshold

- **Range**

The relative time period over which data is included in the
aggregation.

    + Type: Range object




    	- Value: The length of time of the specified
    	 units




    		* Type: Integer
    		* Required: No
    	- ValueRange: A structure letting customers
    	 specify a relative time window over which over
    	 which data is included in the Calculated
    	 Attribute. Use positive numbers to indicate that
    	 the endpoint is in the past, and negative numbers
    	 to indicate it is in the future. ValueRange
    	 overrides Value.




    		* Type: ValueRange
    		* Required: No




    			+ Start




    				- The start time of when to include objects.
    				 Use positive numbers to indicate that the
    				 startpoint is in the past, and negative numbers to
    				 indicate it is in the future.
    				- Type: Integer
    				- Required: Yes


    			+ End




    				- The end time of when to include objects. Use
    				 positive numbers to indicate that the startpoint
    				 is in the past, and negative numbers to indicate
    				 it is in the future.
    				- Type: Integer
    				- Required: Yes
    	- Unit: Unit of time




    		* Valid values: Days
    		* Required: Yes
    + Required: Yes
    + Initial scope: Max of 366 days

- **ObjectCount**

The number of profile objects used for the calculated
attribute.

    + Type: Number
    + Range: 1 through 100
    + Required: No

- **Threshold**

The comparison logic to generate a true/false calculated
attribute.

    + Type: Threshold object




    	- Value




    		* The value of the threshold
    		* Type: String
    		* Required: No
    	- Operator




    		* The operator of the threshold
    		* Type: ENUM
    		* Valid Values:




    			+ GREATER\_THAN
    			+ LESS\_THAN
    			+ EQUAL\_TO
    			+ NOT\_EQUAL\_TO
    + Required: No

GetCalculatedAttributeDefinition
**GetCalculatedAttributeDefinition**

Retrieve a calculated attribute definition.

**Request**

```
`GET /domains/`DomainName`/calculated-attributes/`CalculatedAttributeName``
```

**Request Body**

```
The request does not have a request body.

```

**Response**

```

{
"CalculatedAttributeName": "string",
    "DisplayName": "string",
    "Description": "string",
    "AttributeDetails": {
"Attributes": [
           {
"Name": "string"
           }
           ...
       ],
       "Expression": "string",
    },
    "Statistic": "AVERAGE" | "COUNT" | "SUM" | "FIRST_OCCURRENCE" | "LAST_OCCURRENCE" | "MINIMUM" | "MAXIMUM" | "MAX_OCCURRENCE"
"Conditions": {
"Range": {
      "Unit": "string",
      "Value": number
      "ValueRange"
        {
            "Start": number
            "End": number
        },
      "TimestampFormat": "string",
      "TimestampSource": "string"
    },
        "ObjectCount": "number",
        "Threshold": {
"Value": "string",
            "Operator": "EQUAL_TO" | "GREATER_THAN" | "LESS_THAN" | "NOT_EQUAL_TO"
        }
    },
    "UseHistoricalData" boolean,
  "Status": "PREPARING" | "IN_PROGRESS" | "COMPLETED" | "FAILED",
  "Readiness": {
        "ProgressPercentage": number,
        "Message": "string",
        },
    "CreatedAt": number,
    "LastUpdatedAt": number,
    "Tags": {}
}

```

**URI request parameters**

- **DomainName**

The unique name of the domain.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **CalculatedAttributeName**

The unique (per domain) name of the calculated
attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

DeleteCalculatedAttributeDefinition
**DeleteCalculatedAttributeDefinition**

Delete an existing calculated attribute definition. Note that deleting
a default calculated attribute is possible, however once deleted you
will be unable to undo that action and will need to recreate it on your
own using the `CreateCalculatedAttributeDefinition` API if
you want it back.

**Request**

```
`DELETE /domains/`DomainName`/calculated-attributes/`CalculatedAttributeName``
```

**Request Body**

```
The request does not have a request body.

```

**Response**

```
The response does not have a response body.

```

**URI request parameters**

- **DomainName**

The unique name of the domain.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **CalculatedAttributeName**

The unique (per domain) name of the calculated
attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

ListCalculatedAttributeDefinitions
**ListCalculatedAttributeDefinitions**

Retrieve all calculated attribute definitions for a domain.

**Request**

```
`GET /domains/`DomainName`/calculated-attributes?max-results=MaxResults&next-token=NextToken`
```

**Request Body**

```
The request does not have a request body.

```

**Response**

```

{
    "Items": [
        {
            "UseHistoricalData": boolean,
            "ReadinessStatus": PREPARING | IN_PROGRESS | COMPLETED | FAILED,
            "CalculatedAttributeName": "string",
            "CreatedAt": number,
            "Description": "string",
            "DisplayName": "string",
            "LastUpdatedAt": number,
            "Tags": {
                "string" : "string"
            }
        }
    ],
    "NextToken": "string"
}

```

**URI request parameters**

- **DomainName**

The unique name of the domain.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **MaxResults**

The maximum number of objects returned per page.

    + Valid Range: Minimum value of 1. Maximum value of
     100

- **NextToken**

The pagination token from the previous
ListCalculatedAttributeDefinition API call.

    + Length Constraints: Minimum length of 1. Maximum
     length of 1024

GetCalculatedAttributeForProfile
**GetCalculatedAttributeForProfile**

Initiates the calculation and retrieves the result of a single
calculated attribute for a single profile.

**Request**

```
`GET /domains/`DomainName`/profile/`ProfileId`/calculated-attributes/`CalculatedAttributeName``
```

**Request Body**

```
The request does not have a request body.

```

**Response**

```

{
"Name": "string",
    "DisplayName": "string",
    "Value": "string",
    "IsDataPartial": "string",
    "LastObjectTimestamp" : number
}

```

**URI request parameters**

- **DomainName**

The unique name of the domain.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **CalculatedAttributeName**

The unique (per domain) name of the calculated
attribute.

    + Type : String
    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

ListCalculatedAttributesForProfile
**ListCalculatedAttributesForProfile**

Initiates the calculation and retrieves the results of all calculated
attributes for a single profile.

**Request**

```
`GET /domains/`DomainName`/profile/`ProfileId`/calculated-attributes?max-results=MaxResults&next-token=NextToken`
```

**Request Body**

```
The request does not have a request body.

```

**Response**

```

{
"Items": [
        {
"CalculatedAttributeName": "string",
            "DisplayName": "string",
            "Value": "string",
            "IsDataPartial" : "string",
            "LastObjectTimestamp" : number
        },
        ...
    ],
    "NextToken": "string"
}

```

**URI request parameters**

- **DomainName**

The unique name of the domain.

    + Length Constraints: Minimum length of 1. Maximum
     length of 64.
    + Pattern: `^[a-zA-Z0-9_-]+$`
    + Required: Yes

- **ProfileId**
  - Pattern: `[a-f0-9]{32}`
  - Required: Yes

- **MaxResults**

The maximum number of objects returned per page.

    + Valid Range: Minimum value of 1. Maximum value of
     100

- **NextToken**

The pagination token from the previous
ListCalculatedAttributeDefinition API call.

    + Length Constraints: Minimum length of 1. Maximum
     length of 1024
