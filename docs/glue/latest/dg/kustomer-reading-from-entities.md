

# Reading from Kustomer entities
<a name="kustomer-reading-from-entities"></a>

**Prerequisite**

A Kustomer object you would like to read from. You will need the object name such as Brands or Cards. The following table shows the supported entities.

**Supported entities for source**:


| Entity | Can be filtered | Supports limit | Supports Order by | Supports Select \* | Supports partitioning | 
| --- | --- | --- | --- | --- | --- | 
| Brands | No | Yes | No | Yes | No | 
| Cards | No | Yes | No | Yes | No | 
| Chat Settings | No | No | No | Yes | No | 
| Companies | Yes | Yes | Yes | Yes | Yes | 
| Conversations | Yes | Yes | Yes | Yes | Yes | 
| Customers | Yes | Yes | Yes | Yes | Yes | 
| Customer Searches Pinned | No | Yes | No | Yes | No | 
| Customer Searches Position | No | No | No | Yes | No | 
| Email Hooks | No | Yes | No | Yes | No | 
| Web Hooks | No | Yes | No | Yes | No | 
| KB Articles | No | Yes | No | Yes | No | 
| KB Categories | No | Yes | No | Yes | No | 
| KB Forms | No | Yes | No | Yes | No | 
| KB Routes | No | Yes | No | Yes | No | 
| KB Tags | No | Yes | No | Yes | No | 
| KB Templates | No | Yes | No | Yes | No | 
| KB Themes | No | Yes | No | Yes | No | 
| Klasses | No | Yes | No | Yes | No | 
| KViews | No | Yes | No | Yes | No | 
| Messages | Yes | Yes | Yes | Yes | Yes | 
| Notes | Yes | Yes | Yes | Yes | Yes | 
| Notifications | No | Yes | No | Yes | No | 

**Example**:

```
Kustomer_read = glueContext.create_dynamic_frame.from_options(
    connection_type="kustomer",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "brands",
        "API_VERSION": "v1"
    }
```

## Kustomer entity and field details
<a name="kustomer-reading-from-entities-field-details"></a>

