

# Searching for DICOM instances in HealthImaging
<a name="dicomweb-search-instances"></a>

Use the `SearchDICOMInstances` API to search for DICOM instances in a HealthImaging [data store](getting-started-concepts.md#concept-data-store). You can search for DICOM instances in HealthImaging by constructing a URL that includes supported DICOM data elements (attributes). The Instance results are returned in JSON format, ordered by ascending (oldest to latest).

**To search for DICOM instances**  


1. Collect HealthImaging `region` and `datastoreId` values. For more information, see [Getting data store properties](get-data-store.md).

1. Collect values for `StudyInstanceUID` and `SeriesInstanceUID`. For more information, see [Getting image set metadata](get-image-set-metadata.md).

1. Construct a URL for the request, including all applicable search elements. To view the entire URL path in the following example, scroll over the **Copy** button. The URL is of the form:

   ```
   GET https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/studies/{{StudyInstanceUID}}/series/{{SeriesInstanceUID}}/instances[?query]
   ```  
**Instance elements for `SearchDICOMInstances`**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthimaging/latest/devguide/dicomweb-search-instances.html)

   HealthImaging uses the DICOM element [(0008,1196)](https://dicom.nema.org/dicom/2013/output/chtml/part18/sect_6.6.html#sect_6.6.1.3.2.1.1) to persist import warning codes. The import warning codes are searchable at the instance level. Import warning codes may be searched with wildcard or specific warning codes. See [HealthImaging Warning Codes](reference-warning-codes.md).

1. Prepare and send your request. `SearchDICOMInstances` uses a HTTP GET request with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) signing protocol. The following example uses the `curl` command line tool to search for information about DICOM instances.

------
#### [ curl ]

   ```
   curl --request GET \
     "https://dicom-medical-imaging.us-east-1.amazonaws.com/datastore/{{datastoreId}}/studies/{{StudyInstanceUID}}/series/{{SeriesInstanceUID}}/instances[?query]"
     --aws-sigv4 'aws:amz:us-east-1:medical-imaging' \
     --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
     --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
     --header 'Accept: application/dicom+json' \
     --output results.json
   ```

   Instance search results are returned in JSON format, ordered by `Instance Number (0020,0013)` in ascending order (oldest to latest)

------