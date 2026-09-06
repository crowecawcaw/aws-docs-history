

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Box data source connector field mappings
<a name="box-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q Box connector supports the following entities and the associated reserved and custom attributes.

**Topics**
+ [Files and folders](#box-field-mappings-files-folders)
+ [Comments](#box-field-mappings-comments)
+ [Tasks](#box-field-mappings-tasks)
+ [Web links](#box-field-mappings-web-links)

## Files and folders
<a name="box-field-mappings-files-folders"></a>


| Box field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| bx\_createdAt | \_created\_at | Default | Date | 
| bx\_modifiedAt | \_last\_updated\_at | Default | Date | 
| bx\_authors | \_authors | Default | String list | 
| bx\_uri | \_source\_uri | Default | String | 
| bx\_size | bx\_file\_size | Custom | String | 
| bx\_category | \_category | Default | String | 

## Comments
<a name="box-field-mappings-comments"></a>


| Box field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| bx\_createdAt | \_created\_at | Default | Date | 
| bx\_modifiedAt | \_last\_updated\_at | Default | Date | 
| bx\_author | \_authors | Custom | String | 
| bx\_parentFile | bx\_comment\_item | Custom | String | 
| bx\_category | \_category | Default | String | 

## Tasks
<a name="box-field-mappings-tasks"></a>


| Box field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| bx\_createdAt | \_created\_at | Default | Date | 
| bx\_action | bx\_task\_action | Custom | String | 
| bx\_taskComplete | bx\_task\_completed | Custom | String | 
| bx\_taskItem | bx\_task\_item | Custom | String | 
| bx\_taskAssigned | bx\_task\_assigned\_to | Custom | String | 
| bx\_author | bx\_author | Custom | String | 
| bx\_category | \_category | Default | String | 
| bx\_uri | \_source\_uri | Default | String | 

## Web links
<a name="box-field-mappings-web-links"></a>


| Box field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| bx\_createdAt | \_created\_at | Default | Date | 
| bx\_author | bx\_author | Custom | String | 
| bx\_category | \_category | Default | String | 
| bx\_uri | \_source\_uri | Default | String | 