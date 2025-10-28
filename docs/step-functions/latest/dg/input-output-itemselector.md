# ItemSelector (Map)

###### Managing state and transforming data

Learn about [Passing data between states with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

By default, the effective input for the `Map` state is the set of individual
data items present in the raw state input. With the `ItemSelector` field, you can
override the data items’ values before they’re passed on to the `Map` state.

To override the values, specify a valid JSON input that contains a collection of key-value
pairs. The pairs can be static values provided in your state machine definition, values
selected from the state input using a [path](amazon-states-language-paths.md "amazon-states-language-paths.md"), or values accessed from the [Context
object](input-output-contextobject.md "input-output-contextobject.md").

If you specify key-value pairs using a path or Context object, the key name must end in `.$`.

###### Note

The `ItemSelector` field replaces the `Parameters` field within the
`Map` state. If you use the `Parameters` field in your
`Map` state definitions to create custom input, we recommend that you replace
them with `ItemSelector`.

You can specify the `ItemSelector` field in both
an
_Inline Map state_ and
a
_Distributed Map state_.

For example, consider the following JSON input that contains an array of three items
within the `imageData` node. For each _`Map` state iteration_, an array item is passed to the iteration as input.

```
[
  {
    "resize": "true",
    "format": "jpg"
  },
  {
    "resize": "false",
    "format": "png"
  },
  {
    "resize": "true",
    "format": "jpg"
  }
]
```

Using the `ItemSelector` field, you can define a custom JSON input to override
the original input as shown in the following example. Step Functions then passes this custom input to
each _`Map` state iteration_. The custom input contains a static value for `size` and the value of a Context object data for `Map` state. The
`$$.Map.Item.Value` Context object contains the value of each individual data
item.

```
{
  "ItemSelector": {
    "size": 10,
    "value.$": "$$.Map.Item.Value"
  }
}
```

The following example shows the input received by one
iteration
of the _Inline Map state_:

```
{
  "size": 10,
  "value": {
    "resize": "true",
    "format": "jpg"
  }
}
```

###### Tip

For a complete example of a _Distributed Map state_ that uses the `ItemSelector` field, see [Copy large-scale CSV using Distributed Map](tutorial-map-distributed.md "tutorial-map-distributed.md").
