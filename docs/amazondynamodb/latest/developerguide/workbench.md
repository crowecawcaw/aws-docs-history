

# NoSQL Workbench for DynamoDB
<a name="workbench"></a>

 NoSQL Workbench for Amazon DynamoDB is a cross-platform, client-side GUI application that you can use for modern database development and operations. It's available for Windows, macOS, and Linux. NoSQL Workbench lets you design DynamoDB data models, define access patterns as real DynamoDB operations, and validate them using sample data. Additionally you can organize your data models into projects. NoSQL Workbench includes DynamoDB local, which makes it possible to test your tables and indexes before committing your data model to the cloud. To learn more about DynamoDB local and its requirements, see [Setting up DynamoDB local (downloadable version)](DynamoDBLocal.md).

**Data modeler**  
 With NoSQL Workbench for DynamoDB, you can start a new project from scratch or use a sample project that matches your use case. Then, you design tables and Global Secondary Indexes, define attributes, and configure sample data. You can also visualize your access patterns as real DynamoDB operations (PutItem, UpdateItem, Query, and others) and run these operations against the configured sample data to validate that the access pattern works as intended, making adjustments to the data model based on validation results. Finally, after validation, you commit the model to either DynamoDB local or your AWS account for further testing and production use. For collaboration, you can import and export designed data models. For more information, see [Building data models with NoSQL Workbench](workbench.Modeler.md).

**Operation builder**  
NoSQL Workbench provides a rich graphical user interface for you to develop and test queries. You can use the *operation builder* to view, explore, and query live datasets. The structured operation builder supports projection expression, condition expression, and generates sample code in multiple languages. You can directly clone tables from one Amazon DynamoDB account to another one in different Regions. You can also directly clone tables between DynamoDB local and an Amazon DynamoDB account for faster copying of your table’s key schema (and optionally GSI schema and items) between your development environments. For more information, see [Exploring datasets and building operations with NoSQL Workbench](workbench.querybuilder.md).

The video below details concepts of data modeling with NoSQL Workbench.

[![AWS Videos](http://img.youtube.com/vi/p5va6ZX9_o0?si=vqQuf6FjoBuK1phR/0.jpg)](http://www.youtube.com/watch?v=p5va6ZX9_o0?si=vqQuf6FjoBuK1phR)


**Topics**
+ [Download NoSQL Workbench for DynamoDB](workbench.settingup.md)
+ [Building data models with NoSQL Workbench](workbench.Modeler.md)
+ [Exploring datasets and building operations with NoSQL Workbench](workbench.querybuilder.md)
+ [Sample data models for NoSQL Workbench](workbench.SampleModels.md)
+ [Release history for NoSQL Workbench](WorkbenchDocumentHistory.md)