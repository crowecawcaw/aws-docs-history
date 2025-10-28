# Getting DICOM bulkdata from HealthImaging

Use the `GetDICOMBulkdata` action to retrieve binary data that has been separated from DICOM metadata in a
HealthImaging data store. When retrieving instance or series metadata, binary attributes larger than 1MB will be
represented by a `BulkDataURI` instead of inline values. You can retrieve the binary data for any primary image
set in the HealthImaging data store by using the `BulkDataURI` provided in the metadata response. You can retrieve bulkdata
for non-Primary image sets by providing the image set ID as a query parameter.

###### To get DICOM bulkdata

When you retrieve DICOM metadata from a HealthImaging DICOMweb WADO-RS action, such as `GetDICOMInstanceMetadata` or `GetDICOMSeriesMetadata`, large binary attributes will be replaced in-line with BulkDataURIs, as shown below:

```
"00451026": {
    "vr": "UN",
    "BulkDataURI": "https://dicom-medical-imaging.us-west-2.amazonaws.com/datastore/<datastoreId>/studies/<StudyInstanceUID>/series/<SeriesInstanceUID>/instances/<SOPInstanceUID>/bulkdata/<bulkdataUriHash>"
}
```

To retrieve a DICOM element with the `GetDICOMBulkdata` action, use the following steps.

1. Construct a URL for the request using the values from the `BulkDataURI`, of the form:

```
https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastore-id`/studies/`study-instance-uid`/series/`series-instance-uid`/instances/`sop-instance-uid`/bulkdata/`bulkdata-uri-hash`
```

2. Issue your `GetDICOMBulkdata` command as an HTTP GET request with [AWS Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md")
   signing protocol. The following code example uses the `curl` command line tool to retrieve a DICOM element from a primary image set:

```
curl --request GET \
  'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/instances/1.2.840.10008.5.1.4.1.1.7/bulkdata/b026324c6904b2a9cb4b88d6d61c81d1' \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/octet-stream' \
  --output 'bulkdata.bin'
```

To retrieve a DICOM data element from a non-primary image set, supply an `ImageSetId` parameter:

```
curl --request GET \
  'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/instances/1.2.840.10008.5.1.4.1.1.7/bulkdata/b026324c6904b2a9cb4b88d6d61c81d1?imageSetId=459e50687f121185f747b67bb60d1bc8' \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/octet-stream' \
  --output 'bulkdata.bin'
```

###### Note

The `imageSetId` parameter is required to retrieve bulkdata for non-primary image sets. The
GetDICOMBulkdata action will only return bulkdata for primary image sets if the `datastoreId`, `studyInstanceUID`,
`seriesInstanceUID`, and `SOPInstanceUID` are specified (without an `imagesetID`).
