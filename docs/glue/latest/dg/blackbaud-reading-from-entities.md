# Reading from Blackbaud Raiser's Edge NXT entities

**Prerequisite**

A Blackbaud Raiser's Edge NXT object you would like to read from. You will need the object name.

**Supported entities for source**:

| Entity                            | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| --------------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Constituent Address               | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Education             | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Email address         | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Phone                 | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Note                  | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Relationship          | Yes             | Yes            | No                | Yes                | Yes                   |
| Constituent Online presence       | Yes             | Yes            | No                | Yes                | Yes                   |
| Opportunity                       | Yes             | Yes            | No                | Yes                | Yes                   |
| Appeal                            | Yes             | Yes            | No                | Yes                | Yes                   |
| Campaign                          | Yes             | Yes            | No                | Yes                | Yes                   |
| Fund                              | Yes             | Yes            | No                | Yes                | Yes                   |
| Package                           | Yes             | Yes            | No                | Yes                | Yes                   |
| Gift Batch                        | Yes             | Yes            | No                | Yes                | No                    |
| Event Participant                 | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Constituent Fundraiser Assignment | No              | No             | No                | Yes                | No                    |
| Gift                              | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Membership                        | Yes             | Yes            | No                | Yes                | Yes                   |
| Action                            | Yes             | Yes            | No                | Yes                | No                    |
| Constituent                       | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Constituent Goods                 | Yes             | Yes            | No                | Yes                | Yes                   |
| Event                             | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Gift custom field                 | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**:

```
blackbaud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="BLACKBAUD",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v1",
        "SUBSCRIPTION_KEY": <Subscription key associated with one's developer account>
    }
```

## Blackbaud Raiser's Edge NXT entity and field details

For more information about the entities and field details see:

- [Action](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Action "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Action")
- [Constituent](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Constituent "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Constituent")
- [Constituent Address](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Address "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Address")
- [Constituent Membership](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Membership "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Membership")
- [Constituent Fundraiser Assignment](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#FundraiserAssignment "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#FundraiserAssignment")
- [Constituent Education](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Education "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Education")
- [Constituent Email Address](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#EmailAddress "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#EmailAddress")
- [Constituent Phone](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Phone "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Phone")
- [Constituent Note](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Note "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Note")
- [Constituent Online Presence](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#OnlinePresence "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#OnlinePresence")
- [Constituent Relationship](https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Relationship "https://developer.blackbaud.com/skyapi/renxt/constituent/entities#Relationship")
- [Event](https://developer.blackbaud.com/skyapi/renxt/event/entities#Event "https://developer.blackbaud.com/skyapi/renxt/event/entities#Event")
- [Event Participant](https://developer.blackbaud.com/skyapi/renxt/event/entities#Participant "https://developer.blackbaud.com/skyapi/renxt/event/entities#Participant")
- [Appeal](https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Appeal "https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Appeal")
- [Campaign](https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Campaign "https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Campaign")
- [Fund](https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Fund "https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Fund")
- [Package](https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Package "https://developer.blackbaud.com/skyapi/renxt/fundraising/entities#Package")
- [Gift](https://developer.blackbaud.com/skyapi/renxt/gift/entities#Gift "https://developer.blackbaud.com/skyapi/renxt/gift/entities#Gift")
- [Gift Custom Field](https://developer.blackbaud.com/skyapi/renxt/gift/entities#CustomField "https://developer.blackbaud.com/skyapi/renxt/gift/entities#CustomField")
- [Gift Batch](https://developer.blackbaud.com/skyapi/renxt/gift-batch/entities#GiftBatch "https://developer.blackbaud.com/skyapi/renxt/gift-batch/entities#GiftBatch")
- [Opportunity](https://developer.blackbaud.com/skyapi/renxt/opportunity/entities#Opportunity "https://developer.blackbaud.com/skyapi/renxt/opportunity/entities#Opportunity")
- [Constituent Codes](https://developer.sky.blackbaud.com/api#api=56b76470069a0509c8f1c5b3 "https://developer.sky.blackbaud.com/api#api=56b76470069a0509c8f1c5b3")

###### Note

Struct and List data types are converted to String data type, and DateTime data type is converted to Timestamp in the response of the connectors.

## Partitioning queries

**Field-based partitioning**:

Blackbaud Raiser's Edge NXT doesn’t support field based or record based partitioning.

**Record-based partitioning**:

You can provide the additional Spark option `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
this parameter, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

In record based partitioning, the total number of records present is queried from Blackbaud Raiser’s Edge NXT API, and it is divided by `NUM_PARTITIONS` number provided. The resulting number of records are then concurrently fetched by each sub-query.

- `NUM_PARTITIONS`: the number of partitions.

Example:

```
blackbaud_read = glueContext.create_dynamic_frame.from_options(
    connection_type="BLACKBAUD",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v1",
        "NUM_PARTITIONS": "2",
        "SUBSCRIPTION_KEY": <Subscription key associated with one's developer account>
    }
```
