# Reporting an error

There are some instances where the parameters selected by Amazon Nova can cause an external error. It can be beneficial then to communicate this back to Amazon Nova so the request can be modified and retried. To notify about errors, still return a tool result but modify the status to report the error and share the exception message.

Here is an example that reports an error status message:

```
`tool_result_message = {
 "role": "user",
 "content": [
 {
 "toolResult": {
 "toolUseId": tool["toolUseId"],
 "content": [{"text": "A validation exception occured on field: sample.field"}],
 "status": "error"
 }
 }
 ]
}`
```
