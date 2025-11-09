# Reading from Kustomer entities

**Prerequisite**

A Kustomer object you would like to read from. You will need the object name such as Brands or Cards. The following table shows the supported entities.

**Supported entities for source**:

| Entity                     | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| -------------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Brands                     | No              | Yes            | No                | Yes                | No                    |
| Cards                      | No              | Yes            | No                | Yes                | No                    |
| Chat Settings              | No              | No             | No                | Yes                | No                    |
| Companies                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Conversations              | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Customers                  | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Customer Searches Pinned   | No              | Yes            | No                | Yes                | No                    |
| Customer Searches Position | No              | No             | No                | Yes                | No                    |
| Email Hooks                | No              | Yes            | No                | Yes                | No                    |
| Web Hooks                  | No              | Yes            | No                | Yes                | No                    |
| KB Articles                | No              | Yes            | No                | Yes                | No                    |
| KB Categories              | No              | Yes            | No                | Yes                | No                    |
| KB Forms                   | No              | Yes            | No                | Yes                | No                    |
| KB Routes                  | No              | Yes            | No                | Yes                | No                    |
| KB Tags                    | No              | Yes            | No                | Yes                | No                    |
| KB Templates               | No              | Yes            | No                | Yes                | No                    |
| KB Themes                  | No              | Yes            | No                | Yes                | No                    |
| Klasses                    | No              | Yes            | No                | Yes                | No                    |
| KViews                     | No              | Yes            | No                | Yes                | No                    |
| Messages                   | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Notes                      | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Notifications              | No              | Yes            | No                | Yes                | No                    |

**Example**:

```
Kustomer_read = glueContext.create_dynamic_frame.from_options(
    connection_type="kustomer",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "brands",
        "API_VERSION": "v1"
    }
```

## Kustomer entity and field details

For more information about the entities and field details see:

- [Brands](https://api.kustomerapp.com/v1/brands "https://api.kustomerapp.com/v1/brands")
- [Cards](https://api.kustomerapp.com/v1/cards "https://api.kustomerapp.com/v1/cards")
- [Chat Settings](https://api.kustomerapp.com/v1/chat/settings "https://api.kustomerapp.com/v1/chat/settings")
- [Companies](https://api.kustomerapp.com/v1/companies "https://api.kustomerapp.com/v1/companies")
- [Conversations](https://api.kustomerapp.com/v1/conversations "https://api.kustomerapp.com/v1/conversations")
- [Customers](https://api.kustomerapp.com/v1/customers "https://api.kustomerapp.com/v1/customers")
- [Customers Searches Pinned](https://api.kustomerapp.com/v1/customers/searches/pinned "https://api.kustomerapp.com/v1/customers/searches/pinned")
- [Customer Searches Positions](https://api.kustomerapp.com/v1/customers/searches/positions "https://api.kustomerapp.com/v1/customers/searches/positions")
- [Hooks Email](https://api.kustomerapp.com/v1/hooks/email "https://api.kustomerapp.com/v1/hooks/email")
- [Hooks Web](https://api.kustomerapp.com/v1/hooks/web "https://api.kustomerapp.com/v1/hooks/web")
- [KB Articles](https://api.kustomerapp.com/v1/kb/articles "https://api.kustomerapp.com/v1/kb/articles")
- [KB Categories](https://api.kustomerapp.com/v1/kb/categories "https://api.kustomerapp.com/v1/kb/categories")
- [KB Forms](https://api.kustomerapp.com/v1/kb/forms " https://api.kustomerapp.com/v1/kb/forms")
- [KB Routes](https://api.kustomerapp.com/v1/kb/routes "https://api.kustomerapp.com/v1/kb/routes")
- [KB Tags](https://api.kustomerapp.com/v1/kb/tags "https://api.kustomerapp.com/v1/kb/tags")
- [KB Templates](https://api.kustomerapp.com/v1/kb/templates "https://api.kustomerapp.com/v1/kb/templates")
- [KB Themes](https://api.kustomerapp.com/v1/kb/themes "https://api.kustomerapp.com/v1/kb/themes")
- [Klasses](https://api.kustomerapp.com/v1/klasses "https://api.kustomerapp.com/v1/klasses")
- [Kviews](https://api.kustomerapp.com/v1/kviews "https://api.kustomerapp.com/v1/kviews")
- [Messages](https://api.kustomerapp.com/v1/messages "https://api.kustomerapp.com/v1/messages")
- [Notes](https://api.kustomerapp.com/v1/notes "https://api.kustomerapp.com/v1/notes")
- [Notifications](https://api.kustomerapp.com/v1/notifications "https://api.kustomerapp.com/v1/notifications")

Kustomer API v1

| Entity                                | Field    | Data type                    | Supported operators |
| ------------------------------------- | -------- | ---------------------------- | ------------------- |
| Brands                                | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| iconUrl                               | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| default                               | Boolean  | N/A                          |
| Cards                                 | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| description                           | String   | N/A                          |
| url                                   | String   | N/A                          |
| contexts                              | List     | N/A                          |
| Chat Settings                         | id       | String                       | N/A                 |
| settingsVersion                       | Integer  | N/A                          |
| widgetType                            | String   | N/A                          |
| version                               | Integer  | N/A                          |
| teamName                              | String   | N/A                          |
| greeting                              | String   | N/A                          |
| autoreply                             | String   | N/A                          |
| embedIconUrl                          | String   | N/A                          |
| embedIconColor                        | String   | N/A                          |
| fallbackEmailSubject                  | String   | N/A                          |
| fallbackEmailIntroduction             | String   | N/A                          |
| enabled                               | Boolean  | N/A                          |
| outboundChatEnabled                   | Boolean  | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| offhoursMessage                       | String   | N/A                          |
| offhoursImageUrl                      | String   | N/A                          |
| closableChat                          | Boolean  | N/A                          |
| noHistory                             | Boolean  | N/A                          |
| disableAttachments                    | Boolean  | N/A                          |
| volumeControl                         | Struct   | N/A                          |
| singleSessonChat                      | Boolean  | N/A                          |
| showTypingIndicatorWeb                | Boolean  | N/A                          |
| Companies                             | id       | String                       | N/A                 |
| name                                  | String   | =, !=, CONTAINS              |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| tags                                  | List     | N/A                          |
| domains                               | List     | N/A                          |
| emails                                | List     | N/A                          |
| phones                                | List     | N/A                          |
| whatsapps                             | List     | N/A                          |
| socials                               | List     | N/A                          |
| urls                                  | List     | N/A                          |
| locations                             | List     | N/A                          |
| roleGroupVersions                     | List     | N/A                          |
| rev                                   | Integer  | N/A                          |
| Conversations                         | id       | String                       | N/A                 |
| name                                  | String   | =, !=, CONTAINS              |
| preview                               | String   | N/A                          |
| channels                              | List     | N/A                          |
| status                                | String   | =, !=, CONTAINS              |
| messageCount                          | Integer  | =, !=, >, >=, <, <=          |
| noteCount                             | Integer  | =, !=, >, >=, <, <=          |
| satisfaction                          | Integer  | =, !=, >, >=, <, <=          |
| satisfactionLevel                     | Struct   | N/A                          |
| createdAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| updatedAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| modifiedAt                            | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| lastActivityAt                        | DateTime | N/A                          |
| spam                                  | Boolean  | N/A                          |
| ended                                 | Boolean  | =, !=                        |
| endedAt                               | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| endedReason                           | String   | CONTAINS                     |
| endedByType                           | String   | N/A                          |
| importedAt                            | String   | N/A                          |
| tags                                  | List     | N/A                          |
| suggestedTags                         | List     | N/A                          |
| sentiment                             | String   | N/A                          |
| predictions                           | List     | N/A                          |
| suggestedShortcuts                    | List     | N/A                          |
| firstMessageIn                        | Struct   | N/A                          |
| firstMessageOut                       | Struct   | N/A                          |
| lastMessageIn                         | Struct   | N/A                          |
| lastMessageOut                        | Struct   | N/A                          |
| lastMessageAt                         | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| lastMessageUnrespondedTo              | Struct   | N/A                          |
| lastMessageUnrespondedToSinceLastDone | Struct   | N/A                          |
| assignedUsers                         | List     | N/A                          |
| assignedTeams                         | List     | N/A                          |
| firstResponse                         | Struct   | N/A                          |
| firstResponseSinceLastDone            | Struct   | N/A                          |
| lastResponse                          | Struct   | N/A                          |
| firstDone                             | Struct   | N/A                          |
| lastDone                              | Struct   | N/A                          |
| direction                             | String   | =, !=, CONTAINS              |
| lastMessageDirection                  | String   | N/A                          |
| outboundMessageCount                  | Integer  | N/A                          |
| inboundMessageCount                   | Integer  | N/A                          |
| rev                                   | Integer  | N/A                          |
| priority                              | Integer  | =, !=, >, >=, <, <=          |
| roleGroupVersions                     | List     | N/A                          |
| accessOverride                        | List     | N/A                          |
| assistant                             | Struct   | N/A                          |
| phase                                 | String   | N/A                          |
| Skills                                | List     | N/A                          |
| matchedTimeBasedRules                 | List     | N/A                          |
| Customers                             | id       | String                       | N/A                 |
| name                                  | String   | =, !=, CONTAINS              |
| displayName                           | String   | N/A                          |
| displayColor                          | String   | N/A                          |
| displayIcon                           | String   | N/A                          |
| externalId                            | String   | =, !=, CONTAINS              |
| externalIds                           | List     | N/A                          |
| sharedExternalIds                     | List     | N/A                          |
| emails                                | List     | N/A                          |
| sharedEmails                          | List     | N/A                          |
| phones                                | List     | N/A                          |
| sharedPhones                          | List     | N/A                          |
| whatsapps                             | List     | N/A                          |
| facebookIds                           | List     | N/A                          |
| instagramIds                          | List     | N/A                          |
| socials                               | List     | N/A                          |
| sharedSocials                         | List     | N/A                          |
| urls                                  | List     | N/A                          |
| locations                             | List     | N/A                          |
| activeUsers                           | List     | N/A                          |
| watchers                              | List     | N/A                          |
| recentLocation                        | Struct   | N/A                          |
| locale                                | String   | =, !=, CONTAINS              |
| timeZone                              | String   | N/A                          |
| gender                                | String   | =, !=, CONTAINS              |
| createdAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| updatedAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| modifiedAt                            | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| lastActivityAt                        | DateTime | N/A                          |
| deleted                               | Boolean  | N/A                          |
| lastConversation                      | Struct   | N/A                          |
| conversationCounts                    | Struct   | N/A                          |
| preview                               | Struct   | N/A                          |
| tags                                  | List     | N/A                          |
| progressiveStatus                     | String   | =, !=, CONTAINS              |
| verified                              | Boolean  | N/A                          |
| rev                                   | Integer  | N/A                          |
| recentItems                           | List     | N/A                          |
| defaultLang                           | String   | =, !=, CONTAINS              |
| satisfactionLevel                     | Struct   | N/A                          |
| roleGroupVersions                     | List     | N/A                          |
| accessOverride                        | List     | N/A                          |
| companyName                           | String   | N/A                          |
| firstName                             | String   | N/A                          |
| lastName                              | String   | N/A                          |
| Customer Searches Pinned              | id       | String                       | N/A                 |
| search                                | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| Customer Searches Positions           | id       | String                       | N/A                 |
| positions                             | List     | N/A                          |
| children                              | List     | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| rev                                   | Integer  | N/A                          |
| Email Hooks                           | id       | String                       | N/A                 |
| description                           | String   | N/A                          |
| debug                                 | Boolean  | N/A                          |
| email                                 | String   | N/A                          |
| eventName                             | String   | N/A                          |
| title                                 | String   | N/A                          |
| hash                                  | String   | N/A                          |
| key                                   | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| Web Hooks                             | id       | String                       | N/A                 |
| description                           | String   | N/A                          |
| eventName                             | String   | N/A                          |
| hash                                  | String   | N/A                          |
| url                                   | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| title                                 | String   | N/A                          |
| version                               | Integer  | N/A                          |
| debug                                 | Boolean  | N/A                          |
| KB Articles                           | id       | String                       | N/A                 |
| hash                                  | String   | N/A                          |
| title                                 | String   | N/A                          |
| source                                | String   | N/A                          |
| status                                | String   | N/A                          |
| scope                                 | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| deleted                               | Boolean  | N/A                          |
| deletedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| publishedAt                           | DateTime | N/A                          |
| tags                                  | List     | N/A                          |
| categories                            | List     | N/A                          |
| knowledgeBases                        | List     | N/A                          |
| metaTitle                             | String   | N/A                          |
| metaDescription                       | String   | N/A                          |
| metaKeywords                          | List     | N/A                          |
| langVersions                          | Struct   | N/A                          |
| latestLangs                           | Struct   | N/A                          |
| KB Categories                         | id       | String                       | N/A                 |
| hash                                  | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| published                             | Boolean  | N/A                          |
| positions                             | List     | N/A                          |
| categoryPositions                     | List     | N/A                          |
| root                                  | Boolean  | N/A                          |
| langs                                 | Struct   | N/A                          |
| KB Forms                              | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| slug                                  | String   | N/A                          |
| hash                                  | String   | N/A                          |
| body                                  | String   | N/A                          |
| layout                                | List     | N/A                          |
| layoutV2                              | List     | N/A                          |
| componentsV2                          | Struct   | N/A                          |
| conditions                            | Struct   | N/A                          |
| advanced                              | Boolean  | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| publishedAt                           | DateTime | N/A                          |
| modifiedAt                            | String   | N/A                          |
| published                             | Boolean  | N/A                          |
| snippets                              | List     | N/A                          |
| recaptcha                             | Boolean  | N/A                          |
| klass                                 | String   | N/A                          |
| channel                               | String   | N/A                          |
| deflection                            | Boolean  | N/A                          |
| formHookEnabled                       | Boolean  | N/A                          |
| replyFrom                             | String   | N/A                          |
| wcag                                  | Boolean  | N/A                          |
| KB Routes                             | id       | String                       | N/A                 |
| url                                   | String   | N/A                          |
| routableType                          | String   | N/A                          |
| routableId                            | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| KB Tags                               | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| KB Templates                          | id       | String                       | N/A                 |
| title                                 | String   | N/A                          |
| description                           | String   | N/A                          |
| beta                                  | Boolean  | N/A                          |
| manifest                              | Struct   | N/A                          |
| jsxSnippets                           | List     | N/A                          |
| images                                | List     | N/A                          |
| version                               | String   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| KB Themes                             | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| active                                | Boolean  | N/A                          |
| default                               | Boolean  | N/A                          |
| lastfileUpdatedAt                     | DateTime | N/A                          |
| custom                                | Boolean  | N/A                          |
| status                                | String   | N/A                          |
| templateVersionId                     | String   | N/A                          |
| templateTitle                         | String   | N/A                          |
| templateVersion                       | String   | N/A                          |
| manifest                              | Struct   | N/A                          |
| configSnippets                        | List     | N/A                          |
| jsxSnippets                           | List     | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| rev                                   | Integer  | N/A                          |
| Klasses                               | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| icon                                  | String   | N/A                          |
| color                                 | String   | N/A                          |
| appDisabled                           | Boolean  | N/A                          |
| status                                | String   | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| createdAt                             | DateTime | N/A                          |
| s3DataUrl                             | String   | N/A                          |
| KViews                                | id       | String                       | N/A                 |
| resource                              | String   | N/A                          |
| template                              | String   | N/A                          |
| context                               | String   | N/A                          |
| meta                                  | Struct   | N/A                          |
| appDisabled                           | Boolean  | N/A                          |
| enabled                               | Boolean  | N/A                          |
| advanced                              | Boolean  | N/A                          |
| layout                                | List     | N/A                          |
| components                            | Struct   | N/A                          |
| conditions                            | Struct   | N/A                          |
| rev                                   | Integer  | N/A                          |
| createdAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| Notifications                         | id       | String                       | N/A                 |
| name                                  | String   | N/A                          |
| status                                | String   | N/A                          |
| event                                 | Struct   | N/A                          |
| createdAt                             | DateTime | N/A                          |
| updatedAt                             | DateTime | N/A                          |
| Messages                              | id       | String                       | N/A                 |
| externalId                            | String   | N/A                          |
| channel                               | String   | =, !=, CONTAINS              |
| app                                   | String   | N/A                          |
| size                                  | Integer  | =, !=, >, >=, <, <=          |
| direction                             | String   | =, !=, CONTAINS              |
| preview                               | String   | N/A                          |
| subject                               | String   | N/A                          |
| meta                                  | Struct   | N/A                          |
| status                                | String   | =, !=, CONTAINS              |
| directionType                         | String   | =, !=, CONTAINS              |
| assignedTeams                         | List     | N/A                          |
| assignedUsers                         | List     | N/A                          |
| errorAt                               | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| auto                                  | Boolean  | =, !=                        |
| sentAt                                | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| createdAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| updatedAt                             | DateTime | N/A                          |
| modifiedAt                            | DateTime | N/A                          |
| redacted                              | Boolean  | N/A                          |
| createdByTeams                        | List     | N/A                          |
| rev                                   | Integer  | N/A                          |
| reactions                             | List     | N/A                          |
| intentDetections                      | List     | N/A                          |
| Notes                                 | id       | String                       | N/A                 |
| body                                  | String   | CONTAINS                     |
| createdAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| updatedAt                             | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| modifiedAt                            | DateTime | =, !=, >, >=, <, <=, BETWEEN |
| createdByTeams                        | List     | N/A                          |

## Partitioning queries

**Field-based partitioning**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the DateTime field, we accept the value in ISO format.

Example of valid value:

```
"2023-01-15T11:18:39.205Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Entity-wise partitioning field support details are captured in the following table:

| Entity name             | Partitioning fields                                      | Data type |
| ----------------------- | -------------------------------------------------------- | --------- |
| Companies               | modifiedAt                                               | DateTime  |
| Conversations           | createdAt, updatedAt, modifiedAt, endedAt, lastMessageAt | DateTime  |
| messageCount, noteCount | BigInteger                                               |
| priority                | Integer                                                  |
| Customers               | createdAt, updatedAt, modifiedAt                         | DateTime  |
| Messages                | errorAt, sentAt, createdAt                               | DateTime  |
| size                    | BigInteger                                               |
| Notes                   | createdAt, updatedAt, modifiedAt                         | DateTime  |

Example:

```
Kustomer_read = glueContext.create_dynamic_frame.from_options(
    connection_type="kustomer",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "conversation",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "createdAt"
        "LOWER_BOUND": "2023-01-15T11:18:39.205Z"
        "UPPER_BOUND": "2023-02-15T11:18:39.205Z"
        "NUM_PARTITIONS": "2"
    }
```
