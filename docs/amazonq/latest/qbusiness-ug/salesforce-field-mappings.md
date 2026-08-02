Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Salesforce Online data source connector field mappings

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

| Salesforce field name  | Index field name               | Description | Data type      |
| ---------------------- | ------------------------------ | ----------- | -------------- |
| category               | \_category                     | Default     | String         |
| sourceUrl              | \_source\_uri                  | Default     | String         |
| createdAt              | \_created\_at                  | Default     | Date           |
| updatedAt              | \_last\_updated\_at            | Default     | Date           |
| authors                | \_authors                      | Default     | String list    |
| lastModifiedBy         | sf\_last\_modified\_by         | Custom      | String         |
| shippingCity           | sf\_shipping\_city             | Custom      | String         |
| shippingCountry        | sf\_shipping\_country          | Custom      | String         |
| shippingState          | sf\_shipping\_state            | Custom      | String         |
| website                | sf\_website                    | Custom      | String         |
| industry               | sf\_industry                   | Custom      | String         |
| accountSource          | sf\_account\_source            | Custom      | String         |
| billingCity            | sf\_billing\_city              | Custom      | String         |
| billingCountry         | sf\_billing\_country           | Custom      | String         |
| billingState           | sf\_billing\_state             | Custom      | String         |
| createdBy              | sf\_created\_by                | Custom      | String         |
| lastActivityDate       | sf\_last\_activity\_date       | Custom      | Date           |
| parentId               | sf\_parent\_id                 | Custom      | String         |
| typeValue              | sf\_type\_value                | Custom      | String         |
| billingStreet          | sf\_billing\_street            | Custom      | String         |
| billingPostalCode      | sf\_billing\_postal\_code      | Custom      | String         |
| billingLatitude        | sf\_billing\_latitude          | Custom      | String         |
| billingLongitude       | sf\_billing\_longitude         | Custom      | String         |
| billingGeocodeAccuracy | sf\_billing\_geocode\_accuracy | Custom      | String         |
| shippingStreet         | sf\_shipping\_street           | Custom      | String         |
| shippingPostalCode     | sf\_shipping\_postal\_code     | Custom      | String         |
| phone                  | sf\_phone                      | Custom      | String         |
| fax                    | sf\_fax                        | Custom      | String         |
| annualRevenue          | sf\_annual\_revenue            | Custom      | String         |
| numberOfEmployees      | sf\_number\_of\_employees      | Custom      | Long (numeric) |
| jigsaw                 | sf\_jigsaw                     | Custom      | String         |

## Campaign

Amazon Q supports crawling [Salesforce Online Campaigns](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_campaign.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_campaign.htm") and offers the following campaign field
mappings.

| Salesforce field name    | Index field name                   | Description | Data type      |
| ------------------------ | ---------------------------------- | ----------- | -------------- |
| category                 | \_category                         | Default     | String         |
| sourceUrl                | \_source\_uri                      | Default     | String         |
| createdAt                | \_created\_at                      | Default     | Date           |
| isActive                 | sf\_is\_active                     | Custom      | String         |
| updatedAt                | \_last\_updated\_at                | Default     | Date           |
| ownerName                | \_authors                          | Default     | String list    |
| lastModifiedBy           | sf\_last\_modified\_by             | Custom      | String         |
| createdBy                | sf\_created\_by                    | Custom      | String         |
| lastActivityDate         | sf\_last\_activity\_date           | Custom      | Date           |
| parentId                 | sf\_parent\_id                     | Custom      | String         |
| campaignName             | sf\_campaign\_name                 | Custom      | String         |
| status                   | sf\_status                         | Custom      | String         |
| parentName               | sf\_parent\_name                   | Custom      | String         |
| campaignType             | sf\_type                           | Custom      | String         |
| expectedRevenue          | sf\_expected\_revenue              | Custom      | Long (numeric) |
| budgetedCost             | sf\_budgeted\_cost                 | Custom      | Long (numeric) |
| actualCost               | sf\_actual\_cost                   | Custom      | Long(numeric)  |
| expectedResponse         | sf\_expected\_response             | Custom      | String         |
| numberSent               | sf\_number\_sent                   | Default     | Long numeric)  |
| numberOfLeads            | sf\_number\_of\_leads              | Custom      | Long (numeric) |
| numberOfConvertedLeads   | sf\_number\_of\_convererted\_leads | Custom      | Long (numeric) |
| numberOfContacts         | sf\_number\_of\_contacts           | Custom      | Long (numeric) |
| numberOfResponses        | sf\_number\_of\_responses          | Custom      | Long (numeric) |
| numberOfOpportunites     | sf\_number\_of\_opportunities      | Custom      | Long (numeric) |
| numberOfWonOpportunities | sf\_number\_of\_won\_opportunitues | Custom      | Long (numeric) |
| amountAllOpportunities   | sf\_amount\_all\_opportunities     | Custom      | Long (numeric) |
| amountWonOpportunities   | sf\_amount\_won\_opportunities     | Custom      | Long (numeric) |

