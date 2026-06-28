# Reading from Facebook Page Insights entities

**Prerequisite**

A Facebook Page Insights object you would like to read from. You will need the object name.

**Supported entities for source**:

| Entity                 | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning |
| ---------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Page Content           | Yes             | No             | Yes               | Yes                | Yes                   |
| Page CTA Clicks        | Yes             | No             | No                | Yes                | Yes                   |
| Page Engagement        | Yes             | No             | No                | Yes                | Yes                   |
| Page Impressions       | Yes             | No             | No                | Yes                | Yes                   |
| Page Posts             | Yes             | No             | No                | Yes                | Yes                   |
| Page Post Engagement   | No              | No             | No                | Yes                | No                    |
| Page Post Reactions    | No              | No             | No                | Yes                | No                    |
| Page Reactions         | Yes             | No             | No                | Yes                | Yes                   |
| Stories                | Yes             | No             | No                | Yes                | Yes                   |
| Page User Demographics | Yes             | No             | No                | Yes                | Yes                   |
| Page Video Views       | Yes             | No             | No                | Yes                | Yes                   |
| Page Views             | Yes             | No             | No                | Yes                | Yes                   |
| Page Video Posts       | Yes             | No             | No                | Yes                | Yes                   |
| Pages                  | No              | Yes            | No                | Yes                | No                    |
| Feeds                  | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**:

```
facebookPageInsights_read = glueContext.create_dynamic_frame. from options(
    connection_type="facebookpageinsights",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v21"
   }
```

**Facebook Page Insights field details**:

