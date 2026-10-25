

# Response expressions
<a name="functions-expressions-response"></a>

The response expression runs against the raw response body of the model, as its root. Its job is to reduce that body to the value you actually want on the timeline.

Where the generated text lives in that body depends on the model family. For an Anthropic Claude model, it is in the first `content` block of type `text`. Some Claude models return a `thinking` block before it, so select the block by type rather than by position.

```
{ "result": content[type = "text"][0].text }
```

For any other family, take the path from the response syntax in the Amazon Bedrock documentation for that model. If you aren't sure, create the function without a response expression, let it run once, and read the stored value: it is the whole response body, which shows you the path to use. Then add the expression with `UpdateFunction`.

You can keep more than the text – for example, the token usage, so you can correlate spend with content.

```
{
  "summary": content[type = "text"][0].text,
  "outputTokens": usage.output_tokens
}
```

If you asked the model to answer in JSON, parse its text so that the stored value is structured data rather than a string containing JSON.

```
$parse(content[type = "text"][0].text)
```

Omitting the response expression stores the whole model response, including its metadata fields. That is useful while you are developing a function, and wasteful in production.

A response expression that evaluates to nothing stores `null` for that window. It doesn't remove the window from the timeline.