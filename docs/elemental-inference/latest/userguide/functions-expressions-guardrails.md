

# Expression limits and guardrails

Expressions run in a sandbox with an allowlist of built-in functions and always-on limits on CPU time, memory, and stack depth. The limits apply to the sample run when you save the function and to every run on a feed. The following table lists the limits and guardrails.


| Limit | Value | 
| --- | --- | 
| Length of each expression | 1–5,120 characters | 
| CPU time for each evaluation | 1,000 ms | 
| Memory allocated during each evaluation | 10 MB | 
| Stack depth | 100 | 
| Size of the request after media substitution | 25 MB | 
| Nodes visited while substituting media | 16,384 | 
| Placing the same frame or clip more than once | Not allowed | 
| Altering a media value instead of placing it whole | Not allowed | 
| Built-in functions | Allowlisted. For more information, see [Allowed built-in functions](functions-jsonata-allowed.md). | 

A run that breaks a guardrail produces no metadata for that window, and logs the reason. For more information, see [Function error codes and other causes of missing metadata](functions-troubleshooting-runtime.md).