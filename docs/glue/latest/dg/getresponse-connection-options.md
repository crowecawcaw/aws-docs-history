

# GetResponse connection options
<a name="getresponse-connection-options"></a>

The following are connection options for GetResponse:
+ `ENTITY_NAME` – (Required) Used for Read. The name of the GetResponse object to read.
+ `SELECTED_FIELDS` – Default: empty (SELECT \*). Used for Read. The columns you want to select for the object.
+ `FILTER_PREDICATE` – Default: empty. Used for Read. A filter predicate that AWS Glue pushes down to GetResponse for the fields listed in the filtering support table below. Supply it as a AWS Glue `FILTER_PREDICATE` option (for example, from a Spark `DataFrame` filter).

GetResponse supports server-side (pushed-down) filtering on the following entities, with the operators shown, through `FILTER_PREDICATE`:


| Entity | Filterable fields | Supported operators | 
| --- | --- | --- | 
| autoresponders | name, subject, campaignId, status, createdOn\_after, createdOn\_before | equals only | 
| campaigns | name | equals only | 
| contacts | email, name, origin, changedOn\_after, changedOn\_before, createdOn\_after, createdOn\_before, campaignId | equals only | 
| custom\_fields | name | equals only | 
| landing\_pages | name, status | equals only | 
| newsletters | name, subject, type, status, sendOn\_after, sendOn\_before, createdOn\_after, createdOn\_before, campaignId | equals only | 
| shops | name | equals only | 
| tags | name, createdAt\_after, createdAt\_before | equals only | 
| webinars | status, type, name, campaignId | equals only | 

AWS Glue applies filters on any other GetResponse entity after it reads records, through the Spark DataFrame filters.