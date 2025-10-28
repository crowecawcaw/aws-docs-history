# Data mapping example for fulfillment

Below is an example to map brick and mortar or online sales to outbound order line dataset and optimize the historical demand setup. Use this example to structure your data for accurate forecasting.
Review the configurations in this example to make sure your forecasting models capture the different fulfillment scenarios.

###### Note

If the data fields _ship_from_site_id_, _ship_to_site_id_, and _channel_id_ are selected for forecast granularity, make sure they have
values or enter _NULL_ as the value. The forecast will fail if the fields are blank.

| Data field        | Description                        | Scenario 1 – Store sales (POS)         | Scenario 2 – E-commerce demand fulfilled by store | Scenario 3 – E-commerce demand fulfilled by online fulfillment center (direct to customer) |
| ----------------- | ---------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ship_from_site_id | Site at which inventory is managed | Store ID                               | Store ID                                          | Fulfillment Center ID                                                                      |
| ship_to_site_id   | Site that received the order       | Enter _NULL_ to avoid forecast failure | Country, Region, State, or Zip – as applicable    | External retailer sore ID, or Country, Region, State, or Zip – as applicable               |
| channel_id        | Map how an item is sold            | Brick and mortar                       | E-commerce                                        | E-commerce                                                                                 |
