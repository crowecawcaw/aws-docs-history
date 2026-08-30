# Features not supported in the new data preparation experience

While the new data preparation experience offers enhanced capabilities, some features from the legacy experience are
not yet supported. This section outlines these features and provides guidance for handling affected workflows.

When using unsupported data sources, Amazon Quick Sight automatically defaults to the legacy experience. For other unsupported
features, select **Switch to legacy experience** in the top right corner of the data preparation page.
Rules Datasets created in the legacy experience remain compatible with both legacy and new experience datasets.

###### Note

The new data preparation experience now supports the following features:

- Google Sheets
- Incremental refresh
- JODA date formats
- Column folders
- Column descriptions
- Geospatial data type
- SPICE and Direct Query parent dataset selection from the legacy experience (you can now use a legacy SPICE or Direct Query dataset as a parent for a new experience dataset).

###### Setting the geospatial type

You set the geospatial type on the **Output** tab, not through
**Change data type** on the **Transform** tab. Geospatial types
(such as latitude and longitude) are not part of the regular data types. Because Amazon Quick Sight does not
apply further transformations to these columns, it places them on the **Output** tab.

To set the geospatial type of a column:

1. On the data preparation page, choose the **Output** tab at the top
   (next to **Transform**).
2. In the **Schema** pane on the left, choose the column you want to set
   (for example, **City**).
3. Open the **Geospatial type** dropdown and choose a value, such as
   **Country**, **State**, **County**,
   **City**, **Postcode**, **Latitude**, or
   **Longitude**. To clear the geospatial type, choose **Unspecified**.

## Unsupported data sources

The following data sources are currently available only in the legacy experience.

| Data Source  | Details                                     |
| ------------ | ------------------------------------------- |
| Salesforce   | Automatically defaults to legacy experience |
| S3 Analytics | **S3 data sources are supported**           |

## Other unsupported features

The following features are currently available only in the legacy experience.

| Feature Category      | Unsupported features                                                                                                                                                                                                               |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dataset Management    | [Dataset parameters](dataset-parameters.md "dataset-parameters.md")                                                                                                                                                                |
| Data Types            | [ELF/CLF formats](supported-data-sources.md#file-data-sources "supported-data-sources.md#file-data-sources"),<br>[Zip/GZip files in S3](supported-data-sources.md#file-data-sources "supported-data-sources.md#file-data-sources") |
| Configuration Options | ["Start from row" in file upload settings](choosing-file-upload-settings.md "choosing-file-upload-settings.md")                                                                                                                    |
| Calculated Fields     | UnMaterialized Calculated Columns (UMCC)                                                                                                                                                                                           |
| Geospatial            | Geo Hierarchy                                                                                                                                                                                                                      |

## Future development

Amazon Quick Sight plans to implement these features in the new data preparation experience in the future. This approach
ensures that the initial launch for the new data preparation experience prioritizes:

**Enhanced capabilities**

- Visual transformation workflows
- Improved process transparency
- Advanced preparation techniques through Divergence
- Powerful new features like Append, Aggregate, and Pivot

**Flexible adoption**

Users can choose between experiences before publishing datasets, ensuring uninterrupted workflows while teams transition
at their own pace. This approach allows immediate access to new capabilities while maintaining support for specialized
requirements through the legacy experience.
