

# Creating a new data model
<a name="workbench.Modeler.CreateNew"></a>

Follow these steps to create a new data model in Amazon DynamoDB using NoSQL Workbench.

**To create a new data model**

1.  Open NoSQL Workbench, and on the main screen, choose **Create model manually**. 

    A new page opens with an empty configuration for your first table. NoSQL Workbench creates all new data models with a default name (for example, untitled-2) and adds them to the **Drafts** project folder. 

1.  On **Table configuration screen**, specify the following: 
   +  **Table name** — Enter a unique name for the table. 
   +  **Partition key** — Enter a partition key name, and specify its type. Optionally, you can also select a more granular data type format for sample data generation. 
   +  If you want to add a **Sort key**, specify the sort key name and its type. Optionally, you can select a more granular data type format for sample data generation. 
**Note**  
 To learn more about primary key design, designing and using partition keys effectively, and using sort keys, see the following:   
 [Primary key](HowItWorks.CoreComponents.md#HowItWorks.CoreComponents.PrimaryKey) 
 [Best practices for designing and using partition keys effectively in DynamoDB](bp-partition-key-design.md) 
 [Best practices for using sort keys to organize data in DynamoDB](bp-sort-keys.md) 

1. You can add other attributes to more clearly validate your model and access patterns. To add other attributes:
   +  Choose **Add an attribute**. 
   +  Specify the attribute name and its type. 
   +  Optionally, you can select a more granular data type format for sample data generation. 

1.  If you want to add a global secondary index, choose **Add global secondary index**. Specify the **Global secondary index name**, **Partition key** attribute, and **Projection type**. 

   For more information about working with global secondary indexes in DynamoDB, see [Global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html).

1.  Optionally, **Add a facet**. A facet is a virtual construct in NoSQL Workbench. It is not a functional construct in DynamoDB. Facets in NoSQL Workbench help you visualize an application's different data access patterns for DynamoDB with only a subset of the data in a table. 
**Note**  
 We recommend you use [Adding and validating access patterns](workbench.Modeler.AccessPatterns.md) to visualize how your application will access data in DynamoDB instead of Facets. Access patterns mirror your actual database interactions and help you build the correct data model for your use case, although facets are non-functional visualizations. 

    Choose **Add facet**. Specify the following: 
   +  The **Facet name**. 
   +  A **Partition key alias** to help distinguish this facet view. 
   +  A **Sort key alias** if you provided a **Sort key** for the table. 
   +  Choose the **Attributes** that are part of this facet. 

    Repeat this step if you want to add more facets. 

1.  Finally, choose **Save** to create the table. 

1.  If you need other **Tables** or **Global Secondary Indexes**, choose the **\+** icon above the table you just created. 