

# Reading from Facebook Page Insights entities
<a name="facebook-page-insights-reading-from-entities"></a>

**Prerequisite**

A Facebook Page Insights object you would like to read from. You will need the object name.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Page Content | Yes | No | Yes | Yes | Yes | 
| Page CTA Clicks | Yes | No | No | Yes | Yes | 
| Page Engagement | Yes | No | No | Yes | Yes | 
| Page Impressions | Yes | No | No | Yes | Yes | 
| Page Posts | Yes | No | No | Yes | Yes | 
| Page Post Engagement | No | No | No | Yes | No | 
| Page Post Reactions | No | No | No | Yes | No | 
| Page Reactions | Yes | No | No | Yes | Yes | 
| Stories | Yes | No | No | Yes | Yes | 
| Page User Demographics | Yes | No | No | Yes | Yes | 
| Page Video Views | Yes | No | No | Yes | Yes | 
| Page Views | Yes | No | No | Yes | Yes | 
| Page Video Posts | Yes | No | No | Yes | Yes | 
| Pages | No | Yes | No | Yes | No | 
| Feeds | Yes | Yes | No | Yes | Yes | 

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



- **Page Content**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page CTA Clicks**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Engagement**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Impressions**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Posts**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Post Engagement**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Post Reactions**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page User Demographics**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Video Views**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Views**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Page Video Posts**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Period / **Data type:** Period / **Supported operators:** EQUAL\_TO
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO
  - **Field:** Values / **Data type:** List / **Supported operators:** N/A
  - **Field:** Title / **Data type:** String / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_from\_api\_doc / **Data type:** String / **Supported operators:** N/A
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A

