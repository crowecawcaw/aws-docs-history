# Create segments from imported

files in Amazon Connect

###### Note

To access the segmentation builder experience in the Amazon Connect admin website, ensure that the
appropriate security profiles permissions are configured. For more information,
see [Assign security
profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md "security-profile-customer-profile-segmentation.md").

Customer segment import uses a CSV file containing profile data to create new
profiles or update existing ones, which are then grouped into a segment. The CSV
file must be under 1GB in size and include valid headers that map to standard
profile attributes.

The following steps describe creating and configuring an imported customer
segment:

1. [Create a new segment](#create-new-segment "#create-new-segment")
2. [Upload CSV file](#upload-csv-file "#upload-csv-file")
3. [Configure segment details](#configure-segment-details "#configure-segment-details")
4. [Map customer attributes](#map-customer-attributes "#map-customer-attributes")
5. [Set profile expiry](#set-profile-expiry "#set-profile-expiry")
6. [Create and monitor segment
   import](#create-monitor-segment-import "#create-monitor-segment-import")

## Create a new segment

1. To create a segment, ensure that you have created security profiles
   permissions as a prerequisite. For more information, see [Assign security
   profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md "security-profile-customer-profile-segmentation.md").
2. In the Amazon Connect admin website, navigate to
3. Choose **Create segment** and select **From
   file upload** from the dropdown

## Upload CSV file

Choose a CSV file by either:

- Choosing **Choose file** and selecting your
  file.
- Dragging and dropping your file into the upload area.

The file must be:

- In CSV format
- Under 1GB in size
- Contain headers
- UTF-8 encoded

## Configure segment details

For **Name**, specify a recognizable identifier
for your segment. This field is required.

- Use only letters (a-z, A-Z), numbers (0-9), hyphens (-), or
  underscores (\_)
- Begin with a letter or number (not an underscore)
- Maximum length of 255 characters

###### Note

The Amazon Connect admin website uses this name as the `DisplayName` of the segment
and generates a unique `SegmentDefinitionName` identifier. This
identifier is used when accessing the segment through Amazon Connect Customer Profiles APIs.

For **Description**, (optional), add details
about your segment:

- Maximum length of 1000 characters

## Map customer attributes

Object type mapping defines how Customer Profiles processes your CSV data. This
mapping:

- Determines how CSV data populates standard profile objects.
- Specifies which fields to index for profile assignment.

For more information about object type mapping, see [Create and ingest customer data
into Customer Profiles](customer-profiles-object-type-mappings.md "customer-profiles-object-type-mappings.md").

Choose one of these options to map your CSV columns to Customer Profiles attributes:

### Option 1: AI-powered mapping (Recommended)

1. Choose **Generate customer attributes**, then
   choose **Next**.
2. The system analyzes your CSV headers and suggests appropriate
   mappings to standard profile attributes.
3. Review the suggested mappings.
4. Optional: Customize the mappings:
   - Modify standard profile attribute mappings.
   - Add custom attributes using the format:
     `Attributes.`attribute-name``.
   - Update the unique identifier.

### Option 2: Manual mapping

1. Map each CSV column header to a profile attribute:
   - Use standard profile attributes. For a complete list, see
     [Standard profile definition in
     the Amazon Connect Customer Profiles](standard-profile-definition.md "standard-profile-definition.md").
   - Create custom attributes using the format:
     `Attributes.`attribute-name``.

###### Note

You can map up to 25 attributes. 2. Choose one mapped attribute as the customer identifier (unique
key).

### Choose a customer identifier

After completing the mapping, choose one mapped attribute as the customer
identifier. Amazon Connect Customer Profiles uses this identifier to:

- Create new profiles or update existing ones.
- Match incoming data with existing profiles.

###### Note

Attribute mappings can be modified at any time during setup, whether
using AI-powered or manual mapping.

## Set profile expiry

Specify when imported profiles expire:

1. Choose an expiry option:
   - Default: 14 days from import date
   - Custom: Select a date using the date picker

2. For custom expiry dates:
   - Minimum: 1 day after import
   - Maximum: 90 days after import

Customer Profiles removes expired profiles from the segment and the profiles domain.

###### Note

Choose an expiry period that aligns with your data retention requirements.
Consider whether the default 14-day period meets your business needs before
selecting a custom date.

## Create and monitor segment

import

###### Create the segment

1. Review your configuration.
2. Choose **Create segment**.
3. The system will:
   - Upload your CSV file.
   - Create/update profiles based on the data.
   - Group the profiles into a segment.
   - Show progress by using a notification banner.

Monitor import progress

- View the import progress on the segment details page.
- The notification banner shows that the import job is in
  progress.
- The import job details table shows:
  - File name
  - Import job creation date
  - Import job completion date
  - Number of profiles processed
  - Number of successful imports
  - Number of failed imports

- You can cancel the import while in progress.
- The segment can be used in campaigns while the import job is still in
  progress.

###### Note

Imported segments can be used like any other segment for outbound
campaigns or exports once the import is complete. You can view the segment
details, including import status and results, from the segment details
page.
