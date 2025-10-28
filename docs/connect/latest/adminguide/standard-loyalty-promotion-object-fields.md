# Customer Profiles

standard loyalty promotion object fields

The following table lists all the fields in the Customer Profiles standard
loyalty promotion object.

| Loyalty Promotion     | Standard loyaltyPromotion field | Type                                                                  | Description            |
| --------------------- | ------------------------------- | --------------------------------------------------------------------- | ---------------------- | ------------------------------- | -------------------------------- | ------------------------------- | ---- | ----------- |
| PromotionId           | String                          | Unique identifier of the standard loyalty promotion.                  |
| PromotionName         | String                          | Display name of the promotion.                                        |
| PromotionType         | String                          | The type or category of promotion (e.g., bonus, tier boost, voucher). |
| ProgramType           | String                          | Indicates the type of loyalty program the promotion is tied to.       |
| ProgramRef            | String                          | Reference ID to the related loyalty program.                          |
| PartnerId             | String                          | Reference ID of a partner organization involved in the promotion.     |
| PartnerNumber         | String                          | An identifier or number related to the partner.                       |
| Tier                  | String                          | Tier level targeted or impacted by the promotion.                     |
| StartDate             | String                          | When the promotion becomes active.                                    |
| EnrolledDate          | String                          | Date the user enrolled in the promotion.                              |
| EndDate               | String                          | When the promotion ends.                                              |
| Amount                | String                          | Associated monetary or point value with the promotion.                |
| Period                | String                          | Time period of the promotion (e.g., weekly, monthly, campaign-based). |
| Status                | String                          | Current status of the promotion (e.g., active, expired, completed).   |
| CreatedDate           | String                          | Date the promotion record was created.                                |
| CreatedBy             | String                          | User or system that created the promotion record.                     |
| UpdatedDate           | String                          | Last date the promotion record was updated.                           |
| UpdatedBy             | String                          | User or system that last updated the promotion.                       |
| CampaignRef           | String                          | External reference to a broader campaign this promotion belongs to.   |
| AdditionalInformation | String                          | Miscellaneous notes or marketing copy about the promotion.            |
| TriggerLimit          | TriggerLimit                    | Trigger limit details                                                 |
| Usage                 | Usage                           | Usage details                                                         |
| Rules                 | Rules                           | Promotion rule details                                                |
| Incentive             | Incentive                       | Promotion incentive details                                           |
| Attributes            | Map<String, String>             | Additional metadata or program-specific values.                       | Standard Index Fields  | Standard index name             | Standard preference record field |
| ---                   | ---                             |                                                                       | \_loyaltyPromotionId   | PromotionId                     | Rules data type                  | Standard loyaltyPromotion field | Type | Description |
| ---                   | ---                             | ---                                                                   |
| Name                  | String                          | Rule name within the promotion rules.                                 |
| Description           | String                          | Rule description within the promotion rules.                          | Incentive data type    | Standard loyaltyPromotion field | Type                             | Description                     |
| ---                   | ---                             | ---                                                                   |
| Type                  | String                          | The type of incentive (e.g., bonusPoints, voucher, tierUpgrade).      |
| Value                 | String                          | Value of the incentive, such as point amount or voucher value.        |
| Unit                  | String                          | The unit for the incentive value (e.g., points, %, USD).              | TriggerLimit data type | Standard loyaltyPromotion field | Type                             | Description                     |
| ---                   | ---                             | ---                                                                   |
| Times                 | String                          | Number of times a promotion can be triggered.                         |
| Interval              | String                          | Interval for trigger limit.                                           | Usage data type        | Standard loyaltyPromotion field | Type                             | Description                     |
| ---                   | ---                             | ---                                                                   |
| UsageProgressPercent  | String                          | Progress percentage of the promotion usage.                           |
| UsageCompleted        | String                          | Number of completed usages.                                           |
| UsageTarget           | String                          | Target number of usages.                                              |
