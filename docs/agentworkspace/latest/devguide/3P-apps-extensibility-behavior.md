

# Interceptor behavior in Connect Customer agent workspace
<a name="3P-apps-extensibility-behavior"></a>

The following rules describe how the framework evaluates interceptors at runtime:
+ **Multiple interceptors** – When you register multiple interceptors for the same key, the framework runs them in sequence, one at a time. Evaluation stops at the first interceptor that blocks the action or fails. If an interceptor returns `{ continue: false }`, the framework blocks the action and does not run the remaining interceptors, unless that interceptor has reached its `maxConsecutiveBlocks` limit. In that case, the framework treats the result as `{ continue: true }` and runs the next interceptor.
+ **Thrown error** – If your interceptor throws an error, the framework stops the evaluation and skips the remaining interceptors. The agent sees an error alert, and the default action proceeds.
+ **Invalid return value** – If your interceptor returns a value that is not a `boolean` or an object with a `continue` property, the framework treats it like a thrown error. The remaining interceptors are skipped, the agent sees an error alert, and the default action proceeds.
+ **Timeout** – If your interceptor does not resolve within its timeout, the framework treats it as if it returned `{ continue: true }` and runs the next interceptor.