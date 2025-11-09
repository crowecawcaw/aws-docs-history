# ItemsPath (Map, JSONPath only)

###### Managing state and transforming data

This page refers to JSONPath. Step Functions recently added variables and JSONata to manage state and transform data.

Learn about [Passing data with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

In JSONPath-based states, use the `ItemsPath` field to select an array or object within a JSON input provided to a `Map` state.
By default, the `Map` state sets `ItemsPath` to `$`, which selects the entire input.

- If the input to the `Map` state is a JSON array, it runs
  an iteration for each item in the array, passing that item to the iteration as input
- If the input to the `Map` state is a JSON object, it runs
  an iteration for each key-value pair in the object, passing the pair to the iteration as input

###### Note

You can use `ItemsPath` in the _Distributed Map state_
only
if you use a JSON input passed from a previous state in the
workflow.

The value of `ItemsPath` must be a [Reference Path](amazon-states-language-paths.md#amazon-states-language-reference-paths "amazon-states-language-paths.md#amazon-states-language-reference-paths"), and
that path must evaluate to a JSON array or object. For instance, consider input to a
`Map` state that includes two arrays, like the following example.

```
{
  "ThingsPiratesSay": [
    {
      "say": "Avast!"
    },
    {
      "say": "Yar!"
    },
    {
      "say": "Walk the Plank!"
    }
  ],
  "ThingsGiantsSay": [
    {
      "say": "Fee!"
    },
    {
      "say": "Fi!"
    },
    {
      "say": "Fo!"
    },
    {
      "say": "Fum!"
    }
  ]
}
```

In this case, you could specify which array to use for `Map` state
iterations by selecting
it
with `ItemsPath`. The following state machine definition specifies the
`ThingsPiratesSay` array in the input using
`ItemsPath`.It
then
runs
an iteration of the `SayWord` pass state for each item in the
`ThingsPiratesSay` array.

```
{
  "StartAt": "PiratesSay",
  "States": {
    "PiratesSay": {
      "Type": "Map",
      "ItemsPath": "$.ThingsPiratesSay",
      "ItemProcessor": {
         "StartAt": "SayWord",
         "States": {
           "SayWord": {
             "Type": "Pass",
             "End": true
           }
         }
      },
      "End": true
    }
  }
}
```

For nested JSON objects, you can use `ItemsPath` to select a specific object within the input. Consider the following input with nested configuration data:

```
{
  "environment": "production",
  "servers": {
    "web": {
      "server1": {"port": 80, "status": "active"},
      "server2": {"port": 8080, "status": "inactive"}
    },
    "database": {
      "primary": {"host": "db1.example.com", "port": 5432},
      "replica": {"host": "db2.example.com", "port": 5432}
    }
  }
}
```

To iterate over the web servers object, you would set `ItemsPath` to `$.servers.web`:

```
{
  "StartAt": "ProcessWebServers",
  "States": {
    "ProcessWebServers": {
      "Type": "Map",
      "ItemsPath": "$.servers.web",
      "ItemProcessor": {
         "StartAt": "CheckServer",
         "States": {
           "CheckServer": {
             "Type": "Pass",
             "End": true
           }
         }
      },
      "End": true
    }
  }
}
```

When processing input,
the
`Map` state applies
`ItemsPath`
after [InputPath](input-output-inputpath-params.md#input-output-inputpath "input-output-inputpath-params.md#input-output-inputpath"). It operates
on the effective input to the
state after
`InputPath`
filters
the input.

For more information on `Map` states, see the following:

- [Map state](state-map.md "state-map.md")
- [Map state processing modes](state-map.md#concepts-map-process-modes "state-map.md#concepts-map-process-modes")
- [Repeat actions with Inline Map](tutorial-map-inline.md "tutorial-map-inline.md")
- [Inline Map state
  input and output processing](state-map-inline.md#inline-map-state-output "state-map-inline.md#inline-map-state-output")
