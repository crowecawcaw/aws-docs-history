

# Limitations
<a name="salesforce-commerce-cloud-connector-limitations"></a>

The following are limitations for the Salesforce Commerce Cloud connector:
+ The Contains filter is not working as expected when partitioning.
+ CDN Zones' entity doesn't support sandbox instances, and it supports only Development and production instance types. For more information, see [ https://help.salesforce.com/s/articleView?id=cc.b2c\_embedded\_cdn\_overview.htm ](https://help.salesforce.com/s/articleView?id=cc.b2c_embedded_cdn_overview.htm).
+ In Salesforce Commerce Cloud, there is no API endpoint to fetch Dynamic Metadata. As a result, there is no provision to support the custom fields in the Product and Category entity.
+ Site id is a mandatory query parameter. You must pass the Site Id value through the Custom Connector Setting. For more information, see [Base URL and Request Formation ](https://developer.salesforce.com/docs/commerce/commerce-api/guide/base-url.html).
+ You can apply filters on maximum two fields (excluding Levels if present) in single API request with the combination of different operators as mentioned in the below table:

<a name="salesforce-commerce-cloud-limitations-filters"></a>
<table>
<thead>
  <tr><th>Filter criteria</th><th>Is supported?</th></tr>
</thead>
<tbody>
  <tr><td>One field with CONTAINS operator in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with Equals operator in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with BETWEEN operator in single API request.</td><td>Yes</td></tr>
  <tr><td>Two or more fields with CONTAINS operator in single API request.</td><td>No</td></tr>
  <tr><td>Two or more fields with Equals operator in single API request.</td><td>No</td></tr>
  <tr><td>Two or more fields with BETWEEN operator in single API request.</td><td>No</td></tr>
  <tr><td>One field with Equals and one field with CONTAINS operator in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with BETWEEN and one field with CONTAINS operator in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with BETWEEN and one field with Equals operator in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with Equals, one field with CONTAINS and one field with BETWEEN operator in single API request.</td><td>No</td></tr>
  <tr><td>One field with Equals operator when INCREMENTAL PULL is applied in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with CONTAINS operator when INCREMENTAL PULL is applied in single API request.</td><td>Yes</td></tr>
  <tr><td>One field with BETWEEN operator when INCREMENTAL PULL is applied in single API request.</td><td>No</td></tr>
  <tr><td>One Equals and one CONTAINS operator when INCREMENTAL PULL is applied in single API request.</td><td>No</td></tr>
</tbody>
</table>

+ In some of the entities, the data type for the fields while retrieving is different from when it is used as searchable fields. As a result, there is no provision of filter feature for these fields. The following table provides the details about such fields. 

<a name="salesforce-commerce-cloud-limitations-filters-provision"></a>
<table>
<thead>
  <tr><th>Sr. No.</th><th>Entity Name</th><th>Searchable Field Name</th><th>Data Type as Searchable</th><th>Data Type as Retrievable</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>Catalog</td><td>name</td><td>String</td><td>Struct</td></tr>
  <tr><td>2</td><td>Catalog</td><td>description</td><td>String</td><td>Struct</td></tr>
  <tr><td>3</td><td>Category</td><td>name</td><td>String</td><td>Struct</td></tr>
  <tr><td>4</td><td>Category</td><td>description</td><td>String</td><td>Struct</td></tr>
  <tr><td>5</td><td>Product</td><td>name</td><td>String</td><td>Struct</td></tr>
  <tr><td>6</td><td>Product</td><td>searchable</td><td>Boolean</td><td>Struct</td></tr>
  <tr><td>7</td><td>Product</td><td>validFrom</td><td>DateTime</td><td>Struct</td></tr>
  <tr><td>8</td><td>Product</td><td>validTo</td><td>DateTime</td><td>Struct</td></tr>
  <tr><td>9</td><td>Product</td><td>type</td><td>String</td><td>Struct</td></tr>
  <tr><td>10</td><td>Product</td><td>onlineFlag</td><td>Boolean</td><td>Struct</td></tr>
  <tr><td>11</td><td>Promotion</td><td>name</td><td>String</td><td>Struct</td></tr>
</tbody>
</table>
