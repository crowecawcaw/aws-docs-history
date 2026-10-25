

# Troubleshooting schedule action requests
<a name="feed-scheduling-errors"></a>

The schedule action operations can return the following errors.


| HTTP status | Exception | Cause | 
| --- | --- | --- | 
| 400 | ValidationException | The request isn't valid. For example, the start configuration isn't fixed mode; scheduledAt is missing, less than 1 hour in the future, more than 3 years in the future, or not in whole seconds; operations is empty or has more than 10 items; an operation doesn't contain exactly one member; outputName doesn't refer to an existing output, or a clipping operation targets an output that isn't an event clipping output; status isn't valid; fixtureId isn't 1–128 characters, refers to a game that Elemental Inference can't find, or isn't in a supported sport; the action's clipping operations name more than one game; the feed already has an action with the same name; the feed is archived or is a VOD feed; or, for DeleteScheduleAction, the action has already run. | 
| 402 | ServiceQuotaExceededException | The feed already has 100 schedule actions. | 
| 403 | AccessDeniedException | You don't have permission to perform the operation. For CreateScheduleAction, feed scheduling isn't enabled for your account, or the game that you named is in a sport that isn't enabled for your account. | 
| 404 | ResourceNotFoundException | The feed doesn't exist. For DeleteScheduleAction, the action might not exist. | 
| 409 | ConflictException | For DeleteScheduleAction, the action started to run while your request was in progress. | 
| 429 | TooManyRequestException | The request rate is too high. Retry the request later. | 
| 500 | InternalServerErrorException | An unexpected service error occurred. Retry the request. | 