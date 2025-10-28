# Error codes with ErrorDetail

information in Amazon EMR

When an EMR cluster terminates with an error, the `DescribeCluster` and
`ListClusters` APIs return an error code and an error message. For some
cluster errors, the `ErrorDetail` data array can help you troubleshoot the
failure.

Errors that include an `ErrorDetail` array provide the following
details:

**`ErrorCode`**

A unique error code that you can use for programmatic access.

**`ErrorData`**

A list of identifiers in key-value pairs that you can use for programming or
manual lookup. For descriptions of the `ErrorData` values that an
error code includes, see the troubleshooting page for the error code.

**`ErrorMessage`**

Description of the error with a link to more information in the Amazon EMR
documentation.

###### Note

We don’t recommend that you parse the text from `ErrorMessage`
because this text is subject to change.

###### Error codes by category

- [Bootstrap failures](emr-troubleshoot-error-errordetail-bootstrap.md "emr-troubleshoot-error-errordetail-bootstrap.md")
- [Internal errors](emr-troubleshoot-error-errordetail-internal.md "emr-troubleshoot-error-errordetail-internal.md")
- [Validation failures](emr-troubleshoot-error-errordetail-validation.md "emr-troubleshoot-error-errordetail-validation.md")
