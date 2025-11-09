# Searching for DICOM instances in HealthImaging

Use the `SearchDICOMInstances` API to search for DICOM instances in a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). You can search for DICOM instances in HealthImaging by
constructing a URL that includes supported DICOM data elements (attributes). The Instance results
are returned in JSON format, ordered by ascending (oldest to latest).

###### To search for DICOM instances

1. Collect HealthImaging `region` and `datastoreId` values. For more
   information, see [Getting data store properties](get-data-store.md "get-data-store.md").
2. Collect values for `StudyInstanceUID` and `SeriesInstanceUID`. For
   more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md").
3. Construct a URL for the request, including all applicable search elements. To view the
   entire URL path in the following example, scroll over the **Copy** button.
   The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastoreId`/studies/`StudyInstanceUID`/series/`SeriesInstanceUID`/instances[?query]
```

| Instance elements for `SearchDICOMInstances` | DICOM element tag  | DICOM element name |
| -------------------------------------------- | ------------------ | ------------------ |
| `(0008,0016)`                                | `SOP Class UID`    |
| `(0008,0018)`                                | `SOP Instance UID` |

4. Prepare and send your request. `SearchDICOMInstances` uses a HTTP GET request
   with [AWS Signature
   Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following example uses the `curl` command
   line tool to search for information about DICOM instances.

curl

```
curl --request GET \
  "https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/`datastoreId`/studies/`StudyInstanceUID`/series/`SeriesInstanceUID`/instances[?query]"
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/dicom+json' \
  --output results.json

```

Instance search results are returned in JSON format, ordered by `Instance Number
 (0020,0013)` in ascending order (oldest to latest)
