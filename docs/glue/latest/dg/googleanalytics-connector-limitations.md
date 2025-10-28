# Limitations and considerations

The following are limitations for the Google Analytics 4 connector:

- For the Core Report entity, only 9 dimension fields and 10 metric fields are allowed to send in a request.
  If the allowed number of fields is exceeded then request will fail and connector will throw an error message.
- For the Realtime Report entity, only 4 dimension fields are allowed to send in a request. If the allowed number of
  fields is exceeded then request will fail and connector will throw an error message.
- Google Analytics 4 is a beta version free tool, so there will be regular update on new feature, entities enhancement,
  adding new fields and deprecating existing fields.
- Core Report fields are populated dynamically, so there will be addition, depreciation and renaming of fields and
  imposing new limits on fields can be done anytime.
- The default start date is 30 days and the end date is yesterday (one day before the current date), and these dates
  will get overridden in filter expression code if user has set the value OR if the flow is incremental.
- As per the documentation, Real-Time report entity returns 10,000 records if limit is not pass in the request,
  otherwise the API returns a maximum of 250,000 rows per request, no matter how many you ask for. For more
  information see
  [Method: properties.runRealtimeReport](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runRealtimeReport "https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runRealtimeReport") in the Google Analytics documentation.
- Real-Time Report entity does not support Record Based Partition as it does not support pagination. Also, it does not
  support Field Based Partition as none of the fields fulfill the criteria defined.
- Due to the limitation on number of fields that can be passed in a request. We are setting default dimension and metric
  fields within the designated limits. If "select all" is chosen, only the data from those predetermined fields will be
  retrieved.
  - Core Report
    - As per limitation from SAAS - requests are allowed up to 9 dimensions and up to 10 metrics only (that is,
      a request can contain a maximum of 19 fields(metrics + dimension).
    - As per the implementation - If user utilizes SELECT_ALL or selected fields more than 25, then default
      fields will be pass in the request.
    - The following fields are considered as default fields for Core Report -
      "country", "city", "eventName", "cityId", "browser", "date", "currencyCode", "deviceCategory",
      "transactionId", active1DayUsers", "active28DayUsers", "active7DayUsers", "activeUsers",
      "averagePurchaseRevenue", "averageRevenuePerUser", "averageSessionDuration", "engagedSessions",
      "eventCount", "engagementRate".

  - Real-Time Report
    - As per limitation from SAAS requests are allowed up to 4 dimensions.
    - If user pass SELECT_ALL or selected fields more than 15, then default fields will be pass in the request.
    - The following fields are considered as default fields for RealTime Report -
      "country", "deviceCategory", "city", "cityId", "activeUsers", "conversions", "eventCount",
      "screenPageViews".

- In Core-Report entity, if partition on date field and filter on startDate is present simultaneously.
  In that case dateRange value gets overridden with the startDate filter value, But, since partition must always
  be the priority, hence discarding startDate filter if partition on date field is already present.
- As now cohortSpecs is also a part of core-report request body we enhanced the current core-report entity to include
  support for the cohortSpec attribute. In cohortSpecs request body, nearly all fields require user input. To address
  this, we have set default values for those attributes/fields and provided provision for user to override these values
  if needed.

| FieldName   | Default values                    | Sample query to pass in filterPredicate options to override default values |
| ----------- | --------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| startDate   | 30 days ago from the current date | "startDate between "2023-05-09" and "2023-05-10"                           |
| endDate     | 1 day ago from current date       | "startDate between "2023-05-09" and "2023-05-10"                           |
| startOffset | 0                                 | startOffset=2                                                              |
| endOffset   | 1                                 | endOffset=10                                                               |
| granularity | DAILY                             | granularity="WEEKLY"                                                       | <br>• You can also pass all these filters together at once or with other filters. + Example 1 - filterPredicate: startDate between "2023-05-09" and "2023-05-10" AND startOffset=1 AND endOffset=2 AND granularity="WEEKLY" + Example 2 - filterPredicate: city=“xyz” AND startOffset=1 AND endOffset=2 AND granularity="WEEKLY" <br>• In cohort request: + If ‘cohortNthMonth’ is passed in the request, then internally granularity value will be set as “MONTHLY” + Similarly, if ‘cohortNthWeek’ is passed, then granularity value will be set as “WEEKLY” + And, for ‘cohortNthDay’ granularity value will be set as “DAILY”. For more information, see: <br>• [https://developers.google.com/analytics/devguides/reporting/data/v1/advanced](https://developers.google.com/analytics/devguides/reporting/data/v1/advanced "https://developers.google.com/analytics/devguides/reporting/data/v1/advanced") <br>• [https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/CohortSpec](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/CohortSpec "https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/CohortSpec") + Provision is given for the user to override dateRange and granularity default value. Refer to the above table. |
