

# Reading from Maxio entities

**Prerequisites**

A Maxio object you want to read from. See the supported entities table below for the available entities.

**Supported entities for source**


| Entity | Can be filtered | Supports limit | Supports select \* | Supports order by | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| customer | Yes | No | Yes | No | Yes | 
| invoice | Yes | No | Yes | No | Yes | 
| subscription | Yes | No | Yes | No | No | 
| product | Yes | No | Yes | No | Yes | 
| coupon | No | No | Yes | No | No | 
| component | Yes | No | Yes | No | Yes | 
| component-price-point | No | No | Yes | No | No | 
| event | No | No | Yes | No | No | 
| product-family | Yes | No | Yes | No | Yes | 
| product-price-point | No | No | Yes | No | No | 
| subscription-component | No | No | Yes | No | No | 
| invoice-event | No | No | Yes | No | No | 
| subscription-component-usage | Yes | No | Yes | No | Yes | 
| allocation | No | No | Yes | No | No | 
| credit-note | Yes | No | Yes | No | Yes | 
| payment-profile | No | No | Yes | No | No | 
| subscription-group | No | No | Yes | No | No | 
| offer | No | No | Yes | No | No | 

**Example – Reading from a Maxio entity**  
The following example reads from the `customer` entity. Replace {{connectionName}} with the name of your Maxio connection:

```
read_df = glueContext.create_dynamic_frame.from_options(
    connection_type="maxio",
    connection_options={
        "connectionName": "{{connectionName}}",
        "ENTITY_NAME": "customer"
    }
)
```

**Partitioning queries**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` to read in parallel. The query is split into `NUM_PARTITIONS` sub-queries that Spark runs concurrently. The following entities and fields support partitioning:


| Entity | Partitioning field | 
| --- | --- | 
| customer | created\_at | 
| invoice | created\_at | 
| product | created\_at | 
| component | created\_at | 
| product-family | created\_at | 
| subscription-component-usage | created\_at | 
| credit-note | issue\_date | 