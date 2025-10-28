# Identifying resources with AWS Cloud Control API

Every resource type has a property that is defined as its _primary identifier_. The value
of this property must be unique for each resource of that type in a given AWS account and AWS Region. For
example, many resource types include a `Name` property that must be unique for each resource of that type.
In some cases, the primary identifier is defined as a combination of multiple properties that together form a unique
identifier. By using this primary identifier, combined with the resource type, you can specify exactly which resource
on which you want to perform resource operations such as `update-resource` or
`delete-resource`.

In addition, some resource types define _secondary identifiers_ that can also be used to
uniquely identify resources of that type.

To determine which resource property (or combination of properties) is the primary identifier for a resource
type, refer to the `primaryIdentifier` attribute of the resource type schema. The schema includes
secondary identifiers defined, as well. For more information, see [Viewing resource type schemas](resource-types.md#resource-types-schemas "resource-types.md#resource-types-schemas").

## Getting a resource's primary identifier

You can find the identifier _value_ for a specific resource by using Cloud Control API commands. Each
of the following commands returns a `ProgressEvent` object that contains the primary identifier of the
specified resources:

- ```
  cancel-resource-request
  ```

````
* ```
create-resource
````

- ```
  get-resource-request-status
  ```

````
* ```
list-resource-requests
````

## Using a resource's primary

identifier

When using Cloud Control API commands, you can specify the primary identifier or any secondary identifier defined
for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be
specified as a string or JSON; secondary identifiers must be specified as JSON.

For compound primary identifiers (that is, one that consists of multiple resource properties strung
together), to specify the primary identifier as a string, list the property values _in the order that they
are specified_ in the primary identifier definition, separated by `|`.

For example, the primary identifier for the resource is defined as:

`"primaryIdentifier": [ "/properties/DatabaseName", "/properties/TableName" ]`

So, to specify the primary identifier of a resource as a string, you use the following format.

`DatabaseName|TableName`

For example, given a database with a database name of `MyDatabase` and
table name of `MyTable`, you specify
`MyDatabase|MyTable`.

For compound identifiers specified as JSON, property order is not required, as shown in the following
example.

```
{
  "TableName": "MyTable",
  "DatabaseName": "MyDatabase"
}
```

For more information about resource identifiers, see [primaryidentifier](../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier "../../../cloudformation-cli/latest/userguide/resource-type-schema.md#schema-properties-primaryidentifier") in the _CloudFormation Command Line Interface User Move for Extension
Development_.
