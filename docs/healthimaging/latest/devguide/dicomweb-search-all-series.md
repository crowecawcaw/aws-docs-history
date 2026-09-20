

# Searching for all DICOM series in HealthImaging
<a name="dicomweb-search-all-series"></a>

Use the `SearchDICOMAllSeries` API to search for all DICOM series across an HealthImaging [data store](getting-started-concepts.md#concept-data-store). Construct a request URL with supported DICOM data elements (attributes) to filter results. The API returns series search results in JSON format, ordered by `Series Number (0020,0011)` in ascending order (oldest to latest).

**To search for all DICOM series**  


1. Collect HealthImaging `region` and `datastoreId` values. For more information, see [Getting data store properties](get-data-store.md).

1. Construct a URL for the request, including all applicable Series elements. The URL is of the form:

   ```
   GET https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/series[?query]
   ```

   The following table lists the supported DICOM data elements (attributes).


**Series elements for `SearchDICOMAllSeries`**  

<table>
<thead>
  <tr><th>DICOM element tag</th><th>DICOM element name</th></tr>
</thead>
<tbody>
  <tr><td><code>(0008,0020)</code></td><td><code>Study Date</code></td></tr>
  <tr><td><code>(0008,0030)</code></td><td><code>Study Time</code></td></tr>
  <tr><td><code>(0008,0050)</code></td><td><code>Accession Number</code></td></tr>
  <tr><td><code>(0008,0061)</code></td><td><code>Modalities in Study</code></td></tr>
  <tr><td><code>(0008,0060)</code></td><td><code>Modality</code></td></tr>
  <tr><td><code>(0008,0090)</code></td><td><code>Referring Physician Name</code></td></tr>
  <tr><td><code>(0008,1030)</code></td><td><code>Study Description</code></td></tr>
  <tr><td><code>(0010,0010)</code></td><td><code>Patient Name</code></td></tr>
  <tr><td><code>(0010,0020)</code></td><td><code>Patient ID</code></td></tr>
  <tr><td><code>(0010,0030)</code></td><td><code>Patient BirthDate</code></td></tr>
  <tr><td><code>(0010,0032)</code></td><td><code>Patient BirthTime</code></td></tr>
  <tr><td><code>(0020,000D)</code></td><td><code>Study Instance UID</code></td></tr>
  <tr><td><code>(0020,0010)</code></td><td><code>Study ID</code></td></tr>
  <tr><td><code>(0020,000E)</code></td><td><code>Series Instance UID</code></td></tr>
  <tr><td><code>(0020,0011)</code></td><td><code>Series Number</code></td></tr>
  <tr><td><code>(0040,0244)</code></td><td><code>Performed Procedure Step Start Date</code></td></tr>
  <tr><td><code>(0040,0245)</code></td><td><code>Performed Procedure Step Start Time</code></td></tr>
</tbody>
</table>


1. Prepare and send your request. `SearchDICOMAllSeries` uses an HTTP GET request signed with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). The following example uses the `curl` command-line tool. Replace `{{region}}` with your AWS Region. Replace `{{datastoreId}}` with your data store ID.

------
#### [ curl ]

   ```
   curl --request GET \
     "https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/series[?query]" \
     --aws-sigv4 'aws:amz:{{region}}:medical-imaging' \
     --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
     --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
     --header 'Accept: application/dicom+json' \
     --output results.json
   ```

------