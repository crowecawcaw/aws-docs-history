

# Create segments from imported files in Connect Customer
<a name="customer-segments-imported-files"></a>

**Note**  
To access the segmentation builder experience in the Connect Customer admin website, make sure that the appropriate security profiles permissions are configured. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md).

Customer segment import uses a CSV file containing profile data to create new profiles or update existing ones, which are then grouped into a segment. The CSV file must be under 1GB in size and include valid headers that map to standard profile attributes.

The following steps describe creating and configuring an imported customer segment:

1. [Create a new segment](#create-new-segment)

1. [Upload CSV file](#upload-csv-file)

1. [Configure segment details](#configure-segment-details)

1. [Map customer attributes](#map-customer-attributes)

1. [Set profile expiry](#set-profile-expiry)

1. [Create and monitor segment import](#create-monitor-segment-import)

## Create a new segment
<a name="create-new-segment"></a>

1. To create a segment, make sure that you have created security profiles permissions as a prerequisite. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md).

1. In the Connect Customer admin website, navigate to **Customer Profiles****Customer segments**

1. Choose **Create segment** and select **From file upload** from the dropdown

## Upload CSV file
<a name="upload-csv-file"></a>

Choose a CSV file by either:
+ Choosing **Choose file** and selecting your file.
+ Dragging and dropping your file into the upload area.

The file must be:
+ In CSV format
+ Under 1GB in size
+ Contain headers
+ UTF-8 encoded
**Note**  
UTF-8 with BOM (Byte Order Mark) is not supported. If your import fails with a missing header error, re-save the file with UTF-8 encoding without BOM.

## Configure segment details
<a name="configure-segment-details"></a>

For **Name**, specify a recognizable identifier for your segment. This field is required.
+ Use only letters (a-z, A-Z), numbers (0-9), hyphens (-), or underscores (\_)
+ Begin with a letter or number (not an underscore)
+ Maximum length of 255 characters

**Note**  
The Connect Customer admin website uses this name as the `DisplayName` of the segment and generates a unique `SegmentDefinitionName` identifier. This identifier is used when accessing the segment through Connect Customer Customer Profiles APIs.

For **Description**, (optional), add details about your segment:
+ Maximum length of 1000 characters

## Map customer attributes
<a name="map-customer-attributes"></a>

Object type mapping defines how Customer Profiles processes your CSV data. This mapping:
+ Determines how CSV data populates standard profile objects.
+ Specifies which fields to index for profile assignment.

For more information about object type mapping, see [Create and ingest customer data into Customer Profiles](customer-profiles-object-type-mappings.md).

Choose one of these options to map your CSV columns to Customer Profiles attributes:

### Option 1: AI-powered mapping (Recommended)
<a name="ai-powered-mapping"></a>

1. Choose **Generate customer attributes**, then choose **Next**.

1. The system analyzes your CSV headers and suggests appropriate mappings to standard profile attributes.

1. Review the suggested mappings.

1. Optional: Customize the mappings:
   + Modify standard profile attribute mappings.
   + Add custom attributes using the format: `Attributes.{{attribute-name}}`.
   + Update the unique identifier.

### Option 2: Manual mapping
<a name="manual-mapping"></a>

1. Map each CSV column header to a profile attribute:
   + Use standard profile attributes. For a complete list, see [Standard profile definition in the Connect Customer Customer Profiles](standard-profile-definition.md).
   + Create custom attributes using the format: `Attributes.{{attribute-name}}`.
**Note**  
You can map up to 25 attributes.

1. Choose one mapped attribute as the customer identifier (unique key).

### Choose a customer identifier
<a name="select-customer-identifier"></a>

After completing the mapping, choose one mapped attribute as the customer identifier. Connect Customer Customer Profiles uses this identifier to:
+ Create new profiles or update existing ones.
+ Match incoming data with existing profiles.

**Note**  
Attribute mappings can be modified at any time during setup, whether using AI-powered or manual mapping.

## Set profile expiry
<a name="set-profile-expiry"></a>

Specify when imported profiles expire.

1. Choose an expiry option:
   + Default: 14 days from import date
   + Custom: Select a date using the date picker

1. For custom expiry dates:
   + Minimum: 1 day after import
   + Maximum: 90 days after import

Customer Profiles removes expired profiles from the segment and the profiles domain. For more information, see [Data expiration in Customer Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles-data-expiration.html).

**Note**  
Choose an expiry period that aligns with your data retention requirements. Consider whether the default 14-day period meets your business needs before selecting a custom date.

## Create and monitor segment import
<a name="create-monitor-segment-import"></a>

**Create the segment**

1. Review your configuration.

1. Choose **Create segment**.

1. The system will:
   + Upload your CSV file.
   + Create/update profiles based on the data.
   + Group the profiles into a segment.
   + Show progress by using a notification banner.

Monitor import progress
+ View the import progress on the segment details page.
+ The notification banner shows that the import job is in progress.
+ The import job details table shows:
  + File name
  + Import job creation date
  + Import job completion date
  + Number of profiles processed
  + Number of successful imports
  + Number of failed imports
+ You can cancel the import while in progress.
+ The segment can be used in campaigns while the import job is still in progress.

**Note**  
Imported segments can be used like any other segment for outbound campaigns or exports after the import is complete. You can view the segment details, including import status and results, from the segment details page.