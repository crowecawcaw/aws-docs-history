# Reading from Google Ads entities

**Prerequisites**

- A Google Ads Object you would like to read from. Refer the supported entities table below to check the available
  entities.

**Supported entities**

| Entity          | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| --------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Ad Group Ad     | Yes             | Yes            | Yes               | No                 | Yes                   |
| Ad Group        | Yes             | Yes            | Yes               | No                 | Yes                   |
| Campaign Budget | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Account Budget  | Yes             | No             | Yes               | Yes                | No                    |
| Campaign        | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Account         | Yes             | No             | Yes               | No                 | No                    |

**Example**

```
googleAds_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googleads",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "campaign-3467***",
        "API_VERSION": "v16"
    }
```

**Google Ads entity and field details**

| Entity          | Field                                     | Data Type  | Supported Operators          |
| --------------- | ----------------------------------------- | ---------- | ---------------------------- |
| Account         | resourceName                              | String     | !=, =                        |
| Account         | callReportingEnabled                      | Boolean    | !=, =                        |
| Account         | callConversionReportingEnabled            | Boolean    | !=, =                        |
| Account         | callConversionAction                      | String     | !=, =                        |
| Account         | conversionTrackingId                      | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | crossAccountConversionTrackingId          | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | payPerConversionEligibilityFailureReasons | List       |                              |
| Account         | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | currencyCode                              | String     | !=, =, LIKE                  |
| Account         | timeZone                                  | String     | !=, =, LIKE                  |
| Account         | autoTaggingEnabled                        | Boolean    | !=, =                        |
| Account         | hasPartnersBadge                          | Boolean    | !=, =                        |
| Account         | manager                                   | Boolean    | !=, =                        |
| Account         | testAccount                               | Boolean    | !=, =                        |
| Account         | date                                      | Date       | BETWEEN, =, <, >, <=, >=     |
| Account         | costMicros                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | acceptedCustomerDataTerms                 | Boolean    |                              |
| Account         | conversionTrackingStatus                  | String     | !=, =, LIKE                  |
| Account         | enhancedConversionsForLeadsEnabled        | Boolean    |                              |
| Account         | googleAdsConversionCustomer               | String     |                              |
| Account         | status                                    | String     | !=, =                        |
| Account         | allConversionsByConversionDate            | Double     | !=, =, <, >                  |
| Account         | allConversionsValueByConversionDate       | Double     | !=, =, <, >                  |
| Account         | conversionsByConversionDate               | Double     | !=, =, <, >                  |
| Account         | conversionsValueByConversionDate          | Double     | !=, =, <, >                  |
| Account         | valuePerAllConversionsByConversionDate    | Double     | !=, =, <, >                  |
| Account         | videoViews                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | clicks                                    | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | invalidClicks                             | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | costPerAllConversions                     | Double     | !=, =, <, >                  |
| Account         | costPerConversion                         | Double     | !=, =, <, >                  |
| Account         | conversions                               | Double     | !=, =, <, >                  |
| Account         | absoluteTopImpressionPercentage           | Double     | !=, =, <, >                  |
| Account         | impressions                               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | topImpressionPercentage                   | Double     | !=, =, <, >                  |
| Account         | averageCpc                                | Double     | !=, =, <, >                  |
| Account         | activeViewMeasurableCostMicros            | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account         | averageCost                               | Double     | !=, =, <, >                  |
| Account         | ctr                                       | Double     | !=, =, <, >                  |
| Account         | activeViewCtr                             | Double     | !=, =, <, >                  |
| Account         | searchImpressionShare                     | Double     | !=, =, <, >                  |
| Account         | conversionAction                          | String     | !=, =                        |
| Account         | conversionActionCategory                  | String     | !=, =                        |
| Account         | conversionActionName                      | String     | !=, =, LIKE                  |
| Account Budget  | resourceName                              | String     | !=, =                        |
| Account Budget  | status                                    | String     | !=, =                        |
| Account Budget  | proposedEndTimeType                       | String     | !=, =                        |
| Account Budget  | approvedEndTimeType                       | String     | !=, =                        |
| Account Budget  | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account Budget  | billingSetup                              | String     | !=, =                        |
| Account Budget  | name                                      | String     | !=, =, LIKE                  |
| Account Budget  | approvedStartDateTime                     | DateTime   | BETWEEN, =, <, >, <=, >=     |
| Account Budget  | proposedSpendingLimitMicros               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account Budget  | approvedSpendingLimitMicros               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account Budget  | adjustedSpendingLimitMicros               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Account Budget  | amountServedMicros                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | resourceName                              | String     | !=, =, LIKE                  |
| Ad Group        | status                                    | String     | !=, =, LIKE                  |
| Ad Group        | type                                      | String     | !=, =, LIKE                  |
| Ad Group        | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | name                                      | String     | !=, =, LIKE                  |
| Ad Group        | campaign                                  | String     | !=, =                        |
| Ad Group        | cpcBidMicros                              | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | targetCpaMicros                           | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | cpmBidMicros                              | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | cpvBidMicros                              | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | targetCpmMicros                           | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | effectiveTargetCpaMicros                  | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | date                                      | Date       | BETWEEN, =, <, >, <=, >=     |
| Ad Group        | costMicros                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | useAudienceGrouped                        | Boolean    | !=, =                        |
| Ad Group        | effectiveCpcBidMicros                     | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | allConversionsByConversionDate            | Double     | !=, =, <, >                  |
| Ad Group        | allConversionsValueByConversionDate       | Double     | !=, =, <, >                  |
| Ad Group        | conversionsByConversionDate               | Double     | !=, =, <, >                  |
| Ad Group        | conversionsValueByConversionDate          | Double     | !=, =, <, >                  |
| Ad Group        | valuePerAllConversionsByConversionDate    | Double     | !=, =, <, >                  |
| Ad Group        | valuePerConversionsByConversionDate       | Double     | !=, =, <, >                  |
| Ad Group        | averageCost                               | Double     | !=, =, <, >                  |
| Ad Group        | costPerAllConversions                     | Double     | !=, =, <, >                  |
| Ad Group        | costPerConversion                         | Double     | !=, =, <, >                  |
| Ad Group        | averagePageViews                          | Double     | !=, =, <, >                  |
| Ad Group        | videoViews                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | clicks                                    | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | allConversions                            | Double     | !=, =, <, >                  |
| Ad Group        | averageCpc                                | Double     | !=, =, <, >                  |
| Ad Group        | absoluteTopImpressionPercentage           | Double     | !=, =, <, >                  |
| Ad Group        | impressions                               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group        | topImpressionPercentage                   | Double     | !=, =, <, >                  |
| Ad Group        | activeViewCtr                             | Double     | !=, =, <, >                  |
| Ad Group        | ctr                                       | Double     | !=, =, <, >                  |
| Ad Group        | searchTopImpressionShare                  | Double     | !=, =, <, >                  |
| Ad Group        | searchImpressionShare                     | Double     | !=, =, <, >                  |
| Ad Group        | searchAbsoluteTopImpressionShare          | Double     | !=, =, <, >                  |
| Ad Group        | relativeCtr                               | Double     | !=, =, <, >                  |
| Ad Group        | conversionAction                          | String     | !=, =                        |
| Ad Group        | conversionActionCategory                  | String     | !=, =                        |
| Ad Group        | conversionActionName                      | String     | !=, =, LIKE                  |
| Ad Group        | updateMask                                | String     |                              |
| Ad Group        | create                                    | Struct     |                              |
| Ad Group        | update                                    | Struct     |                              |
| Ad Group        | primaryStatus                             | String     | !=, =                        |
| Ad Group        | primaryStatusReasons                      | List       |                              |
| Ad Group Ad     | resourceName                              | String     | !=, =                        |
| Ad Group Ad     | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | status                                    | String     | !=, =                        |
| Ad Group Ad     | labels                                    | List       |                              |
| Ad Group Ad     | adGroup                                   | String     | !=, =                        |
| Ad Group Ad     | costMicros                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | approvalStatus                            | String     | !=, =                        |
| Ad Group Ad     | reviewStatus                              | String     | !=, =                        |
| Ad Group Ad     | adStrength                                | String     | !=, =                        |
| Ad Group Ad     | type                                      | String     | !=, =                        |
| Ad Group Ad     | businessName                              | String     | !=, =, LIKE                  |
| Ad Group Ad     | date                                      | Date       | BETWEEN, =, <, >, <=, >=     |
| Ad Group Ad     | allConversionsByConversionDate            | Double     | !=, =, <, >                  |
| Ad Group Ad     | allConversionsValueByConversionDate       | Double     | !=, =, <, >                  |
| Ad Group Ad     | conversionsByConversionDate               | Double     | !=, =, <, >                  |
| Ad Group Ad     | conversionsValueByConversionDate          | Double     | !=, =, <, >                  |
| Ad Group Ad     | valuePerAllConversionsByConversionDate    | Double     | !=, =, <, >                  |
| Ad Group Ad     | valuePerConversionsByConversionDate       | Double     | !=, =, <, >                  |
| Ad Group Ad     | activeViewMeasurableCostMicros            | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | averageCost                               | Double     | !=, =, <, >                  |
| Ad Group Ad     | costPerAllConversions                     | Double     | !=, =, <, >                  |
| Ad Group Ad     | costPerConversion                         | Double     | !=, =, <, >                  |
| Ad Group Ad     | clicks                                    | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | averagePageViews                          | Double     | !=, =, <, >                  |
| Ad Group Ad     | videoViews                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | allConversions                            | Double     | !=, =, <, >                  |
| Ad Group Ad     | averageCpc                                | Double     | !=, =, <, >                  |
| Ad Group Ad     | topImpressionPercentage                   | Double     | !=, =, <, >                  |
| Ad Group Ad     | impressions                               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Ad Group Ad     | absoluteTopImpressionPercentage           | Double     | !=, =, <, >                  |
| Ad Group Ad     | activeViewCtr                             | Double     | !=, =, <, >                  |
| Ad Group Ad     | ctr                                       | Double     | !=, =, <, >                  |
| Ad Group Ad     | conversionAction                          | String     | !=, =                        |
| Ad Group Ad     | conversionActionCategory                  | String     | !=, =                        |
| Ad Group Ad     | conversionActionName                      | String     | !=, =, LIKE                  |
| Ad Group Ad     | updateMask                                | String     |                              |
| Ad Group Ad     | create                                    | Struct     |                              |
| Ad Group Ad     | update                                    | Struct     |                              |
| Ad Group Ad     | policyValidationParameter                 | Struct     |                              |
| Ad Group Ad     | primaryStatus                             | String     | !=, =                        |
| Ad Group Ad     | primaryStatusReasons                      | List       |                              |
| Campaign        | resourceName                              | String     | !=, =                        |
| Campaign        | status                                    | String     | !=, =                        |
| Campaign        | baseCampaign                              | String     | !=, =                        |
| Campaign        | name                                      | String     | !=, =, LIKE                  |
| Campaign        | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | campaignBudget                            | String     | !=, =, LIKE                  |
| Campaign        | startDate                                 | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign        | endDate                                   | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign        | adServingOptimizationStatus               | String     | !=, =                        |
| Campaign        | advertisingChannelType                    | String     | !=, =                        |
| Campaign        | advertisingChannelSubType                 | String     | !=, =                        |
| Campaign        | experimentType                            | String     | !=, =                        |
| Campaign        | servingStatus                             | String     | !=, =                        |
| Campaign        | biddingStrategyType                       | String     | !=, =                        |
| Campaign        | domainName                                | String     | !=, =, LIKE                  |
| Campaign        | languageCode                              | String     | !=, =, LIKE                  |
| Campaign        | useSuppliedUrlsOnly                       | Boolean    | !=, =                        |
| Campaign        | positiveGeoTargetType                     | String     | !=, =                        |
| Campaign        | negativeGeoTargetType                     | String     | !=, =                        |
| Campaign        | paymentMode                               | String     | !=, =                        |
| Campaign        | optimizationGoalTypes                     | List       |                              |
| Campaign        | date                                      | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign        | averageCost                               | Double     |                              |
| Campaign        | clicks                                    | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | costMicros                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | impressions                               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | useAudienceGrouped                        | Boolean    | !=, =                        |
| Campaign        | activeViewMeasurableCostMicros            | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | costPerAllConversions                     | Double     | !=, =, <, >                  |
| Campaign        | costPerConversion                         | Double     | !=, =, <, >                  |
| Campaign        | invalidClicks                             | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | publisherPurchasedClicks                  | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | averagePageViews                          | Double     | !=, =, <, >                  |
| Campaign        | videoViews                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign        | allConversionsByConversionDate            | Double     | !=, =, <, >                  |
| Campaign        | allConversionsValueByConversionDate       | Double     | !=, =, <, >                  |
| Campaign        | conversionsByConversionDate               | Double     | !=, =, <, >                  |
| Campaign        | conversionsValueByConversionDate          | Double     | !=, =, <, >                  |
| Campaign        | valuePerAllConversionsByConversionDate    | Double     | !=, =, <, >                  |
| Campaign        | valuePerConversionsByConversionDate       | Double     | !=, =, <, >                  |
| Campaign        | allConversions                            | Double     | !=, =, <, >                  |
| Campaign        | absoluteTopImpressionPercentage           | Double     | !=, =, <, >                  |
| Campaign        | searchAbsoluteTopImpressionShare          | Double     | !=, =, <, >                  |
| Campaign        | averageCpc                                | Double     | !=, =, <, >                  |
| Campaign        | searchImpressionShare                     | Double     | !=, =, <, >                  |
| Campaign        | searchTopImpressionShare                  | Double     | !=, =, <, >                  |
| Campaign        | activeViewCtr                             | Double     | !=, =, <, >                  |
| Campaign        | ctr                                       | Double     | !=, =, <, >                  |
| Campaign        | relativeCtr                               | Double     | !=, =, <, >                  |
| Campaign        | updateMask                                | String     |                              |
| Campaign        | create                                    | Struct     |                              |
| Campaign        | update                                    | Struct     |                              |
| Campaign Budget | resourceName                              | String     | !=, =                        |
| Campaign Budget | id                                        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | status                                    | String     | !=, =                        |
| Campaign Budget | deliveryMethod                            | String     | !=, =                        |
| Campaign Budget | period                                    | String     | !=, =                        |
| Campaign Budget | type                                      | String     | !=, =                        |
| Campaign Budget | name                                      | String     | !=, =, LIKE                  |
| Campaign Budget | amountMicros                              | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | explicitlyShared                          | Boolean    | !=, =                        |
| Campaign Budget | referenceCount                            | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | hasRecommendedBudget                      | Boolean    | !=, =                        |
| Campaign Budget | date                                      | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign Budget | costMicros                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | startDate                                 | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign Budget | endDate                                   | Date       | BETWEEN, =, <, >, <=, >=     |
| Campaign Budget | maximizeConversionValueTargetRoas         | Double     | !=, =, <, >                  |
| Campaign Budget | maximizeConversionsTargetCpaMicros        | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | selectiveOptimizationConversionActions    | String     |                              |
| Campaign Budget | averageCost                               | Double     | !=, =, <, >                  |
| Campaign Budget | costPerAllConversions                     | Double     | !=, =, <, >                  |
| Campaign Budget | costPerConversion                         | Double     | !=, =, <, >                  |
| Campaign Budget | videoViews                                | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | clicks                                    | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | allConversions                            | Double     | !=, =, <, >                  |
| Campaign Budget | valuePerAllConversions                    | Double     | !=, =, <, >                  |
| Campaign Budget | averageCpc                                | Double     | !=, =, <, >                  |
| Campaign Budget | impressions                               | BigInteger | BETWEEN, =, !=, <, >, <=, >= |
| Campaign Budget | ctr                                       | Double     | !=, =, <, >                  |
| Campaign Budget | updateMask                                | String     |                              |
| Campaign Budget | create                                    | Struct     |                              |
| Campaign Budget | update                                    | Struct     |                              |

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

Entity-wise partitioning field support details are captured in the following table.

| Entity Name     | Partitioning Field | Data Type |
| --------------- | ------------------ | --------- |
| Ad Group Ad     | date               | Date      |
| Ad Group        | date               | Date      |
| Campaign        | date               | Date      |
| Campaign Budget | date               | Date      |

**Example**

```
googleads_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googleads",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "campaign-3467***",
        "API_VERSION": "v16",
        "PARTITION_FIELD": "date"
        "LOWER_BOUND": "2024-01-01"
        "UPPER_BOUND": "2024-06-05"
        "NUM_PARTITIONS": "10"
    }
)
```
