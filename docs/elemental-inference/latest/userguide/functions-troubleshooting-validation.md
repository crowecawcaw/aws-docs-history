

# `ValidationException`, `ConflictException`, and `ServiceQuotaExceededException` errors

Elemental Inference returns `ValidationException`, `ConflictException`, or `ServiceQuotaExceededException` when it rejects a request to create, update, or delete a function, or to create or update a feed that has a function output. The following tables list the causes of each error and what to do about them.

**Creating or updating a function**

When you save a function, Elemental Inference checks the syntax of both expressions and runs the request expression against sample media. For a passthrough function, it also runs the response expression on the result. For a model target, the response expression is checked for syntax only, so an error in it appears only when the function runs on a feed. The following table lists the errors.


| Cause | Error | What to do | 
| --- | --- | --- | 
| An expression isn't valid JSONata. | ValidationException | The message names the expression that failed, followed by the parser's error. Unbalanced braces and a missing comma between object fields are the common causes. | 
| An expression is nested too deeply. | ValidationException | Flatten it. Bind intermediate values with := instead of nesting them. | 
| The request expression, or a passthrough function's response expression, is valid JSONata but fails when it runs. | ValidationException | The message gives the reason and, for a guardrail, its code. Common causes are a built-in function that isn't on the allowlist, a guardrail limit, and a media value that is altered or placed more than once. For more information about allowed built-in functions and guardrails, see [Allowed built-in functions](functions-jsonata-allowed.md) and [Expression limits and guardrails](functions-expressions-guardrails.md). | 
| For a model target, the request expression doesn't produce a JSON object. | ValidationException | The request body sent to the model must be an object. The message reports what the expression produced instead. A path that doesn't exist produces no value rather than an error, so check the paths the expression reads. | 
| A passthrough function produces no value: the request expression yields nothing, or the response expression yields nothing when applied to the request expression's result. | ValidationException | Such a function would never write metadata. Make the response expression read the fields that the request expression builds. A model-style path such as $.output.text finds nothing in a passthrough result. | 
| The request expression references two feature contexts – two of media.transcript, media.contextual, and media.clip. | ValidationException | Reading data from more than one existing feature is not supported. Split the work into two functions. You can combine any one of them with media.frames. | 
| A passthrough function references media.frames. | ValidationException | A passthrough function invokes no model, so it can't send media anywhere. Remove the reference, or change the target to a model. | 
| The name, model, or description doesn't match its required pattern or length. | ValidationException | For information about the required patterns and lengths, see the property table in [Creating a function](functions-create.md). | 
| You changed the name or the target of a function that a feed is using. | ValidationException | Remove the function output from every feed that uses the function, or create a new function. | 
| You changed which media context the request expression reads while a feed is using the function. | ValidationException | Each feed's trigger and source outputs are set up for the function's current context. Remove the function output from the feeds, update the function, then add the output again. | 
| You deleted a function that a feed is using. | ConflictException | The message reports how many feeds hold it, and the function's references field lists them. Remove the function output from each of those feeds. A disabled function output still holds the reference. | 

**Creating or updating a feed with a function output**

The following table lists the errors. Unless the table says otherwise, the error is `ValidationException`.


| Message reports | What to do | 
| --- | --- | 
| The function ARN isn't a valid function ARN. | Check the ARN. It must have the form arn:aws:elemental-inference:{{region}}:{{account}}:function/{{id}}. | 
| The function can't be found. | Confirm that the function exists in the same AWS Region as the feed. | 
| The function belongs to a different AWS account. | A feed can reference only functions in its own account. Create the function in the feed's account. | 
| The function output invokes a model, so the feed must specify an accessRoleArn. | Add accessRoleArn to the request. For more information, see [Setting up the access role](functions-prerequisites-access-role.md). | 
| A feed with an enabled function output must also have an enabled cropping, clipping, subtitling, or contextual metadata output. | Enable a smart crop, event clipping, smart subtitles, or contextual metadata output on the feed, or disable the function output. | 
| The function uses transcript context but names no subtitling output, or names one that isn't an enabled subtitling output on this feed. | Add subtitlingSettings.outputName, and confirm that the output it names is a smart subtitles output on this feed with "status": "ENABLED". | 
| Transcript context isn't supported with this trigger. | A transcript function must use fixedInterval. | 
| Contextual metadata context is only available on a perScene or perShot trigger. | Use perScene, or perShot with contextualMetadataSettings.outputName set. | 
| The scene or contextual metadata source isn't set, or isn't an enabled contextual metadata output. | Add contextualMetadataSettings.outputName, naming an enabled contextual metadata output on this feed. | 
| Clip context is only available on a perClip or fixedInterval trigger, or the clipping source isn't set. | Use perClip or fixedInterval, and set clippingSettings.outputName to an enabled event clipping output on this feed. | 
| The output requests more frame media than fits a single inference request. | The frames are too large for one model request. Reduce the frameSettings count or set a smaller frameSettings.frameSize. | 
| ServiceQuotaExceededException for enabled function outputs. | Disable a function output, or request a quota increase. For more information, see [AWS Elemental Inference function quotas](functions-quotas.md). | 
| ServiceQuotaExceededException for enabled outputs, or for outputs enabled and disabled combined. | Disable or remove another output. These quotas can't be increased. For more information, see [AWS Elemental Inference function quotas](functions-quotas.md). | 