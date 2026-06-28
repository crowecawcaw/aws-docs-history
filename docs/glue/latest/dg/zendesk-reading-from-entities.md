# Reading from Zendesk entities

**Prerequisite**

A Zendesk Object you would like to read from. You will need the object name such as ticket
or user or article, as mentioned in the following table.

| Entity              | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Ticket              | Y               | Y              | Y                 | Y                  | N                     |
| User                | Y               | Y              | Y                 | Y                  | N                     |
| Organization        | Y               | Y              | Y                 | Y                  | N                     |
| Article             | Y               | Y              | N                 | Y                  | N                     |
| Ticket Event        | Y               | Y              | N                 | Y                  | N                     |
| Ticket Metric Event | Y               | Y              | N                 | Y                  | N                     |
| Ticket Comment      | Y               | Y              | Y                 | Y                  | N                     |
| Ticket Field        | Y               | Y              | N                 | Y                  | N                     |
| Ticket Metric       | Y               | Y              | N                 | Y                  | N                     |
| Ticket Activity     | Y               | Y              | N                 | Y                  | N                     |
| Ticket Skip         | N               | Y              | N                 | Y                  | N                     |
| Group               | Y               | Y              | Y                 | Y                  | N                     |
| Group Membership    | N               | Y              | Y                 | Y                  | N                     |
| Satisfaction Rating | Y               | Y              | N                 | Y                  | N                     |
| View                | Y               | Y              | Y                 | Y                  | N                     |
| Trigger             | Y               | Y              | Y                 | Y                  | N                     |
| Trigger Category    | N               | Y              | Y                 | Y                  | N                     |
| Macro               | Y               | Y              | Y                 | Y                  | N                     |
| Automation          | N               | Y              | Y                 | Y                  | N                     |

**Example**:

```
Zendesk_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Zendesk",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v2"
    }
```

**Zendesk entities and field details**:

