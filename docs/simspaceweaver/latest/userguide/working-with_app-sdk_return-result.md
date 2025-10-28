End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# API methods return a Result

The majority of SimSpace Weaver API functions have a return type
`Aws::WeaverRuntime::Result<T>`. If the function has
executed successfully, the `Result` contains `T`.
Otherwise, the `Result` contains an `Aws::WeaverRuntime::ErrorCode`
that represents an error code from the Rust App SDK.

###### Example

```
Result<Transaction> BeginUpdate(Application& app)

```

This method:

- Returns `Transaction` if `BeginUpdate()` executes successfully.
- Returns `Aws::WeaverRuntime::ErrorCode` if `BeginUpdate()` fails.
