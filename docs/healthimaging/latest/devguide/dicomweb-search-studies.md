# Searching for DICOM studies in HealthImaging

Use the `SearchDICOMStudies` API to search for DICOM studies in a HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). You can search for DICOM studies in HealthImaging by
constructing a URL that includes supported DICOM data elements (attributes). Study search results
are returned in JSON format, ordered by last update, date descending (latest to oldest).

###### To search for DICOM studies

1. Collect HealthImaging `region` and `datastoreId` values. For more
   information, see [Getting data store properties](get-data-store.md "get-data-store.md").
2. Construct a URL for the request, including all applicable Study elements. To view the
   entire URL path in the following example, scroll over the **Copy** button.
   The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastoreId`/studies[?query]
```

| Study elements for `SearchDICOMStudies` | DICOM element tag          | DICOM element name |
| --------------------------------------- | -------------------------- | ------------------ |
| `(0008,0020)`                           | `Study Date`               |
| `(0008,0030)`                           | `StudyTime`                |
| `(0008,0050)`                           | `Accession Number`         |
| `(0008,0061)`                           | `Modalities in Study`      |
| `(0008,0090)`                           | `Referring Physician Name` |
| `(0008,1030)`                           | `Study Description`        |
| `(0010,0010)`                           | `Patient Name`             |
| `(0010,0020)`                           | `Patient ID`               |
| `(0010,0030)`                           | `Patient BirthDate`        |
| `(0010,0032)`                           | `Patient BirthTime`        |
| `(0020,000D)`                           | `Study Instance UID`       |
| `(0020,0010)`                           | `Study ID`                 |

3. Prepare and send your request. `SearchDICOMStudies` uses a HTTP GET request with
   [AWS Signature
   Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following example uses the `curl` command
   line tool to search for information about DICOM studies.

curl

```
curl --request GET \
  "https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/`datastoreId`/studies[?query]"
  --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/dicom+json' \
  --output results.json

```

Study search results are returned in JSON format, ordered by last update, date
descending (latest to oldest).
