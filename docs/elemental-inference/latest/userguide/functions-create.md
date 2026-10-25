

# Creating a function
<a name="functions-create"></a>

A function is an account-level resource. Creating one has no effect on any feed and starts no processing – you attach it to a feed in a separate step, described in [Attaching a function to a feed](functions-attach.md).

A function has the following properties.


| Property | Required | Description | 
| --- | --- | --- | 
| name | Yes | 1–128 characters. Must begin and end with a letter or a number, and can contain letters, numbers, hyphens, and underscores. | 
| target | Yes | Either bedrock (invoke an Amazon Bedrock model) or passthrough (invoke nothing). | 
| requestExpression | Yes | JSONata that builds the request. 1–5,120 characters. See [Writing function expressions](functions-expressions.md). | 
| responseExpression | No | JSONata that selects what to keep from the result. 1–5,120 characters. If you omit it, Elemental Inference stores the whole result. | 
| description | No | Up to 1,024 characters. Can contain letters, numbers, spaces, underscores, and the characters - . , ' @ : ; | 
| tags | No | Tags for the function. You can set them only when you create the function; after that, use TagResource and UntagResource. | 

For a `bedrock` target you also specify the following.
+ `api` – the Amazon Bedrock API to call. `INVOKE_MODEL` is the only value.
+ `model` – a model ID, an inference profile ID, or the ARN of a custom or provisioned model. Elemental Inference invokes the model in the feed's Region. To use a model in other Regions, specify a cross-Region inference profile ID. A custom or provisioned model must be in the feed's Region.

The response to a create or get request also includes fields that Elemental Inference computes and that you can't set.
+ `id` and `arn` – the identifier of the function. You use the ARN when you attach the function to a feed.
+ `status` – see [Function status](functions-managing-lifecycle.md).
+ `references` – the IDs of the feeds that currently use this function.
+ `contextTypes` – the media context that Elemental Inference derived from your request expression. See [What a function can read](functions-context.md).

When you create or update a function, Elemental Inference rejects it with a `ValidationException` unless the following are true.
+ Both expressions are valid JSONata.
+ The request expression reads at most one of `media.transcript`, `media.contextual`, and `media.clip`. It can combine that one with `media.frames` and `media.video`.
+ A passthrough request expression doesn't read `media.frames` or `media.video`. There is no model to send them to.
+ The request expression runs without error against sample media context. For a `bedrock` target, it must produce a JSON object, because it becomes the request body. For a `passthrough` target, the request expression, followed by the response expression if there is one, must produce a value. A `bedrock` response expression is checked for syntax only, because the model response isn't known until the function runs.

**Topics**
+ [Creating a function using the console](functions-create-console.md)
+ [Creating a function using the CLI](functions-create-cli.md)