

# Reading from Smartsheet entities
<a name="smartsheet-reading-from-entities"></a>

 **Prerequisites** 

A `Smartsheet` Object you would like to read from. Refer the supported entities table below to check the available entities. 

 **Supported entities** 


| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning | 
| --- | --- | --- | --- | --- | --- | 
| List Sheet | Yes | Yes | No | Yes | No | 
| Row Metadata | Yes | Yes | No | Yes | No | 
| Sheet Metadata | No | No | No | Yes | No | 
| Sheet Data | Yes | Yes | Yes | Yes | No | 
| Event | Yes | Yes | No | Yes | No | 

 **Example** 

```
Smartsheet_read = glueContext.create_dynamic_frame.from_options(
    connection_type="smartsheet",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "list-sheets",
        "API_VERSION": "2.0",
        "INSTANCE_URL": "https://api.smartsheet.com"
    })
```

 **Smartsheet entity and field details** 



- ** List Sheets **
  - **Field:** id / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** accessLevel / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** createdAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** modifiedAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** name / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** permalink / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** modifiedSince / **Data Type:** DateTime / ****Supported Operators**:** >=
  - **Field:** version / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** source / **Data Type:** Struct / ****Supported Operators**:** NA

- ** Row Metadata **
  - **Field:** id / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** sheetId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** accessLevel / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** attachments / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** columns / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** conditionalFormat / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** createdAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** createdBy / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** discussions / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** proofs / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** expanded / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** filteredOut / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** format / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** inCriticalPath / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** locked / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** lockedForUser / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** modifiedAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** modifiedBy / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** permalink / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** rowNumber / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** version / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** totalRowCount / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** rowsModifiedSince / **Data Type:** DateTime / ****Supported Operators**:** >
  - **Field:** filterId / **Data Type:** Long / ****Supported Operators**:** “="
  - **Field:** siblingId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** parentId / **Data Type:** Long / ****Supported Operators**:** NA

- **Sheet metadata**
  - **Field:** id / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** fromId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** ownerId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** accessLevel / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** attachments / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** columns / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** createdAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** crossSheetReferences / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** dependenciesEnabled / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** discussions / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** effectiveAttachmentOptions / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** favorite / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** ganttEnabled / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** hasSummaryFields / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** modifiedAt / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** name / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** owner / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** permalink / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** projectSettings / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** readOnly / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** resourceManagementEnabled / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** showParentRowsForFilters / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** source / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** summary / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** totalRowCount / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** userPermissions / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** userSettings / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** version / **Data Type:** Integer / ****Supported Operators**:** NA
  - **Field:** workspace / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** filters / **Data Type:** List / ****Supported Operators**:** NA
  - **Field:** ganttConfig / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** resourceManagementType / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** cellImageUploadEnabled / **Data Type:** Boolean / ****Supported Operators**:** NA
  - **Field:** isMultiPicklistEnabled / **Data Type:** Boolean / ****Supported Operators**:** NA

- **Events**
  - **Field:** eventId / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** objectType / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** action / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** objectId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** eventTimestamp / **Data Type:** DateTime / ****Supported Operators**:** NA
  - **Field:** userId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** requestUserId / **Data Type:** Long / ****Supported Operators**:** NA
  - **Field:** accessTokenName / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** source / **Data Type:** String / ****Supported Operators**:** NA
  - **Field:** additionalDetails / **Data Type:** Struct / ****Supported Operators**:** NA
  - **Field:** since / **Data Type:** DateTime / ****Supported Operators**:** >=

