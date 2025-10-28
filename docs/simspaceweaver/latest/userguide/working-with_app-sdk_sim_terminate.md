End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Terminate a simulation

Use `Result<void> DestroyApplication(Application&& app)`
to terminate the app and the simulation.

Other apps find out that the simulation is shutting down when they receive
`ErrorCode::ShuttingDown` from their calls to `BeginUpdateWillBlock()`
or `BeginUpdate()`. When an app receives `ErrorCode::ShuttingDown`,
it can call `Result<void> DestroyApplication(Application&& app)`
to terminate itself.

###### Example

```
Result<void> AppDriver::EncounteredAppError(Application&& application) noexcept
{
    const ErrorCode errorCode = WEAVERRUNTIME_EXPECT_ERROR(runAppResult);

    switch (errorCode)
    {
    case ErrorCode::ShuttingDown:
        {
            // insert custom shutdown process here.

            WEAVERRUNTIME_TRY(Api::DestroyApplication(std::move(application)));
            return Success();
        }
    default:
        {
            OnAppError(errorCode);
            return errorCode;
        }
    }
}

```

###### Important

Only call `Result<void> DestroyApplication(Application&& app)`
after `Api::Commit()`. Destroying an application during an update can
cause undefined behavior.

###### Important

You must call `DestroyApplication()` before the program exits to make sure
that the application reports as terminating successfully.

Failure to call `DestroyApplication()` when the program exits will cause
the status to be considered as `FATAL`.
