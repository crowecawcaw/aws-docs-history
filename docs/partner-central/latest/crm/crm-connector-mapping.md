

# Mapping ACE objects
<a name="crm-connector-mapping"></a>

The CRM connector provides the **ACE Mappings** page. The page enables you to map objects and fields between your Salesforce organization and AWS Partner Network (APN).

The following sections explain how to create object mappings.

**Topics**
+ [Using the ACE Mappings page](mapping-page.md)
+ [Multi-object mapping](multi-object-mappings.md)
+ [Picklist mapping](picklist-mapping.md)
+ [Mapping ACE and Salesforce objects](#mapping-guidance)
+ [Sync logs and reports](crm-connector-sync-logs-and-reports.md)

## Mapping ACE and Salesforce objects
<a name="mapping-guidance"></a>

The following sections explain how to map ACE and Salesforce custom objects in object maps.

### Using an AWS ACE opportunity custom object
<a name="ace-opportunity-custom-object"></a>

Version 2.0 and later of the CRM connector includes an ACE custom opportunity object. You can use the object to manage AWS opportunities in Salesforce.

When using the custom object on the **ACE Mappings** page, partners can automatically map AWS fields to Salesforce fields. Additionally, the custom opportunity object is aligned with the new ACE data model and has validations built in to the user interface that help users submit new opportunities.

To use a custom ACE opportunity object, complete the following steps:

1. In Salesforce, navigate to the **ACE Mappings** page, and choose **Opportunity** from the left navigation pane.

1. Under **Object Selector**, choose **ACE Opportunity **.

1. To map Salesforce fields to AWS fields, choose the **Auto Map ACE object** button.

### Using a standard Salesforce object or custom object
<a name="custom-ace-opportunity-object"></a>

Partners can use the Salesforce standard opportunity object or their own custom opportunity object. To avoid ACE synchronization failures, ensure that the custom opportunity object contains all of the relevant ACE mandatory fields or conditionally mandatory fields. The data type of the mapped AWS field must be the same data type as the Salesforce field created in the custom object. If the data type doesn't match, the field will not appear in the ACE mapping screen. For example, the text field **customerCompanyName** can be mapped only to a text (string) field in the standard or custom opportunity object. For required data types, refer to the ACE opportunity fields.

To use a standard Salesforce object or custom object, complete the following steps:

1. Navigate to the **ACE Mappings** page, and choose **Opportunity** from the left navigation pane.

1. Under **Object Selector**, choose your object.

1. Complete the mapping by selecting the required Salesforce fields against the corresponding AWS fields, and then choose **Save**.

**Note**  
The Auto Map feature is available only for ACE opportunity custom objects.