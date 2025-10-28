# Thing types

Thing types allow you to store description and configuration information that is
common to all things associated with the same thing type. This simplifies the management
of things in the registry. For example, you can define a LightBulb thing type. All
things associated with the LightBulb thing type share a set of attributes: serial
number, manufacturer, and wattage. When you create a thing of type LightBulb (or change
the type of an existing thing to LightBulb) you can specify values for each of the
attributes defined in the LightBulb thing type.

Although thing types are optional, their use makes it easier to discover
things.

- Things with a thing type can have up to 50 attributes.
- Things without a thing type can have up to three attributes.
- A thing can be associated with only one thing type.
- There is no limit on the number of thing types you can create in your
  account.
  You can't change a thing type name after it has been created. You can deprecate a
  thing type at any time to prevent new things from being associated with it. You can also
  delete thing types that have no things associated with them.

###### Topics:

- [Create a thing type](create-thing-type.md "create-thing-type.md")
- [List thing types](list-thing-types.md "list-thing-types.md")
- [Describe a thing type](describe-thing-type.md "describe-thing-type.md")
- [Associate a thing type with a thing](associate-thing-type.md "associate-thing-type.md")
- [Update a thing type](update-thing-type.md "update-thing-type.md")
- [Deprecate a thing type](deprecate-thing-type.md "deprecate-thing-type.md")
- [Delete a thing type](delete-thing-types.md "delete-thing-types.md")
