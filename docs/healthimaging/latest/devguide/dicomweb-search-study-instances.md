

# Searching for a study's DICOM instances in HealthImaging
<a name="dicomweb-search-study-instances"></a>

Use the `SearchDICOMStudyInstances` API to search for all DICOM instances within a study in an HealthImaging [data store](getting-started-concepts.md#concept-data-store). Construct a request URL with supported DICOM data elements (attributes) to filter results. The API returns instance search results in JSON format, ordered by last update date, descending (latest to oldest).

**To search for a study's DICOM instances**  


1. Collect HealthImaging `region` and `datastoreId` values. For more information, see [Getting data store properties](get-data-store.md).

1. Collect the `StudyInstanceUID` value. For more information, see [Getting image set metadata](get-image-set-metadata.md).

1. Construct a URL for the request, including all applicable search elements. The URL is of the form:

   ```
   GET https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/studies/{{StudyInstanceUID}}/instances[?query]
   ```

   The following table lists the supported DICOM data elements (attributes).


**Instance elements for `SearchDICOMStudyInstances`**  

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
  <tr><td><code>(0008,0016)</code></td><td><code>SOP Class UID</code></td></tr>
  <tr><td><code>(0008,0018)</code></td><td><code>SOP Instance UID</code></td></tr>
</tbody>
</table>


1. Prepare and send your request. `SearchDICOMStudyInstances` uses an HTTP GET request signed with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). The following example uses the `curl` command-line tool. Replace `{{region}}` with your AWS Region. Replace `{{datastoreId}}` with your data store ID. Replace `{{StudyInstanceUID}}` with the study's UID.

------
#### [ curl ]

   ```
   curl --request GET \
     "https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/studies/{{StudyInstanceUID}}/instances[?query]" \
     --aws-sigv4 'aws:amz:{{region}}:medical-imaging' \
     --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
     --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
     --header 'Accept: application/dicom+json' \
     --output results.json
   ```

------