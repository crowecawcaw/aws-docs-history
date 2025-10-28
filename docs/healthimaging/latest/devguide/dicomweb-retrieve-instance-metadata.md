# Getting DICOM instance metadata from

HealthImaging

Use the `GetDICOMInstanceMetadata` action to retrieve the metadata from a DICOM
instance in a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") by specifying the
Series, Study, and Instance UIDs associated with the resource. The API will only return instance
metadata from primary image sets unless the optional [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set")
parameter is provided. You can retrieve any instance metadata (from primary or non-primary image sets)
in the data store by specifying the `imageSetId` as a query parameter.

###### To get DICOM instance metadata (`.json`)

1. Collect HealthImaging `datastoreId` and `imageSetId` parameter values.
2. Use the [`GetImageSetMetadata`](../APIReference/API_GetImageSetMetadata.md "../APIReference/API_GetImageSetMetadata.md") action with the `datastoreId` and
   `imageSetId` parameter values to retrieve associated metadata values for
   `studyInstanceUID`, `seriesInstanceUID`, and `sopInstanceUID`.
   For more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md").
3. Construct a URL for the request using the values for `datastoreId`,
   `studyInstanceUID`, `seriesInstanceUID`, `sopInstanceUID`, and
   `imageSetId`. To view the entire URL path in the following example, scroll over the
   **Copy** button. The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastore-id`/studies/`study-instance-uid`/series/`series-instance-uid`/instances/`sop-instance-uid`/metadata?imageSetId=`image-set-id`

```

4. Prepare and send your request. `GetDICOMInstanceMetadata` uses a HTTP GET
   request with [AWS
   Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following code example uses the
   `curl` command line tool to get DICOM instance metadata (`.json`
   file) from HealthImaging.

Shell

```
curl --request GET \
  'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/instances/1.3.6.1.4.1.5962.1.1.4.1.1.20040826186059.5457/metadata?imageSetId=459e50687f121185f747b67bb60d1bc8' \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/dicom+json'

```

###### Note

The Transfer Syntax UID indicated in the metadata matches the Stored Transfer Syntax UID
(`StoredTransferSyntaxUID`) in HealthImaging.
