# AEM (Server) data source connector field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to
fields in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use
  reserved attributes to map commonly occurring document attributes in your data
  source to Amazon Q index fields.
- **Custom** – You can create custom attributes to
  map document attributes that are unique to your data to Amazon Q
  index fields.
  When you connect Amazon Q to a data source, Amazon Q
  automatically maps specific data source document attributes to fields within an Amazon Q index. If a document attribute in your data source doesn't have a
  attribute mapping already available, or if you want to map additional document
  attributes to index fields, use the custom field mappings to specify how a data source
  attribute maps to an Amazon Q index field. You create field mappings by
  editing your data source after your application environment and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes-types.md "doc-attributes-types.md").

###### Important

Filtering using document attributes in chat is only supported through the
API.

The Amazon Q
Adobe Experience Manager (AEM) connector supports the following entities
and the associated reserved and custom attributes.

###### Important

If you map any AEM (Server) field to Amazon Q document title and document body fields,
Amazon Q will generate responses from data in the document title and body.

###### Supported entities and field mappings

- [Pages](#aem-field-mappings-pages "#aem-field-mappings-pages")
- [Assets](#aem-field-mappings-assets "#aem-field-mappings-assets")

## Pages

Amazon Q supports crawling [AEM Pages](https://experienceleague.adobe.com/docs/experience-manager-65/content/sites/authoring/essentials/page-authoring.html?lang=en "https://experienceleague.adobe.com/docs/experience-manager-65/content/sites/authoring/essentials/page-authoring.html?lang=en") and offers the following page field
mappings.

| Adobe Experience Manager (AEM) field name | Index field name     | Description | Data type   |
| ----------------------------------------- | -------------------- | ----------- | ----------- |
| aem_page_source_uri                       | \_source_uri         | Default     | String      |
| aem_page_createdBy                        | \_authors            | Default     | String list |
| aem_page_template                         | aem_page_template    | Custom      | String      |
| aem_entity_type                           | \_category           | Default     | String      |
| aem_page_createdAt                        | \_created_at         | Default     | Date        |
| aem_page_lastModified                     | \_last_updated_at    | Default     | Date        |
| aem_page_lastReplicatedBy                 | aem_page_publisher   | Custom      | String      |
| aem_page_lastReplicatedAt                 | aem_page_publishedAt | Custom      | Date        |

## Assets

Amazon Q supports crawling [AEM Assets](https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/assets.html?lang=en "https://experienceleague.adobe.com/docs/experience-manager-65/content/assets/assets.html?lang=en") and offers the following asset field
mappings.

| Adobe Experience Manager (AEM) field name | Index field name     | Description | Data type   |
| ----------------------------------------- | -------------------- | ----------- | ----------- |
| aem_page_source_uri                       | \_source_uri         | Default     | String      |
| aem_page_createdBy                        | \_authors            | Default     | String list |
| aem_entity_type                           | \_category           | Default     | String      |
| aem_page_createdAt                        | \_created_at         | Default     | Date        |
| aem_page_lastModified                     | \_last_updated_at    | Default     | Date        |
| aem_page_lastReplicatedBy                 | aem_page_publisher   | Custom      | String      |
| aem_page_lastReplicatedAt                 | aem_page_publishedAt | Custom      | Date        |
