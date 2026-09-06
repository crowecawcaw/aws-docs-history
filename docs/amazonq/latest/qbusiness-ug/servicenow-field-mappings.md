

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# ServiceNow Online data source connector field mappings
<a name="servicenow-field-mappings"></a>

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:
+ **Reserved or default** – Reserved attributes are based on document attributes that commonly occur in most data. You can use reserved attributes to map commonly occurring document attributes in your data source to Amazon Q index fields.
+ **Custom** – You can create custom attributes to map document attributes that are unique to your data to Amazon Q index fields.

When you connect Amazon Q to a data source, Amazon Q automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a attribute mapping already available, or if you want to map additional document attributes to index fields, use the custom field mappings to specify how a data source attribute maps to an Amazon Q index field. You create field mappings by editing your data source after your application and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see [Document attributes and types in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html).

**Important**  
Filtering using document attributes in chat is only supported through the API.

The Amazon Q ServiceNow connector supports the following entities and the associated reserved and custom attributes.

**Topics**
+ [Knowledge articles](#servicenow-field-mappings-ka)
+ [Service catalog](#servicenow-field-mappings-sc)
+ [Attachments](#servicenow-field-mappings-attachment)
+ [Incidents](#servicenow-field-mappings-incidents)

## Knowledge articles
<a name="servicenow-field-mappings-ka"></a>

Amazon Q supports crawling [ServiceNow Online Knowledge articles](https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/knowledge-management/task/create-knowledge-article.html) and offers the following knowledge article field mappings.


| ServiceNow field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| text | sn\_ka\_text | Custom | String | 
| short\_description | sn\_ka\_short\_description | Custom | String | 
| sys\_created\_on | \_created\_at | Default | Date | 
| sys\_updated\_on | \_last\_updated\_at | Default | Date | 
| kb\_category\_name | \_category | Default | String | 
| sys\_created\_by | \_authors | Default | String | 
| sys\_updated\_by | sn\_updatedBy | Custom | String | 
| sys\_id | sn\_sys\_id | Custom | String | 
| published | sn\_ka\_publish\_date | Custom | Date | 
| workflow\_state | sn\_ka\_workflow\_state | Custom | String | 
| kb\_category | sn\_ka\_category | Custom | String | 
| article\_type | sn\_ka\_article\_type | Custom | String | 
| first\_name | sn\_ka\_first\_name | Custom | String | 
| last\_name | sn\_ka\_last\_name | Custom | String | 
| user\_name | sn\_ka\_user\_name | Custom | String | 
| valid\_to | sn\_ka\_valid\_to | Custom | Date | 
| kb\_knowledge\_base | sn\_ka\_knowledge\_base | Custom | String | 
| number | sn\_ka\_number | Custom | String | 
| url | sn\_url | Custom | String | 
| diplayUrl | \_source\_uri | Default | String | 
| replacement\_article | sn\_ka\_replacement\_article | Custom | String | 
| description | sn\_ka\_description | Custom | String | 
| wiki | sn\_ka\_wiki | Custom | String | 
| rating | sn\_ka\_rating | Custom | String | 
| rating | sn\_ka\_rating | Custom | String | 
| view\_as\_allowed | sn\_ka\_view\_as\_allowed | Custom | String | 
| source | sn\_ka\_source | Custom | String | 
| image | sn\_ka\_image | Custom | String | 
| author | sn\_ka\_author | Custom | String | 
| active | sn\_ka\_active | Custom | String | 
| helpful\_count | sn\_ka\_helpful\_count | Custom | String | 
| meta\_description | sn\_ka\_meta\_description | Custom | String | 
| meta | sn\_ka\_meta | Custom | String | 
| topic | sn\_ka\_topic | Custom | String | 
| roles | sn\_ka\_roles | Custom | String | 
| disable\_suggesting | sn\_ka\_disable\_suggesting | Custom | String | 
| use\_count | sn\_ka\_use\_count | Custom | String | 
| flagged | sn\_ka\_flagged | Custom | String | 
| disable\_commenting | sn\_ka\_disable\_commenting | Custom | String | 
| retired | sn\_ka\_retired | Custom | String | 
| display\_attachments | sn\_ka\_display\_attachments | Custom | String | 
| taxonomy\_topic | sn\_ka\_taxonomy\_topic | Custom | String | 

## Service catalog
<a name="servicenow-field-mappings-sc"></a>

Amazon Q supports crawling [ServiceNow Online service catalogs](https://docs.servicenow.com/bundle/vancouver-servicenow-platform/page/product/service-catalog-management/concept/service-catalog.html) and offers the following service catalog field mappings.


| ServiceNow field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| description | sn\_sc\_description | Custom | String | 
| short\_description | sn\_sc\_short\_description | Custom | String | 
| sys\_created\_on | \_created\_at | Default | Date | 
| sys\_updated\_on | \_last\_updated\_at | Default | Date | 
| category\_name | \_category | Default | String | 
| sys\_created\_by | \_authors | Default | String list | 
| sys\_updated\_by | sn\_updated\_by | Custom | String | 
| sys\_id | sn\_sys\_id | Custom | String | 
| sc\_catalogs | sn\_sc\_catalogs | Custom | String | 
| sc\_catalogs\_name | sn\_sc\_catalogs\_name | Custom | String | 
| category | sn\_sc\_category | Custom | String | 
| category\_full\_name | sn\_sc\_category | Custom | String | 
| url | sn\_url | Custom | String | 
| displayUrl | \_source\_uri | Default | String | 
| show\_variable\_help\_on\_load | sn\_sc\_show\_var\_help\_on\_load | Custom | String | 
| no\_order\_now | sn\_sc\_no\_order\_now | Custom | String | 
| sc\_ic\_version | sn\_sc\_sc\_ic\_version | Custom | String | 
| delivery\_time | sn\_sc\_deliver\_time | Custom | String | 
| published\_ref | sn\_sc\_published\_ref | Custom | String | 
| price | sn\_sc\_price | Custom | String | 
| recurring\_frequency | sn\_sc\_recurring\_frequency | Custom | String | 
| sys\_name | sn\_sc\_sys\_name | Custom | String | 
| model | sn\_sc\_model | Custom | String | 
| state | sn\_sc\_state | Custom | String | 
| no\_cart | sn\_sc\_no\_cart | Custom | String | 
| group | sn\_sc\_group | Custom | String | 
| hide\_sp | sn\_sc\_hide\_sp | Custom | String | 
| order | sn\_sc\_order | Custom | String | 
| start\_closed | sn\_sc\_start\_closed | Custom | String | 
| image | sn\_sc\_image | Custom | String | 
| no\_quantity | sn\_sc\_no\_quantity | Custom | String | 
| delivery\_plan | sn\_sc\_delivery\_plan | Custom | String | 
| active | sn\_sc\_active | Custom | String | 
| checked\_out | sn\_sc\_checked\_out | Custom | String | 
| custom\_cart | sn\_sc\_custom\_cart | Custom | String | 
| no\_cart\_v2 | sn\_sc\_no\_cart\_v2 | Custom | String | 
| no\_proceed\_checkout | sn\_sc\_no\_proceed\_checkout | Custom | String | 
| ignore\_price | sn\_sc\_ignore\_price | Custom | String | 
| sys\_update\_name | sn\_sc\_sys\_update\_name | Custom | String | 
| meta | sn\_sc\_meta | Custom | String | 
| omit\_price | sn\_sc\_omit\_price | Custom | String | 
| name | sn\_sc\_name | Custom | String | 
| mobile\_hide\_price | sn\_sc\_mobile\_hide\_price | Custom | String | 
| no\_wishlist\_v2 | sn\_sc\_no\_wishlist\_v2 | Custom | String | 
| preview | sn\_sc\_preview | Custom | String | 
| type | sn\_sc\_type | Custom | String | 
| access\_type | sn\_sc\_access\_type | Custom | String | 
| roles | sn\_sc\_roles | Custom | String | 
| icon | sn\_sc\_icon | Custom | String | 
| mobile\_picture | sn\_sc\_mobile\_picture | Custom | String | 
| availability | sn\_sc\_availability | Custom | String | 
| mandatory\_attachment | sn\_sc\_mandatory\_attachment | Custom | String | 
| request\_method | sn\_sc\_request\_method | Custom | String | 
| visible\_guide | sn\_sc\_visible\_guide | Custom | String | 
| visible\_standalone | sn\_sc\_visible\_standalone | Custom | String | 
| no\_order | sn\_sc\_no\_order | Custom | String | 
| vendor | sn\_sc\_vendor | Custom | String | 
| no\_attachment\_v2 | sn\_sc\_no\_attachment\_v2 | Custom | String | 
| mobile\_picture\_type | sn\_sc\_mobile\_picture\_type | Custom | String | 
| visible\_bundle | sn\_sc\_visible\_bundle | Custom | String | 
| ordered\_item\_link | sn\_sc\_ordered\_item\_link | Custom | String | 
| owner | sn\_sc\_owner | Custom | String | 
| no\_delivery\_time\_v2 | sn\_sc\_no\_delivery\_time\_v2 | Custom | String | 
| cost | sn\_sc\_cost | Custom | String | 
| no\_quantity\_v2 | sn\_sc\_no\_quantity\_v2 | Custom | String | 
| recurring\_price | sn\_sc\_recurring\_price | Custom | String | 
| list\_price | sn\_sc\_list\_price | Custom | String | 
| syst\_tags | sn\_sc\_sys\_tags | Custom | String | 
| billable | sn\_sc\_billable | Custom | String | 
| picture | sn\_sc\_picture | Custom | String | 
| display\_price\_property | sn\_sc\_display\_price\_property | Custom | String | 
| taxonomy\_topic | sn\_sc\_taxonomy\_topic | Custom | String | 
| delivery\_plain\_script | sn\_sc\_delivery\_plain\_script | Custom | String | 
| location | sn\_sc\_location | Custom | String | 

## Attachments
<a name="servicenow-field-mappings-attachment"></a>

Amazon Q supports crawling [ServiceNow Online attachments](https://docs.servicenow.com/bundle/tokyo-platform-user-interface/page/use/using-forms/task/t_AddingAnAttachment.html) and offers the following attachment field mappings.


| ServiceNow field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| size\_bytes | sn\_file\_size | Custom | Long (numeric) | 
| file\_name | sn\_file\_name | Custom | String | 
| sys\_mod\_count | sn\_sys\_mod\_count | Custom | String | 
| average\_image\_color | sn\_average\_image\_color | Custom | String | 
| image\_width | sn\_image\_width | Custom | String | 
| sys\_updated\_on | \_last\_updated\_at | Default | Date | 
| sys\_tags | sn\_sys\_tags | Custom | String | 
| table\_name | sn\_table\_name | Custom | String | 
| sys\_id | sn\_sys\_id | Custom | String | 
| image\_height | sn\_image\_height | Custom | String | 
| sys\_updated\_by | sn\_updated\_by | Custom | String | 
| content\_type | sn\_content\_type | Custom | String | 
| sys\_created\_on | \_created\_at | Default | Date | 
| size\_compressed | sn\_size\_compressed | Custom | String | 
| compressed | sn\_compressed | Custom | String | 
| state | sn\_state | Custom | String | 
| table\_sys\_id | sn\_table\_sys\_id | Custom | String | 
| chunk\_size\_bytes | sn\_chunk\_size\_bytes | Custom | String | 
| hash | sn\_hash | Custom | String | 
| sys\_created\_by | \_authors | Default | String list | 
| sys\_updated\_by | sn\_updated\_by | Custom | String | 
| url | sn\_url | Custom | String | 
| displayUrl | \_source\_uri | Default | String | 

## Incidents
<a name="servicenow-field-mappings-incidents"></a>

Amazon Q supports crawling [ServiceNow Online incidents](https://docs.servicenow.com/bundle/tokyo-it-service-management/page/product/incident-management/concept/c_IncidentManagement.html) and offers the following incident field mappings.


| ServiceNow field name | Index field name | Description | Data type | 
| --- | --- | --- | --- | 
| short\_description | sn\_inc\_short\_description | Custom | String | 
| description | sn\_inc\_description | Custom | String | 
| sys\_updated\_on | \_last\_updated\_at | Default | Date | 
| number | sn\_inc\_number | Custom | String | 
| sys\_updated\_by | sn\_updatedBy | Custom | String | 
| displayUrl | \_source\_uri | Default | String | 
| opened\_by | sn\_inc\_opened\_by | Custom | String | 
| sys\_created\_on | \_created\_at | Default | Date | 
| state | sn\_inc\_state | Custom | String | 
| sys\_created\_by | \_authors | Default | String list | 
| business\_impact | sn\_inc\_business\_impact | Default | String | 
| impact | sn\_inc\_business\_impact | Custom | String | 
| priority | sn\_inc\_priority | Custom | String | 
| urgency | sn\_inc\_urgency | Custom | String | 
| opened\_at | an\_inc\_opened\_at | Custom | String | 
| business\_duration | sn\_inc\_business\_duration | Custom | String | 
| caller\_id | sn\_inc\_caller\_id | Custom | String | 
| resolved\_at | sn\_inc\_resolved\_at | Custom | String | 
| category | sn\_inc\_category | Custom | String | 
| subcategory | sn\_inc\_subcategory | Custom | String | 
| close\_code | sn\_inc\_close\_code | Custom | String | 
| assignment\_group | sn\_inc\_assignment\_group | Custom | String | 
| close\_notes | sn\_inc\_close\_notes | Custom | String | 
| displayUrl | \_source\_uri | Default | String | 
| sys\_class\_name | sn\_inc\_sys\_class\_name | Custom | String | 
| parent\_incident | an\_inc\_parent\_incident | Custom | String | 
| incident\_state | sn\_incident\_state | Custom | String | 
| company | sn\_inc\_company | Custom | String | 
| assigned\_to | sn\_inc\_assigned\_to | Custom | String | 
| hold\_reason | an\_inc\_hold\_reason | Custom | String | 
| work\_notes | sn\_inc\_work\_notes | Custom | String | 
| comments\_and\_work\_notes | sn\_inc\_comments\_and\_work\_notes | Custom | String | 
| work\_notes\_list | sn\_work\_notes\_list | Custom | String | 
| comments | sn\_inc\_comments | Custom | String | 
| sys\_id | sn\_inc\_sys\_id | Custom | String | 
| url | sn\_url | Custom | String | 
| active | sn\_inc\_active | Custom | String | 
| activity\_due | sn\_inc\_activity\_due | Custom | String | 
| additional\_assignee\_list | sn\_inc\_additional\_assign\_list | Custom | String | 
| approval | sn\_inc\_approval | Custom | String | 
| approval\_history | sn\_inc\_approval\_history | Custom | String | 
| approval\_set | sn\_inc\_approval\_set | Custom | Date | 
| business\_service | sn\_inc\_business\_service | Custom | String | 
| closed\_by | sn\_inc\_closed\_by | Custom | String | 
| cmdb\_ci | sn\_inc\_cmdb\_id | Custom | String | 
| resolved\_by | sn\_inc\_resolved\_by | Custom | String | 
| sys\_domain | sn\_inc\_sys\_domain | Custom | String | 
| business\_stc | sn\_inc\_business\_stc | Custom | String | 
| calendar\_duration | sn\_inc\_calendar\_duration | Custom | String | 
| calendar\_stc | sn\_inc\_calendar\_stc | Custom | String | 
| cause | sn\_inc\_cause | Custom | String | 
| caused\_by | sn\_inc\_caused\_by | Custom | String | 
| child\_incidents | sn\_inc\_child\_incidents | Custom | String | 
| closed\_at | sn\_inc\_closed\_at | Custom | String | 
| contact\_type | sn\_inc\_contact\_type | Custom | String | 
| contract | sn\_inc\_contract | Custom | String | 
| correlation\_display | sn\_inc\_correlation\_display | Custom | String | 
| delivery\_plan | sn\_inc\_delivery\_plan | Custom | String | 
| delivery\_task | sn\_inc\_delivery\_task | Custom | String | 
| due\_date | sn\_inc\_due\_date | Custom | String | 
| escalation | sn\_inc\_escalation | Custom | String | 
| expected\_start | sn\_inc\_expected\_start | Custom | String | 
| follow\_up | sn\_inc\_follow\_up | Custom | String | 
| group\_list | sn\_inc\_group\_list | Custom | String | 
| knowledge | sn\_inc\_knowledge | Custom | String | 
| location | sn\_inc\_location | Custom | String | 
| made\_sla | sn\_inc\_made\_sla | Custom | String | 
| notify | sn\_inc\_notify | Custom | String | 
| order | sn\_inc\_order | Custom | String | 
| origin\_id | sn\_inc\_origin\_id | Custom | String | 
| origin\_table | sn\_inc\_origin\_table | Custom | String | 
| parent | sn\_inc\_parent | Custom | String | 
| problem\_id | sn\_inc\_problem\_id | Custom | String | 
| reassignment\_count | sn\_inc\_reassignment\_count | Custom | String | 
| repoen\_count | sn\_inc\_reopen\_count | Custom | String | 
| reopened\_by | sn\_inc\_reopened\_by | Custom | String | 
| reopened\_time | sn\_inc\_reopened\_time | Custom | String | 
| rfc | sn\_inc\_rfc | Custom | String | 
| route\_reason | sn\_inc\_route\_reason | Custom | String | 
| service\_offering | sn\_inc\_service\_offering | Custom | String | 
| severity | sn\_inc\_severity | Custom | String | 
| sla\_due | sn\_inc\_sla\_due | Custom | Date | 
| task\_effective\_number | sn\_inc\_task\_effective\_number | Custom | String | 
| time\_worked | sn\_inc\_time\_worked | Custom | Date | 
| universal\_request | sn\_inc\_universal\_request | Custom | String | 
| upon\_approval | sn\_inc\_upon\_approval | Custom | String | 
| upon\_reject | sn\_inc\_upon\_reject | Custom | String | 
| user\_input | sn\_inc\_user\_input | Custom | String | 
| watch\_list | sn\_inc\_watch\_list | Custom | String | 
| work\_end | sn\_inc\_work\_end | Custom | String | 
| work\_start | sn\_inc\_work\_start | Custom | String | 