

# Searching for DICOM studies in HealthImaging
<a name="dicomweb-search-studies"></a>

Use the `SearchDICOMStudies` API to search for DICOM studies in a HealthImaging [data store](getting-started-concepts.md#concept-data-store). You can search for DICOM studies in HealthImaging by constructing a URL that includes supported DICOM data elements (attributes). Study search results are returned in JSON format, ordered by last update, date descending (latest to oldest).

**To search for DICOM studies**  


1. Collect HealthImaging `region` and `datastoreId` values. For more information, see [Getting data store properties](get-data-store.md).

1. Construct a URL for the request, including all applicable Study elements. To view the entire URL path in the following example, scroll over the **Copy** button. The URL is of the form:

   ```
   GET https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/studies[?query]
   ```


**Study elements for `SearchDICOMStudies`**  

<table>
<thead>
  <tr><th>DICOM element tag</th><th>DICOM element name</th></tr>
</thead>
<tbody>
  <tr><td><code>(0008,0020)</code></td><td><code>Study Date</code></td></tr>
  <tr><td><code>(0008,0030)</code></td><td><code>StudyTime</code></td></tr>
  <tr><td><code>(0008,0050)</code></td><td><code>Accession Number</code></td></tr>
  <tr><td><code>(0008,0061)</code></td><td><code>Modalities in Study</code></td></tr>
  <tr><td><code>(0008,0090)</code></td><td><code>Referring Physician Name</code></td></tr>
  <tr><td><code>(0008,1030)</code></td><td><code>Study Description</code></td></tr>
  <tr><td><code>(0010,0010)</code></td><td><code>Patient Name</code></td></tr>
  <tr><td><code>(0010,0020)</code></td><td><code>Patient ID</code></td></tr>
  <tr><td><code>(0010,0030)</code></td><td><code>Patient BirthDate</code></td></tr>
  <tr><td><code>(0010,0032)</code></td><td><code>Patient BirthTime</code></td></tr>
  <tr><td><code>(0020,000D)</code></td><td><code>Study Instance UID</code></td></tr>
  <tr><td><code>(0020,0010)</code></td><td><code>Study ID</code></td></tr>
</tbody>
</table>


1. Prepare and send your request. `SearchDICOMStudies` uses a HTTP GET request with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) signing protocol. The following example uses the `curl` command line tool to search for information about DICOM studies.

------
#### [ curl ]

   ```
   curl --request GET \
     "https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/{{datastoreId}}/studies[?query]"
     --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
     --user "{{$AWS_ACCESS_KEY_ID}}:{{$AWS_SECRET_ACCESS_KEY}}" \
     --header "x-amz-security-token:{{$AWS_SESSION_TOKEN}}" \
     --header 'Accept: application/dicom+json' \
     --output results.json
   ```

   Study search results are returned in JSON format, ordered by last update, date descending (latest to oldest).

------