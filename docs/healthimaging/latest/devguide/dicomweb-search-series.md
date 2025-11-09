# Searching for DICOM series in HealthImaging

Use the `SearchDICOMSeries` API to search for DICOM series in a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). You can search for DICOM series in HealthImaging by
constructing a URL that includes supported DICOM data elements (attributes). Series search results
are returned in JSON format, ordered by ascending (oldest to latest).

###### To search for DICOM series

1. Collect HealthImaging `region` and `datastoreId` values. For more
   information, see [Getting data store properties](get-data-store.md "get-data-store.md").
2. Collect the `StudyInstanceUID` value. For more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md").
3. Construct a URL for the request, including all applicable Series elements. To view the
   entire URL path in the following example, scroll over the **Copy** button.
   The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastoreId`/studies/`StudyInstanceUID`/series[?query]
```

| Series elements for `SearchDICOMSeries` | DICOM element tag     | DICOM element name |
| --------------------------------------- | --------------------- | ------------------ |
| `(0008,0060)`                           | `Modality`            |
| `(0020,000E)`                           | `Series Instance UID` |

4. Prepare and send your request. `SearchDICOMSeries` uses a HTTP GET request with
   [AWS Signature
   Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following example uses the `curl` command
   line tool to search for DICOM series information.

curl

```
curl --request GET \
  "https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/`datastoreId`/studies/`StudyInstanceUID`/series[?query]"
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/dicom+json' \
  --output results.json

```

Series search results are returned in JSON format, ordered by `Series Number
 (0020,0011)` in ascending order (oldest to latest).
