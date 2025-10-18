Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").
 

# Attribute Rules

Rules describe permissible values of an attribute type and constrain the values that are
 allowed for any particular attribute. You must specify rules as part of an attribute
 definition when you create a facet. Cloud Directory supports the following rule types:


* String length
* Binary length
* String from set
* Number comparison
**String length** 

Constrains the length of a string attribute value.

Allowed rule parameter keys: min, max

Allowed rule parameter values: number

**Binary length**

Constrains the byte array length of a binary attribute value.

Allowed rule parameter keys: min, max

Allowed rule parameter values: number

**String from set**

Constrains the value of a string attribute to the allowed set of specified strings. 

Allowed rule parameter keys: allowedValues

Allowed rule parameter values: Set of strings with each string to be UTF-8 encoded

Allowed values are comma delimited and can be wrapped in quotes. This is useful when
 allowed values include comma’s. For example:


* One,two,three = matches One two or three
* “with,comma”,”withoutcomma” = matches “with,comma” or “withoutcomma”
* with”quote,withoutquote matches ‘with”quote’ or ‘withoutquote’
**Number comparison**

Constraints the numeric value allowed for a number attribute.

Allowed rule parameter keys: min, max

Allowed rule parameter values: number
