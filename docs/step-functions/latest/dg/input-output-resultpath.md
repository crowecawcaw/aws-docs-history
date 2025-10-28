# Specifying state output using ResultPath in Step Functions

###### Managing state and transforming data

This page refers to JSONPath. Step Functions recently added variables and JSONata to manage state and transform data.

Learn about [Passing data with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

The output of a state can be a copy of its input, the result it produces (for example,
output from a `Task` state’s Lambda function), or a combination of its input and
result. Use `ResultPath` to control which combination of these is passed to the state
output.

The following state types can generate a result and can include
`ResultPath:`

- [Pass workflow state](state-pass.md "state-pass.md")
- [Task workflow state](state-task.md "state-task.md")
- [Parallel workflow state](state-parallel.md "state-parallel.md")
- [Map workflow state](state-map.md "state-map.md")
  Use `ResultPath` to combine a task result with task input, or to select one of
  these. The path you provide to `ResultPath` controls what information passes to the
  output.

###### Note

`ResultPath` is limited to using [reference paths](amazon-states-language-paths.md#amazon-states-language-reference-paths "amazon-states-language-paths.md#amazon-states-language-reference-paths"), which limit
scope so the path must identify only a single node in JSON. See [Reference Paths](amazon-states-language-paths.md#amazon-states-language-reference-paths "amazon-states-language-paths.md#amazon-states-language-reference-paths") in the [Amazon States Language](concepts-amazon-states-language.md "concepts-amazon-states-language.md").

## Use ResultPath to replace input with the

task result

If you do not specify a `ResultPath`, the default behavior is the same as
`"ResultPath": "$"`. The state will replace the entire state input with the
result from the task.

```
# State Input
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions"
}

# Path
"ResultPath": "$"

# Task result
"Hello, Step Functions!"

# State Output
"Hello, Step Functions!"
```

###### Note

`ResultPath` is used to include content from the result with the input,
before passing it to the output. But, if `ResultPath` isn't specified,
the default action is to replace the entire input.

## Discard the result and keep the original input

If you set `ResultPath` to `null`, the state will pass the **original input** to the output. The state's input payload will be
copied directly to the output, with no regard for the task result.

```
# State Input
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions"
}

# Path
"ResultPath": null

# Task result
"Hello, Step Functions!"

# State Output
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions"
}
```

## Use ResultPath to include the result with the

input

If you specify a path for ResultPath, the state output will combine the state input
and task result:

```
# State Input
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions"
}

# Path
"ResultPath": "$.taskresult"

# Task result
"Hello, Step Functions!"

# State Output
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions",
 "taskresult" : "Hello, Step Functions!"
}
```

You can also insert the result into a child node of the input. Set the
`ResultPath` to the following.

```
"ResultPath": "$.strings.lambdaresult"
```

Given the following input:

```
{
  "comment": "An input comment.",
  "strings": {
    "string1": "foo",
    "string2": "bar",
    "string3": "baz"
  },
  "who": "AWS Step Functions"
}
```

The task result would be inserted as a child of the `strings` node in the
input.

```
{
  "comment": "An input comment.",
  "strings": {
    "string1": "foo",
    "string2": "bar",
    "string3": "baz",
    "lambdaresult": "Hello, Step Functions!"
  },
  "who": "AWS Step Functions"
}
```

The state output now includes the original input JSON with the result as a child
node.

## Use ResultPath to update a node in the input

with the result

If you specify an existing node for ResultPath, the task result will replace that
existing node:

```
# State Input
{
 "comment": "This is a test",
 "details": "Default example",
 "who" : "Step Functions"
}

# Path
"ResultPath": "$.comment"

# Task result
"Hello, Step Functions!"

# State Output
{
 "comment": "Hello, Step Functions!",
 "details": "Default example",
 "who" : "Step Functions"
}
```

## Use ResultPath to include both error and input

in a `Catch`

In some cases, you might want to preserve the original input with the error. Use
`ResultPath` in a `Catch` to include the error with the original
input, instead of replacing it.

```
"Catch": [{
  "ErrorEquals": ["States.ALL"],
  "Next": "NextTask",
  "ResultPath": "$.error"
}]
```

If the previous `Catch` statement catches an error, it includes the result in
an `error` node within the state input. For example, with the following
input:

```
{"foo": "bar"}
```

The state output when catching an error is the following.

```
{
  "foo": "bar",
  "error": {
    "Error": "`Error here`"
  }
}
```

For more information about error handling, see the following:

- [Handling errors in Step Functions workflows](concepts-error-handling.md "concepts-error-handling.md")
- [Handling error conditions in a Step Functions
  state machine](tutorial-handling-error-conditions.md "tutorial-handling-error-conditions.md")
