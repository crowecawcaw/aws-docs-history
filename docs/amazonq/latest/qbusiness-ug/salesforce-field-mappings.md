# Salesforce Online data source connector

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
Salesforce connector supports the following entities and the associated
reserved and custom attributes.

###### Note

You can map any Salesforce field to the document title or document body
Amazon Q reserved/default index fields.

###### Supported entities and field mappings

- [Account](#salesforce-field-mappings-account "#salesforce-field-mappings-account")
- [Campaign](#salesforce-field-mappings-sc "#salesforce-field-mappings-sc")
- [Case](#salesforce-field-mappings-case "#salesforce-field-mappings-case")
- [Contact](#salesforce-field-mappings-contact "#salesforce-field-mappings-contact")
- [Contract](#salesforce-field-mappings-contract "#salesforce-field-mappings-contract")
- [Document](#salesforce-field-mappings-document "#salesforce-field-mappings-document")
- [Group](#salesforce-field-mappings-group "#salesforce-field-mappings-group")
- [Idea](#salesforce-field-mappings-idea "#salesforce-field-mappings-idea")
- [Lead](#salesforce-field-mappings-lead "#salesforce-field-mappings-lead")
- [Opportunity](#salesforce-field-mappings-opportunity "#salesforce-field-mappings-opportunity")
- [Partner](#salesforce-field-mappings-partner "#salesforce-field-mappings-partner")
- [Pricebook](#salesforce-field-mappings-pricebook "#salesforce-field-mappings-pricebook")
- [Product](#salesforce-field-mappings-product "#salesforce-field-mappings-product")
- [Solution](#salesforce-field-mappings-solution "#salesforce-field-mappings-solution")
- [Profile](#salesforce-field-mappings-profile "#salesforce-field-mappings-profile")
- [Task](#salesforce-field-mappings-task "#salesforce-field-mappings-task")
- [User](#salesforce-field-mappings-user "#salesforce-field-mappings-user")
- [Chatter](#salesforce-field-mappings-chatter "#salesforce-field-mappings-chatter")
- [Knowledge articles](#salesforce-field-mappings-ka "#salesforce-field-mappings-ka")
- [Attachments](#salesforce-field-mappings-attachments "#salesforce-field-mappings-attachments")
- [Custom object](#salesforce-field-mappings-co "#salesforce-field-mappings-co")

## Account

Amazon Q supports crawling [Salesforce Online Accounts](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_account.htm") and offers the following account field
mappings.

| Salesforce field name  | Index field name            | Description | Data type      |
| ---------------------- | --------------------------- | ----------- | -------------- |
| category               | \_category                  | Default     | String         |
| sourceUrl              | \_source_uri                | Default     | String         |
| createdAt              | \_created_at                | Default     | Date           |
| updatedAt              | \_last_updated_at           | Default     | Date           |
| authors                | \_authors                   | Default     | String list    |
| lastModifiedBy         | sf_last_modified_by         | Custom      | String         |
| shippingCity           | sf_shipping_city            | Custom      | String         |
| shippingCountry        | sf_shipping_country         | Custom      | String         |
| shippingState          | sf_shipping_state           | Custom      | String         |
| website                | sf_website                  | Custom      | String         |
| industry               | sf_industry                 | Custom      | String         |
| accountSource          | sf_account_source           | Custom      | String         |
| billingCity            | sf_billing_city             | Custom      | String         |
| billingCountry         | sf_billing_country          | Custom      | String         |
| billingState           | sf_billing_state            | Custom      | String         |
| createdBy              | sf_created_by               | Custom      | String         |
| lastActivityDate       | sf_last_activity_date       | Custom      | Date           |
| parentId               | sf_parent_id                | Custom      | String         |
| typeValue              | sf_type_value               | Custom      | String         |
| billingStreet          | sf_billing_street           | Custom      | String         |
| billingPostalCode      | sf_billing_postal_code      | Custom      | String         |
| billingLatitude        | sf_billing_latitude         | Custom      | String         |
| billingLongitude       | sf_billing_longitude        | Custom      | String         |
| billingGeocodeAccuracy | sf_billing_geocode_accuracy | Custom      | String         |
| shippingStreet         | sf_shipping_street          | Custom      | String         |
| shippingPostalCode     | sf_shipping_postal_code     | Custom      | String         |
| phone                  | sf_phone                    | Custom      | String         |
| fax                    | sf_fax                      | Custom      | String         |
| annualRevenue          | sf_annual_revenue           | Custom      | String         |
| numberOfEmployees      | sf_number_of_employees      | Custom      | Long (numeric) |
| jigsaw                 | sf_jigsaw                   | Custom      | String         |

## Campaign

Amazon Q supports crawling [Salesforce Online Campaigns](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_campaign.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_campaign.htm") and offers the following campaign field
mappings.

| Salesforce field name    | Index field name               | Description | Data type      |
| ------------------------ | ------------------------------ | ----------- | -------------- |
| category                 | \_category                     | Default     | String         |
| sourceUrl                | \_source_uri                   | Default     | String         |
| createdAt                | \_created_at                   | Default     | Date           |
| isActive                 | sf_is_active                   | Custom      | String         |
| updatedAt                | \_last_updated_at              | Default     | Date           |
| ownerName                | \_authors                      | Default     | String list    |
| lastModifiedBy           | sf_last_modified_by            | Custom      | String         |
| createdBy                | sf_created_by                  | Custom      | String         |
| lastActivityDate         | sf_last_activity_date          | Custom      | Date           |
| parentId                 | sf_parent_id                   | Custom      | String         |
| campaignName             | sf_campaign_name               | Custom      | String         |
| status                   | sf_status                      | Custom      | String         |
| parentName               | sf_parent_name                 | Custom      | String         |
| campaignType             | sf_type                        | Custom      | String         |
| expectedRevenue          | sf_expected_revenue            | Custom      | Long (numeric) |
| budgetedCost             | sf_budgeted_cost               | Custom      | Long (numeric) |
| actualCost               | sf_actual_cost                 | Custom      | Long(numeric)  |
| expectedResponse         | sf_expected_response           | Custom      | String         |
| numberSent               | sf_number_sent                 | Default     | Long numeric)  |
| numberOfLeads            | sf_number_of_leads             | Custom      | Long (numeric) |
| numberOfConvertedLeads   | sf_number_of_convererted_leads | Custom      | Long (numeric) |
| numberOfContacts         | sf_number_of_contacts          | Custom      | Long (numeric) |
| numberOfResponses        | sf_number_of_responses         | Custom      | Long (numeric) |
| numberOfOpportunites     | sf_number_of_opportunities     | Custom      | Long (numeric) |
| numberOfWonOpportunities | sf_number_of_won_opportunitues | Custom      | Long (numeric) |
| amountAllOpportunities   | sf_amount_all_opportunities    | Custom      | Long (numeric) |
| amountWonOpportunities   | sf_amount_won_opportunities    | Custom      | Long (numeric) |

## Case

Amazon Q supports crawling [Salesforce Online Cases](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_case.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_case.htm") and offers the following case field
mappings.

| Salesforce field name | Index field name      | Description | Data type   |
| --------------------- | --------------------- | ----------- | ----------- |
| category              | \_category            | Default     | String      |
| sourceUrl             | \_source_uri          | Default     | String      |
| authors               | \_authors             | Default     | String list |
| createdAt             | \_created_at          | Default     | Date        |
| updatedAt             | \_last_updated_at     | Default     | Date        |
| ownerName             | sf_owner_name         | Custom      | String      |
| createdBy             | sf_created_by         | Custom      | String      |
| caseNumber            | sf_case_number        | Custom      | String      |
| isClosed              | sf_is_closed          | Custom      | String      |
| isEscalated           | sf_is_escalated       | Custom      | String      |
| priority              | sf_priority           | Custom      | String      |
| status                | sf_status             | Custom      | String      |
| accountName           | sf_account_name       | Custom      | String      |
| lastModifiedBy        | af_last_modified_by   | Custom      | String      |
| updatedAt             | \_last_updated_at     | Default     | Date        |
| typeValue             | sf_type               | Custom      | String      |
| reason                | sf_reason             | Custom      | String      |
| contactId             | sf_contact_id         | Custom      | String      |
| origin                | sf_origin             | Custom      | String      |
| parentId              | sf_parent_id          | Custom      | String      |
| contactName           | sf_contact_name       | Custom      | String      |
| parentCaseNumber      | sf_parent_case_number | Custom      | String      |
| parentSubject         | sf_parent_subject     | Custom      | String      |
| suppliedEmail         | sf_supplied_email     | Custom      | String      |
| contactPhone          | sf_contact_phone      | Custom      | String      |
| contactMobile         | sf_contact_mobile     | Custom      | String      |
| contactEmail          | sf_contact_email      | Custom      | String      |
| contactFax            | sf_contact_fax        | Custom      | String      |
| comments              | sf_comments           | Custom      | String      |
| lastViewedDate        | sf_last_viewed_date   | Custom      | String      |

## Contact

Amazon Q supports crawling [Salesforce Online Contacts](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm") and offers the following contact field
mappings.

| Salesforce field name  | Index field name            | Description | Data type   |
| ---------------------- | --------------------------- | ----------- | ----------- |
| category               | \_category                  | Default     | String      |
| sourceUrl              | \_source_uri                | Default     | String      |
| authors                | \_authors                   | Default     | String list |
| createdAt              | \_created_at                | Default     | Date        |
| updatedAt              | \_last_updated_at           | Default     | Date        |
| lastModifiedBy         | sf_last_modified_by         | Custom      | String      |
| lastActivityDate       | sf_last_activity_date       | Custom      | Date        |
| createdBy              | sf_created_by               | Custom      | String      |
| contactName            | sf_contact_name             | Custom      | String      |
| phone                  | sf_phone                    | Custom      | String      |
| email                  | sf_email                    | Custom      | String      |
| department             | sf_department               | Custom      | String      |
| lastname               | sf_lastname                 | Custom      | String      |
| title                  | sf_title                    | Custom      | String      |
| reportsTo              | sf_reports_to               | Custom      | String      |
| account                | sf_account                  | Custom      | String      |
| otherStreet            | sf_other_street             | Custom      | String      |
| otherCity              | sf_other_city               | Custom      | String      |
| otherState             | sf_other_state              | Custom      | String      |
| otherPostalCode        | sf_other_postal_code        | Custom      | String      |
| otherCountry           | sf_other_country            | Custom      | String      |
| otherLatitude          | sf_other_latitude           | Custom      | String      |
| otherLongitude         | sf_other_longitude          | Custom      | String      |
| otherGeocodeAccuracy   | sf_other_geocode_accuracy   | Custom      | String      |
| mailingStreet          | sf_mailing_street           | Custom      | String      |
| mailingCity            | sf_mailing_city             | Custom      | String      |
| mailingState           | sf_mailing_state            | Custom      | String      |
| mailingPostalCode      | sf_mailing_postal_code      | Custom      | String      |
| mailingCountry         | sf_mailing_country          | Custom      | String      |
| mailingLatitude        | sf_mailing_latitude         | Custom      | String      |
| mailingLongitude       | sf_mailing_longitude        | Custom      | String      |
| mailingGeocodeAccuracy | sf_mailing_geocode_accuracy | Custom      | String      |
| fax                    | sf_fax                      | Custom      | String      |
| mobilePhone            | sf_mobile_phone             | Custom      | String      |
| homePhone              | sf_home_phone               | Custom      | String      |
| otherPhone             | sf_other_phone              | Custom      | String      |
| assistantPhone         | sf_assistant_phone          | Custom      | String      |
| assistantName          | sf_assistant_name           | Custom      | String      |
| leadSource             | sf_lead_source              | Custom      | String      |
| birthDate              | sf_birthdate                | Custom      | Date        |
| jigsaw                 | sf_jigsaw                   | Custom      | String      |

## Contract

Amazon Q supports crawling [Salesforce Online Contracts](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contract.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contract.htm") and offers the following contract field
mappings.

| Salesforce field name    | Index field name               | Description | Data type   |
| ------------------------ | ------------------------------ | ----------- | ----------- |
| category                 | \_category                     | Default     | String      |
| sourceUrl                | \_source_uri                   | Default     | String      |
| authors                  | \_authors                      | Default     | String list |
| createdAt                | \_created_at                   | Default     | Date        |
| updatedAt                | \_last_updated_at              | Default     | Date        |
| authors                  | \_authors                      | Default     | String list |
| accountId                | \_sf_accoung_id                | Custom      | String      |
| ownerExpirationNotice    | sf_owner_expiration_notice     | Custom      | String      |
| billingStreet            | sf_billing_street              | Custom      | String      |
| billingCity              | sf_billing_city                | Custom      | String      |
| billingState             | sf_billing_state               | Custom      | String      |
| billingPostalCode        | sf_billing_postal_code         | Custom      | String      |
| billingCountry           | sf_billing_country             | Custom      | String      |
| contractTerm             | sf_contract_term               | Custom      | String      |
| ownerId                  | sf_owner_id                    | Custom      | String      |
| status                   | sf_status                      | Custom      | String      |
| customerSignedTitle      | sf_customer_signed_title       | Custom      | String      |
| specialTerms             | sf_special_terms               | Custom      | String      |
| statusCode               | sf_status_code                 | Custom      | String      |
| contractNumber           | sf_contract_number             | Custom      | String      |
| lastViewedDate           | sf_last_viewed_date            | Custom      | Date        |
| lastReferenceDate        | sf_last_reference_date         | Custom      | Date        |
| billingAddressCity       | sf_billing_address_city        | Custom      | String      |
| billingAddressCountry    | sf_billing_address_country     | Custom      | String      |
| billingAddressPostalCode | sf_billing_address_postal_code | Custom      | String      |
| billingAddressState      | sf_billing_address_state       | Custom      | String      |
| billingAddressStreet     | sf_billing_address_street      | Custom      | String      |
| pricebookDescription     | sf_pricebook_description       | Custom      | String      |
| pricebookId              | sf_pricebook_id                | Custom      | String      |
| billingLatitude          | sf_billing_latitude            | Custom      | String      |
| billingLongitude         | sf_billing_longitude           | Custom      | String      |
| billingGeocodeAccuracy   | sf_billing_geocode_accuracy    | Custom      | String      |
| companySignedId          | sf_company_signed_id           | Custom      | String      |
| companySignedDate        | sf_company_signed_date         | Custom      | Date        |
| customerSignedId         | sf_customer_signed_id          | Custom      | String      |
| activatedById            | sf_activated_by_id             | Custom      | String      |
| activatedDate            | sf_activated_date              | Custom      | Date        |
| lastApprovedDate         | sf_last_approved_date          | Custom      | Date        |
| lastActivityDate         | sf_last_activity_date          | Custom      | Date        |
| accountName              | sf_account_name                | Custom      | String      |
| startDate                | sf_start_date                  | Custom      | Date        |
| endDate                  | sf_end_date                    | Custom      | Date        |
| createdBy                | sf_created_by                  | Custom      | String      |

## Document

Amazon Q supports crawling [Salesforce Online Documents](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_document.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_document.htm") and offers the following document field
mappings.

| Salesforce field name | Index field name        | Description | Data type      |
| --------------------- | ----------------------- | ----------- | -------------- |
| category              | \_category              | Default     | String         |
| sourceUrl             | \_source_uri            | Default     | String         |
| author                | \_authors               | Default     | String list    |
| createdAt             | \_created_at            | Default     | Date           |
| folder                | sf_folder_name          | Custom      | String         |
| isInternalUseOnly     | sf_is_internal_use_only | Custom      | String         |
| isPublic              | sf_is_public            | Custom      | String         |
| keywords              | sf_keywords             | Custom      | String         |
| lastModifiedBy        | sf_last_modified_by     | Custom      | String         |
| updatedAt             | \_last_updated_at       | Default     | Date           |
| fileName              | sf_file_name            | Custom      | String         |
| fileType              | \_file_type             | Default     | String         |
| fileSize              | sf_file_size            | Custom      | Long (numeric) |
| createdBy             | sf_created_by           | Custom      | String         |
| isBodySearchable      | sf_is_body_searchable   | Custom      | String         |

## Group

Amazon Q supports crawling [Salesforce Online Groups](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm") and offers the following group field
mappings.

| Salesforce field name  | Index field name             | Description | Data type   |
| ---------------------- | ---------------------------- | ----------- | ----------- |
| category               | \_category                   | Default     | String      |
| sourceUrl              | \_source_uri                 | Default     | String      |
| createdAt              | \_created_at                 | Default     | Date        |
| groupEmail             | sf_group_email               | Custom      | String      |
| lastModifiedBy         | sf_last_modified_by          | Custom      | String      |
| lastModifiedDate       | \_last_modified_at           | Default     | Date        |
| ownerId                | sf_owner_id                  | Custom      | String      |
| groupName              | sf_group_name                | Custom      | String      |
| createdBy              | \_authors                    | Default     | String list |
| lastFeedModifiedDate   | sf_last_feed_modified_date   | Custom      | Date        |
| hasPrivateFieldsAccess | sf_has_private_fields_access | Custom      | String      |
| canHaveGuests          | sf_can_have_guests           | Custom      | String      |
| isArchived             | sf_is_archived               | Custom      | String      |
| isAutoArchived         | sf_is_auto_archive_disabled  | Custom      | String      |
| memberCount            | sf_member_count              | Custom      | String      |
| collaborationType      | sf_collabotration_type       | Custom      | String      |
| informationTitle       | sf_information_title         | Custom      | String      |

## Idea

Amazon Q supports crawling [Salesforce Online Ideas](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_idea.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_idea.htm") and offers the following idea field
mappings.

| Salesforce field name | Index field name      | Description | Data type      |
| --------------------- | --------------------- | ----------- | -------------- |
| category              | \_category            | Default     | String         |
| sourceUrl             | \_source_uri          | Default     | String         |
| createdAt             | \_created_at          | Default     | Date           |
| lastModifiedBy        | sf_last_modified_by   | Custom      | String         |
| title                 | sf_title              | Custom      | String         |
| status                | sf_status             | Custom      | String         |
| createdByName         | sf_created_by         | Custom      | String         |
| parentIdea            | sf_parent_idea_id     | Custom      | String         |
| parentIdeaId          | sf_parent_idea_id     | Custom      | String         |
| lastModifiedDate      | \_last_modified_at    | Default     | Date           |
| recordTypeId          | sf_record_type_id     | Custom      | String         |
| communityId           | sf_community_id       | Custom      | String         |
| numComments           | sf_number_of_comments | Custom      | Long (numeric) |
| voteScore             | sf_vote_score         | Custom      | Long (numeric) |
| voteTotal             | sf_vote_total         | Custom      | Long (numeric) |
| lastCommentDate       | sf_last_comment_date  | Custom      | Date           |

## Lead

Amazon Q supports crawling [Salesforce Online Leads](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm") and offers the following lead field
mappings.

| Salesforce field name  | Index field name            | Description | Data type      |
| ---------------------- | --------------------------- | ----------- | -------------- |
| category               | \_category                  | Default     | String         |
| sourceUrl              | \_source_uri                | Default     | String         |
| city                   | sf_city                     | Custom      | String         |
| company                | sf_company                  | Custom      | String         |
| country                | sf_country                  | Custom      | String         |
| createdAt              | \_created_at                | Default     | Date           |
| lastModifiedBy         | sf_last_modified_by         | Custom      | String         |
| updatedAt              | \_last_updated_at           | Default     | Date           |
| leadSource             | sf_lead_source              | Custom      | String         |
| state                  | sf_state                    | Custom      | String         |
| status                 | sf_status                   | Custom      | String         |
| convertedAccount       | sf_converted_account        | Custom      | String         |
| convertedAccountId     | sf_converted_account_id     | Custom      | String         |
| convertedContact       | sf_converted_contact        | Custom      | String         |
| convertedContactId     | sf_converted_contact_id     | Custom      | String         |
| convertedDate          | sf_converted_date           | Custom      | Date           |
| convertedOpportunity   | sf_converted_opportunity    | Custom      | String         |
| convertedOpportunityId | sf_converted_opportunity_id | Custom      | String         |
| firstName              | sf_first_name               | Custom      | String         |
| createdBy              | \_authors                   | Default     | String list    |
| isConverted            | sf_is_converted             | Custom      | String         |
| owner                  | sf_owner_name               | Custom      | String         |
| lastActivityDate       | sf_last_activity_date       | Custom      | Date           |
| ownerId                | sf_owner_id                 | Custom      | String         |
| lastName               | sf_last_name                | Custom      | String         |
| title                  | sf_title                    | Custom      | String         |
| street                 | sf_street                   | Custom      | String         |
| postalCode             | sf_postal_code              | Custom      | String         |
| latitude               | sf_latitude                 | Custom      | String         |
| longitude              | sf_longitude                | Custom      | String         |
| geocodeAccuracy        | sf_geocode_accuracy         | Custom      | String         |
| phone                  | sf_phone                    | Custom      | String         |
| email                  | sf_email                    | Custom      | String         |
| industry               | sf_industry                 | Custom      | String         |
| rating                 | sf_rating                   | Custom      | String         |
| annualRevenue          | sf_annual_revenue           | Custom      | String         |
| numberofEmployees      | sf_number_of_employees      | Custom      | Long (numeric) |
| jigsaw                 | sf_jigsaw                   | Custom      | String         |
| jigsawContactId        | sf_jigsaw_contact_id        | Custom      | String         |
| emailBouncedReason     | sf_email_bounced_reason     | Custom      | String         |
| individualId           | sf_individual_id            | Custom      | String         |

## Opportunity

Amazon Q supports crawling [Salesforce Online Opportunities](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm") and offers the following opportunity field
mappings.

| Salesforce field name  | Index field name             | Description | Data type      |
| ---------------------- | ---------------------------- | ----------- | -------------- |
| category               | \_category                   | Default     | String         |
| sourceUrl              | \_source_uri                 | Default     | String         |
| accountName            | sf_account_name              | Custom      | String         |
| amount                 | sf_amount                    | Custom      | String         |
| campaign               | sf_campaign_name             | Custom      | String         |
| createdAt              | \_created_at                 | Default     | Date           |
| createdBy              | sf_created_by                | Custom      | String         |
| lastModifiedBy         | sf_last_modified_by          | Custom      | String         |
| lastModifiedDate       | \_last_updated_at            | Default     | Date           |
| fiscalQuarter          | sf_fiscal_quarter            | Custom      | String         |
| fiscalYear             | sf_fiscal_year               | Custom      | String         |
| isClosed               | sf_is_closed                 | Custom      | String         |
| isWon                  | sf_is_won                    | Custom      | String         |
| leadSource             | sf_lead_source               | Custom      | String         |
| opportunityName        | sf_opportunity_name          | Custom      | String         |
| accountId              | sf_account_id                | Custom      | String         |
| campaignId             | sf_campaign_id               | Custom      | String         |
| closeDate              | sf_close_date                | Custom      | Date           |
| typeValue              | sf_type_value                | Custom      | String         |
| lastActivityDate       | sf_last_activity_date        | Date        | String         |
| ownerName              | sf_owner_name                | Custom      | String         |
| ownerId                | sf_owner_id                  | Custom      | String         |
| stageName              | sf_stage_name                | Custom      | String         |
| probability            | sf_probability               | Custom      | Long (numeric) |
| nextStep               | sf_next_step                 | Custom      | String         |
| forestCategory         | sf_forecast_category         | Custom      | String         |
| forestCategoryName     | sf_forest_category_name      | Custom      | String         |
| hasOpportunityLineItem | sf_has_opportunity_line_item | Custom      | String         |
| pricebook2id           | sf_pricebook2_id             | Custom      | String         |
| pushCount              | sf_push_count                | Custom      | String         |
| fiscal                 | sf_fiscal                    | Custom      | String         |
| contactId              | sf_contact_id                | Custom      | String         |
| lastViewedDate         | sf_last_viewed_date          | Custom      | Date           |
| hasOpenActivity        | sf_has_open_activity         | Custom      | Long (numeric) |
| hasOverdueTask         | sf_has_overdue_task          | Custom      | String         |

## Partner

Amazon Q supports crawling [Salesforce Online Partner](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_partner.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_partner.htm") and offers the following partner field
mappings.

| Salesforce field name | Index field name      | Description | Data type   |
| --------------------- | --------------------- | ----------- | ----------- |
| category              | \_category            | Default     | String      |
| sourceUrl             | \_source_uri          | Default     | String      |
| createdAt             | \_created_at          | Default     | Date        |
| updatedAt             | \_last_updated_at     | Default     | Date        |
| createdBy             | \_authors             | Default     | String list |
| opportunityId         | sf_opportunity_id     | Custom      | String      |
| accountFromId         | sf_account_from_id    | Custom      | String      |
| accountToId           | sf_role               | Custom      | String      |
| role                  | sf_role               | Custom      | String      |
| isPrimary             | sf_is_primary         | Custom      | String      |
| systemModstamp        | sf_system_modstamp    | Custom      | Date        |
| reversePartnerId      | sf_reverse_partner_id | Custom      | String      |
| opportunity           | sf_opportunity        | Custom      | String      |
| accountFrom           | sf_account_from       | Custom      | String      |
| accountTo             | sf_account_to         | Custom      | String      |

## Pricebook

Amazon Q supports crawling [Salesforce Online Pricebooks](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebook2.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebook2.htm") and offers the following pricebook field
mappings.

| Salesforce field name | Index field name    | Description | Data type   |
| --------------------- | ------------------- | ----------- | ----------- |
| category              | \_category          | Default     | String      |
| sourceUrl             | \_source_uri        | Default     | String      |
| isActive              | sf_is_active        | Custom      | String      |
| lastModifiedBy        | sf_last_modified_by | Default     | String      |
| lastModifiedDate      | \_last_updated_at   | Default     | Date        |
| pricebookName         | sf_pricebook_name   | Custom      | String      |
| createdAt             | \_created_at        | Default     | Date        |
| createdBy             | \_authors           | Default     | String list |
| lastViewedDate        | sf_last_viewed_date | Custom      | Date        |
| isStandard            | sf_is_standard      | Custom      | String      |

## Product

Amazon Q supports crawling [Salesforce Online Product](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_product2.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_product2.htm") and offers the following product field
mappings.

| Salesforce field name | Index field name            | Description | Data type   |
| --------------------- | --------------------------- | ----------- | ----------- |
| category              | \_category                  | Default     | String      |
| sourceUrl             | \_source_uri                | Default     | String      |
| family                | sf_family                   | Custom      | String      |
| isActive              | sf_is_active                | Custom      | String      |
| createdAt             | \_created_at                | Default     | Date        |
| updatedAt             | \_last_updated_at           | Default     | Date        |
| lastModifiedBy        | sf_last_modified_by         | Custom      | String      |
| productCode           | sf_product_code             | Custom      | String      |
| createdBy             | \_authors                   | Default     | String list |
| productName           | sf_product_name             | Custom      | String      |
| externalDataSourceId  | sf_external_datasource_id   | Custom      | String      |
| externalId            | sf_external_id              | Custom      | String      |
| displayUrl            | sf_display_url              | Custom      | String      |
| quantityUnitOfMeasure | sf_quantity_unit_of_measure | Custom      | String      |
| isArchived            | sf_is_archived              | Custom      | String      |
| lastViewedDate        | sf_last_viewed_date         | Custom      | Date        |
| stockKeepingUnit      | sf_stock_keeping_unit       | Custom      | String      |

## Solution

Amazon Q supports crawling [Salesforce Online Solutions](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_solution.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_solution.htm") and offers the following solution field
mappings.

| Salesforce field name | Index field name    | Description | Data type   |
| --------------------- | ------------------- | ----------- | ----------- |
| category              | \_category          | Default     | String      |
| sourceUrl             | \_source_uri        | Default     | String      |
| isPublished           | sf_is_published     | Custom      | String      |
| isReviewed            | sf_is_reviewed      | Custom      | String      |
| lastModifiedBy        | sf_last_modified_by | Custom      | String      |
| lastModifiedDate      | \_last_updated_at   | Default     | Date        |
| ownerName             | sf_owner_name       | Custom      | String      |
| solutionNumber        | sf_solution_number  | Custom      | String      |
| status                | sf_status           | Custom      | String      |
| timesUsed             | sf_times_used       | Custom      | String      |
| solutionName          | sf_solution_name    | Custom      | String      |
| createdByName         | \_authors           | Default     | String list |
| createdAt             | \_created_at        | Default     | Date        |
| solutionNote          | sf_solution_note    | Custom      | String      |
| ownderId              | sf_ownderId         | Custom      | String      |
| lastViewedDate        | sf_last_viewed_date | Custom      | Date        |

## Profile

Amazon Q supports crawling [Salesforce Online Profiles](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm") and offers the following profile field
mappings.

| Salesforce field name | Index field name    | Description | Data type   |
| --------------------- | ------------------- | ----------- | ----------- |
| category              | \_category          | Default     | String      |
| sourceUrl             | \_source_uri        | Default     | String      |
| updatedAt             | \_last_updated_at   | Default     | Date        |
| lastModifiedBy        | sf_last_modified_by | Custom      | String      |
| createdBy             | \_authors           | Default     | String list |
| createdAt             | \_created_at        | Default     | Date        |
| userType              | sf_user_type        | Custom      | String      |

## Task

Amazon Q supports crawling [Salesforce Online Tasks](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_task.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_task.htm") and offers the following task field
mappings.

| Salesforce field name | Index field name    | Description | Data type   |
| --------------------- | ------------------- | ----------- | ----------- |
| category              | \_category          | Default     | String      |
| sourceUrl             | \_source_uri        | Default     | String      |
| accountName           | sf_account_name     | Custom      | String      |
| lastModifiedBy        | sf_last_modified_by | Custom      | String      |
| lastModifiedDate      | \_last_updated_at   | Default     | Date        |
| ownerName             | sf_owner_name       | Custom      | String      |
| isRecurrence          | sf_is_recurrence    | Custom      | String      |
| isClosed              | sf_is_closed        | Custom      | String      |
| isArchived            | sf_is_archived      | Custom      | String      |
| priority              | sf_priority         | Custom      | String      |
| status                | sf_status           | Custom      | String      |
| whatId                | sf_what_id          | Custom      | String      |
| createdByName         | \_authors           | Default     | String list |
| createdAt             | \_created_at        | Default     | Date        |
| subject               | sf_subject          | Custom      | String      |
| activityDate          | sf_activity_date    | Custom      | Date        |
| activityDate          | sf_activity_date    | Custom      | Date        |
| isHighPriority        | sf_is_high_priority | Custom      | String      |
| ownerId               | sf_owner_id         | Custom      | String      |
| callType              | sf_call_type        | Custom      | String      |

## User

Amazon Q supports crawling [Salesforce Online Users](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm") and offers the following user field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source_uri           | Default     | String      |
| account               | sf_account             | Custom      | String      |
| isActive              | sf_is_active           | Custom      | String      |
| city                  | sf_city                | Custom      | String      |
| lastModifiedBy        | sf_last_modified_by    | Custom      | String      |
| updatedAt             | \_last_updated_at      | Default     | Date        |
| companyName           | sf_company_name        | Custom      | String      |
| country               | sf_country             | Custom      | String      |
| department            | sf_department          | Custom      | String      |
| division              | sf_division            | Custom      | String      |
| email                 | sf_email               | Custom      | String      |
| employeeNumber        | sf_employee_number     | Custom      | String      |
| firstName             | sf_first_name          | Custom      | String      |
| lastName              | sf_last_name           | Custom      | String      |
| manager               | sf_manager             | Custom      | String      |
| state                 | sf_state               | Custom      | String      |
| userRole              | sf_user_role           | Custom      | String      |
| username              | sf_username            | Custom      | String      |
| createdBy             | \_authors              | Default     | String list |
| createdAt             | \_created_at           | Default     | Date        |
| street                | sf_street              | Custom      | String      |
| postalCode            | sf_postal_code         | Custom      | String      |
| latitude              | sf_latitiude           | Custom      | String      |
| longitude             | sf_longitude           | Custom      | String      |
| geocodeAccuracy       | sf_geocode_accuracy    | Custom      | String      |
| phone                 | sf_phone               | Custom      | String      |
| fax                   | sf_fax                 | Custom      | String      |
| mobilePhone           | sf_mobile_phone        | Custom      | String      |
| profileName           | sf_profile_name        | Custom      | String      |
| aboutMe               | sf_about_me            | Custom      | String      |
| languageLocaleKey     | sf_language_locale_key | Custom      | String      |

## Chatter

Amazon Q supports crawling [Salesforce Online Chatters](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_chatteractivity.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_chatteractivity.htm") and offers the following chatter field
mappings.

| Salesforce field name | Index field name   | Description | Data type   |
| --------------------- | ------------------ | ----------- | ----------- |
| category              | \_category         | Default     | String      |
| sourceUrl             | \_source_uri       | Default     | String      |
| body                  | sf_body            | Custom      | String      |
| createdAt             | \_created_at       | Default     | Date        |
| lastEditById          | sf_last_edit_by_id | Custom      | String      |
| lastEditDate          | sf_last_edit_date  | Custom      | Date        |
| lastModifiedDate      | \_last_updated_at  | Default     | Date        |
| insertedById          | sf_inserted_by_id  | Custom      | String      |
| createdBy             | \_authors          | Default     | String list |
| parentId              | sf_parent_id       | Custom      | String      |
| revision              | sf_revision        | Custom      | String      |
| status                | sf_status          | Custom      | String      |
| isRichText            | sf_is_rich_texrt   | Custom      | String      |

## Knowledge articles

Amazon Q supports crawling [Salesforce Online Knowledge articles](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_knowledgearticle.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_knowledgearticle.htm") and offers the following knowledge
article field mappings.

| Salesforce field name        | Index field name             | Description | Data type      |
| ---------------------------- | ---------------------------- | ----------- | -------------- |
| category                     | \_category                   | Default     | String         |
| sourceUrl                    | \_source_uri                 | Default     | String         |
| articleTitle                 | sf_title                     | Custom      | String         |
| articleNumber                | sf_article_number            | Default     | Date           |
| knowledgeArticleId           | sf_knowledge_article_id      | Custom      | String         |
| lastPublishedDate            | sf_last_published_date       | Custom      | Date           |
| publishStatus                | sf_publish_status            | Custom      | String         |
| versionNumber                | sf_version_number            | Custom      | String         |
| language                     | sf_language                  | Custom      | String         |
| ownerId                      | sf_ownder_id                 | Custom      | String         |
| summary                      | sf_summary                   | Custom      | String         |
| firstPublishedDate           | sf_first_published_date      | Custom      | Date           |
| updatedAt                    | \_last_updated_at            | Default     | Date           |
| archivedDate                 | sf_archived_date             | Custom      | Date           |
| isLatestVersion              | sf_is_latest_version         | Custom      | String         |
| sourceId                     | sf_sourceId                  | Custom      | String         |
| createdBy                    | \_authors                    | Default     | String list    |
| assignmentDate               | sf_assignment_date           | Custom      | Long (numeric) |
| assignmentDueDate            | sf_assignment_due_date       | Custom      | Date           |
| articleCaseAttachCount       | sf_article_case_attach_count | Custom      | Long (numeric) |
| articleTotalViewCount        | sf_article_total_view_count  | Custom      | Long (numeric) |
| urlName                      | sf_url_name                  | Custom      | String         |
| assignmentNote               | sf_assignment_date           | Custom      | String         |
| migratedToFromArticleVersion | sf_migrated_article_version  | Custom      | String         |
| assignedBy                   | sf_assigned_by               | Custom      | String         |
| assignedTo                   | sf_assigned_to               | Custom      | Date           |

## Attachments

Amazon Q supports crawling [Salesforce Online Attachments](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_attachment.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_attachment.htm") and offers the following attachment field
mappings.

| Salesforce field name | Index field name  | Description | Data type      |
| --------------------- | ----------------- | ----------- | -------------- |
| category              | \_category        | Default     | String         |
| sourceUrl             | \_source_uri      | Default     | String         |
| createdAt             | \_created_at      | Default     | Date           |
| updatedAt             | \_last_updated_at | Default     | Date           |
| fileName              | sf_file_name      | Custom      | String         |
| fileType              | \_file_type       | Default     | String         |
| fileSize              | sf_file_size      | Custom      | Long (numeric) |
| parentName            | sf_parent_name    | Default     | String         |
| createdBy             | \_authors         | Default     | String list    |

## Custom object

Amazon Q supports crawling custom objects and offers the following custom
object field mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source_uri           | Default     | String      |
| createdAt             | \_created_at           | Default     | Date        |
| updatedAt             | \_last_updated_at      | Default     | Date        |
| lastModifiedById      | sf_last_modified_by_id | Custom      | String      |
| customObjectName      | sf_custom_object_name  | Custom      | String      |
| createdBy             | \_authors              | Default     | String list |
| lastModifiedBy        | sf_last_modified_by    | Custom      | String      |
| documentbody          | \_document_body        | Custom      | String      |
