# Reading from Mixpanel entities

**Prerequisites**

You must have a Mixpanel object, such as `Funnels`, `Retention`,
or `Retention Funnels`, from which you would like to read data. Additionally,
you will need to know the object name.

**Supported entities**

| Entity                   | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------------------ | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Funnels                  | Yes             | No             | No                | Yes                | No                    |
| Retention                | Yes             | No             | No                | Yes                | No                    |
| Segmentation             | Yes             | No             | No                | Yes                | No                    |
| Segmentation Sum         | Yes             | No             | No                | Yes                | No                    |
| Segmentation Average     | Yes             | No             | No                | Yes                | No                    |
| Cohorts                  | Yes             | No             | No                | Yes                | No                    |
| Engage                   | No              | Yes            | No                | Yes                | No                    |
| Events                   | Yes             | No             | No                | Yes                | No                    |
| Events Top               | Yes             | No             | No                | Yes                | No                    |
| Events Names             | Yes             | No             | No                | Yes                | No                    |
| Events Properties        | Yes             | No             | No                | Yes                | No                    |
| Events Properties Top    | Yes             | No             | No                | Yes                | No                    |
| Events Properties Values | Yes             | No             | No                | Yes                | No                    |
| Annotations              | Yes             | No             | No                | Yes                | No                    |
| Profile Event Activity   | Yes             | No             | No                | Yes                | No                    |

**Example**

```
mixpanel_read = glueContext.create_dynamic_frame.from_options(
    connection_type="mixpanel",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "/cohorts/list?project_id=2603353",
        "API_VERSION": "2.0",
        "INSTANCE_URL": "https://www.mixpanel.com/api/app/me"
    }

```

**Mixpanel entity and field details**

| Entity                 | Field         | Data Type | **Supported Operators** |
| ---------------------- | ------------- | --------- | ----------------------- |
| Funnel                 | funnel\_id    | Integer   | '='                     |
| workspace\_id          | Integer       | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '=’       |
| length                 | Integer       | '='       |
| length\_unit           | String        | '='       |
| interval               | Integer       | '='       |
| unit                   | String        | '='       |
| limit                  | Integer       | '='       |
| data                   | Struct        |           |
| meta                   | Struct        |           |
| Retention              | workspace\_id | Integer   | '='                     |
| unit                   | String        | '='       |
| addiction\_unit        | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| event                  | String        | '='       |
| limit                  | Integer       | '='       |
| data                   | Struct        |           |
| Segmentation           | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| unit                   | String        | '='       |
| interval               | Integer       | '='       |
| limit                  | Integer       | '='       |
| type                   | String        | '='       |
| series                 | List          |           |
| values                 | Struct        |           |
| data                   | Struct        |           |
| Segmentation Numeric   | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| on                     | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| unit                   | String        | '='       |
| type                   | String        | '='       |
| series                 | List          |           |
| values                 | Struct        |           |
| Segmentation Sum       | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| on                     | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| unit                   | String        | '='       |
| metadata               | Struct        |           |
| results                | Struct        |           |
| Segmentation Average   | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| on                     | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| unit                   | String        | '='       |
| metadata               | Struct        |           |
| results                | Struct        |           |
| Cohorts                | count         | Integer   |                         |
| is\_visible            | Integer       |           |
| description            | String        |           |
| created                | DateTime      |           |
| project\_id            | Integer       |           |
| id                     | BigInteger    |           |
| name                   | String        |           |
| data\_group\_id        | String        |           |
| Engage                 | distinct\_id  | String    |                         |
|                        | properties    | Struct    |
| Event                  | workspace     | Integer   | '='                     |
| event                  | String        | '='       |
| type                   | String        | '='       |
| unit                   | String        | '='       |
| interval               | Integer       | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| series                 | List          |           |
| values                 | Struct        |           |
| Events Top             | type          | String    | '='                     |
| workspace\_id          | Integer       | '='       |
| limit                  | Integer       | '='       |
| amount                 | Integer       |           |
| event                  | String        |           |
| percent\_change        | Float         |           |
| Event Name             | data          | List      |                         |
| workspace\_id          | Integer       | '='       |
| type                   | String        | '='       |
| limit                  | Integer       | '='       |
| Event Properties       | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| name                   | String        | '='       |
| type                   | String        | '='       |
| unit                   | String        | '='       |
| interval               | Integer       | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| limit                  | Integer       | '='       |
| data                   | Struct        |           |
| series                 | List          |           |
| values                 | Struct        |           |
| Event Properties Top   | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| limit                  | Integer       | '='       |
| data                   | Struct        |           |
| Event Properties Value | workspace\_id | Integer   | '='                     |
| event                  | String        | '='       |
| limit                  | Integer       | '='       |
| name                   | String        | '='       |
| data                   | List          |           |
| Annotation             | workspace\_id | Integer   |                         |
| date                   | DateTime      |           |
| project\_id            | Integer       |           |
| id                     | BigInteger    |           |
| description            | String        |           |
| from\_date             | Date          | BETWEEN   |
| Profile Event Activity | workspace\_id | Integer   | '='                     |
| distinct\_ids          | String        | '='       |
| from\_date             | Date          | '='       |
| to\_date               | Date          | '='       |
| event                  | String        |           |
| properties             | Struct        |           |
