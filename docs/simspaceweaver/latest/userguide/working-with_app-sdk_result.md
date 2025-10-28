End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Result and error handling

The `Aws::WeaverRuntime::Result<T>` class uses a third-party `Outcome` library.
You can use the following pattern to check the `Result` and catch errors returned by API calls.

```
void DoBeginUpdate(Application& app)
{
    Result<Transaction> transactionResult = Api::BeginUpdate(app);

    if (transactionResult)
    {
        Transaction transaction =
            std::move(transactionResult).assume_value();

        /**
         * Do things with transaction ...
         */
    }
    else
    {
        ErrorCode errorCode = WEAVERRUNTIME_EXPECT_ERROR(transactionResult);
        /**
         * Macro compiles to:
         * ErrorCode errorCode = transactionResult.assume_error();
         */
    }
}

```

## Result control statement macro

Inside a function with a return type `Aws::WeaverRuntime::Result<T>`,
you can use the `WEAVERRUNTIME_TRY` macro instead of the previous code pattern.
The macro will execute the function passed to it. If the passed function fails, the macro
will make the enclosing function return an error. If the passed function succeeds,
execution progresses to the next line. The following example shows a rewrite of the
previous `DoBeginUpdate()` function. This version uses the
`WEAVERRUNTIME_TRY` macro instead of the if-else control
structure. Note that the return type of the function is
`Aws::WeaverRuntime::Result<void>`.

```
Aws::WeaverRuntime::Result<void> DoBeginUpdate(Application& app)
{
    /**
     * Execute Api::BeginUpdate()
     * and return from DoBeginUpdate() if BeginUpdate() fails.
     * The error is available as part of the Result.
     */
    WEAVERRUNTIME_TRY(Transaction transaction, Api::BeginUpdate(m_app));

    /**
     * Api::BeginUpdate executed successfully.
     *
     * Do things here.
     */

    return Aws::Success();
}

```

If `BeginUpdate()` fails, the macro makes `DoBeginUpdate()`
return early with a failure. You can use the `WEAVERRUNTIME_EXPECT_ERROR`
macro to get the `Aws::WeaverRuntime::ErrorCode` from `BeginUpdate()`.
The following example shows how the `Update()` function calls `DoBeginUpdate()`
and gets the error code on failure.

```
void Update(Application& app)
{
    Result<void> doBeginUpdateResult = DoBeginUpdate(app);

    if (doBeginUpdateResult)
    {
        /**
         * Successful.
         */
    }
    else
    {
        /**
         * Get the error from Api::BeginUpdate().
         */
        ErrorCode errorCode = WEAVERRUNTIME_EXPECT_ERROR(doBeginUpdateResult);

    }
}

```

You can make the error code from `BeginUpdate()` available to a function
that calls `Update()` by changing the return type of `Update()` to
`Aws::WeaverRuntime::Result<void>`. You can repeat this process to keep
sending the error code further down the call stack.
