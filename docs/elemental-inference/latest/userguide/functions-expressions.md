

# Writing function expressions
<a name="functions-expressions"></a>

A function has two expressions, both written in [JSONata](https://jsonata.org/), an open-source query and transformation language for JSON. Elemental Inference uses the same JSONata implementation as AWS Elemental MediaTailor functions, so expressions look familiar if you have written one for MediaTailor. The set of allowed built-in functions differs; see [Allowed built-in functions](functions-jsonata-allowed.md).


| Expression | Evaluated against | Must produce | 
| --- | --- | --- | 
| Request expression | The media object. See [What a function can read](functions-context.md). | For a model target, a JSON object that is a valid request body for the model's InvokeModel API. For a passthrough target, any JSON value. | 
| Response expression | The result, as its root ($) – the raw model response body for a model target, or the output of the request expression for a passthrough target. | Any JSON. This is what Elemental Inference stores on the metadata timeline. | 

**Important**  
`media` is in scope only in the request expression. A response expression that references `media.frames` resolves to nothing, without an error.

When you create a function, or update its expressions or target, Elemental Inference checks that both expressions are valid JSONata and that the context the request expression references is consistent. It also runs the request expression against sample context, under the same limits that apply on a feed, and rejects the function if the expression fails or produces an unusable result:
+ For a model target, the result must be a JSON object. The response expression is checked for syntax only, because Elemental Inference can't predict the model's response.
+ For a passthrough target, the response expression also runs, and the final result must have a value.

The sample can't reach every branch of a conditional expression, so a function that saves can still fail at run time. Elemental Inference doesn't validate the request body against the model: the reference for the body shape is the Amazon Bedrock documentation for the model you chose. A body that the model rejects appears as a failed run — no metadata for that window — not as an error when you save the function.

**Topics**
+ [Placing media in the request](functions-expressions-media.md)
+ [Request expression examples by model family](functions-expressions-request.md)
+ [Response expressions](functions-expressions-response.md)
+ [Passthrough functions](functions-expressions-passthrough.md)
+ [Expression limits and guardrails](functions-expressions-guardrails.md)