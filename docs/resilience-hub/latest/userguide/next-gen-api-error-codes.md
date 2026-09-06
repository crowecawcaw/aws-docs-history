

# Error codes
<a name="next-gen-api-error-codes"></a>

The following table lists error codes returned by the next generation of Resilience Hub API.


| Error code | HTTP status | Description | 
| --- | --- | --- | 
| ValidationException | 400 | Request parameters are invalid. | 
| ResourceNotFoundException | 404 | The specified resource does not exist. | 
| ConflictException | 409 | Operation conflicts with current state (for example, an assessment is already running). | 
| AccessDeniedException | 403 | Caller lacks required permissions. | 
| ThrottlingException | 429 | Request rate exceeded. | 
| InternalServerException | 500 | Internal service error. | 
| ServiceQuotaExceededException | 402 | A service quota has been exceeded. | 