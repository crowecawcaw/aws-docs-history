# Error retries for EBS direct APIs

The **AWS SDKs** implement automatic retry logic for
requests that return error responses. You can configure the retry settings for the AWS
SDKs. For more information, see your SDK's documentation.

You can configure the **AWS CLI** to automatically retry some
failed requests. For more information about configuring retries for the AWS CLI, see [AWS CLI
retries](../../../cli/latest/userguide/cli-configure-retries.md "../../../cli/latest/userguide/cli-configure-retries.md") in the _AWS Command Line Interface User Guide_.

The **AWS Query API** does not support retry logic for
failed requests. If you are using HTTP or HTTPS requests, you must implement retry logic
in your client application.

The following table shows the possible API error responses. Some API errors are
retryable. Your client application should always retry failed requests that receive a
retryable error.

| Error                                                            | Response code | Description                                                                                                                                                                                                                                                | Thrown by        | Retryable?       |
| ---------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------- | --- |
| `InternalServerException`                                        | 500           | The request failed due to a network or AWS server-side issue.                                                                                                                                                                                              | All APIs         | Yes              |
| `ThrottlingException`                                            | 400           | The number of API requests has exceeded the maximum allowed API request<br>throttling limit for the account.                                                                                                                                               | All APIs         | Yes              |
| `RequestThrottleException`                                       | 400           | The number of API requests has exceeded the maximum allowed API request<br>throttling limit for the snapshot.                                                                                                                                              | GetSnapshotBlock | PutSnapshotBlock | Yes |
| `ValidationException` with message "`Failed to read block data`" | 400           | The provided data block was not readable.                                                                                                                                                                                                                  | PutSnapshotBlock | Yes              |
| `ValidationException` with any other message                     | 400           | The request syntax is malformed, or the input does not satisfy the constraints<br>specified by the AWS service.                                                                                                                                            | All APIs         | No               |
| `ResourceNotFoundException`                                      | 404           | The specified snapshot ID does not exist.                                                                                                                                                                                                                  | All APIs         | No               |
| `ConflictException`                                              | 409           | The specified client token was previously used in a similar request that had different request<br>parameters. For more information, see [Ensure idempotency in StartSnapshot API requests](ebs-direct-api-idempotency.md "ebs-direct-api-idempotency.md"). | StartSnapshot    | No               |
| `AccessDeniedException`                                          | 403           | You do not have permission to perform the requested operation.                                                                                                                                                                                             | All APIs         | No               |
| `ServiceQuotaExceededException`                                  | 402           | The request failed because fulfilling the request would exceed one or more dependent service<br>quotas for your account.                                                                                                                                   | All APIs         | No               |
| `InvalidSignatureException`                                      | 403           | The request authorization signature has expired. You can retry the request only<br>after refreshing the authorization signature.                                                                                                                           | All APIs         | No               |
