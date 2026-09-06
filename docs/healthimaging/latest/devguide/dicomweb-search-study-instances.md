

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthimaging/latest/devguide/dicomweb-search-study-instances.html)

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