# Searching for all DICOM instances in HealthImaging

Use the `SearchDICOMAllInstances` API to search for all DICOM instances across an
HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store"). Construct a URL that includes
supported DICOM data elements (attributes) to filter results. The API returns instance search
results in JSON format, ordered by `Instance Number (0020,0013)` in ascending order
(oldest to latest).

###### To search for all DICOM instances

1. Collect HealthImaging `region` and `datastoreId` values. For more
   information, see [Getting data store properties](get-data-store.md "get-data-store.md").
2. Construct a URL for the request, including all applicable search elements.
   The URL is of the form:

```
GET https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastoreId`/instances[?query]
```

The following table lists the supported DICOM data elements (attributes).

Instance elements for `SearchDICOMAllInstances`| DICOM element tag | DICOM element name |
| --- | --- |
| `(0008,0020)` | `Study Date` |
| `(0008,0030)` | `Study Time` |
| `(0008,0050)` | `Accession Number` |
| `(0008,0061)` | `Modalities in Study` |
| `(0008,0060)` | `Modality` |
| `(0008,0090)` | `Referring Physician Name` |
| `(0008,1030)` | `Study Description` |
| `(0010,0010)` | `Patient Name` |
| `(0010,0020)` | `Patient ID` |
| `(0010,0030)` | `Patient BirthDate` |
| `(0010,0032)` | `Patient BirthTime` |
| `(0020,000D)` | `Study Instance UID` |
| `(0020,0010)` | `Study ID` |
| `(0020,000E)` | `Series Instance UID` |
| `(0020,0011)` | `Series Number` |
| `(0040,0244)` | `Performed Procedure Step Start Date` |
| `(0040,0245)` | `Performed Procedure Step Start Time` |
| `(0008,0016)` | `SOP Class UID` |
| `(0008,0018)` | `SOP Instance UID` | 3. Prepare and send your request. `SearchDICOMAllInstances` uses an HTTP GET
request signed with [AWS
Signature Version 4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md"). The following example uses the `curl` command-line
tool. Replace `region` with your AWS Region. Replace
`datastoreId` with your data store ID.

curl

```
curl --request GET \
  "https://dicom-medical-imaging.`region`.amazonaws.com/datastore/`datastoreId`/instances[?query]" \
  --aws-sigv4 'aws:amz:`region`:medical-imaging' \
  --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
  --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
  --header 'Accept: application/dicom+json' \
  --output results.json

```
