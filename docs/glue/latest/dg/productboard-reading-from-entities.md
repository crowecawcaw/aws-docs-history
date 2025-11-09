# Reading from Productboard

entities

**Prerequisites**

An Productboard Object you would like to read from. Refer the supported entities table
below to check the available entities.

**Supported entities**

- [Abuse-reports](https://productboard.com/developer/marketing/api/campaign-abuse/ "https://productboard.com/developer/marketing/api/campaign-abuse/")
- [Automation](https://productboard.com/developer/marketing/api/automation/list-automations/ "https://productboard.com/developer/marketing/api/automation/list-automations/")
- [Campaigns](https://productboard.com/developer/marketing/api/campaigns/list-campaigns/ "https://productboard.com/developer/marketing/api/campaigns/list-campaigns/")
- [Click-details](https://productboard.com/developer/marketing/api/link-clickers/ "https://productboard.com/developer/marketing/api/link-clickers/")
- [Lists](https://productboard.com/developer/marketing/api/link-clickers/ "https://productboard.com/developer/marketing/api/link-clickers/")
- [Members](https://productboard.com/developer/marketing/api/list-segment-members/ "https://productboard.com/developer/marketing/api/list-segment-members/")
- [Open-details](https://productboard.com/developer/marketing/api/list-members/ "https://productboard.com/developer/marketing/api/list-members/")
- [Segments](https://productboard.com/developer/marketing/api/list-segments/ "https://productboard.com/developer/marketing/api/list-segments/")
- [Stores](https://productboard.com/developer/marketing/api/ecommerce-stores/list-stores/ "https://productboard.com/developer/marketing/api/ecommerce-stores/list-stores/")
- [Unsubscribed](https://productboard.com/developer/marketing/api/unsub-reports/ "https://productboard.com/developer/marketing/api/unsub-reports/")

| Entity                   | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------------------ | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Features                 | Yes             | Yes            | No                | Yes                | Yes                   |
| Components               | No              | Yes            | No                | Yes                | No                    |
| Products                 | No              | Yes            | No                | Yes                | No                    |
| Feature Statuses         | No              | Yes            | No                | Yes                | Yes                   |
| Custom Field Definitions | No              | Yes            | No                | Yes                | No                    |
| Custom Field Values      | Yes             | Yes            | No                | Yes                | No                    |

**Example**

```
Productboard_read = glueContext.create_dynamic_frame.from_options(
    connection_type="Productboard",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "feature",
        "API_VERSION": "1"
    }
```

**Productboard entity and field details**

- [Features](https://developer.productboard.com/#tag/features "https://developer.productboard.com/#tag/features")
- [Components](https://developer.productboard.com/#tag/components "https://developer.productboard.com/#tag/components")
- [Feature
  statuses](https://developer.productboard.com/#tag/statuses "https://developer.productboard.com/#tag/statuses")
- [Products](https://developer.productboard.com/#tag/products "https://developer.productboard.com/#tag/products")
- [Custom fields definitions](https://developer.productboard.com/#tag/hierarchyEntitiesCustomFields "https://developer.productboard.com/#tag/hierarchyEntitiesCustomFields")
- [Custom fields values](https://developer.productboard.com/#tag/hierarchyEntitiesCustomFieldsValues "https://developer.productboard.com/#tag/hierarchyEntitiesCustomFieldsValues")
