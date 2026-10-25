

# Updating a function
<a name="functions-managing-update"></a>

`update-function` changes only the fields that you send, so you don't have to resend the whole function. You can't remove a response expression after you set it; replace it with another expression, or create a new function without one. In the console, open the function and choose **Edit**.

```
aws elemental-inference update-function \
  --region {{us-west-2}} \
  --id {{function-id}} \
  --response-expression '{ "description": content[type = "text"][0].text, "tokens": usage.output_tokens }'
```

Elemental Inference checks an update the same way it checks a new function. See [Creating a function](functions-create.md). Changing a request expression re-derives `contextTypes`. While a feed references the function, an update that would change `contextTypes` fails with `ValidationException`, because each feed's trigger and source outputs are set up for the current media context. To change the media context, detach the function from its feeds, update it, and attach it again.

**Important**  
A function is shared. Editing one that several feeds use changes the behavior of all of them, with no change to the feeds. If you want to try a change on one feed first, copy the function and attach the copy.

To change the name or the target of a function that is in use, detach it from every feed first, or create a new function and move the feeds to it.