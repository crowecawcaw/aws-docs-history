

# Defining relationships between datasets in a Topic
<a name="topics-relationships"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  Amazon Quick administrators and authors  | 

Relationships tell Quick Sight how to join datasets when a question or visual spans multiple tables. You define relationships by specifying join keys between dataset pairs using a JSON configuration file.

The relationship graph must be a directed acyclic graph (DAG) — circular relationships are not supported. We recommend modeling your datasets in a star schema with one or more central fact tables joined to shared dimension tables.

**To define relationships between datasets**

1. Open the Topic that you want to configure.

1. Navigate to the **Relationships** tab.  
![Topic editor showing the Relationships tab with six datasets listed: PRODUCT_DIM, CUSTOMER_DIM, DATE_DIM, SALES_FACT, RETURN_FACT, and STORE_DIM.](http://docs.aws.amazon.com/quick/latest/userguide/images/topic-relationships-tab.png)

1. Choose **Upload file** or **Create manually**.  
![Relationships tab showing Upload file and Create manually buttons, with supported file types YAML and JSON noted.](http://docs.aws.amazon.com/quick/latest/userguide/images/topic-relationships-upload.png)

1. Upload a JSON file defining your relationships (see the following example). After uploading, the relationship graph displays visually at left and the join key details appear at right. Select a join to verify the relationship mapping.  
![Relationship graph showing SALES_FACT and RETURN_FACT as central fact tables connected to PRODUCT_DIM, CUSTOMER_DIM, DATE_DIM, and STORE_DIM with join keys displayed on the right panel.](http://docs.aws.amazon.com/quick/latest/userguide/images/topic-relationships-graph.png)

1. To edit a relationship, choose **Edit**, update the join columns using the dropdown selectors, and choose **Save**.  
![Relationships edit mode showing editable join column dropdowns for each dataset pair, with Cancel and Save buttons at upper right.](http://docs.aws.amazon.com/quick/latest/userguide/images/topic-relationships-edit.png)

## Relationship JSON format
<a name="topics-relationships-json"></a>

The following example shows a star schema configuration with a central SALES\_FACT table joined to dimension tables:

```
{
  "datasetPairs": [
    {
      "datasetLeft": { "datasetName": "SALES_FACT", "joinColumnNames": ["CUSTOMER_ID"] },
      "datasetRight": { "datasetName": "CUSTOMER_DIM", "joinColumnNames": ["CUSTOMER_ID"] }
    },
    {
      "datasetLeft": { "datasetName": "SALES_FACT", "joinColumnNames": ["PRODUCT_ID"] },
      "datasetRight": { "datasetName": "PRODUCT_DIM", "joinColumnNames": ["PRODUCT_ID"] }
    },
    {
      "datasetLeft": { "datasetName": "SALES_FACT", "joinColumnNames": ["STORE_ID"] },
      "datasetRight": { "datasetName": "STORE_DIM", "joinColumnNames": ["STORE_ID"] }
    }
  ]
}
```

Each entry in `datasetPairs` specifies a pair of datasets and the columns used to join them. Composite keys are supported by including multiple column names in the `joinColumnNames` array.

## Best practices for relationships
<a name="topics-relationships-best-practices"></a>
+ **Start with a star schema.** A central fact table surrounded by dimension tables minimizes join complexity and maximizes query performance.
+ **Use clean join keys.** Use integer surrogate keys where possible. Confirm matching data types on both sides. Remove null values from join key columns (nulls never match in inner joins).
+ **Validate referential integrity.** Every foreign key in the fact table should exist in the dimension table.
+ **Avoid circular joins.** The relationship graph must be acyclic. If your model creates a cycle, break it by removing one leg and denormalizing the redundant path.
+ **Pre-join snowflake chains when feasible.** If a dimension has sub-dimensions (for example, Customer → Geography → Region), consider flattening them into a single dimension dataset to reduce join hops.

## Current limitations
<a name="topics-relationships-limitations"></a>

The following limitations apply to defined relationships:
+ Relationships use *inner join* semantics for analysis sheets. Only rows with matching keys in both datasets appear in results.
+ The relationship graph must be acyclic (no circular joins).
+ Self-relationships (a dataset related to itself) are not supported.
+ All datasets in a Topic must use the same query mode (SPICE or Direct Query).
+ A Topic cannot exceed 12 datasets.

**Note**  
When using Topics in Amazon Quick chat, the LLM-powered chat agent is not limited to inner joins. It can generate SQL with left joins, outer joins, unions, and subqueries based on your custom instructions. These join-type limitations apply only to the analysis sheet consumption path.