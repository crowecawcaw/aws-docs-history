

# Interceptor behavior in Connect Customer agent workspace
<a name="3P-apps-extensibility-behavior"></a>

The following rules describe how the framework evaluates interceptors at runtime:
+ **Thrown error** – If your interceptor throws an error, the framework catches it and allows the default action to proceed.
+ **Multiple interceptors** – When you register multiple interceptors for the same key, the framework evaluates all of them. If any interceptor returns `{ continue: false }`, the framework blocks the action.