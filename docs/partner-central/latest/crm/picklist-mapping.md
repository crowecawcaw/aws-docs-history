# Picklist mapping

The picklist dialog box allows limited and extended mappings between the partner’s
picklist field and APN. The **ACE Mappings** page also has an Auto Map
function if using the provided **custom ACE opportunity object** . For more information about the object, refer to
[Using a standard Salesforce object or
custom object](crm-connector-mapping.md#custom-ace-opportunity-object "crm-connector-mapping.md#custom-ace-opportunity-object") later in this guide.

If an exact match is found between the partner’s field values and APN, those
values are mapped automatically. The option for extended mapping lets partners map a single
APN value to multiple sources, configure additional target mappings, and set default
mappings.

## Limited mapping

1. On the **ACE Mappings**
   page, select a source field, and then choose **Map Values**.

The mapping dialog box appears. 2. For **Step 1: Primary APN Values**, choose either **Auto
Map** or the Salesforce value for the corresponding ACE pipeline manager,
and then choose **Save**. 3. Repeat steps 1 and 2 as necessary to map all of your ACE pipeline manager values. 4. To close the mapping dialog box, choose **Close**.

Partners receive a confirmation message that the value mappings were saved.

## Extended mapping

1. If the same source value maps to multiple APN values, proceed with the mapping as
   previously described.
2. On the **Primary APN Values** tab, choose the same value mapping
   for multiple APN values.
3. If unmapped values exist in the partner’s organization, the **Additional
   APN Value** tab lets you map additional values to APN. This helps partners
   ensure that all applicable values in their organization are mapped to appropriate APN
   values.
4. If a single value in the partner’s organization is mapped to more than one APN
   value, use the **Secondary APN Values** tab to set the default value
   for outbound integrations.