## Case

Amazon Q supports crawling [Salesforce Online Cases](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_case.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_case.htm") and offers the following case field
mappings.

| Salesforce field name | Index field name         | Description | Data type   |
| --------------------- | ------------------------ | ----------- | ----------- |
| category              | \_category               | Default     | String      |
| sourceUrl             | \_source\_uri            | Default     | String      |
| authors               | \_authors                | Default     | String list |
| createdAt             | \_created\_at            | Default     | Date        |
| updatedAt             | \_last\_updated\_at      | Default     | Date        |
| ownerName             | sf\_owner\_name          | Custom      | String      |
| createdBy             | sf\_created\_by          | Custom      | String      |
| caseNumber            | sf\_case\_number         | Custom      | String      |
| isClosed              | sf\_is\_closed           | Custom      | String      |
| isEscalated           | sf\_is\_escalated        | Custom      | String      |
| priority              | sf\_priority             | Custom      | String      |
| status                | sf\_status               | Custom      | String      |
| accountName           | sf\_account\_name        | Custom      | String      |
| lastModifiedBy        | af\_last\_modified\_by   | Custom      | String      |
| updatedAt             | \_last\_updated\_at      | Default     | Date        |
| typeValue             | sf\_type                 | Custom      | String      |
| reason                | sf\_reason               | Custom      | String      |
| contactId             | sf\_contact\_id          | Custom      | String      |
| origin                | sf\_origin               | Custom      | String      |
| parentId              | sf\_parent\_id           | Custom      | String      |
| contactName           | sf\_contact\_name        | Custom      | String      |
| parentCaseNumber      | sf\_parent\_case\_number | Custom      | String      |
| parentSubject         | sf\_parent\_subject      | Custom      | String      |
| suppliedEmail         | sf\_supplied\_email      | Custom      | String      |
| contactPhone          | sf\_contact\_phone       | Custom      | String      |
| contactMobile         | sf\_contact\_mobile      | Custom      | String      |
| contactEmail          | sf\_contact\_email       | Custom      | String      |
| contactFax            | sf\_contact\_fax         | Custom      | String      |
| comments              | sf\_comments             | Custom      | String      |
| lastViewedDate        | sf\_last\_viewed\_date   | Custom      | String      |

## Contact

Amazon Q supports crawling [Salesforce Online Contacts](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contact.htm") and offers the following contact field
mappings.

| Salesforce field name  | Index field name               | Description | Data type   |
| ---------------------- | ------------------------------ | ----------- | ----------- |
| category               | \_category                     | Default     | String      |
| sourceUrl              | \_source\_uri                  | Default     | String      |
| authors                | \_authors                      | Default     | String list |
| createdAt              | \_created\_at                  | Default     | Date        |
| updatedAt              | \_last\_updated\_at            | Default     | Date        |
| lastModifiedBy         | sf\_last\_modified\_by         | Custom      | String      |
| lastActivityDate       | sf\_last\_activity\_date       | Custom      | Date        |
| createdBy              | sf\_created\_by                | Custom      | String      |
| contactName            | sf\_contact\_name              | Custom      | String      |
| phone                  | sf\_phone                      | Custom      | String      |
| email                  | sf\_email                      | Custom      | String      |
| department             | sf\_department                 | Custom      | String      |
| lastname               | sf\_lastname                   | Custom      | String      |
| title                  | sf\_title                      | Custom      | String      |
| reportsTo              | sf\_reports\_to                | Custom      | String      |
| account                | sf\_account                    | Custom      | String      |
| otherStreet            | sf\_other\_street              | Custom      | String      |
| otherCity              | sf\_other\_city                | Custom      | String      |
| otherState             | sf\_other\_state               | Custom      | String      |
| otherPostalCode        | sf\_other\_postal\_code        | Custom      | String      |
| otherCountry           | sf\_other\_country             | Custom      | String      |
| otherLatitude          | sf\_other\_latitude            | Custom      | String      |
| otherLongitude         | sf\_other\_longitude           | Custom      | String      |
| otherGeocodeAccuracy   | sf\_other\_geocode\_accuracy   | Custom      | String      |
| mailingStreet          | sf\_mailing\_street            | Custom      | String      |
| mailingCity            | sf\_mailing\_city              | Custom      | String      |
| mailingState           | sf\_mailing\_state             | Custom      | String      |
| mailingPostalCode      | sf\_mailing\_postal\_code      | Custom      | String      |
| mailingCountry         | sf\_mailing\_country           | Custom      | String      |
| mailingLatitude        | sf\_mailing\_latitude          | Custom      | String      |
| mailingLongitude       | sf\_mailing\_longitude         | Custom      | String      |
| mailingGeocodeAccuracy | sf\_mailing\_geocode\_accuracy | Custom      | String      |
| fax                    | sf\_fax                        | Custom      | String      |
| mobilePhone            | sf\_mobile\_phone              | Custom      | String      |
| homePhone              | sf\_home\_phone                | Custom      | String      |
| otherPhone             | sf\_other\_phone               | Custom      | String      |
| assistantPhone         | sf\_assistant\_phone           | Custom      | String      |
| assistantName          | sf\_assistant\_name            | Custom      | String      |
| leadSource             | sf\_lead\_source               | Custom      | String      |
| birthDate              | sf\_birthdate                  | Custom      | Date        |
| jigsaw                 | sf\_jigsaw                     | Custom      | String      |

## Contract

Amazon Q supports crawling [Salesforce Online Contracts](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contract.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_contract.htm") and offers the following contract field
mappings.

| Salesforce field name    | Index field name                   | Description | Data type   |
| ------------------------ | ---------------------------------- | ----------- | ----------- |
| category                 | \_category                         | Default     | String      |
| sourceUrl                | \_source\_uri                      | Default     | String      |
| authors                  | \_authors                          | Default     | String list |
| createdAt                | \_created\_at                      | Default     | Date        |
| updatedAt                | \_last\_updated\_at                | Default     | Date        |
| authors                  | \_authors                          | Default     | String list |
| accountId                | \_sf\_accoung\_id                  | Custom      | String      |
| ownerExpirationNotice    | sf\_owner\_expiration\_notice      | Custom      | String      |
| billingStreet            | sf\_billing\_street                | Custom      | String      |
| billingCity              | sf\_billing\_city                  | Custom      | String      |
| billingState             | sf\_billing\_state                 | Custom      | String      |
| billingPostalCode        | sf\_billing\_postal\_code          | Custom      | String      |
| billingCountry           | sf\_billing\_country               | Custom      | String      |
| contractTerm             | sf\_contract\_term                 | Custom      | String      |
| ownerId                  | sf\_owner\_id                      | Custom      | String      |
| status                   | sf\_status                         | Custom      | String      |
| customerSignedTitle      | sf\_customer\_signed\_title        | Custom      | String      |
| specialTerms             | sf\_special\_terms                 | Custom      | String      |
| statusCode               | sf\_status\_code                   | Custom      | String      |
| contractNumber           | sf\_contract\_number               | Custom      | String      |
| lastViewedDate           | sf\_last\_viewed\_date             | Custom      | Date        |
| lastReferenceDate        | sf\_last\_reference\_date          | Custom      | Date        |
| billingAddressCity       | sf\_billing\_address\_city         | Custom      | String      |
| billingAddressCountry    | sf\_billing\_address\_country      | Custom      | String      |
| billingAddressPostalCode | sf\_billing\_address\_postal\_code | Custom      | String      |
| billingAddressState      | sf\_billing\_address\_state        | Custom      | String      |
| billingAddressStreet     | sf\_billing\_address\_street       | Custom      | String      |
| pricebookDescription     | sf\_pricebook\_description         | Custom      | String      |
| pricebookId              | sf\_pricebook\_id                  | Custom      | String      |
| billingLatitude          | sf\_billing\_latitude              | Custom      | String      |
| billingLongitude         | sf\_billing\_longitude             | Custom      | String      |
| billingGeocodeAccuracy   | sf\_billing\_geocode\_accuracy     | Custom      | String      |
| companySignedId          | sf\_company\_signed\_id            | Custom      | String      |
| companySignedDate        | sf\_company\_signed\_date          | Custom      | Date        |
| customerSignedId         | sf\_customer\_signed\_id           | Custom      | String      |
| activatedById            | sf\_activated\_by\_id              | Custom      | String      |
| activatedDate            | sf\_activated\_date                | Custom      | Date        |
| lastApprovedDate         | sf\_last\_approved\_date           | Custom      | Date        |
| lastActivityDate         | sf\_last\_activity\_date           | Custom      | Date        |
| accountName              | sf\_account\_name                  | Custom      | String      |
| startDate                | sf\_start\_date                    | Custom      | Date        |
| endDate                  | sf\_end\_date                      | Custom      | Date        |
| createdBy                | sf\_created\_by                    | Custom      | String      |

## Document

Amazon Q supports crawling [Salesforce Online Documents](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_document.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_document.htm") and offers the following document field
mappings.

| Salesforce field name | Index field name            | Description | Data type      |
| --------------------- | --------------------------- | ----------- | -------------- |
| category              | \_category                  | Default     | String         |
| sourceUrl             | \_source\_uri               | Default     | String         |
| author                | \_authors                   | Default     | String list    |
| createdAt             | \_created\_at               | Default     | Date           |
| folder                | sf\_folder\_name            | Custom      | String         |
| isInternalUseOnly     | sf\_is\_internal\_use\_only | Custom      | String         |
| isPublic              | sf\_is\_public              | Custom      | String         |
| keywords              | sf\_keywords                | Custom      | String         |
| lastModifiedBy        | sf\_last\_modified\_by      | Custom      | String         |
| updatedAt             | \_last\_updated\_at         | Default     | Date           |
| fileName              | sf\_file\_name              | Custom      | String         |
| fileType              | \_file\_type                | Default     | String         |
| fileSize              | sf\_file\_size              | Custom      | Long (numeric) |
| createdBy             | sf\_created\_by             | Custom      | String         |
| isBodySearchable      | sf\_is\_body\_searchable    | Custom      | String         |

## Group

Amazon Q supports crawling [Salesforce Online Groups](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_group.htm") and offers the following group field
mappings.

| Salesforce field name  | Index field name                 | Description | Data type   |
| ---------------------- | -------------------------------- | ----------- | ----------- |
| category               | \_category                       | Default     | String      |
| sourceUrl              | \_source\_uri                    | Default     | String      |
| createdAt              | \_created\_at                    | Default     | Date        |
| groupEmail             | sf\_group\_email                 | Custom      | String      |
| lastModifiedBy         | sf\_last\_modified\_by           | Custom      | String      |
| lastModifiedDate       | \_last\_modified\_at             | Default     | Date        |
| ownerId                | sf\_owner\_id                    | Custom      | String      |
| groupName              | sf\_group\_name                  | Custom      | String      |
| createdBy              | \_authors                        | Default     | String list |
| lastFeedModifiedDate   | sf\_last\_feed\_modified\_date   | Custom      | Date        |
| hasPrivateFieldsAccess | sf\_has\_private\_fields\_access | Custom      | String      |
| canHaveGuests          | sf\_can\_have\_guests            | Custom      | String      |
| isArchived             | sf\_is\_archived                 | Custom      | String      |
| isAutoArchived         | sf\_is\_auto\_archive\_disabled  | Custom      | String      |
| memberCount            | sf\_member\_count                | Custom      | String      |
| collaborationType      | sf\_collabotration\_type         | Custom      | String      |
| informationTitle       | sf\_information\_title           | Custom      | String      |

## Idea

Amazon Q supports crawling [Salesforce Online Ideas](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_idea.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_idea.htm") and offers the following idea field
mappings.

| Salesforce field name | Index field name         | Description | Data type      |
| --------------------- | ------------------------ | ----------- | -------------- |
| category              | \_category               | Default     | String         |
| sourceUrl             | \_source\_uri            | Default     | String         |
| createdAt             | \_created\_at            | Default     | Date           |
| lastModifiedBy        | sf\_last\_modified\_by   | Custom      | String         |
| title                 | sf\_title                | Custom      | String         |
| status                | sf\_status               | Custom      | String         |
| createdByName         | sf\_created\_by          | Custom      | String         |
| parentIdea            | sf\_parent\_idea\_id     | Custom      | String         |
| parentIdeaId          | sf\_parent\_idea\_id     | Custom      | String         |
| lastModifiedDate      | \_last\_modified\_at     | Default     | Date           |
| recordTypeId          | sf\_record\_type\_id     | Custom      | String         |
| communityId           | sf\_community\_id        | Custom      | String         |
| numComments           | sf\_number\_of\_comments | Custom      | Long (numeric) |
| voteScore             | sf\_vote\_score          | Custom      | Long (numeric) |
| voteTotal             | sf\_vote\_total          | Custom      | Long (numeric) |
| lastCommentDate       | sf\_last\_comment\_date  | Custom      | Date           |

## Lead

Amazon Q supports crawling [Salesforce Online Leads](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.htm") and offers the following lead field
mappings.

| Salesforce field name  | Index field name               | Description | Data type      |
| ---------------------- | ------------------------------ | ----------- | -------------- |
| category               | \_category                     | Default     | String         |
| sourceUrl              | \_source\_uri                  | Default     | String         |
| city                   | sf\_city                       | Custom      | String         |
| company                | sf\_company                    | Custom      | String         |
| country                | sf\_country                    | Custom      | String         |
| createdAt              | \_created\_at                  | Default     | Date           |
| lastModifiedBy         | sf\_last\_modified\_by         | Custom      | String         |
| updatedAt              | \_last\_updated\_at            | Default     | Date           |
| leadSource             | sf\_lead\_source               | Custom      | String         |
| state                  | sf\_state                      | Custom      | String         |
| status                 | sf\_status                     | Custom      | String         |
| convertedAccount       | sf\_converted\_account         | Custom      | String         |
| convertedAccountId     | sf\_converted\_account\_id     | Custom      | String         |
| convertedContact       | sf\_converted\_contact         | Custom      | String         |
| convertedContactId     | sf\_converted\_contact\_id     | Custom      | String         |
| convertedDate          | sf\_converted\_date            | Custom      | Date           |
| convertedOpportunity   | sf\_converted\_opportunity     | Custom      | String         |
| convertedOpportunityId | sf\_converted\_opportunity\_id | Custom      | String         |
| firstName              | sf\_first\_name                | Custom      | String         |
| createdBy              | \_authors                      | Default     | String list    |
| isConverted            | sf\_is\_converted              | Custom      | String         |
| owner                  | sf\_owner\_name                | Custom      | String         |
| lastActivityDate       | sf\_last\_activity\_date       | Custom      | Date           |
| ownerId                | sf\_owner\_id                  | Custom      | String         |
| lastName               | sf\_last\_name                 | Custom      | String         |
| title                  | sf\_title                      | Custom      | String         |
| street                 | sf\_street                     | Custom      | String         |
| postalCode             | sf\_postal\_code               | Custom      | String         |
| latitude               | sf\_latitude                   | Custom      | String         |
| longitude              | sf\_longitude                  | Custom      | String         |
| geocodeAccuracy        | sf\_geocode\_accuracy          | Custom      | String         |
| phone                  | sf\_phone                      | Custom      | String         |
| email                  | sf\_email                      | Custom      | String         |
| industry               | sf\_industry                   | Custom      | String         |
| rating                 | sf\_rating                     | Custom      | String         |
| annualRevenue          | sf\_annual\_revenue            | Custom      | String         |
| numberofEmployees      | sf\_number\_of\_employees      | Custom      | Long (numeric) |
| jigsaw                 | sf\_jigsaw                     | Custom      | String         |
| jigsawContactId        | sf\_jigsaw\_contact\_id        | Custom      | String         |
| emailBouncedReason     | sf\_email\_bounced\_reason     | Custom      | String         |
| individualId           | sf\_individual\_id             | Custom      | String         |

## Opportunity

Amazon Q supports crawling [Salesforce Online Opportunities](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_opportunity.htm") and offers the following opportunity field
mappings.

| Salesforce field name  | Index field name                 | Description | Data type      |
| ---------------------- | -------------------------------- | ----------- | -------------- |
| category               | \_category                       | Default     | String         |
| sourceUrl              | \_source\_uri                    | Default     | String         |
| accountName            | sf\_account\_name                | Custom      | String         |
| amount                 | sf\_amount                       | Custom      | String         |
| campaign               | sf\_campaign\_name               | Custom      | String         |
| createdAt              | \_created\_at                    | Default     | Date           |
| createdBy              | sf\_created\_by                  | Custom      | String         |
| lastModifiedBy         | sf\_last\_modified\_by           | Custom      | String         |
| lastModifiedDate       | \_last\_updated\_at              | Default     | Date           |
| fiscalQuarter          | sf\_fiscal\_quarter              | Custom      | String         |
| fiscalYear             | sf\_fiscal\_year                 | Custom      | String         |
| isClosed               | sf\_is\_closed                   | Custom      | String         |
| isWon                  | sf\_is\_won                      | Custom      | String         |
| leadSource             | sf\_lead\_source                 | Custom      | String         |
| opportunityName        | sf\_opportunity\_name            | Custom      | String         |
| accountId              | sf\_account\_id                  | Custom      | String         |
| campaignId             | sf\_campaign\_id                 | Custom      | String         |
| closeDate              | sf\_close\_date                  | Custom      | Date           |
| typeValue              | sf\_type\_value                  | Custom      | String         |
| lastActivityDate       | sf\_last\_activity\_date         | Date        | String         |
| ownerName              | sf\_owner\_name                  | Custom      | String         |
| ownerId                | sf\_owner\_id                    | Custom      | String         |
| stageName              | sf\_stage\_name                  | Custom      | String         |
| probability            | sf\_probability                  | Custom      | Long (numeric) |
| nextStep               | sf\_next\_step                   | Custom      | String         |
| forestCategory         | sf\_forecast\_category           | Custom      | String         |
| forestCategoryName     | sf\_forest\_category\_name       | Custom      | String         |
| hasOpportunityLineItem | sf\_has\_opportunity\_line\_item | Custom      | String         |
| pricebook2id           | sf\_pricebook2\_id               | Custom      | String         |
| pushCount              | sf\_push\_count                  | Custom      | String         |
| fiscal                 | sf\_fiscal                       | Custom      | String         |
| contactId              | sf\_contact\_id                  | Custom      | String         |
| lastViewedDate         | sf\_last\_viewed\_date           | Custom      | Date           |
| hasOpenActivity        | sf\_has\_open\_activity          | Custom      | Long (numeric) |
| hasOverdueTask         | sf\_has\_overdue\_task           | Custom      | String         |

## Partner

Amazon Q supports crawling [Salesforce Online Partner](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_partner.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_partner.htm") and offers the following partner field
mappings.

| Salesforce field name | Index field name         | Description | Data type   |
| --------------------- | ------------------------ | ----------- | ----------- |
| category              | \_category               | Default     | String      |
| sourceUrl             | \_source\_uri            | Default     | String      |
| createdAt             | \_created\_at            | Default     | Date        |
| updatedAt             | \_last\_updated\_at      | Default     | Date        |
| createdBy             | \_authors                | Default     | String list |
| opportunityId         | sf\_opportunity\_id      | Custom      | String      |
| accountFromId         | sf\_account\_from\_id    | Custom      | String      |
| accountToId           | sf\_role                 | Custom      | String      |
| role                  | sf\_role                 | Custom      | String      |
| isPrimary             | sf\_is\_primary          | Custom      | String      |
| systemModstamp        | sf\_system\_modstamp     | Custom      | Date        |
| reversePartnerId      | sf\_reverse\_partner\_id | Custom      | String      |
| opportunity           | sf\_opportunity          | Custom      | String      |
| accountFrom           | sf\_account\_from        | Custom      | String      |
| accountTo             | sf\_account\_to          | Custom      | String      |

## Pricebook

Amazon Q supports crawling [Salesforce Online Pricebooks](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebook2.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_pricebook2.htm") and offers the following pricebook field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source\_uri          | Default     | String      |
| isActive              | sf\_is\_active         | Custom      | String      |
| lastModifiedBy        | sf\_last\_modified\_by | Default     | String      |
| lastModifiedDate      | \_last\_updated\_at    | Default     | Date        |
| pricebookName         | sf\_pricebook\_name    | Custom      | String      |
| createdAt             | \_created\_at          | Default     | Date        |
| createdBy             | \_authors              | Default     | String list |
| lastViewedDate        | sf\_last\_viewed\_date | Custom      | Date        |
| isStandard            | sf\_is\_standard       | Custom      | String      |

## Product

Amazon Q supports crawling [Salesforce Online Product](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_product2.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_product2.htm") and offers the following product field
mappings.

| Salesforce field name | Index field name                | Description | Data type   |
| --------------------- | ------------------------------- | ----------- | ----------- |
| category              | \_category                      | Default     | String      |
| sourceUrl             | \_source\_uri                   | Default     | String      |
| family                | sf\_family                      | Custom      | String      |
| isActive              | sf\_is\_active                  | Custom      | String      |
| createdAt             | \_created\_at                   | Default     | Date        |
| updatedAt             | \_last\_updated\_at             | Default     | Date        |
| lastModifiedBy        | sf\_last\_modified\_by          | Custom      | String      |
| productCode           | sf\_product\_code               | Custom      | String      |
| createdBy             | \_authors                       | Default     | String list |
| productName           | sf\_product\_name               | Custom      | String      |
| externalDataSourceId  | sf\_external\_datasource\_id    | Custom      | String      |
| externalId            | sf\_external\_id                | Custom      | String      |
| displayUrl            | sf\_display\_url                | Custom      | String      |
| quantityUnitOfMeasure | sf\_quantity\_unit\_of\_measure | Custom      | String      |
| isArchived            | sf\_is\_archived                | Custom      | String      |
| lastViewedDate        | sf\_last\_viewed\_date          | Custom      | Date        |
| stockKeepingUnit      | sf\_stock\_keeping\_unit        | Custom      | String      |

## Solution

Amazon Q supports crawling [Salesforce Online Solutions](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_solution.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_solution.htm") and offers the following solution field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source\_uri          | Default     | String      |
| isPublished           | sf\_is\_published      | Custom      | String      |
| isReviewed            | sf\_is\_reviewed       | Custom      | String      |
| lastModifiedBy        | sf\_last\_modified\_by | Custom      | String      |
| lastModifiedDate      | \_last\_updated\_at    | Default     | Date        |
| ownerName             | sf\_owner\_name        | Custom      | String      |
| solutionNumber        | sf\_solution\_number   | Custom      | String      |
| status                | sf\_status             | Custom      | String      |
| timesUsed             | sf\_times\_used        | Custom      | String      |
| solutionName          | sf\_solution\_name     | Custom      | String      |
| createdByName         | \_authors              | Default     | String list |
| createdAt             | \_created\_at          | Default     | Date        |
| solutionNote          | sf\_solution\_note     | Custom      | String      |
| ownderId              | sf\_ownderId           | Custom      | String      |
| lastViewedDate        | sf\_last\_viewed\_date | Custom      | Date        |

## Profile

Amazon Q supports crawling [Salesforce Online Profiles](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_profile.htm") and offers the following profile field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source\_uri          | Default     | String      |
| updatedAt             | \_last\_updated\_at    | Default     | Date        |
| lastModifiedBy        | sf\_last\_modified\_by | Custom      | String      |
| createdBy             | \_authors              | Default     | String list |
| createdAt             | \_created\_at          | Default     | Date        |
| userType              | sf\_user\_type         | Custom      | String      |

## Task

Amazon Q supports crawling [Salesforce Online Tasks](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_task.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_task.htm") and offers the following task field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source\_uri          | Default     | String      |
| accountName           | sf\_account\_name      | Custom      | String      |
| lastModifiedBy        | sf\_last\_modified\_by | Custom      | String      |
| lastModifiedDate      | \_last\_updated\_at    | Default     | Date        |
| ownerName             | sf\_owner\_name        | Custom      | String      |
| isRecurrence          | sf\_is\_recurrence     | Custom      | String      |
| isClosed              | sf\_is\_closed         | Custom      | String      |
| isArchived            | sf\_is\_archived       | Custom      | String      |
| priority              | sf\_priority           | Custom      | String      |
| status                | sf\_status             | Custom      | String      |
| whatId                | sf\_what\_id           | Custom      | String      |
| createdByName         | \_authors              | Default     | String list |
| createdAt             | \_created\_at          | Default     | Date        |
| subject               | sf\_subject            | Custom      | String      |
| activityDate          | sf\_activity\_date     | Custom      | Date        |
| activityDate          | sf\_activity\_date     | Custom      | Date        |
| isHighPriority        | sf\_is\_high\_priority | Custom      | String      |
| ownerId               | sf\_owner\_id          | Custom      | String      |
| callType              | sf\_call\_type         | Custom      | String      |

## User

Amazon Q supports crawling [Salesforce Online Users](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_user.htm") and offers the following user field
mappings.

| Salesforce field name | Index field name          | Description | Data type   |
| --------------------- | ------------------------- | ----------- | ----------- |
| category              | \_category                | Default     | String      |
| sourceUrl             | \_source\_uri             | Default     | String      |
| account               | sf\_account               | Custom      | String      |
| isActive              | sf\_is\_active            | Custom      | String      |
| city                  | sf\_city                  | Custom      | String      |
| lastModifiedBy        | sf\_last\_modified\_by    | Custom      | String      |
| updatedAt             | \_last\_updated\_at       | Default     | Date        |
| companyName           | sf\_company\_name         | Custom      | String      |
| country               | sf\_country               | Custom      | String      |
| department            | sf\_department            | Custom      | String      |
| division              | sf\_division              | Custom      | String      |
| email                 | sf\_email                 | Custom      | String      |
| employeeNumber        | sf\_employee\_number      | Custom      | String      |
| firstName             | sf\_first\_name           | Custom      | String      |
| lastName              | sf\_last\_name            | Custom      | String      |
| manager               | sf\_manager               | Custom      | String      |
| state                 | sf\_state                 | Custom      | String      |
| userRole              | sf\_user\_role            | Custom      | String      |
| username              | sf\_username              | Custom      | String      |
| createdBy             | \_authors                 | Default     | String list |
| createdAt             | \_created\_at             | Default     | Date        |
| street                | sf\_street                | Custom      | String      |
| postalCode            | sf\_postal\_code          | Custom      | String      |
| latitude              | sf\_latitiude             | Custom      | String      |
| longitude             | sf\_longitude             | Custom      | String      |
| geocodeAccuracy       | sf\_geocode\_accuracy     | Custom      | String      |
| phone                 | sf\_phone                 | Custom      | String      |
| fax                   | sf\_fax                   | Custom      | String      |
| mobilePhone           | sf\_mobile\_phone         | Custom      | String      |
| profileName           | sf\_profile\_name         | Custom      | String      |
| aboutMe               | sf\_about\_me             | Custom      | String      |
| languageLocaleKey     | sf\_language\_locale\_key | Custom      | String      |

## Chatter

Amazon Q supports crawling [Salesforce Online Chatters](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_chatteractivity.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_chatteractivity.htm") and offers the following chatter field
mappings.

| Salesforce field name | Index field name       | Description | Data type   |
| --------------------- | ---------------------- | ----------- | ----------- |
| category              | \_category             | Default     | String      |
| sourceUrl             | \_source\_uri          | Default     | String      |
| body                  | sf\_body               | Custom      | String      |
| createdAt             | \_created\_at          | Default     | Date        |
| lastEditById          | sf\_last\_edit\_by\_id | Custom      | String      |
| lastEditDate          | sf\_last\_edit\_date   | Custom      | Date        |
| lastModifiedDate      | \_last\_updated\_at    | Default     | Date        |
| insertedById          | sf\_inserted\_by\_id   | Custom      | String      |
| createdBy             | \_authors              | Default     | String list |
| parentId              | sf\_parent\_id         | Custom      | String      |
| revision              | sf\_revision           | Custom      | String      |
| status                | sf\_status             | Custom      | String      |
| isRichText            | sf\_is\_rich\_texrt    | Custom      | String      |

## Knowledge articles

Amazon Q supports crawling [Salesforce Online Knowledge articles](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_knowledgearticle.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_knowledgearticle.htm") and offers the following knowledge
article field mappings.

| Salesforce field name        | Index field name                 | Description | Data type      |
| ---------------------------- | -------------------------------- | ----------- | -------------- |
| category                     | \_category                       | Default     | String         |
| sourceUrl                    | \_source\_uri                    | Default     | String         |
| articleTitle                 | sf\_title                        | Custom      | String         |
| articleNumber                | sf\_article\_number              | Default     | Date           |
| knowledgeArticleId           | sf\_knowledge\_article\_id       | Custom      | String         |
| lastPublishedDate            | sf\_last\_published\_date        | Custom      | Date           |
| publishStatus                | sf\_publish\_status              | Custom      | String         |
| versionNumber                | sf\_version\_number              | Custom      | String         |
| language                     | sf\_language                     | Custom      | String         |
| ownerId                      | sf\_ownder\_id                   | Custom      | String         |
| summary                      | sf\_summary                      | Custom      | String         |
| firstPublishedDate           | sf\_first\_published\_date       | Custom      | Date           |
| updatedAt                    | \_last\_updated\_at              | Default     | Date           |
| archivedDate                 | sf\_archived\_date               | Custom      | Date           |
| isLatestVersion              | sf\_is\_latest\_version          | Custom      | String         |
| sourceId                     | sf\_sourceId                     | Custom      | String         |
| createdBy                    | \_authors                        | Default     | String list    |
| assignmentDate               | sf\_assignment\_date             | Custom      | Long (numeric) |
| assignmentDueDate            | sf\_assignment\_due\_date        | Custom      | Date           |
| articleCaseAttachCount       | sf\_article\_case\_attach\_count | Custom      | Long (numeric) |
| articleTotalViewCount        | sf\_article\_total\_view\_count  | Custom      | Long (numeric) |
| urlName                      | sf\_url\_name                    | Custom      | String         |
| assignmentNote               | sf\_assignment\_date             | Custom      | String         |
| migratedToFromArticleVersion | sf\_migrated\_article\_version   | Custom      | String         |
| assignedBy                   | sf\_assigned\_by                 | Custom      | String         |
| assignedTo                   | sf\_assigned\_to                 | Custom      | Date           |

## Attachments

Amazon Q supports crawling [Salesforce Online Attachments](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_attachment.htm "https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_attachment.htm") and offers the following attachment field
mappings.

| Salesforce field name | Index field name    | Description | Data type      |
| --------------------- | ------------------- | ----------- | -------------- |
| category              | \_category          | Default     | String         |
| sourceUrl             | \_source\_uri       | Default     | String         |
| createdAt             | \_created\_at       | Default     | Date           |
| updatedAt             | \_last\_updated\_at | Default     | Date           |
| fileName              | sf\_file\_name      | Custom      | String         |
| fileType              | \_file\_type        | Default     | String         |
| fileSize              | sf\_file\_size      | Custom      | Long (numeric) |
| parentName            | sf\_parent\_name    | Default     | String         |
| createdBy             | \_authors           | Default     | String list    |

## Custom object

Amazon Q supports crawling custom objects and offers the following custom
object field mappings.

| Salesforce field name | Index field name           | Description | Data type   |
| --------------------- | -------------------------- | ----------- | ----------- |
| category              | \_category                 | Default     | String      |
| sourceUrl             | \_source\_uri              | Default     | String      |
| createdAt             | \_created\_at              | Default     | Date        |
| updatedAt             | \_last\_updated\_at        | Default     | Date        |
| lastModifiedById      | sf\_last\_modified\_by\_id | Custom      | String      |
| customObjectName      | sf\_custom\_object\_name   | Custom      | String      |
| createdBy             | \_authors                  | Default     | String list |
| lastModifiedBy        | sf\_last\_modified\_by     | Custom      | String      |
| documentbody          | \_document\_body           | Custom      | String      |