- **Pages**
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** About / **Data type:** String / **Supported operators:** N/A
  - **Field:** access\_token / **Data type:** String / **Supported operators:** N/A
  - **Field:** ad\_campaign / **Data type:** String / **Supported operators:** N/A
  - **Field:** Affiliation / **Data type:** String / **Supported operators:** N/A
  - **Field:** app\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** artists\_we\_like / **Data type:** String / **Supported operators:** N/A
  - **Field:** Attire / **Data type:** String / **Supported operators:** N/A
  - **Field:** Awards / **Data type:** String / **Supported operators:** N/A
  - **Field:** band\_interests / **Data type:** String / **Supported operators:** N/A
  - **Field:** band\_members / **Data type:** String / **Supported operators:** N/A
  - **Field:** best\_page / **Data type:** String / **Supported operators:** N/A
  - **Field:** Bio / **Data type:** String / **Supported operators:** N/A
  - **Field:** Birthday / **Data type:** String / **Supported operators:** N/A
  - **Field:** booking\_agent / **Data type:** String / **Supported operators:** N/A
  - **Field:** Built / **Data type:** String / **Supported operators:** N/A
  - **Field:** can\_checkin / **Data type:** String / **Supported operators:** N/A
  - **Field:** can\_post / **Data type:** String / **Supported operators:** N/A
  - **Field:** Category / **Data type:** String / **Supported operators:** N/A
  - **Field:** category\_list / **Data type:** List / **Supported operators:** N/A
  - **Field:** Checkins / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** company\_overview / **Data type:** String / **Supported operators:** N/A
  - **Field:** connected\_instagram\_account / **Data type:** String / **Supported operators:** N/A
  - **Field:** contact\_address / **Data type:** String / **Supported operators:** N/A
  - **Field:** country\_page\_likes / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** Cover / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** culinary\_team / **Data type:** String / **Supported operators:** N/A
  - **Field:** current\_location / **Data type:** String / **Supported operators:** N/A
  - **Field:** delivery\_and\_pickup\_option\_info / **Data type:** List / **Supported operators:** N/A
  - **Field:** Description / **Data type:** String / **Supported operators:** N/A
  - **Field:** description\_html / **Data type:** String / **Supported operators:** N/A
  - **Field:** differently\_open\_offerings / **Data type:** List / **Supported operators:** N/A
  - **Field:** directed\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** display\_subtext / **Data type:** String / **Supported operators:** N/A
  - **Field:** displayed\_message\_response\_time / **Data type:** String / **Supported operators:** N/A
  - **Field:** Emails / **Data type:** String / **Supported operators:** N/A
  - **Field:** Engagement / **Data type:** String / **Supported operators:** N/A
  - **Field:** fan\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** featured\_video / **Data type:** String / **Supported operators:** N/A
  - **Field:** Features / **Data type:** String / **Supported operators:** N/A
  - **Field:** followers\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** food\_styles / **Data type:** List / **Supported operators:** N/A
  - **Field:** Founded / **Data type:** String / **Supported operators:** N/A
  - **Field:** general\_info / **Data type:** String / **Supported operators:** N/A
  - **Field:** general\_manager / **Data type:** String / **Supported operators:** N/A
  - **Field:** Genre / **Data type:** String / **Supported operators:** N/A
  - **Field:** global\_brand\_page\_name / **Data type:** String / **Supported operators:** N/A
  - **Field:** global\_brand\_root\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** has\_added\_app / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** has\_transitioned\_to\_new\_page\_experience / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** has\_whatsapp\_business\_number / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** has\_whatsapp\_number / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** Hometown / **Data type:** String / **Supported operators:** N/A
  - **Field:** Hours / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Impressum / **Data type:** String / **Supported operators:** N/A
  - **Field:** Influences / **Data type:** String / **Supported operators:** N/A
  - **Field:** instagram\_business\_account / **Data type:** String / **Supported operators:** N/A
  - **Field:** is\_always\_open / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_chain / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_community\_page / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_eligible\_for\_branded\_content / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_messenger\_bot\_get\_started\_enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_messenger\_platform\_bot / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_owned / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_permanently\_closed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_published / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** Name / **Data type:** String / **Supported operators:** N/A
  - **Field:** Tasks / **Data type:** List / **Supported operators:** N/A
  - **Field:** is\_unclaimed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_webhooks\_subscribed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** leadgen\_tos\_acceptance\_time / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** leadgen\_tos\_accepted / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** leadgen\_tos\_accepting\_user / **Data type:** String / **Supported operators:** N/A
  - **Field:** leadgen\_tos\_accepting\_user / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Link / **Data type:** Link / **Supported operators:** N/A
  - **Field:** Location / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Members / **Data type:** String / **Supported operators:** N/A
  - **Field:** merchant\_review\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** messenger\_ads\_default\_icebreakers / **Data type:** List / **Supported operators:** N/A
  - **Field:** messenger\_ads\_default\_page\_welcome\_message / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** messenger\_ads\_default\_quick\_replies / **Data type:** List / **Supported operators:** N/A
  - **Field:** messenger\_ads\_quick\_replies\_type / **Data type:** String / **Supported operators:** N/A
  - **Field:** Mission / **Data type:** String / **Supported operators:** N/A
  - **Field:** Mpg / **Data type:** String / **Supported operators:** N/A
  - **Field:** name\_with\_location\_descriptor / **Data type:** String / **Supported operators:** N/A
  - **Field:** Network / **Data type:** String / **Supported operators:** N/A
  - **Field:** new\_like\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** offer\_eligible / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** overall\_star\_rating / **Data type:** Float / **Supported operators:** N/A
  - **Field:** page\_token / **Data type:** String / **Supported operators:** N/A
  - **Field:** parent\_page / **Data type:** String / **Supported operators:** N/A
  - **Field:** Parking / **Data type:** String / **Supported operators:** N/A
  - **Field:** payment\_options / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** personal\_info / **Data type:** String / **Supported operators:** N/A
  - **Field:** personal\_interests / **Data type:** String / **Supported operators:** N/A
  - **Field:** pharma\_safety\_info / **Data type:** String / **Supported operators:** N/A
  - **Field:** Phone / **Data type:** String / **Supported operators:** N/A
  - **Field:** pickup\_options / **Data type:** List / **Supported operators:** N/A
  - **Field:** place\_type / **Data type:** String / **Supported operators:** N/A
  - **Field:** plot\_outline / **Data type:** String / **Supported operators:** N/A
  - **Field:** press\_contact / **Data type:** String / **Supported operators:** N/A
  - **Field:** price\_range / **Data type:** String / **Supported operators:** N/A
  - **Field:** privacy\_info\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** produced\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** Products / **Data type:** String / **Supported operators:** N/A
  - **Field:** promotion\_eligible / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** promotion\_ineligible\_reason / **Data type:** String / **Supported operators:** N/A
  - **Field:** public\_transit / **Data type:** String / **Supported operators:** N/A
  - **Field:** rating\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** record\_label / **Data type:** String / **Supported operators:** N/A
  - **Field:** release\_date / **Data type:** String / **Supported operators:** N/A
  - **Field:** restaurant\_services / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** restaurant\_specialties / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Schedule / **Data type:** String / **Supported operators:** N/A
  - **Field:** screenplay\_by / **Data type:** String / **Supported operators:** N/A
  - **Field:** Season / **Data type:** String / **Supported operators:** N/A
  - **Field:** single\_line\_address / **Data type:** String / **Supported operators:** N/A
  - **Field:** Starring / **Data type:** String / **Supported operators:** N/A
  - **Field:** start\_info / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** store\_code / **Data type:** String / **Supported operators:** N/A
  - **Field:** store\_location\_descriptor / **Data type:** String / **Supported operators:** N/A
  - **Field:** store\_number / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** Studio / **Data type:** String / **Supported operators:** N/A
  - **Field:** supports\_donate\_button\_in\_live\_video / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** talking\_about\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** temporary\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** unread\_message\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** unread\_notif\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** unseen\_message\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** Username / **Data type:** String / **Supported operators:** N/A
  - **Field:** verification\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** voip\_info / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Website / **Data type:** String / **Supported operators:** N/A
  - **Field:** were\_here\_count / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** whatsapp\_number / **Data type:** String / **Supported operators:** N/A

