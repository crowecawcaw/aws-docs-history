# ServiceNow Online data source connector

field mappings

To improve retrieved results and customize the end user chat experience, Amazon Q Business enables you to map document attributes from your data sources to fields
in your Amazon Q index.

Amazon Q offers two kinds of attributes to map to index fields:

- **Reserved or default** – Reserved attributes are
  based on document attributes that commonly occur in most data. You can use reserved
  attributes to map commonly occurring document attributes in your data source to
  Amazon Q index fields.
- **Custom** – You can create custom attributes to map
  document attributes that are unique to your data to Amazon Q index
  fields.
  When you connect Amazon Q to a data source, Amazon Q automatically
  maps specific data source document attributes to fields within an Amazon Q index.
  If a document attribute in your data source doesn't have a attribute mapping already
  available, or if you want to map additional document attributes to index fields, use the
  custom field mappings to specify how a data source attribute maps to an Amazon Q
  index field. You create field mappings by editing your data source after your application
  and retriever are created.

To learn more about document attributes and how they work in Amazon Q, see
[Document attributes and types in Amazon Q](doc-attributes.md "doc-attributes.md").

###### Important

Filtering using document attributes in chat is only supported through the API.

The Amazon Q
ServiceNow connector supports the following entities and the associated
reserved and custom attributes.

###### Supported entities and field mappings