| Entity                                          | Field    | Data type | Supported operators |
| ----------------------------------------------- | -------- | --------- | ------------------- |
| Page Content                                    | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page CTA Clicks                                 | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Engagement                                 | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Impressions                                | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Posts                                      | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Post Engagement                            | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Post Reactions                             | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page User Demographics                          | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Video Views                                | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Views                                      | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Page Video Posts                                | Name     | String    | N/A                 |
| Period                                          | Period   | EQUAL\_TO |
| Since                                           | DateTime | EQUAL\_TO |
| Values                                          | List     | N/A       |
| Title                                           | String   | N/A       |
| Description                                     | String   | N/A       |
| description\_from\_api\_doc                     | String   | N/A       |
| Id                                              | String   | N/A       |
| Pages                                           | Name     | String    | N/A                 |
| About                                           | String   | N/A       |
| access\_token                                   | String   | N/A       |
| ad\_campaign                                    | String   | N/A       |
| Affiliation                                     | String   | N/A       |
| app\_id                                         | String   | N/A       |
| artists\_we\_like                               | String   | N/A       |
| Attire                                          | String   | N/A       |
| Awards                                          | String   | N/A       |
| band\_interests                                 | String   | N/A       |
| band\_members                                   | String   | N/A       |
| best\_page                                      | String   | N/A       |
| Bio                                             | String   | N/A       |
| Birthday                                        | String   | N/A       |
| booking\_agent                                  | String   | N/A       |
| Built                                           | String   | N/A       |
| can\_checkin                                    | String   | N/A       |
| can\_post                                       | String   | N/A       |
| Category                                        | String   | N/A       |
| category\_list                                  | List     | N/A       |
| Checkins                                        | Integer  | N/A       |
| company\_overview                               | String   | N/A       |
| connected\_instagram\_account                   | String   | N/A       |
| contact\_address                                | String   | N/A       |
| country\_page\_likes                            | Integer  | N/A       |
| Cover                                           | Struct   | N/A       |
| culinary\_team                                  | String   | N/A       |
| current\_location                               | String   | N/A       |
| delivery\_and\_pickup\_option\_info             | List     | N/A       |
| Description                                     | String   | N/A       |
| description\_html                               | String   | N/A       |
| differently\_open\_offerings                    | List     | N/A       |
| directed\_by                                    | String   | N/A       |
| display\_subtext                                | String   | N/A       |
| displayed\_message\_response\_time              | String   | N/A       |
| Emails                                          | String   | N/A       |
| Engagement                                      | String   | N/A       |
| fan\_count                                      | Integer  | N/A       |
| featured\_video                                 | String   | N/A       |
| Features                                        | String   | N/A       |
| followers\_count                                | Integer  | N/A       |
| food\_styles                                    | List     | N/A       |
| Founded                                         | String   | N/A       |
| general\_info                                   | String   | N/A       |
| general\_manager                                | String   | N/A       |
| Genre                                           | String   | N/A       |
| global\_brand\_page\_name                       | String   | N/A       |
| global\_brand\_root\_id                         | String   | N/A       |
| has\_added\_app                                 | Boolean  | N/A       |
| has\_transitioned\_to\_new\_page\_experience    | Boolean  | N/A       |
| has\_whatsapp\_business\_number                 | Boolean  | N/A       |
| has\_whatsapp\_number                           | Boolean  | N/A       |
| Hometown                                        | String   | N/A       |
| Hours                                           | Struct   | N/A       |
| Impressum                                       | String   | N/A       |
| Influences                                      | String   | N/A       |
| instagram\_business\_account                    | String   | N/A       |
| is\_always\_open                                | Boolean  | N/A       |
| is\_chain                                       | Boolean  | N/A       |
| is\_community\_page                             | Boolean  | N/A       |
| is\_eligible\_for\_branded\_content             | Boolean  | N/A       |
| is\_messenger\_bot\_get\_started\_enabled       | Boolean  | N/A       |
| is\_messenger\_platform\_bot                    | Boolean  | N/A       |
| is\_owned                                       | Boolean  | N/A       |
| is\_permanently\_closed                         | Boolean  | N/A       |
| is\_published                                   | Boolean  | N/A       |
| Name                                            | String   | N/A       |
| Tasks                                           | List     | N/A       |
| is\_unclaimed                                   | Boolean  | N/A       |
| is\_webhooks\_subscribed                        | Boolean  | N/A       |
| leadgen\_tos\_acceptance\_time                  | DateTime | N/A       |
| leadgen\_tos\_accepted                          | Boolean  | N/A       |
| leadgen\_tos\_accepting\_user                   | String   | N/A       |
| leadgen\_tos\_accepting\_user                   | Struct   | N/A       |
| Link                                            | Link     | N/A       |
| Location                                        | Struct   | N/A       |
| Members                                         | String   | N/A       |
| merchant\_review\_status                        | String   | N/A       |
| messenger\_ads\_default\_icebreakers            | List     | N/A       |
| messenger\_ads\_default\_page\_welcome\_message | Struct   | N/A       |
| messenger\_ads\_default\_quick\_replies         | List     | N/A       |
| messenger\_ads\_quick\_replies\_type            | String   | N/A       |
| Mission                                         | String   | N/A       |
| Mpg                                             | String   | N/A       |
| name\_with\_location\_descriptor                | String   | N/A       |
| Network                                         | String   | N/A       |
| new\_like\_count                                | Integer  | N/A       |
| offer\_eligible                                 | Boolean  | N/A       |
| overall\_star\_rating                           | Float    | N/A       |
| page\_token                                     | String   | N/A       |
| parent\_page                                    | String   | N/A       |
| Parking                                         | String   | N/A       |
| payment\_options                                | Struct   | N/A       |
| personal\_info                                  | String   | N/A       |
| personal\_interests                             | String   | N/A       |
| pharma\_safety\_info                            | String   | N/A       |
| Phone                                           | String   | N/A       |
| pickup\_options                                 | List     | N/A       |
| place\_type                                     | String   | N/A       |
| plot\_outline                                   | String   | N/A       |
| press\_contact                                  | String   | N/A       |
| price\_range                                    | String   | N/A       |
| privacy\_info\_url                              | String   | N/A       |
| produced\_by                                    | String   | N/A       |
| Products                                        | String   | N/A       |
| promotion\_eligible                             | Boolean  | N/A       |
| promotion\_ineligible\_reason                   | String   | N/A       |
| public\_transit                                 | String   | N/A       |
| rating\_count                                   | Integer  | N/A       |
| record\_label                                   | String   | N/A       |
| release\_date                                   | String   | N/A       |
| restaurant\_services                            | Struct   | N/A       |
| restaurant\_specialties                         | Struct   | N/A       |
| Schedule                                        | String   | N/A       |
| screenplay\_by                                  | String   | N/A       |
| Season                                          | String   | N/A       |
| single\_line\_address                           | String   | N/A       |
| Starring                                        | String   | N/A       |
| start\_info                                     | Struct   | N/A       |
| store\_code                                     | String   | N/A       |
| store\_location\_descriptor                     | String   | N/A       |
| store\_number                                   | Integer  | N/A       |
| Studio                                          | String   | N/A       |
| supports\_donate\_button\_in\_live\_video       | Boolean  | N/A       |
| talking\_about\_count                           | Integer  | N/A       |
| temporary\_status                               | String   | N/A       |
| unread\_message\_count                          | Integer  | N/A       |
| unread\_notif\_count                            | Integer  | N/A       |
| unseen\_message\_count                          | Integer  | N/A       |
| Username                                        | String   | N/A       |
| verification\_status                            | String   | N/A       |
| voip\_info                                      | Struct   | N/A       |
| Website                                         | String   | N/A       |
| were\_here\_count                               | Integer  | N/A       |
| whatsapp\_number                                | String   | N/A       |
| written\_by                                     | String   | N/A       |
| Feeds                                           | Id       | String    | N/A                 |
| Actions                                         | List     | N/A       |
| admin\_creator                                  | Object   | N/A       |
| Application                                     | Object   | N/A       |
| Attachments                                     | Objects  | N/A       |
| backdated\_time                                 | DateTime | N/A       |
| call\_to\_action                                | Object   | N/A       |
| can\_reply\_privately                           | Boolean  | N/A       |
| child\_attachments                              | List     | N/A       |
| Coordinates                                     | Struct   | N/A       |
| created\_time                                   | DateTime | N/A       |
| Event                                           | Struct   | N/A       |
| expanded\_height                                | Integer  | N/A       |
| expanded\_width                                 | Integer  | N/A       |
| feed\_targeting                                 | Object   | N/A       |
| From                                            | Object   | N/A       |
| full\_picture                                   | String   | N/A       |
| Height                                          | Integer  | N/A       |
| Icon                                            | String   | N/A       |
| instagram\_eligibility                          | String   | N/A       |
| is\_eligible\_for\_promotion                    | Boolean  | N/A       |
| is\_expired                                     | Boolean  | N/A       |
| is\_hidden                                      | Boolean  | N/A       |
| is\_inline\_created                             | Boolean  | N/A       |
| is\_instagram\_eligible                         | Boolean  | N/A       |
| is\_popular                                     | Boolean  | N/A       |
| is\_published                                   | Boolean  | N/A       |
| is\_spherical                                   | Boolean  | N/A       |
| Message                                         | String   | N/A       |
| message\_tags                                   | List     | N/A       |
| multi\_share\_end\_card                         | Boolean  | N/A       |
| multi\_share\_optimized                         | Boolean  | N/A       |
| parent\_id                                      | String   | N/A       |
| permalink\_url                                  | String   | N/A       |
| Place                                           | String   | N/A       |
| Privacy                                         | Object   | N/A       |
| promotable\_id                                  | String   | N/A       |
| promotion\_status                               | String   | N/A       |
| Properties                                      | List     | N/A       |
| scheduled\_publish\_time                        | Float    | N/A       |
| Shares                                          | Object   | N/A       |
| status\_type                                    | String   | N/A       |
| Story                                           | String   | N/A       |
| story\_tags                                     | List     | N/A       |
| Subscribed                                      | Boolean  | N/A       |
| Target                                          | Struct   | N/A       |
| Targeting                                       | Object   | N/A       |
| To                                              | Object   | N/A       |
| timeline\_visibility                            | String   | N/A       |
| updated\_time                                   | DateTime | N/A       |
| Via                                             | Struct   | N/A       |
| video\_buying\_eligibility                      | List     | N/A       |
| Width                                           | Integer  | N/A       |
| Since                                           | DateTime | EQUAL\_TO |

## Partitioning queries

**Filter-based partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`,
`LOWER_BOUND`, `UPPER_BOUND`, and
`NUM_PARTITIONS` if you want to utilize concurrency in Spark. With
these parameters, the original query would be split into `NUM_PARTITIONS`
number of sub-queries that can be executed by Spark tasks
concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

Examples of valid value:

```
"2024-09-30T01:01:01.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

Example:

```
facebookPageInsights_read = glueContext.create_dynamic_frame.from_options(
     connection_type="facebookpageinsights",
     connection_options={
         "connectionName": "connectionName",
         "ENTITY_NAME": "entityName",
         "API_VERSION": "v21",
         "PARTITION_FIELD": "created_Time"
         "LOWER_BOUND": "2024-10-27T07:00:00+0000"
         "UPPER_BOUND": "2024-10-27T07:00:00+0000"
         "NUM_PARTITIONS": "10"
     }
```
