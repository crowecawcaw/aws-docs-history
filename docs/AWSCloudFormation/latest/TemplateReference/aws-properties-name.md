This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# AWS CloudFormation resource custom naming

You can assign custom names to supported resource types in your CloudFormation template to make
them more meaningful and easily identifiable. By default, CloudFormation generates a unique physical
ID to name a resource. For example, CloudFormation might name an Amazon S3 bucket with the following
physical ID `MyStack-MyBucket-abcdefghijk1`. With custom names, you can specify a
name that's easier to read and identify, such as `production-app-logs` or
`business-metrics`.

Not all resources support custom names. Each AWS service independently determines which
resource types support custom names.

Resource names must be unique across all your active stacks. If you reuse templates to
create multiple stacks, you must change or remove custom names from your template. If you don't
specify a name, CloudFormation generates a unique physical ID to name the resource. Names must begin
with a letter; contain only ASCII letters, digits, and hyphens; and not end with a hyphen or
contain two consecutive hyphens.

Also, don't manage stack resources outside of CloudFormation. For example, if you rename a
resource that's part of a stack without using CloudFormation, you might get an error any time you
try to update or delete that stack.

###### Important

You can't perform an update that causes a custom-named resource to be replaced. If you
must replace the resource, specify a new name.

## Example

If you want to use a custom name, specify a name property for that resource in your
CloudFormation template. Each resource that supports custom names has its own property that you
specify. For example, to name an DynamoDB table, you use the `TableName` property, as
shown in the following sample:

### JSON

```
"myDynamoDBTable" : {
   "Type" : "AWS::DynamoDB::Table",
   "Properties" : {
      "KeySchema" : {
         "HashKeyElement": {
            "AttributeName" : "AttributeName1",
            "AttributeType" : "S"
         },
         "RangeKeyElement" : {
            "AttributeName" : "AttributeName2",
            "AttributeType" : "N"
         }
      },
      "ProvisionedThroughput" : {
         "ReadCapacityUnits" : "5",
         "WriteCapacityUnits" : "10"
      },
      "TableName" : "SampleTable"
   }
}
```

### YAML

```
myDynamoDBTable:
  Type: AWS::DynamoDB::Table
  Properties:
    KeySchema:
      HashKeyElement:
        AttributeName: "AttributeName1"
        AttributeType: "S"
      RangeKeyElement:
        AttributeName: "AttributeName2"
        AttributeType: "N"
    ProvisionedThroughput:
      ReadCapacityUnits: "5"
      WriteCapacityUnits: "10"
    TableName: "SampleTable"
```
