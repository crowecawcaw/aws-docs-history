

# Resource tags columns
<a name="table-dictionary-cur2-resource-tags"></a>

Resource tags columns contain data about resource tags that apply to the line item. Note that you don’t need to select this column if you selected the Tags column because resource tags are also included under the Tags column.



| Column name | Description | Data type | 
| --- | --- | --- | 
| resource\_tags | A map column containing key-value pairs of resource tags and their values for a given line item. The values in this column are all of data type "string".<br />Resource tag keys only appear in this column if they've been enabled as cost allocation tags in the Billing console. After being enabled, a particular key only appears in the map column if it has a value that applies to the specific line item.<br />The keys of this column can be queried as individual columns using the dot operator. For more information, see [Data query](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-data-query.html). | map <string, string> | 