| Entity                               | Field       | Data type | Supported operators                                                                          | Comments |
| ------------------------------------ | ----------- | --------- | -------------------------------------------------------------------------------------------- | -------- |
| articles                             | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| author\_id                           | Long        |           |                                                                                              |
| body                                 | String      |           |                                                                                              |
| comments\_disabled                   | Boolean     |           |                                                                                              |
| draft                                | Boolean     |           |                                                                                              |
| edited\_at                           | DateTime    |           |                                                                                              |
| html\_url                            | String      |           |                                                                                              |
| label\_names                         | List        |           |                                                                                              |
| locale                               | String      | EQUAL\_TO |                                                                                              |
| outdated                             | Boolean     |           |                                                                                              |
| outdated\_locales                    | List        |           |                                                                                              |
| permission\_group\_id                | Long        |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| promoted                             | Boolean     |           |                                                                                              |
| section\_id                          | Long        |           |                                                                                              |
| source\_locale                       | String      |           |                                                                                              |
| name                                 | String      |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| user\_segment\_id                    | Long        |           |                                                                                              |
| content\_tags\_id                    | List        |           |                                                                                              |
| vote\_count                          | Integer     |           |                                                                                              |
| vote\_sum                            | Integer     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| label\_name                          | String      | EQUAL\_TO |                                                                                              |
| group                                | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| is\_public                           | Boolean     |           |                                                                                              |
| name                                 | String      |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| deleted                              | Boolean     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| exclude\_deleted                     | Boolean     | EQUAL\_TO |                                                                                              |
| automation                           | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| active                               | Boolean     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| actions                              | List        |           |                                                                                              |
| positions                            | Integer     |           |                                                                                              |
| conditions                           | Struct      |           |                                                                                              |
| raw\_title                           | String      |           |                                                                                              |
| group-membership                     | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| user\_id                             | Long        |           |                                                                                              |
| group\_id                            | Long        |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| macro                                | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| active                               | Boolean     | EQUAL\_TO |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| actions                              | List        |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| raw\_title                           | String      |           |                                                                                              |
| restriction                          | Struct      |           |                                                                                              |
| access                               | String      | EQUAL\_TO |                                                                                              |
| category                             | Integer     | EQUAL\_TO |                                                                                              |
| group\_id                            | Long        | EQUAL\_TO |                                                                                              |
| only\_viewable                       | Boolean     | EQUAL\_TO |                                                                                              |
| organizations                        | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| external\_id                         | String      |           |                                                                                              |
| name                                 | String      |           |                                                                                              |
| domain\_names                        | List        |           |                                                                                              |
| details                              | String      |           |                                                                                              |
| notes                                | String      |           |                                                                                              |
| group\_id                            | Long        |           |                                                                                              |
| shared\_tickets                      | Boolean     |           |                                                                                              |
| shared\_comments                     | Boolean     |           |                                                                                              |
| tags                                 | List        |           |                                                                                              |
| organization\_fields                 | Struct      |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| DML\_STATUS                          | String      |           | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| satisfaction-rating                  | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| assignee\_id                         | Long        |           |                                                                                              |
| comment                              | String      |           |                                                                                              |
| group\_id                            | Long        |           |                                                                                              |
| reason                               | String      |           |                                                                                              |
| reason\_code                         | Integer     |           |                                                                                              |
| reason\_id                           | Long        |           |                                                                                              |
| requester\_id                        | Long        |           |                                                                                              |
| score                                | String      | EQUAL\_TO |                                                                                              |
| ticket\_id                           | Integer     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| start\_time                          | DateTime    | EQUAL\_TO |                                                                                              |
| end\_time                            | DateTime    | EQUAL\_TO |                                                                                              |
| DML\_STATUS                          | String      |           | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| ticket-activity                      | actor       | Struct    |                                                                                              |          |
| actor\_id                            | Long        |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| id                                   | Long        |           |                                                                                              |
| object                               | Struct      |           |                                                                                              |
| target                               | Struct      |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| url                                  | String      |           |                                                                                              |
| user                                 | Struct      |           |                                                                                              |
| user\_id                             | Long        |           |                                                                                              |
| verb                                 | String      |           |                                                                                              |
| since                                | DateTime    | EQUAL\_TO |                                                                                              |
| ticket-comment                       | id          | Long      |                                                                                              |          |
| type                                 | String      |           |                                                                                              |
| author\_id                           | Long        |           |                                                                                              |
| body                                 | String      |           |                                                                                              |
| html\_body                           | String      |           |                                                                                              |
| plain\_body                          | String      |           |                                                                                              |
| public                               | Boolean     |           |                                                                                              |
| attachments                          | List        |           |                                                                                              |
| audit\_id                            | Long        |           |                                                                                              |
| via                                  | Struct      |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| metadata                             | Struct      |           |                                                                                              |
| ticket\_id                           | Integer     | EQUAL\_TO |                                                                                              |
| include\_inline\_images              | Boolean     | EQUAL\_TO |                                                                                              |
| ticket-events                        | id          | Long      |                                                                                              |          |
| ticket\_id                           | Long        |           |                                                                                              |
| timestamp                            | Long        |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updater\_id                          | Long        |           |                                                                                              |
| child\_events                        | List        |           |                                                                                              |
| via                                  | String      |           |                                                                                              |
| system                               | Struct      |           |                                                                                              |
| event\_type                          | String      |           |                                                                                              |
| comment\_present                     | Boolean     |           |                                                                                              |
| comment\_public                      | Boolean     |           |                                                                                              |
| via\_reference\_id                   | Long        |           |                                                                                              |
| created\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| DML\_STATUS                          | String      |           | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| ticket-field                         | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| type                                 | String      |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| raw\_title                           | String      |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| raw\_description                     | String      |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| active                               | Boolean     |           |                                                                                              |
| required                             | Boolean     |           |                                                                                              |
| collapsed\_for\_agents               | Boolean     |           |                                                                                              |
| regexp\_for\_validation              | String      |           |                                                                                              |
| title\_in\_portal                    | String      |           |                                                                                              |
| raw\_title\_in\_portal               | String      |           |                                                                                              |
| visible\_in\_portal                  | Boolean     |           |                                                                                              |
| editable\_on\_portal                 | Boolean     |           |                                                                                              |
| required\_in\_portal                 | Boolean     |           |                                                                                              |
| tag                                  | String      |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| removable                            | Boolean     |           |                                                                                              |
| agent\_description                   | String      |           |                                                                                              |
| custom\_field\_options               | List        |           |                                                                                              |
| custom\_statuses                     | List        |           |                                                                                              |
| relationship\_filter                 | Struct      |           |                                                                                              |
| relationship\_target\_type           | String      |           |                                                                                              |
| sub\_type\_id                        | Integer     |           |                                                                                              |
| system\_field\_options               | List        |           |                                                                                              |
| locale                               | String      | EQUAL\_TO |                                                                                              |
| ticket-metric-events                 | id          | Long      |                                                                                              |          |
| time                                 | DateTime    | EQUAL\_TO |                                                                                              |
| ticket\_id                           | Integer     |           |                                                                                              |
| metric                               | String      |           |                                                                                              |
| instance\_id                         | Integer     |           |                                                                                              |
| type                                 | String      |           |                                                                                              |
| DML\_STATUS                          | String      | EQUAL\_TO | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| ticket-metric                        | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| ticket\_id                           | Integer     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| group\_stations                      | Integer     |           |                                                                                              |
| assignee\_stations                   | Integer     |           |                                                                                              |
| reopens                              | Integer     |           |                                                                                              |
| replies                              | Integer     |           |                                                                                              |
| assignee\_updated\_at                | DateTime    |           |                                                                                              |
| requester\_updated\_at               | DateTime    |           |                                                                                              |
| initially\_assigned\_at              | DateTime    |           |                                                                                              |
| assigned\_at                         | DateTime    |           |                                                                                              |
| solved\_at                           | DateTime    |           |                                                                                              |
| last\_comment\_added\_at             | DateTime    |           |                                                                                              |
| reply\_time\_in\_minutes             | Struct      |           |                                                                                              |
| first\_resolution\_time\_in\_minutes | Struct      |           |                                                                                              |
| full\_resolution\_time\_in\_minutes  | Struct      |           |                                                                                              |
| agent\_wait\_time\_in\_minutes       | Struct      |           |                                                                                              |
| requester\_wait\_time\_in\_minutes   | Struct      |           |                                                                                              |
| on\_hold\_time\_in\_seconds          | Struct      |           |                                                                                              |
| reply\_time\_in\_seconds             | Struct      |           |                                                                                              |
| custom\_status\_updated\_at          | DateTime    |           |                                                                                              |
| ticket-skip                          | created\_at | DateTime  |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| reason                               | String      |           |                                                                                              |
| ticket                               | Struct      |           |                                                                                              |
| ticket\_id                           | Integer     |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| user\_id                             | Long        |           |                                                                                              |
| tickets                              | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| external\_id                         | String      | EQUAL\_TO |                                                                                              |
| type                                 | String      |           |                                                                                              |
| subject                              | String      |           |                                                                                              |
| raw\_subject                         | String      |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| priority                             | String      |           |                                                                                              |
| status                               | String      |           |                                                                                              |
| recipient                            | String      |           |                                                                                              |
| requester                            | Struct      |           |                                                                                              |
| requester\_id                        | Long        |           |                                                                                              |
| submitter\_id                        | Long        |           |                                                                                              |
| assignee\_id                         | Long        |           |                                                                                              |
| organization\_id                     | Long        |           |                                                                                              |
| group\_id                            | Long        |           |                                                                                              |
| collaborator\_ids                    | List        |           |                                                                                              |
| emails\_cc\_ids                      | List        |           |                                                                                              |
| follower\_ids                        | List        |           |                                                                                              |
| forum\_topic\_id                     | Ling        |           |                                                                                              |
| problem\_id                          | Long        |           |                                                                                              |
| has\_incidents                       | Boolean     |           |                                                                                              |
| due\_at                              | DateTime    |           |                                                                                              |
| tags                                 | List        |           |                                                                                              |
| via                                  | Struct      |           |                                                                                              |
| custom\_fields                       | List        |           |                                                                                              |
| satisfaction\_rating                 | Struct      |           |                                                                                              |
| sharing\_agreement\_ids              | List        |           |                                                                                              |
| followup\_ids                        | List        |           |                                                                                              |
| via\_followup\_source\_id            | Long        |           |                                                                                              |
| ticket\_form\_id                     | Long        |           |                                                                                              |
| brand\_id                            | Long        |           |                                                                                              |
| allow\_channelback                   | Boolean     |           |                                                                                              |
| allow\_attachments                   | Boolean     |           |                                                                                              |
| is\_public                           | Boolean     |           |                                                                                              |
| from\_messaging\_channel             | Boolean     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| assignee\_email                      | String      |           |                                                                                              |
| attribute\_value\_ids                | List        |           |                                                                                              |
| collaborators                        | List        |           |                                                                                              |
| comment                              | Struct      |           |                                                                                              |
| custom\_status\_id                   | Long        |           |                                                                                              |
| email\_ccs                           | Struct      |           |                                                                                              |
| followers                            | Struct      |           |                                                                                              |
| macro\_id                            | Long        |           |                                                                                              |
| macros\_ids                          | List        |           |                                                                                              |
| metadata                             | Struct      |           |                                                                                              |
| safe\_update                         | Boolean     |           |                                                                                              |
| updated\_stamp                       | DateTime    |           |                                                                                              |
| via\_id                              | Long        |           |                                                                                              |
| voice\_comment                       | Struct      |           |                                                                                              |
| DML\_STATUS                          | String      |           | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| trigger-category                     | url         | String    |                                                                                              |          |
| id                                   | String      |           |                                                                                              |
| name                                 | String      |           |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| trigger                              | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| active                               | Boolean     | EQUAL\_TO |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| actions                              | List        |           |                                                                                              |
| conditions                           | Struct      |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| raw\_title                           | String      |           |                                                                                              |
| category\_id                         | String      | EQUAL\_TO |                                                                                              |
| users                                | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| external\_id                         | String      | EQUAL\_TO |                                                                                              |
| email                                | String      |           |                                                                                              |
| active                               | Boolean     |           |                                                                                              |
| alias                                | String      |           |                                                                                              |
| chat\_only                           | Boolean     |           |                                                                                              |
| custom\_roll\_id                     | Long        |           |                                                                                              |
| roll\_type                           | Integer     |           |                                                                                              |
| details                              | String      |           |                                                                                              |
| last\_login\_at                      | DateTime    |           |                                                                                              |
| locale                               | String      |           |                                                                                              |
| locale\_id                           | Integer     |           |                                                                                              |
| moderator                            | Boolean     |           |                                                                                              |
| notes                                | String      |           |                                                                                              |
| name                                 | String      |           |                                                                                              |
| only\_private\_comments              | Boolean     |           |                                                                                              |
| organization\_id                     | Long        |           |                                                                                              |
| default\_group\_id                   | Long        |           |                                                                                              |
| phone                                | String      |           |                                                                                              |
| photo                                | Struct      |           |                                                                                              |
| remote\_photo\_url                   | String      |           |                                                                                              |
| restricted\_agent                    | Boolean     |           |                                                                                              |
| role                                 | String      | EQUAL\_TO |                                                                                              |
| shared                               | Boolean     |           |                                                                                              |
| shared\_agent                        | Boolean     |           |                                                                                              |
| tag                                  | List        |           |                                                                                              |
| signature                            | String      |           |                                                                                              |
| suspended                            | Boolean     |           |                                                                                              |
| ticket\_restriction                  | String      |           |                                                                                              |
| time\_zone                           | String      |           |                                                                                              |
| iana\_time\_zone                     |             |           |                                                                                              |
| two\_factor\_auth\_enabled           |             |           |                                                                                              |
| user\_fields                         |             |           |                                                                                              |
| verified                             | Boolean     |           |                                                                                              |
| report\_csv                          | Boolean     |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| updated\_at                          | DateTime    | EQUAL\_TO |                                                                                              |
| permission\_set                      | Long        | EQUAL\_TO |                                                                                              |
| shared\_phone\_number                | Boolean     |           |                                                                                              |
| DML\_STATUS                          | String      |           | A user-defined field used to track the created, updated and<br>deleted status of the record. |
| view                                 | url         | String    |                                                                                              |          |
| id                                   | Long        |           |                                                                                              |
| title                                | String      |           |                                                                                              |
| active                               | Boolean     | EQUAL\_TO |                                                                                              |
| updated\_at                          | DateTime    |           |                                                                                              |
| created\_at                          | DateTime    |           |                                                                                              |
| default                              | Boolean     |           |                                                                                              |
| position                             | Integer     |           |                                                                                              |
| description                          | String      |           |                                                                                              |
| execution                            | Struct      |           |                                                                                              |
| restriction                          | Struct      |           |                                                                                              |
| raw\_title                           | String      |           |                                                                                              |
| conditions                           | Struct      |           |                                                                                              |
| access                               | String      | EQUAL\_TO |                                                                                              |
| group\_id                            | Long        | EQUAL\_TO |                                                                                              |

###### Note

Struct and List data types are converted to String data type in the response of the connector.

## Partitioning queries

Partitions are not supported in Zendesk.
