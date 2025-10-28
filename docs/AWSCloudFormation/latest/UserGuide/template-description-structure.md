# CloudFormation template Description syntax

The `Description` section (optional) enables you to include a text string that
describes the template. This section must always follow the template format version
section.

The value for the description declaration must be a literal string that is between 0 and
1024 bytes in length. You cannot use a parameter or function to specify the description. The
following snippet is an example of a description declaration:

###### Important

During a stack update, you cannot update the `Description` section by
itself. You can update it only when you include changes that add, modify, or delete
resources.

## JSON

```
"Description" : "Here are some details about the template."
```

## YAML

```
Description: > Here are some details about the template.
```
