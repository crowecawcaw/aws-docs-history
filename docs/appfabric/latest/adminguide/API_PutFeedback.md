# PutFeedback

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Allows users to submit feedback for a given insight or action.

###### Topics

- [Request body](#API_PutFeedback_request "#API_PutFeedback_request")
- [Response elements](#API_PutFeedback_response "#API_PutFeedback_response")

## Request body

The request accepts the following data in JSON format.

| Parameter          | Description                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- | ------------------- | ------- |
| **id**             | The ID of the object for which feedback is being<br>submitted. This can be either the InsightId or the<br>ActionId. |
| **feedbackFor**    | The insight type for which the feedback is being<br>submitted.<br>Possible values: `ACTIONABLE_INSIGHT              | <br>MEETING_INSIGHT | ACTION` |
| **feedbackRating** | Feedback Rating from `1` to `5`.<br>Higher rating the better.                                                       |

## Response elements

If the action is successful, the service sends back an HTTP 201 response with
an empty HTTP body.
