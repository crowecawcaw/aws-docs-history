

# Reading from Google Search Console entities
<a name="google-search-console-reading-from-entities"></a>

**Prerequisite**

A Google Search Console object you would like to read from. You will need the object name.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Search Analytics | Yes | Yes | No | Yes | No | 
| Sites | No | No | No | Yes | No | 
| Sitemaps | No | No | No | Yes | No | 

**Example**:

```
googleSearchConsole_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googlesearchconsole",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "API_VERSION": "v3"
    }
```

**Google Search Console entity and field details**:

Google Search Console provides endpoints to fetch metadata dynamically for supported entities. Accordingly, operator support is captured at the datatype level.



- **Search Analytics**
  - **Field:** keys / **Data type:** List / **Supported operators:** N/A / **Note:** 
  - **Field:** clicks / **Data type:** Double / **Supported operators:** N/A / **Note:** 
  - **Field:** impressions / **Data type:** Double / **Supported operators:** N/A / **Note:** 
  - **Field:** ctr / **Data type:** BigDecimal / **Supported operators:** N/A / **Note:** For BigDecimal datatype, the value '0' is formatted as '0E-18'
  - **Field:** position / **Data type:** Double / **Supported operators:** N/A / **Note:** 
  - **Field:** start\_end\_date / **Data type:** Date / **Supported operators:** BETWEEN / **Note:** Default value for start\_end\_date is between <30 days ago from the current date> AND <yesterday: that is, 1 day ago from the current date> Note: expects you to pass a UTC date value.<br />Example: start\_end\_date between '2022-01-01' AND '2024-09-09'
  - **Field:** country / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS / **Note:** Valid values are "IND", "CAN", etc.
  - **Field:** type / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO / **Note:** Valid values are "discover", "googleNews", "news", "image", "video", "web"
  - **Field:** searchAppearance / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS / **Note:** See [Search Appearance](https://support.google.com/webmasters/answer/7576553#by_search_appearance) for a list of valid values.
  - **Field:** device / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS / **Note:** Valid values are "DESKTOP", "MOBILE", "TABLET"
  - **Field:** dimensions / **Data type:** String / **Supported operators:** EQUAL\_TO / **Note:** Valid values are "country", "device"
  - **Field:** page / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS / **Note:** 
  - **Field:** query / **Data type:** String / **Supported operators:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS / **Note:** 
  - **Field:** dataState / **Data type:** String / **Supported operators:** EQUAL\_TO / **Note:** Valid values are "all" and "final"

- **Sites**
  - **Field:** siteUrl / **Data type:** String / **Supported operators:** N/A / **Note:** 
  - **Field:** permissionLevel / **Data type:** String / **Supported operators:** N/A / **Note:** 

- **Sitemaps**
  - **Field:** path / **Data type:** String / **Supported operators:** N/A / **Note:** 
  - **Field:** type / **Data type:** String / **Supported operators:** N/A / **Note:** 
  - **Field:** lastSubmitted / **Data type:** DateTime / **Supported operators:** N/A / **Note:** 
  - **Field:** isPending / **Data type:** Boolean / **Supported operators:** N/A / **Note:** 
  - **Field:** isSitemapsIndex / **Data type:** Boolean / **Supported operators:** N/A / **Note:** 
  - **Field:** lastDownloaded / **Data type:** DateTime / **Supported operators:** N/A / **Note:** 
  - **Field:** warnings / **Data type:** Long / **Supported operators:** N/A / **Note:** 
  - **Field:** errors / **Data type:** Long / **Supported operators:** N/A / **Note:** 
  - **Field:** contents / **Data type:** List / **Supported operators:** N/A / **Note:** 



**Note**  
For an updated list of valid values for filters, see the [Google Search Console](https://developers.google.com/webmaster-tools/v1/searchanalytics/query) API docs.  
The field `start_end_date` is a combination of `start_date` and `end_date`.

## Partitioning queries
<a name="google-search-console-reading-partitioning-queries"></a>

Filter-based partitioning and record-based partitioning are not supported.