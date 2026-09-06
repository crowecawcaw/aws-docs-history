

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthimaging/latest/devguide/dicomweb-search-studies.html)

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