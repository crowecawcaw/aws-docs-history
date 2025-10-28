# Adding a new data source

You can use AWS Supply Chain to ingest your data stored in your data source and
extract your supply chain information. AWS Supply Chain can store the extracted information
in your Amazon S3 buckets and use the data for _Demand planning_, _Insights_, _Supply Planning_, _N-Tier Visibility_, _Work Order Insights_, and _Sustainability_.

###### Topics

- [Prerequisites to ingest data](#data_prerequisites-profiles "#data_prerequisites-profiles")
- [Uploading files for the first time](uploading_files.md "uploading_files.md")
- [Connecting to an EDI](connecting-edi.md "connecting-edi.md")
- [Connecting to S/4 HANA](connecting-sap-hana.md "connecting-sap-hana.md")
- [Connecting to SAP ECC 6.0](connecting-sap-ecc.md "connecting-sap-ecc.md")
- [Adding a new outbound source for Supply Planning](adding_new_outbound_connector.md "adding_new_outbound_connector.md")

## Prerequisites to ingest data

Note the following before uploading your datasets for ingestion:

- The file that you upload should be less than 5 GB.
- The content in the dataset should follow the UTF-8 encoding format.
- The file type must be supported by the connector. The connectors for SAP systems
  supports CSV, EDI connector supports .txt and .edi formats, and Amazon S3
  supports CSV.
- Data rows must contain non-null values for the required fields.
- The date and time format should follow the ISO8601 standards. For example, 2020-07-10 15:00:00.000, represents the 10th of July 2020 at 3 pm.
- The column names in the dataset shouldn't contain spaces or special characters. Column names should be separated by an underscore (\_) between two words.
- When using the Amazon S3 source path, AWS Supply Chain will create a parent folder named after
  the source system that you selected. Sub-folders are named after the source
  table that you selected. Make sure that the file names are unique. The file
  structure that you build will be used to create the Amazon S3 path.
- AWS Supply Chain follows a multi-step upload process with pre-assigned URLs. Due to browser
  security restrictions, to upload your dataset, your S3 bucket cross-origin
  resource sharing (CORS) permissions must allow _PUT_ requests
  and return an _ETag_ header. To update the CORS policy on
  your Amazon S3 bucket, under **Connections**, scroll-down to CORS
  and paste the following policy:

```

                `[
 {
 "AllowedHeaders": [
 "*"
 ],
 "AllowedMethods": [
 "PUT"
 ],
 "AllowedOrigins": [
 "https://`instance-id`.scn.global.on.aws"
 ],
 "ExposeHeaders": [
 "Etag"
 ]
 }
 ]`

```
