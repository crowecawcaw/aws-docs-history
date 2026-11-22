

# Error Handling in the IVS Linux Broadcast SDK \| Real-Time Streaming

This section is an overview of error conditions, how the IVS real-time streaming Linux broadcast SDK reports them to your application, and what you should do when you encounter those errors.

## Fatal Versus Non-Fatal Errors
<a name="broadcast-linux-fatal-vs-nonfatal-errors"></a>

The error object has an "is fatal" boolean field: `is_fatal` on `aws_ivs_realtime_error` in C, and `IsFatal` on `Error` in Go.

In general, fatal errors are related to connection to the Stages server (either a connection cannot be established or is lost and cannot be recovered). You should re-create the stage and rejoin, possibly with a new token or when your network connection recovers.

Non-fatal errors generally are related to the publish/subscribe state and are handled by the SDK, which retries the publish/subscribe operation.

The error object also has a code and a type. Codes are unique. The type is the category of the error, for example `NETWORK` or `AUTHORIZATION`. Many codes share one type, so match on the type to handle a group of errors together. For the other fields, see the API documentation.

The SDK reports errors in two ways:
+ A function that fails returns `false` in C and writes the error to `out_error`. You own that error and free it with `aws_ivs_realtime_error_destroy`. In Go, the function returns an `error` whose concrete type is `*realtime.Error`.
+ A callback receives an error that the SDK owns. In C, do not free it.

The errors that the documentation lists for a function are not exhaustive. For an error you do not handle by code, use "is fatal" to decide whether you can still use the stage, and log the code and message.

You can check this property:

------
#### [ C ]

```c
if (!aws_ivs_realtime_stage_join(stage, &error)) {
    if (error->is_fatal) {
        // the error is fatal
    }
    aws_ivs_realtime_error_destroy(error);
}
```

------
#### [ Go ]

```go
if err := stage.Join(); err != nil {
    var sdkErr *realtime.Error
    if errors.As(err, &sdkErr) && sdkErr.IsFatal {
        // the error is fatal
    }
}
```

------

## IVS Linux Broadcast SDK Error Codes
<a name="broadcast-linux-error-codes"></a>

Every error has a unique code. The public codes, with a description of each, are in:
+ C: The `aws_ivs_realtime_error_code` enum in `aws_ivs_realtime_errors.h`.
+ Go: The `ErrorCode` constants in the `realtime` package.