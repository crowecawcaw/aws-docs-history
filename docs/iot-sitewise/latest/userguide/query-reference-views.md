# Query reference views

This section provides information to help you understand the views in AWS IoT SiteWise, such as
process metadata and telemetry data.

The following tables provide the view names and descriptions of the views:

| Data model               | **View name**                                                                                                                                  | **View description**                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------- | ------------ |
| asset                    | Contains information about the asset and model derivation.                                                                                     |
| asset_property           | Contains information about the asset property's structure.                                                                                     |
| raw_time_series          | Contains the historical data of the time series.                                                                                               |
| latest_value_time_series | Contains the latest value of the time series.                                                                                                  |
| precomputed_aggregates   | Contains the automatically computed aggregated asset property values. They are a set of basic metrics calculated over multiple time intervals. | The following views list the column names and data types of each view. View:asset | **column name** | **datatype** |
| ---                      | ---                                                                                                                                            |
| asset_id                 | string                                                                                                                                         |
| asset_name               | string                                                                                                                                         |
| asset_description        | string                                                                                                                                         |
| asset_model_id           | string                                                                                                                                         |
| parent_asset_id          | string                                                                                                                                         |
| asset_external_id        | string                                                                                                                                         |
| asset_model_external_id  | string                                                                                                                                         |
| hierarchy_id             | string                                                                                                                                         | View:asset_property                                                               | **column name** | **datatype** |
| ---                      | ---                                                                                                                                            |
| asset_id                 | string                                                                                                                                         |
| property_id              | string                                                                                                                                         |
| property_name            | string                                                                                                                                         |
| property_alias           | string                                                                                                                                         |
| property_external_id     | string                                                                                                                                         |
| asset_composite_model_id | string                                                                                                                                         |
| property_type            | string                                                                                                                                         |
| property_data_type       | string                                                                                                                                         |
| int_attribute_value      | integer                                                                                                                                        |
| double_attribute_value   | double                                                                                                                                         |
| boolean_attribute_value  | boolean                                                                                                                                        |
| string_attribute_value   | string                                                                                                                                         | View:raw_time_series                                                              | **column name** | **datatype** |
| ---                      | ---                                                                                                                                            |
| asset_id                 | string                                                                                                                                         |
| property_id              | string                                                                                                                                         |
| property_alias           | string                                                                                                                                         |
| event_timestamp          | timestamp                                                                                                                                      |
| quality                  | string                                                                                                                                         |
| boolean_value            | boolean                                                                                                                                        |
| int_value                | integer                                                                                                                                        |
| double_value             | double                                                                                                                                         |
| string_value             | string                                                                                                                                         | View:latest_value_time_series                                                     | **column name** | **datatype** |
| ---                      | ---                                                                                                                                            |
| asset_id                 | string                                                                                                                                         |
| property_id              | string                                                                                                                                         |
| property_alias           | string                                                                                                                                         |
| event_timestamp          | timestamp                                                                                                                                      |
| quality                  | string                                                                                                                                         |
| boolean_value            | boolean                                                                                                                                        |
| int_value                | integer                                                                                                                                        |
| double_value             | double                                                                                                                                         |
| string_value             | string                                                                                                                                         | View:precomputed_aggregates                                                       | **column name** | **datatype** |
| ---                      | ---                                                                                                                                            |
| asset_id                 | string                                                                                                                                         |
| property_id              | string                                                                                                                                         |
| property_alias           | string                                                                                                                                         |
| event_timestamp          | timestamp                                                                                                                                      |
| quality                  | string                                                                                                                                         |
| resolution               | string                                                                                                                                         |
| sum_value                | double                                                                                                                                         |
| count_value              | integer                                                                                                                                        |
| average_value            | double                                                                                                                                         |
| maximum_value            | double                                                                                                                                         |
| minimum_value            | double                                                                                                                                         |
| stdev_value              | double                                                                                                                                         |
