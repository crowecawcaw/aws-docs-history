# Writing to Salesforce Marketing Cloud entities

**Prerequisites**

- A Salesforce Marketing object you wish to write to. You will need to specify the object’s name such as `List` or `Campaigns` or any of the other entities outlined in the table below.
- The Salesforce Marketing Cloud connector supports three write operations:

      + INSERT
      + UPSERT
      + UPDATEWhen using the `UPDATE` and `UPSERT` write operations, you must provide the `ID_FIELD_NAMES` option to specify the external ID field for the records.

  **Supported entities for destination**:

| Entity                          | Priority | Interface (REST, SOAP, etc) | Can be Inserted     | Can be Updated      | Can be Upserted |
| ------------------------------- | -------- | --------------------------- | ------------------- | ------------------- | --------------- |
| Campaigns                       | P0       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Content Assets                  | P0       | REST                        | Y<br>• Single, Bulk | Y<br>• Single       | N               |
| Contact                         | P1       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Domain Verification             | P1       | REST                        | Y<br>• Single       | Y<br>• Single, Bulk | N               |
| Event Notification Callback     | P1       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Event Notification Subscription | P1       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Messaging                       | P1       | REST                        | Y<br>• Single       | N                   | N               |
| Object Nested Tag               | P2       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Seed-List                       | P1       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Setup                           | P1       | REST                        | Y<br>• Single       | Y<br>• Single       | N               |
| Data Extension                  | P0       | SOAP                        | Y<br>• Single       | Y<br>• Single       | Y<br>• Single   |
| Email                           | P0       | SOAP                        | Y<br>• Single       | Y<br>• Single       | N               |
| List                            | P0       | SOAP                        | Y<br>• Single       | Y<br>• Single       | N               |
| Send                            | P0       | SOAP                        | Y<br>• Single       | N                   | N               |
| Subscriber                      | P0       | SOAP                        | Y<br>• Single       | Y<br>• Single       | N               |

**Example for INSERT operation for REST**:

```
salesforcemarketingcloud_write = glueContext.write_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Campaigns",
        "API_VERSION": "v1",
        "writeOperation" : "INSERT",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```

**Example for INSERT operation for SOAP**:

```
salesforcemarketingcloud_write = glueContext.write_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "List",
        "API_VERSION": "v1",
        "writeOperation" : "INSERT",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```

**Example for UPDATE operation for REST**:

```
salesforcemarketingcloud_write = glueContext.write_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Campaigns",
        "API_VERSION": "v1",
        "writeOperation" : "UPDATE",
         "ID_FIELD_NAMES": "id",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```

**Example for UPDATE operation for SOAP**:

```
salesforcemarketingcloud_write = glueContext.write_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "List",
        "API_VERSION": "v1",
        "writeOperation" : "UPDATE",
         "ID_FIELD_NAMES": "id",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```

**Example for UPSERT operation for SOAP**:

```
salesforcemarketingcloud_write = glueContext.write_dynamic_frame.from_options(
    connection_type="salesforcemarketingcloud",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "DataExtension/Insert-***E/6*******3",
        "API_VERSION": "v1",
        "writeOperation" : "UPSERT",
        "INSTANCE_URL": "https://**********************.rest.marketingcloudapis.com"
    }
)
```
