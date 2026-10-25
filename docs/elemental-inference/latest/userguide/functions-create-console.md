

# Creating a function using the console
<a name="functions-create-console"></a>

1. Open the [Elemental Inference console](https://console.aws.amazon.com/elemental-inference/).

1. In the left navigation bar, choose **Functions**, then choose **Create function**.

1. In **Start from a template**, choose a starting point. A template fills in the target and both expressions with a working example that you then edit. **Describe frames** is selected by default. Choose **Start from scratch** to begin with empty fields.


<table>
<thead>
  <tr><th>Template</th><th>What it does</th></tr>
</thead>
<tbody>
  <tr><td><b>Describe video</b></td><td>Sends a video clip (<code>media.video</code>) to a video-capable model and keeps the description.</td></tr>
  <tr><td><b>Describe frames</b></td><td>Sends sampled frames (<code>media.frames</code>) to a model that accepts images and keeps the description.</td></tr>
  <tr><td><b>Summarize transcript</b></td><td>Sends the transcript (<code>media.transcript</code>) to a model and keeps the summary.</td></tr>
  <tr><td><b>Derive metadata from a scene</b></td><td>Reshapes the contextual classification of a scene (<code>media.contextual</code>) without invoking a model. Requires a per-scene or per-shot trigger when you attach it.</td></tr>
  <tr><td><b>Derive metadata from clips</b></td><td>Reshapes the clips from an event clipping output (<code>media.clip</code>) without invoking a model. Requires a per-clip or fixed-interval trigger when you attach it.</td></tr>
</tbody>
</table>


1. In **Function settings**, enter a **Name**, and optionally a **Description**. Choose a name that will make sense in a list months from now – for example, **brand-safety-per-scene**.

1. In **Target**, choose the **Target type**: **Amazon Bedrock** to invoke a model, or **Metadata transform** for a passthrough function, which invokes no model. For **Amazon Bedrock**, also specify the following:
   + **Bedrock model ID** – start typing to see suggestions, grouped by what the model accepts (**Text, image, and video**, **Text and image**, **Text only**). The suggestions are a convenience, not a restriction: you can enter any model ID, inference profile ID, or custom or provisioned model ARN.

   If you choose a recognized model that can't accept the context your request expression uses — for example, `media.frames` on a text-only model — the console reports the mismatch and you can't save. An unrecognized model or a custom model ARN isn't checked this way.
**Note**  
If you switch to a model from a different provider while a template's expressions are still unedited, the console rewrites the expressions into that provider's request and response format, if the template has one for that provider. It never rewrites expressions that you have edited.

1. In **Expressions**, write the **Request expression** and, optionally, the **Response expression**. The **Available context variables** table above the request field lists the `media` fields you can reference and what each one requires. The console reports an error on the request field, and you can't save, if the expression reads more than one of `media.transcript`, `media.contextual`, and `media.clip`, or if a metadata transform reads `media.frames` or `media.video`. For guidance, see [Writing function expressions](functions-expressions.md).

1. Optionally, add tags.

1. Choose **Create function**. Elemental Inference checks the expressions, as described earlier in this topic, and reports any error on the field that caused it. On success, the **Functions** page appears with your new function.

Open the function to review it. The detail page shows the target type, the model, the two expressions, the feeds that reference the function, and its tags.