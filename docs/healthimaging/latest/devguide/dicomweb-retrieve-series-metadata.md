# Getting DICOM series metadata from

HealthImaging

Use the `GetDICOMSeriesMetadata` action to retrieve the metadata for a DICOM
series (`.json` file) from a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store").
You can retrieve series metadata for any primary [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set")
in the HealthImaging data store by specifying the Study and Series UIDs associated with the resource.
You can retrieve series metadata for non-Primary image sets by providing the image set ID as a query
parameter. The series metadata is returned in `DICOM JSON` format.

###### To get DICOM series metadata (`.json`)

1. Collect HealthImaging `datastoreId` and `imageSetId` parameter values.
2. Construct a URL for the request using the values for `datastoreId`,
   `studyInstanceUID`, `seriesInstanceUID`, and optionally
   `imageSetId`. To view the entire URL path in the following example, scroll over the
   **Copy** button. The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastore-id`/studies/`study-instance-uid`/series/`series-instance-uid`/metadata
```

3. Prepare and send your request. `GetDICOMSeriesMetadata` uses a HTTP GET
   request with [AWS
   Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following code example uses the
   `curl` command line tool to get metadata (`.json`
   file) from HealthImaging.

Shell

```
curl --request GET \
 'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/metadata \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/dicom+json' \
  --output 'series-metadata.json'

```

With the optional `imageSetId` parameter.

Shell

```
curl --request GET \
  'https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/d9a2a515ab294163a2d2f4069eed584c/studies/1.3.6.1.4.1.5962.1.2.4.20040826285059.5457/series/1.3.6.1.4.1.5962.1.3.4.1.20040825185059.5457/metadata?imageSetId=459e50687f121185f747b67bb60d1bc8' \
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/dicom+json' \
  --output 'series-metadata.json'

```

###### Note

    * The `imageSetId` parameter is required to retrieve series metadata for non-primary
     image sets. The `GetDICOMInstanceMetadata` action will only return series metadata for
     primary image sets if the `datastoreId`, `studyInstanceUID`, `seriesInstanceUID`
     are specified (without an `imagesetID`).