- **written\_by**
  - **Field:** String
  - **Data type:** N/A

- **Feeds**
  - **Field:** Id / **Data type:** String / **Supported operators:** N/A
  - **Field:** Actions / **Data type:** List / **Supported operators:** N/A
  - **Field:** admin\_creator / **Data type:** Object / **Supported operators:** N/A
  - **Field:** Application / **Data type:** Object / **Supported operators:** N/A
  - **Field:** Attachments / **Data type:** Objects / **Supported operators:** N/A
  - **Field:** backdated\_time / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** call\_to\_action / **Data type:** Object / **Supported operators:** N/A
  - **Field:** can\_reply\_privately / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** child\_attachments / **Data type:** List / **Supported operators:** N/A
  - **Field:** Coordinates / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** created\_time / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** Event / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** expanded\_height / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** expanded\_width / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** feed\_targeting / **Data type:** Object / **Supported operators:** N/A
  - **Field:** From / **Data type:** Object / **Supported operators:** N/A
  - **Field:** full\_picture / **Data type:** String / **Supported operators:** N/A
  - **Field:** Height / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** Icon / **Data type:** String / **Supported operators:** N/A
  - **Field:** instagram\_eligibility / **Data type:** String / **Supported operators:** N/A
  - **Field:** is\_eligible\_for\_promotion / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_expired / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_hidden / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_inline\_created / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_instagram\_eligible / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_popular / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_published / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** is\_spherical / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** Message / **Data type:** String / **Supported operators:** N/A
  - **Field:** message\_tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** multi\_share\_end\_card / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** multi\_share\_optimized / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** parent\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** permalink\_url / **Data type:** String / **Supported operators:** N/A
  - **Field:** Place / **Data type:** String / **Supported operators:** N/A
  - **Field:** Privacy / **Data type:** Object / **Supported operators:** N/A
  - **Field:** promotable\_id / **Data type:** String / **Supported operators:** N/A
  - **Field:** promotion\_status / **Data type:** String / **Supported operators:** N/A
  - **Field:** Properties / **Data type:** List / **Supported operators:** N/A
  - **Field:** scheduled\_publish\_time / **Data type:** Float / **Supported operators:** N/A
  - **Field:** Shares / **Data type:** Object / **Supported operators:** N/A
  - **Field:** status\_type / **Data type:** String / **Supported operators:** N/A
  - **Field:** Story / **Data type:** String / **Supported operators:** N/A
  - **Field:** story\_tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** Subscribed / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** Target / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** Targeting / **Data type:** Object / **Supported operators:** N/A
  - **Field:** To / **Data type:** Object / **Supported operators:** N/A
  - **Field:** timeline\_visibility / **Data type:** String / **Supported operators:** N/A
  - **Field:** updated\_time / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** Via / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** video\_buying\_eligibility / **Data type:** List / **Supported operators:** N/A
  - **Field:** Width / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** Since / **Data type:** DateTime / **Supported operators:** EQUAL\_TO



## Partitioning queries
<a name="facebook-page-insights-reading-partitioning-queries"></a>

**Filter-based partitioning**:

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the Datetime field, we accept the Spark timestamp format used in Spark SQL queries.

  Examples of valid value:

  ```
  "2024-09-30T01:01:01.000Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

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