- [Knowledge articles](#servicenow-field-mappings-ka "#servicenow-field-mappings-ka")
- [Service catalog](#servicenow-field-mappings-sc "#servicenow-field-mappings-sc")
- [Attachments](#servicenow-field-mappings-attachment "#servicenow-field-mappings-attachment")
- [Incidents](#servicenow-field-mappings-incidents "#servicenow-field-mappings-incidents")

## Knowledge articles

Amazon Q supports crawling [ServiceNow Online Knowledge articles](https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/knowledge-management/task/create-knowledge-article.html "https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/knowledge-management/task/create-knowledge-article.html") and offers the following knowledge
article field mappings.

| ServiceNow field name      | Index field name               | Description | Data type      |
| -------------------------- | ------------------------------ | ----------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| text                       | sn_ka_text                     | Custom      | String         |
| short_description          | sn_ka_short_description        | Custom      | String         |
| sys_created_on             | \_created_at                   | Default     | Date           |
| sys_updated_on             | \_last_updated_at              | Default     | Date           |
| kb_category_name           | \_category                     | Default     | String         |
| sys_created_by             | \_authors                      | Default     | String         |
| sys_updated_by             | sn_updatedBy                   | Custom      | String         |
| sys_id                     | sn_sys_id                      | Custom      | String         |
| published                  | sn_ka_publish_date             | Custom      | Date           |
| workflow_state             | sn_ka_workflow_state           | Custom      | String         |
| kb_category                | sn_ka_category                 | Custom      | String         |
| article_type               | sn_ka_article_type             | Custom      | String         |
| first_name                 | sn_ka_first_name               | Custom      | String         |
| last_name                  | sn_ka_last_name                | Custom      | String         |
| user_name                  | sn_ka_user_name                | Custom      | String         |
| valid_to                   | sn_ka_valid_to                 | Custom      | Date           |
| kb_knowledge_base          | sn_ka_knowledge_base           | Custom      | String         |
| number                     | sn_ka_number                   | Custom      | String         |
| url                        | sn_url                         | Custom      | String         |
| diplayUrl                  | \_source_uri                   | Default     | String         |
| replacement_article        | sn_ka_replacement_article      | Custom      | String         |
| description                | sn_ka_description              | Custom      | String         |
| wiki                       | sn_ka_wiki                     | Custom      | String         |
| rating                     | sn_ka_rating                   | Custom      | String         |
| rating                     | sn_ka_rating                   | Custom      | String         |
| view_as_allowed            | sn_ka_view_as_allowed          | Custom      | String         |
| source                     | sn_ka_source                   | Custom      | String         |
| image                      | sn_ka_image                    | Custom      | String         |
| author                     | sn_ka_author                   | Custom      | String         |
| active                     | sn_ka_active                   | Custom      | String         |
| helpful_count              | sn_ka_helpful_count            | Custom      | String         |
| meta_description           | sn_ka_meta_description         | Custom      | String         |
| meta                       | sn_ka_meta                     | Custom      | String         |
| topic                      | sn_ka_topic                    | Custom      | String         |
| roles                      | sn_ka_roles                    | Custom      | String         |
| disable_suggesting         | sn_ka_disable_suggesting       | Custom      | String         |
| use_count                  | sn_ka_use_count                | Custom      | String         |
| flagged                    | sn_ka_flagged                  | Custom      | String         |
| disable_commenting         | sn_ka_disable_commenting       | Custom      | String         |
| retired                    | sn_ka_retired                  | Custom      | String         |
| display_attachments        | sn_ka_display_attachments      | Custom      | String         |
| taxonomy_topic             | sn_ka_taxonomy_topic           | Custom      | String         | ## Service catalog Amazon Q supports crawling [ServiceNow Online service catalogs](https://docs.servicenow.com/bundle/vancouver-servicenow-platform/page/product/service-catalog-management/concept/service-catalog.html "https://docs.servicenow.com/bundle/vancouver-servicenow-platform/page/product/service-catalog-management/concept/service-catalog.html") and offers the following service catalog field mappings. |
| ServiceNow field name      | Index field name               | Description | Data type      |
| ---                        | ---                            | ---         | ---            |
| description                | sn_sc_description              | Custom      | String         |
| short_description          | sn_sc_short_description        | Custom      | String         |
| sys_created_on             | \_created_at                   | Default     | Date           |
| sys_updated_on             | \_last_updated_at              | Default     | Date           |
| category_name              | \_category                     | Default     | String         |
| sys_created_by             | \_authors                      | Default     | String list    |
| sys_updated_by             | sn_updated_by                  | Custom      | String         |
| sys_id                     | sn_sys_id                      | Custom      | String         |
| sc_catalogs                | sn_sc_catalogs                 | Custom      | String         |
| sc_catalogs_name           | sn_sc_catalogs_name            | Custom      | String         |
| category                   | sn_sc_category                 | Custom      | String         |
| category_full_name         | sn_sc_category                 | Custom      | String         |
| url                        | sn_url                         | Custom      | String         |
| displayUrl                 | \_source_uri                   | Default     | String         |
| show_variable_help_on_load | sn_sc_show_var_help_on_load    | Custom      | String         |
| no_order_now               | sn_sc_no_order_now             | Custom      | String         |
| sc_ic_version              | sn_sc_sc_ic_version            | Custom      | String         |
| delivery_time              | sn_sc_deliver_time             | Custom      | String         |
| published_ref              | sn_sc_published_ref            | Custom      | String         |
| price                      | sn_sc_price                    | Custom      | String         |
| recurring_frequency        | sn_sc_recurring_frequency      | Custom      | String         |
| sys_name                   | sn_sc_sys_name                 | Custom      | String         |
| model                      | sn_sc_model                    | Custom      | String         |
| state                      | sn_sc_state                    | Custom      | String         |
| no_cart                    | sn_sc_no_cart                  | Custom      | String         |
| group                      | sn_sc_group                    | Custom      | String         |
| hide_sp                    | sn_sc_hide_sp                  | Custom      | String         |
| order                      | sn_sc_order                    | Custom      | String         |
| start_closed               | sn_sc_start_closed             | Custom      | String         |
| image                      | sn_sc_image                    | Custom      | String         |
| no_quantity                | sn_sc_no_quantity              | Custom      | String         |
| delivery_plan              | sn_sc_delivery_plan            | Custom      | String         |
| active                     | sn_sc_active                   | Custom      | String         |
| checked_out                | sn_sc_checked_out              | Custom      | String         |
| custom_cart                | sn_sc_custom_cart              | Custom      | String         |
| no_cart_v2                 | sn_sc_no_cart_v2               | Custom      | String         |
| no_proceed_checkout        | sn_sc_no_proceed_checkout      | Custom      | String         |
| ignore_price               | sn_sc_ignore_price             | Custom      | String         |
| sys_update_name            | sn_sc_sys_update_name          | Custom      | String         |
| meta                       | sn_sc_meta                     | Custom      | String         |
| omit_price                 | sn_sc_omit_price               | Custom      | String         |
| name                       | sn_sc_name                     | Custom      | String         |
| mobile_hide_price          | sn_sc_mobile_hide_price        | Custom      | String         |
| no_wishlist_v2             | sn_sc_no_wishlist_v2           | Custom      | String         |
| preview                    | sn_sc_preview                  | Custom      | String         |
| type                       | sn_sc_type                     | Custom      | String         |
| access_type                | sn_sc_access_type              | Custom      | String         |
| roles                      | sn_sc_roles                    | Custom      | String         |
| icon                       | sn_sc_icon                     | Custom      | String         |
| mobile_picture             | sn_sc_mobile_picture           | Custom      | String         |
| availability               | sn_sc_availability             | Custom      | String         |
| mandatory_attachment       | sn_sc_mandatory_attachment     | Custom      | String         |
| request_method             | sn_sc_request_method           | Custom      | String         |
| visible_guide              | sn_sc_visible_guide            | Custom      | String         |
| visible_standalone         | sn_sc_visible_standalone       | Custom      | String         |
| no_order                   | sn_sc_no_order                 | Custom      | String         |
| vendor                     | sn_sc_vendor                   | Custom      | String         |
| no_attachment_v2           | sn_sc_no_attachment_v2         | Custom      | String         |
| mobile_picture_type        | sn_sc_mobile_picture_type      | Custom      | String         |
| visible_bundle             | sn_sc_visible_bundle           | Custom      | String         |
| ordered_item_link          | sn_sc_ordered_item_link        | Custom      | String         |
| owner                      | sn_sc_owner                    | Custom      | String         |
| no_delivery_time_v2        | sn_sc_no_delivery_time_v2      | Custom      | String         |
| cost                       | sn_sc_cost                     | Custom      | String         |
| no_quantity_v2             | sn_sc_no_quantity_v2           | Custom      | String         |
| recurring_price            | sn_sc_recurring_price          | Custom      | String         |
| list_price                 | sn_sc_list_price               | Custom      | String         |
| syst_tags                  | sn_sc_sys_tags                 | Custom      | String         |
| billable                   | sn_sc_billable                 | Custom      | String         |
| picture                    | sn_sc_picture                  | Custom      | String         |
| display_price_property     | sn_sc_display_price_property   | Custom      | String         |
| taxonomy_topic             | sn_sc_taxonomy_topic           | Custom      | String         |
| delivery_plain_script      | sn_sc_delivery_plain_script    | Custom      | String         |
| location                   | sn_sc_location                 | Custom      | String         | ## Attachments Amazon Q supports crawling [ServiceNow Online attachments](https://docs.servicenow.com/bundle/tokyo-platform-user-interface/page/use/using-forms/task/t_AddingAnAttachment.html "https://docs.servicenow.com/bundle/tokyo-platform-user-interface/page/use/using-forms/task/t_AddingAnAttachment.html") and offers the following attachment field mappings.                                                 |
| ServiceNow field name      | Index field name               | Description | Data type      |
| ---                        | ---                            | ---         | ---            |
| size_bytes                 | sn_file_size                   | Custom      | Long (numeric) |
| file_name                  | sn_file_name                   | Custom      | String         |
| sys_mod_count              | sn_sys_mod_count               | Custom      | String         |
| average_image_color        | sn_average_image_color         | Custom      | String         |
| image_width                | sn_image_width                 | Custom      | String         |
| sys_updated_on             | \_last_updated_at              | Default     | Date           |
| sys_tags                   | sn_sys_tags                    | Custom      | String         |
| table_name                 | sn_table_name                  | Custom      | String         |
| sys_id                     | sn_sys_id                      | Custom      | String         |
| image_height               | sn_image_height                | Custom      | String         |
| sys_updated_by             | sn_updated_by                  | Custom      | String         |
| content_type               | sn_content_type                | Custom      | String         |
| sys_created_on             | \_created_at                   | Default     | Date           |
| size_compressed            | sn_size_compressed             | Custom      | String         |
| compressed                 | sn_compressed                  | Custom      | String         |
| state                      | sn_state                       | Custom      | String         |
| table_sys_id               | sn_table_sys_id                | Custom      | String         |
| chunk_size_bytes           | sn_chunk_size_bytes            | Custom      | String         |
| hash                       | sn_hash                        | Custom      | String         |
| sys_created_by             | \_authors                      | Default     | String list    |
| sys_updated_by             | sn_updated_by                  | Custom      | String         |
| url                        | sn_url                         | Custom      | String         |
| displayUrl                 | \_source_uri                   | Default     | String         | ## Incidents Amazon Q supports crawling [ServiceNow Online incidents](https://docs.servicenow.com/bundle/tokyo-it-service-management/page/product/incident-management/concept/c_IncidentManagement.html "https://docs.servicenow.com/bundle/tokyo-it-service-management/page/product/incident-management/concept/c_IncidentManagement.html") and offers the following incident field mappings.                             |
| ServiceNow field name      | Index field name               | Description | Data type      |
| ---                        | ---                            | ---         | ---            |
| short_description          | sn_inc_short_description       | Custom      | String         |
| description                | sn_inc_description             | Custom      | String         |
| sys_updated_on             | \_last_updated_at              | Default     | Date           |
| number                     | sn_inc_number                  | Custom      | String         |
| sys_updated_by             | sn_updatedBy                   | Custom      | String         |
| displayUrl                 | \_source_uri                   | Default     | String         |
| opened_by                  | sn_inc_opened_by               | Custom      | String         |
| sys_created_on             | \_created_at                   | Default     | Date           |
| state                      | sn_inc_state                   | Custom      | String         |
| sys_created_by             | \_authors                      | Default     | String list    |
| business_impact            | sn_inc_business_impact         | Default     | String         |
| impact                     | sn_inc_business_impact         | Custom      | String         |
| priority                   | sn_inc_priority                | Custom      | String         |
| urgency                    | sn_inc_urgency                 | Custom      | String         |
| opened_at                  | an_inc_opened_at               | Custom      | String         |
| business_duration          | sn_inc_business_duration       | Custom      | String         |
| caller_id                  | sn_inc_caller_id               | Custom      | String         |
| resolved_at                | sn_inc_resolved_at             | Custom      | String         |
| category                   | sn_inc_category                | Custom      | String         |
| subcategory                | sn_inc_subcategory             | Custom      | String         |
| close_code                 | sn_inc_close_code              | Custom      | String         |
| assignment_group           | sn_inc_assignment_group        | Custom      | String         |
| close_notes                | sn_inc_close_notes             | Custom      | String         |
| displayUrl                 | \_source_uri                   | Default     | String         |
| sys_class_name             | sn_inc_sys_class_name          | Custom      | String         |
| parent_incident            | an_inc_parent_incident         | Custom      | String         |
| incident_state             | sn_incident_state              | Custom      | String         |
| company                    | sn_inc_company                 | Custom      | String         |
| assigned_to                | sn_inc_assigned_to             | Custom      | String         |
| hold_reason                | an_inc_hold_reason             | Custom      | String         |
| work_notes                 | sn_inc_work_notes              | Custom      | String         |
| comments_and_work_notes    | sn_inc_comments_and_work_notes | Custom      | String         |
| work_notes_list            | sn_work_notes_list             | Custom      | String         |
| comments                   | sn_inc_comments                | Custom      | String         |
| sys_id                     | sn_inc_sys_id                  | Custom      | String         |
| url                        | sn_url                         | Custom      | String         |
| active                     | sn_inc_active                  | Custom      | String         |
| activity_due               | sn_inc_activity_due            | Custom      | String         |
| additional_assignee_list   | sn_inc_additional_assign_list  | Custom      | String         |
| approval                   | sn_inc_approval                | Custom      | String         |
| approval_history           | sn_inc_approval_history        | Custom      | String         |
| approval_set               | sn_inc_approval_set            | Custom      | Date           |
| business_service           | sn_inc_business_service        | Custom      | String         |
| closed_by                  | sn_inc_closed_by               | Custom      | String         |
| cmdb_ci                    | sn_inc_cmdb_id                 | Custom      | String         |
| resolved_by                | sn_inc_resolved_by             | Custom      | String         |
| sys_domain                 | sn_inc_sys_domain              | Custom      | String         |
| business_stc               | sn_inc_business_stc            | Custom      | String         |
| calendar_duration          | sn_inc_calendar_duration       | Custom      | String         |
| calendar_stc               | sn_inc_calendar_stc            | Custom      | String         |
| cause                      | sn_inc_cause                   | Custom      | String         |
| caused_by                  | sn_inc_caused_by               | Custom      | String         |
| child_incidents            | sn_inc_child_incidents         | Custom      | String         |
| closed_at                  | sn_inc_closed_at               | Custom      | String         |
| contact_type               | sn_inc_contact_type            | Custom      | String         |
| contract                   | sn_inc_contract                | Custom      | String         |
| correlation_display        | sn_inc_correlation_display     | Custom      | String         |
| delivery_plan              | sn_inc_delivery_plan           | Custom      | String         |
| delivery_task              | sn_inc_delivery_task           | Custom      | String         |
| due_date                   | sn_inc_due_date                | Custom      | String         |
| escalation                 | sn_inc_escalation              | Custom      | String         |
| expected_start             | sn_inc_expected_start          | Custom      | String         |
| follow_up                  | sn_inc_follow_up               | Custom      | String         |
| group_list                 | sn_inc_group_list              | Custom      | String         |
| knowledge                  | sn_inc_knowledge               | Custom      | String         |
| location                   | sn_inc_location                | Custom      | String         |
| made_sla                   | sn_inc_made_sla                | Custom      | String         |
| notify                     | sn_inc_notify                  | Custom      | String         |
| order                      | sn_inc_order                   | Custom      | String         |
| origin_id                  | sn_inc_origin_id               | Custom      | String         |
| origin_table               | sn_inc_origin_table            | Custom      | String         |
| parent                     | sn_inc_parent                  | Custom      | String         |
| problem_id                 | sn_inc_problem_id              | Custom      | String         |
| reassignment_count         | sn_inc_reassignment_count      | Custom      | String         |
| repoen_count               | sn_inc_reopen_count            | Custom      | String         |
| reopened_by                | sn_inc_reopened_by             | Custom      | String         |
| reopened_time              | sn_inc_reopened_time           | Custom      | String         |
| rfc                        | sn_inc_rfc                     | Custom      | String         |
| route_reason               | sn_inc_route_reason            | Custom      | String         |
| service_offering           | sn_inc_service_offering        | Custom      | String         |
| severity                   | sn_inc_severity                | Custom      | String         |
| sla_due                    | sn_inc_sla_due                 | Custom      | Date           |
| task_effective_number      | sn_inc_task_effective_number   | Custom      | String         |
| time_worked                | sn_inc_time_worked             | Custom      | Date           |
| universal_request          | sn_inc_universal_request       | Custom      | String         |
| upon_approval              | sn_inc_upon_approval           | Custom      | String         |
| upon_reject                | sn_inc_upon_reject             | Custom      | String         |
| user_input                 | sn_inc_user_input              | Custom      | String         |
| watch_list                 | sn_inc_watch_list              | Custom      | String         |
| work_end                   | sn_inc_work_end                | Custom      | String         |
| work_start                 | sn_inc_work_start              | Custom      | String         |
