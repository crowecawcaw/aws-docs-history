# Invoking a tool

If Amazon Nova decides to call a tool, a tool use block will be returned as a part of the assistant message and the stop reason will be "tool_use". The tool block will contain the name of the tool and it's inputs.

###### Note

To improve the accuracy of tool calls, the default behavior of Amazon Nova models is to use chain-of-thought reasoning for tool calling. The thought process will be made available to you in the assistant message and will be contained in <thinking> tags. It is possible to have multiple tool calls and thinking blocks in a response so your application should take this into account.

If tool choice is configured to `any` or `tool`, this will override the chain-of-thought behavior and the response will only contain the necessary tool calls.

```
`{
 "toolUse":
 {
 "toolUseId": "tooluse_20Z9zl0BQWSXjFuLKdTJcA",
 "name": "top_song",
 "input": {
 "sign": "WZPZ"
 }
 }
}`
```

To actually call the tool, the tool name and arguments can be extracted from the message and the application can then invoke it.

Here is an example for how you can process a tool call.

```
`def get_top_song(sign):
 print(f"Getting the top song at {sign}")
 return ("Espresso", "Sabrina Carpenter")

stop_reason = response["stopReason"]

tool, song, artist = None, None, None
if stop_reason == "tool_use":
 thought_process = next(
 block["text"]
 for block in response["output"]["message"]["content"]
 if "text" in block
 )

 print(thought_process)

 tool = next(
 block["toolUse"]
 for block in response["output"]["message"]["content"]
 if "toolUse" in block
 )

 if tool["name"] == "top_song":
 song, artist = get_top_song(tool["input"]["sign"])`
```

It is important to keep security in mind when you are defining and invoking tools. LLMs like Amazon Nova do not have access to the session details so permissions should be validated when necessary before invoking a tool. Rely on user details from your session instead of augmenting the prompt and allowing Amazon Nova to inject it into the tool call.
