# Exceptions

The following table lists query-side exceptions that could be encountered while using a query.

| Neptune Analytics error code | HTTP status | Retriable | Description                                                                                                                                                                                       |
| ---------------------------- | ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Validation Exception         | 400         | No        | Something is wrong with the required information - Eg. a malformed query.                                                                                                                         |
| AccessDeniedException        | 403         | No        | User is not authorized to perform the requested operation.                                                                                                                                        |
| ResourceNotFoundException    | 404         | No        | Requested resource is not available.                                                                                                                                                              |
| ThrottlingException          | 429         | Yes       | The server has received too many concurrent requests.                                                                                                                                             |
| InternalServerErrorException | 500         | Yes       | The server failed to process the request for an unknown reason.                                                                                                                                   |
| UnprocessableException       | 422         | No        | Request cannot be processed due to known reasons - Eg. The query timed out.                                                                                                                       |
| ConflictException            | 409         | Yes       | Concurrently running queries attempted to modify resources or data records concurrently and the conflict could not be resolved automatically. Please retry with an exponential back-off strategy. |
