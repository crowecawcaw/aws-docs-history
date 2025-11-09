# supplementary_time_series

###### Note

If you cannot locate the supplementary_time_series data entity, your instance might be using an older data model version. You can contact AWS Support to upgrade your data model version or create a new data connection.

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                               | Column |
| ---------------------------------- | ------ |
| forecast_supplementary_time_series | id     |

The table below lists the column names supported by the data entity:

| Column                     | Data type | Required | Description                                                                                                                                                                                                               |
| -------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                         | string    | Yes      | Unique identifier with each supplementary data entry.                                                                                                                                                                     |
| product_id 2               | string    | No       | Unique identifier for a specific product. Corresponds to product_id in the outbound_order_line dataset.                                                                                                                   |
| product_group_id           | string    | No       | Product hierarchy or grouping.                                                                                                                                                                                            |
| order_date                 | timestamp | Yes1     | The timestamp indicating the date and time when the date for the respective time-series was recorded.                                                                                                                     |
| channel_id                 | string    | No       | Unique identifier for a specific product. Corresponds to product_id in the outbound_order_line dataset.                                                                                                                   |
| customer_tpartner_id 2     | string    | No       | Unique identifier for a specific user. Corresponds to customer_tpartner_id field in outbound_order_line dataset.                                                                                                          |
| site_id 2                  | string    | No       | Unique identifier for a specific site or location.                                                                                                                                                                        |
| ship_to_site_id 2          | string    | No       | Unique identifier for a specific site or location. This corresponds to the *ship_to_site_id<br>• in the *outbound_order_line<br>• dataset.                                                                                |
| ship_to_site_address_zip   | string    | No       | Postal code of _ship_to_site_id_.                                                                                                                                                                                         |
| geo_id 2                   | string    | No       | Geographical hierarchy ID.                                                                                                                                                                                                |
| ship_from_site_id 2        | string    | No       | Corresponds to the *ship_from_site_id<br>• in the *outbound_order_line<br>• dataset.                                                                                                                                      |
| ship_from_site_address_zip | string    | No       | Postal code of _ship_from_site_id_.                                                                                                                                                                                       |
| time_series_name           | string    | Yes      | The \*time_series_name<br>• must start with a letter, should be 2 to 56 characters long, and can contain letters, numbers, and underscores. No other special characters are allowed.                                      |
| time_series_value          | string    | Yes      | Value corresponding to the specific time series. This could represent quantities, metric, or string that is relevant to the type of the data. Demand planning only supports numerical value as additional forecast input. |
| source_event_id            | string    | No       | ID of the event created in the source system.                                                                                                                                                                             |
| source_update_dttm         | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                                                                                                                               |

1You must enter a value. When you ingest data from SAP
or EDI, the default value for _string_ is SCN_RESERVED_NO_VALUE_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column               | Category            | FK/Data entity      | FK/Column         |
| -------------------- | ------------------- | ------------------- | ----------------- |
| product_id           | Product             | product             | id                |
| site_id              | Network             | site                | id                |
| customer_tpartner_id | Organization        | trading_partner     | id                |
| ship_to_site_id      | Outbound fulfilment | outbound_order_line | ship_to_site_id   |
| geo_id               | Organization        | geography           | id                |
| ship_from_site_id    | Outbound fulfilment | outbound_order_line | ship_from_site_id |
