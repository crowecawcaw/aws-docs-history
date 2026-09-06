

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Microsoft OneDrive data source connector field mappings
<a name="onedrive-legacy-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved fields** – Mapped to reserved fields in the Amazon Q index that filter chat responses for your end users.
+ **Custom fields** – Mapped to custom fields in the Amazon Q index. You can create custom fields when you create your application or data source. You can use custom fields to provide additional information to help your end users.

For more information, see [Mapping data source fields](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/field-mappings.html).

The following table lists the Microsoft OneDrive data source connector entities and their associated attributes that you can map to Amazon Q index fields.



| Entity | Attributes | Field type | 
| --- | --- | --- | 
| File |  +  createdBy <br />+  createdDateTime <br />+  lastModifiedBy <br />+  lastModifiedDateTime <br />+  name <br />+  parentReference <br />+  size <br />+  webUrl   |  +  String <br />+  Date <br />+  String <br />+  Date <br />+  String <br />+  String <br />+  Long <br />+  String   | 