For more information about the entities and field details see:
+ [Brands](https://api.kustomerapp.com/v1/brands)
+ [Cards](https://api.kustomerapp.com/v1/cards)
+ [Chat Settings](https://api.kustomerapp.com/v1/chat/settings)
+ [Companies](https://api.kustomerapp.com/v1/companies)
+ [Conversations](https://api.kustomerapp.com/v1/conversations)
+ [Customers](https://api.kustomerapp.com/v1/customers)
+ [Customers Searches Pinned](https://api.kustomerapp.com/v1/customers/searches/pinned)
+ [Customer Searches Positions](https://api.kustomerapp.com/v1/customers/searches/positions)
+ [Hooks Email](https://api.kustomerapp.com/v1/hooks/email)
+ [Hooks Web](https://api.kustomerapp.com/v1/hooks/web)
+ [KB Articles](https://api.kustomerapp.com/v1/kb/articles)
+ [KB Categories](https://api.kustomerapp.com/v1/kb/categories)
+ [KB Forms]( https://api.kustomerapp.com/v1/kb/forms)
+ [KB Routes](https://api.kustomerapp.com/v1/kb/routes)
+ [KB Tags](https://api.kustomerapp.com/v1/kb/tags)
+ [KB Templates](https://api.kustomerapp.com/v1/kb/templates)
+ [KB Themes](https://api.kustomerapp.com/v1/kb/themes)
+ [Klasses](https://api.kustomerapp.com/v1/klasses)
+ [Kviews](https://api.kustomerapp.com/v1/kviews)
+ [Messages](https://api.kustomerapp.com/v1/messages)
+ [Notes](https://api.kustomerapp.com/v1/notes)
+ [Notifications](https://api.kustomerapp.com/v1/notifications)

Kustomer API v1



- **Brands**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** iconUrl / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** default / **Data type:** Boolean / **Supported operators:** N/A

- **Cards**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** contexts / **Data type:** List / **Supported operators:** N/A

- **Chat Settings**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** settingsVersion / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** widgetType / **Data type:** String / **Supported operators:** N/A
  - **Field:** version / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** teamName / **Data type:** String / **Supported operators:** N/A
  - **Field:** greeting / **Data type:** String / **Supported operators:** N/A
  - **Field:** autoreply / **Data type:** String / **Supported operators:** N/A
  - **Field:** embedIconUrl / **Data type:** String / **Supported operators:** N/A
  - **Field:** embedIconColor / **Data type:** String / **Supported operators:** N/A
  - **Field:** fallbackEmailSubject / **Data type:** String / **Supported operators:** N/A
  - **Field:** fallbackEmailIntroduction / **Data type:** String / **Supported operators:** N/A
  - **Field:** enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** outboundChatEnabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** offhoursMessage / **Data type:** String / **Supported operators:** N/A
  - **Field:** offhoursImageUrl / **Data type:** String / **Supported operators:** N/A
  - **Field:** closableChat / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** noHistory / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** disableAttachments / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** volumeControl / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** singleSessonChat / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** showTypingIndicatorWeb / **Data type:** Boolean / **Supported operators:** N/A

- **Companies**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** domains / **Data type:** List / **Supported operators:** N/A
  - **Field:** emails / **Data type:** List / **Supported operators:** N/A
  - **Field:** phones / **Data type:** List / **Supported operators:** N/A
  - **Field:** whatsapps / **Data type:** List / **Supported operators:** N/A
  - **Field:** socials / **Data type:** List / **Supported operators:** N/A
  - **Field:** urls / **Data type:** List / **Supported operators:** N/A
  - **Field:** locations / **Data type:** List / **Supported operators:** N/A
  - **Field:** roleGroupVersions / **Data type:** List / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A

- **Conversations**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** preview / **Data type:** String / **Supported operators:** N/A
  - **Field:** channels / **Data type:** List / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** messageCount / **Data type:** Integer / **Supported operators:**  =, \!=, >, >=, <, <=
  - **Field:** noteCount / **Data type:** Integer / **Supported operators:**  =, \!=, >, >=, <, <=
  - **Field:** satisfaction / **Data type:** Integer / **Supported operators:**  =, \!=, >, >=, <, <=
  - **Field:** satisfactionLevel / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** lastActivityAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** spam / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** ended / **Data type:** Boolean / **Supported operators:**  =, \!=
  - **Field:** endedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** endedReason / **Data type:** String / **Supported operators:** CONTAINS
  - **Field:** endedByType / **Data type:** String / **Supported operators:** N/A
  - **Field:** importedAt / **Data type:** String / **Supported operators:** N/A
  - **Field:** tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** suggestedTags / **Data type:** List / **Supported operators:** N/A
  - **Field:** sentiment / **Data type:** String / **Supported operators:** N/A
  - **Field:** predictions / **Data type:** List / **Supported operators:** N/A
  - **Field:** suggestedShortcuts / **Data type:** List / **Supported operators:** N/A
  - **Field:** firstMessageIn / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** firstMessageOut / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastMessageIn / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastMessageOut / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastMessageAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** lastMessageUnrespondedTo / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastMessageUnrespondedToSinceLastDone / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** assignedUsers / **Data type:** List / **Supported operators:** N/A
  - **Field:** assignedTeams / **Data type:** List / **Supported operators:** N/A
  - **Field:** firstResponse / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** firstResponseSinceLastDone / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastResponse / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** firstDone / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** lastDone / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** direction / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** lastMessageDirection / **Data type:** String / **Supported operators:** N/A
  - **Field:** outboundMessageCount / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** inboundMessageCount / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** priority / **Data type:** Integer / **Supported operators:**  =, \!=, >, >=, <, <=
  - **Field:** roleGroupVersions / **Data type:** List / **Supported operators:** N/A
  - **Field:** accessOverride / **Data type:** List / **Supported operators:** N/A
  - **Field:** assistant / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** phase / **Data type:** String / **Supported operators:** N/A
  - **Field:** Skills / **Data type:** List / **Supported operators:** N/A
  - **Field:** matchedTimeBasedRules / **Data type:** List / **Supported operators:** N/A

- **Customers**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** displayName / **Data type:** String / **Supported operators:** N/A
  - **Field:** displayColor / **Data type:** String / **Supported operators:** N/A
  - **Field:** displayIcon / **Data type:** String / **Supported operators:** N/A
  - **Field:** externalId / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** externalIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** sharedExternalIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** emails / **Data type:** List / **Supported operators:** N/A
  - **Field:** sharedEmails / **Data type:** List / **Supported operators:** N/A
  - **Field:** phones / **Data type:** List / **Supported operators:** N/A
  - **Field:** sharedPhones / **Data type:** List / **Supported operators:** N/A
  - **Field:** whatsapps / **Data type:** List / **Supported operators:** N/A
  - **Field:** facebookIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** instagramIds / **Data type:** List / **Supported operators:** N/A
  - **Field:** socials / **Data type:** List / **Supported operators:** N/A
  - **Field:** sharedSocials / **Data type:** List / **Supported operators:** N/A
  - **Field:** urls / **Data type:** List / **Supported operators:** N/A
  - **Field:** locations / **Data type:** List / **Supported operators:** N/A
  - **Field:** activeUsers / **Data type:** List / **Supported operators:** N/A
  - **Field:** watchers / **Data type:** List / **Supported operators:** N/A
  - **Field:** recentLocation / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** locale / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** timeZone / **Data type:** String / **Supported operators:** N/A
  - **Field:** gender / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:**  =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** lastActivityAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** deleted / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** lastConversation / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** conversationCounts / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** preview / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** progressiveStatus / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** verified / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** recentItems / **Data type:** List / **Supported operators:** N/A
  - **Field:** defaultLang / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** satisfactionLevel / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** roleGroupVersions / **Data type:** List / **Supported operators:** N/A
  - **Field:** accessOverride / **Data type:** List / **Supported operators:** N/A
  - **Field:** companyName / **Data type:** String / **Supported operators:** N/A
  - **Field:** firstName / **Data type:** String / **Supported operators:** N/A
  - **Field:** lastName / **Data type:** String / **Supported operators:** N/A

- **Customer Searches Pinned**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** search / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A

- **Customer Searches Positions**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** positions / **Data type:** List / **Supported operators:** N/A
  - **Field:** children / **Data type:** List / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A

- **Email Hooks**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** debug / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** email / **Data type:** String / **Supported operators:** N/A
  - **Field:** eventName / **Data type:** String / **Supported operators:** N/A
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** key / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A

- **Web Hooks**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** eventName / **Data type:** String / **Supported operators:** N/A
  - **Field:** hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** version / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** debug / **Data type:** Boolean / **Supported operators:** N/A

- **KB Articles**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** source / **Data type:** String / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** scope / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** deleted / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** deletedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** publishedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** tags / **Data type:** List / **Supported operators:** N/A
  - **Field:** categories / **Data type:** List / **Supported operators:** N/A
  - **Field:** knowledgeBases / **Data type:** List / **Supported operators:** N/A
  - **Field:** metaTitle / **Data type:** String / **Supported operators:** N/A
  - **Field:** metaDescription / **Data type:** String / **Supported operators:** N/A
  - **Field:** metaKeywords / **Data type:** List / **Supported operators:** N/A
  - **Field:** langVersions / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** latestLangs / **Data type:** Struct / **Supported operators:** N/A

- **KB Categories**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** published / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** positions / **Data type:** List / **Supported operators:** N/A
  - **Field:** categoryPositions / **Data type:** List / **Supported operators:** N/A
  - **Field:** root / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** langs / **Data type:** Struct / **Supported operators:** N/A

- **KB Forms**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** slug / **Data type:** String / **Supported operators:** N/A
  - **Field:** hash / **Data type:** String / **Supported operators:** N/A
  - **Field:** body / **Data type:** String / **Supported operators:** N/A
  - **Field:** layout / **Data type:** List / **Supported operators:** N/A
  - **Field:** layoutV2 / **Data type:** List / **Supported operators:** N/A
  - **Field:** componentsV2 / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** conditions / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** advanced / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** publishedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** String / **Supported operators:** N/A
  - **Field:** published / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** snippets / **Data type:** List / **Supported operators:** N/A
  - **Field:** recaptcha / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** klass / **Data type:** String / **Supported operators:** N/A
  - **Field:** channel / **Data type:** String / **Supported operators:** N/A
  - **Field:** deflection / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** formHookEnabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** replyFrom / **Data type:** String / **Supported operators:** N/A
  - **Field:** wcag / **Data type:** Boolean / **Supported operators:** N/A

- **KB Routes**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** url / **Data type:** String / **Supported operators:** N/A
  - **Field:** routableType / **Data type:** String / **Supported operators:** N/A
  - **Field:** routableId / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A

- **KB Tags**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A

- **KB Templates**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** title / **Data type:** String / **Supported operators:** N/A
  - **Field:** description / **Data type:** String / **Supported operators:** N/A
  - **Field:** beta / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** manifest / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** jsxSnippets / **Data type:** List / **Supported operators:** N/A
  - **Field:** images / **Data type:** List / **Supported operators:** N/A
  - **Field:** version / **Data type:** String / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A

- **KB Themes**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** active / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** default / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** lastfileUpdatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** custom / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** templateVersionId / **Data type:** String / **Supported operators:** N/A
  - **Field:** templateTitle / **Data type:** String / **Supported operators:** N/A
  - **Field:** templateVersion / **Data type:** String / **Supported operators:** N/A
  - **Field:** manifest / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** configSnippets / **Data type:** List / **Supported operators:** N/A
  - **Field:** jsxSnippets / **Data type:** List / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A

- **Klasses**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** icon / **Data type:** String / **Supported operators:** N/A
  - **Field:** color / **Data type:** String / **Supported operators:** N/A
  - **Field:** appDisabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** s3DataUrl / **Data type:** String / **Supported operators:** N/A

- **KViews**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** resource / **Data type:** String / **Supported operators:** N/A
  - **Field:** template / **Data type:** String / **Supported operators:** N/A
  - **Field:** context / **Data type:** String / **Supported operators:** N/A
  - **Field:** meta / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** appDisabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** enabled / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** advanced / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** layout / **Data type:** List / **Supported operators:** N/A
  - **Field:** components / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** conditions / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A

- **Notifications**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** name / **Data type:** String / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:** N/A
  - **Field:** event / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A

- **Messages**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** externalId / **Data type:** String / **Supported operators:** N/A
  - **Field:** channel / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** app / **Data type:** String / **Supported operators:** N/A
  - **Field:** size / **Data type:** Integer / **Supported operators:** =, \!=, >, >=, <, <=
  - **Field:** direction / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** preview / **Data type:** String / **Supported operators:** N/A
  - **Field:** subject / **Data type:** String / **Supported operators:** N/A
  - **Field:** meta / **Data type:** Struct / **Supported operators:** N/A
  - **Field:** status / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** directionType / **Data type:** String / **Supported operators:**  =, \!=, CONTAINS
  - **Field:** assignedTeams / **Data type:** List / **Supported operators:** N/A
  - **Field:** assignedUsers / **Data type:** List / **Supported operators:** N/A
  - **Field:** errorAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** auto / **Data type:** Boolean / **Supported operators:**  =, \!=
  - **Field:** sentAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** N/A
  - **Field:** redacted / **Data type:** Boolean / **Supported operators:** N/A
  - **Field:** createdByTeams / **Data type:** List / **Supported operators:** N/A
  - **Field:** rev / **Data type:** Integer / **Supported operators:** N/A
  - **Field:** reactions / **Data type:** List / **Supported operators:** N/A
  - **Field:** intentDetections / **Data type:** List / **Supported operators:** N/A

- **Notes**
  - **Field:** id / **Data type:** String / **Supported operators:** N/A
  - **Field:** body / **Data type:** String / **Supported operators:** CONTAINS
  - **Field:** createdAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** updatedAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** modifiedAt / **Data type:** DateTime / **Supported operators:** =, \!=, >, >=, <, <=, BETWEEN
  - **Field:** createdByTeams / **Data type:** List / **Supported operators:** N/A



## Partitioning queries
<a name="kustomer-reading-from-partitioning"></a>

**Field-based partitioning**

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.
+ `PARTITION_FIELD`: the name of the field to be used to partition the query.
+ `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

  For the DateTime field, we accept the value in ISO format.

  Example of valid value:

  ```
  "2023-01-15T11:18:39.205Z"
  ```
+ `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
+ `NUM_PARTITIONS`: the number of partitions.

Entity-wise partitioning field support details are captured in the following table:



- **Companies**
  - **Partitioning fields:** modifiedAt
  - **Data type:** DateTime

- **Conversations**
  - **Partitioning fields:** createdAt, updatedAt, modifiedAt, endedAt, lastMessageAt / **Data type:** DateTime
  - **Partitioning fields:** messageCount, noteCount / **Data type:** BigInteger
  - **Partitioning fields:** priority / **Data type:** Integer

- **Customers**
  - **Partitioning fields:** createdAt, updatedAt, modifiedAt
  - **Data type:** DateTime

- **Messages**
  - **Partitioning fields:** errorAt, sentAt, createdAt / **Data type:** DateTime
  - **Partitioning fields:** size / **Data type:** BigInteger

- **Notes**
  - **Partitioning fields:** createdAt, updatedAt, modifiedAt
  - **Data type:** DateTime



Example:

```
Kustomer_read = glueContext.create_dynamic_frame.from_options(
    connection_type="kustomer",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "conversation",
        "API_VERSION": "v1",
        "PARTITION_FIELD": "createdAt"
        "LOWER_BOUND": "2023-01-15T11:18:39.205Z"
        "UPPER_BOUND": "2023-02-15T11:18:39.205Z"
        "NUM_PARTITIONS": "2"
    }
```