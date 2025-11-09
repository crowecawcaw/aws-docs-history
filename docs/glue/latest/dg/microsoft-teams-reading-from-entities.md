# Reading from Microsoft Teams entities

**Prerequisites**

- A Microsoft Teams object you would like to read from. You will need the object name such as team or channel-message.
  The following table shows the supported entities.

**Supported entities for Source**

All entities are supported with API version 1.0.

| Entity                  | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ----------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Teams                   | No              | No             | No                | Yes                | No                    |
| Team Members            | Yes             | Yes            | No                | Yes                | Yes                   |
| Groups                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Group Members           | Yes             | Yes            | No                | Yes                | No                    |
| Channels                | Yes             | No             | No                | Yes                | Yes                   |
| Channel Messages        | No              | Yes            | No                | Yes                | No                    |
| Channel Message Replies | No              | Yes            | No                | Yes                | No                    |
| Channel Tabs            | Yes             | No             | No                | Yes                | No                    |
| Chats                   | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Calendar Events         | Yes             | Yes            | Yes               | Yes                | Yes                   |

**Example**

```
MicrosoftTeams_read = glueContext.create_dynamic_frame.from_options(
    connection_type="MicrosoftTeams",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "company",
        "API_VERSION": "v1.0"
    }
```

## Microsoft Teams Entity and Field Details

Entities list:

- Team: [https://docs.microsoft.com/en-us/graph/api/user-list-joinedteams?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/user-list-joinedteams?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/user-list-joinedteams?view=graph-rest-1.0")
- Team-Member: [https://docs.microsoft.com/en-us/graph/api/team-list-members?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/team-list-members?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/team-list-members?view=graph-rest-1.0")
- Group: [https://docs.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0")
- Group-Member: [https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/group-list-members?view=graph-rest-1.0")
- Channel: [https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/channel-list?view=graph-rest-1.0")
- Channel-Message: [https://docs.microsoft.com/en-us/graph/api/channel-list-messages?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/channel-list-messages?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/channel-list-messages?view=graph-rest-1.0")
- Channel-Message-Reply: [https://docs.microsoft.com/en-us/graph/api/chatmessage-list-replies?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/chatmessage-list-replies?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/chatmessage-list-replies?view=graph-rest-1.0")
- Channel-Tab: [https://docs.microsoft.com/en-us/graph/api/channel-list-tabs?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/channel-list-tabs?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/channel-list-tabs?view=graph-rest-1.0")
- Chat: [https://docs.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0 " https://docs.microsoft.com/en-us/graph/api/chat-list?view=graph-rest-1.0")
- Calendar-Event: [https://docs.microsoft.com/en-us/graph/api/group-list-events?view=graph-rest-1.0](https://docs.microsoft.com/en-us/graph/api/group-list-events?view=graph-rest-1.0 "https://docs.microsoft.com/en-us/graph/api/group-list-events?view=graph-rest-1.0")

**Partitioning queries**

Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`,
`NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters,
the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark
tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition query.
- `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field.

For date, we accept the Spark date format used in Spark SQL queries.
Example of valid values: `"2024-02-06"`.

- `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: number of partitions.

Entity wise partitioning field support details are captured in below table:

| Entity Name     | Partitioning Fields                                  | Data Type |
| --------------- | ---------------------------------------------------- | --------- |
| Team Members    | visibleHistoryStartDateTime                          | DateTime  |
| Groups          | createdDateTime                                      | DateTime  |
| Channels        | createdDateTime                                      | DateTime  |
| Chats           | createdDateTime, lastModifiedDateTime                | DateTime  |
| Calendar Events | createdDateTime, lastModifiedDateTime, originalStart | DateTime  |

**Example**

```
microsoftteams_read = glueContext.create_dynamic_frame.from_options(
    connection_type="MicrosoftTeams",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "group",
        "API_VERSION": "v1.0",
        "PARTITION_FIELD": "createdDateTime"
        "LOWER_BOUND": "2022-07-13T07:55:27.065Z"
        "UPPER_BOUND": "2022-08-12T07:55:27.065Z"
        "NUM_PARTITIONS": "2"
    }
```
