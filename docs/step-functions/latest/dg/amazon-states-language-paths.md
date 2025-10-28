# Using JSONPath paths

###### Managing state and transforming data

Learn about [Passing data between states with variables](workflow-variables.md "workflow-variables.md") and [Transforming data with JSONata](transforming-data.md "transforming-data.md").

In the Amazon States Language, a _path_ is a string beginning with `$` that
you can use to identify components within JSON text. Paths follow [JsonPath](https://datatracker.ietf.org/wg/jsonpath/about/ "https://datatracker.ietf.org/wg/jsonpath/about/") syntax, which is only available when the `QueryLanguage` is set to JSONPath. You can specify a path
to access subsets of the input when specifying values for `InputPath`,
`ResultPath`, and `OutputPath`.

You must use square bracket notation if your field name contains any
character that is not included in the `member-name-shorthand`
definition of the [JsonPath ABNF](https://www.ietf.org/archive/id/draft-ietf-jsonpath-base-21.html#jsonpath-abnf "https://www.ietf.org/archive/id/draft-ietf-jsonpath-base-21.html#jsonpath-abnf") rule. Therefore, to encode special
characters, such as punctuation marks (excluding `_`), you
must use square bracket notation. For example, `$.abc.['def ghi']`.

## Reference Paths

A _reference path_ is a path whose syntax is limited in such a way that it can identify only a single node in a JSON structure:

- You can access object fields using only dot (`.`) and square bracket (`[ ]`) notation.
- Functions such as `length()` aren't supported.
- Lexical operators, which are non-symbolic, such as `subsetof` aren't supported.
- Filtering by regular expression or by referencing another value in the JSON structure is not supported.
- The operators `@`, `,`, `:`, and `?` are not supported

For example, if state input data contains the following values:

```
{
  "foo": 123,
  "bar": ["a", "b", "c"],
  "car": {
      "cdr": true
  }
}
```

The following reference paths would return the following.

```
$.foo => 123
$.bar => ["a", "b", "c"]
$.car.cdr => true

```

Certain states use paths and reference paths to control the flow of a state machine or configure a state's settings or options. For more information,
see [Modeling workflow input and output path processing with
data flow simulator](https://aws.amazon.com/blogs/compute/modeling-workflow-input-output-path-processing-with-data-flow-simulator/ "https://aws.amazon.com/blogs/compute/modeling-workflow-input-output-path-processing-with-data-flow-simulator/") and
[Using JSONPath effectively in AWS Step Functions](https://aws.amazon.com/blogs/compute/using-jsonpath-effectively-in-aws-step-functions/ "https://aws.amazon.com/blogs/compute/using-jsonpath-effectively-in-aws-step-functions/").

### Flattening an array of arrays

If the [Parallel workflow state](state-parallel.md "state-parallel.md") or [Map workflow state](state-map.md "state-map.md") state in your state machines return an array of arrays, you can transform them into a flat array with the [ResultSelector](input-output-inputpath-params.md#input-output-resultselector "input-output-inputpath-params.md#input-output-resultselector") field. You can include this field inside the Parallel or Map state definition to manipulate the result of these states.

To flatten arrays, use the syntax: `[*]` in the `ResultSelector` field as shown in the following example.

```
"ResultSelector": {
    "flattenArray.$": "$[*][*]"
  }
```

For examples that show how to flatten an array, see _Step 3_ in the following tutorials:

- [Processing batch data with a Lambda function in Step Functions](tutorial-itembatcher-param-task.md "tutorial-itembatcher-param-task.md")
- [Processing individual items with a Lambda function in Step Functions](tutorial-itembatcher-single-item-process.md "tutorial-itembatcher-single-item-process.md")
