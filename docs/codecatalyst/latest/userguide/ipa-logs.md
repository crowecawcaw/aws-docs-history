Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Accessing logged events using event logging

When users perform actions in Amazon CodeCatalyst, these actions are recorded as events. You can
use the AWS CLI to view logs of events in a space in a specified timeframe. You can view
these events to review actions taken in the space, including the date and time of the
actions, the name of the user who performed the action, and the IP address where the user
made the request.

###### Note

Management events for a CodeCatalyst space are logged in CloudTrail for the connected billing
account. For more information about CodeCatalyst management events that are logged by CloudTrail,
see [CodeCatalyst information in CloudTrail](ipa-logging-connections.md#info-in-cloudtrail "ipa-logging-connections.md#info-in-cloudtrail").

In order to view a log of events for a space, you must have installed and configured
the AWS CLI with a profile for CodeCatalyst, and you must have the
**Space administrator** role for the space. For more information, see
[Setting up to use the AWS CLI with CodeCatalyst](set-up-cli.md "set-up-cli.md") and [Space administrator role](ipa-role-types.md#ipa-role-space-admin "ipa-role-types.md#ipa-role-space-admin").

###### Note

To view logging for events that occur on behalf of CodeCatalyst in connected AWS accounts,
or to view logging for events for space or project resources in the connected
billing account, you can use AWS CloudTrail. For more information, see [Monitoring API calls by AWS accounts using AWS CloudTrail logging](ipa-logging-connections.md "ipa-logging-connections.md").

1.  Open a terminal or command line and run the **aws codecatalyst
    list-event-logs** command, specifying:

        * The name of the space with the `--space-name`
         option.
        * The date and time when you want to start reviewing events, in coordinated
         universal time (UTC) timestamp format as specified in [RFC
         3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6 "https://www.rfc-editor.org/rfc/rfc3339#section-5.6"), with the `--start-time`
         option.
        * The date and time when you want to stop reviewing events, in coordinated
         universal time (UTC) timestamp format as specified in [RFC
         3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6 "https://www.rfc-editor.org/rfc/rfc3339#section-5.6"), with the `--end-time` option.
        * (Optional) The maximum number of results to return in a single response,
         with the `--max-results` option. If the number of
         results is larger than the number you specify, the response will include a
         `nextToken` element which you can use to return the next
         results.
        * (Optional) Limit the results to a specific event type you want returned,
         with the `--event-name` option.

    This example returns logged events in the space named
    `ExampleCorp` from the time period
    `2022-11-30` to `2022-12-01`,
    and that a maximum of `2` events be returned in the
    response.

```
aws codecatalyst list-event-logs --space-name `ExampleCorp` --start-time `2022-11-30` --end-time `2022-12-01` --event-name `list-event-logs` --max-results `2`
```

2. If events occurred in this time frame, the command returns results similar to the
   following:

```
{
    "nextToken": "EXAMPLE",
    "items": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "eventName": "listEventLogs",
            "eventType": "AwsApiCall",
            "eventCategory": "MANAGEMENT",
            "eventSource": "manage",
            "eventTime": "2022-12-01T22:47:24.605000+00:00",
            "operationType": "READONLY",
            "userIdentity": {
                "userType": "USER",
                "principalId": "a1b2c3d4e5-678fgh90-1a2b-3c4d-e5f6-EXAMPLE11111"
                "userName": "MaryMajor"
            },
            "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "requestPayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"startTime\":\"2022-12-01T00:00:00Z\",\"endTime\":\"2022-12-10T00:00:00Z\",\"maxResults\":\"2\"}"
            },
            "sourceIpAddress": "127.0.0.1",
            "userAgent": "aws-cli/2.9.0 Python/3.9.11 Darwin/21.3.0 exe/x86_64 prompt/off command/codecatalyst.list-event-logs"
        },
        {
            "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "eventName": "createProject",
            "eventType": "AwsApiCall",
            "eventCategory": "MANAGEMENT",
            "eventSource": "manage",
            "eventTime": "2022-12-01T09:15:32.068000+00:00",
            "operationType": "MUTATION",
            "userIdentity": {
                "userType": "USER",
                "principalId": "a1b2c3d4e5-678fgh90-1a2b-3c4d-e5f6-EXAMPLE11111",
                "userName": "MaryMajor"
            },
            "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "requestPayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"name\":\"MyFirstProject\",\"displayName\":\"MyFirstProject\"}"
            },
            "responsePayload": {
                "contentType": "application/json",
                "data": "{\"spaceName\":\"ExampleCorp\",\"name\":\"MyFirstProject\",\"displayName\":\"MyFirstProject\",\"id\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE4444\"}"
            },
            "sourceIpAddress": "192.0.2.23",
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
    ]
}
```

3. Run the **list-event-logs** command again with the
   **--next-token** option and the value of the returned token to
   retrieve the next set of logged events that match the request.
