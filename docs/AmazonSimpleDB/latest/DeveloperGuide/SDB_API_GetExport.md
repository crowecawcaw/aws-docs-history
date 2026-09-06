

# GetExport
<a name="SDB_API_GetExport"></a>

## Description
<a name="SDB_API_GetExport_Description"></a>

Returns information about an export from Amazon SimpleDB to Amazon S3. Use this operation to track the status and details of an export.

The `exportDataCutoffTime` represents when domain processing begins, not when the export was requested. Exports are not point-in-time snapshots. All data inserted before this timestamp is included, but data inserted after this timestamp is not included. For existing items, updates or deletions after the cutoff may not be reflected in the export.

## Request Parameters
<a name="SDB_API_GetExport_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  exportArn  | The unique Amazon Resource Name (ARN) of the export, returned by the StartDomainExport operation.<br />Type: String |  Yes  | 

## Response Elements
<a name="SDB_API_GetExport_ResponseElements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  exportArn  | The unique Amazon Resource Name (ARN) of the export. | 
|  clientToken  | The client token used to create the export. | 
|  exportStatus  | The current state of the export. Valid values: PENDING \| IN\_PROGRESS \| SUCCEEDED \| FAILED | 
|  domainName  | The name of the Amazon SimpleDB domain. | 
|  requestedAt  | The timestamp when the export was initiated. | 
|  s3Bucket  | The name of the Amazon S3 bucket. | 
|  s3BucketOwner  | The AWS account ID that owns the Amazon S3 bucket. | 
|  exportDataCutoffTime  | The cutoff timestamp for data inclusion. All data inserted before this timestamp is included in the export. | 
|  failureCode  | The error code if the export status is FAILED. | 
|  failureMessage  | The error message if the export status is FAILED. | 

## Special Errors
<a name="SDB_API_GetExport_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  MissingParameter  | The request must contain the parameter exportArn. | 
|  InvalidParameterValue  | The specified export ARN is invalid. | 

## Examples
<a name="SDB_API_GetExport_Examples"></a>

**Note**  
The new Export APIs don't support sending requests using `query parameters`. This is shown in the following code example.

```
import software.amazon.awssdk.services.simpledbv2.SimpleDbV2Client;
import software.amazon.awssdk.services.simpledbv2.model.GetExportRequest;
import software.amazon.awssdk.services.simpledbv2.model.GetExportResponse;
import software.amazon.awssdk.services.simpledbv2.model.SimpleDbV2Exception;
import software.amazon.awssdk.regions.Region;

public class SimpleDBGetExportExample {

    private SimpleDbV2Client simpleDbClient;

    public SimpleDBGetExportExample(Region region) {
        this.simpleDbClient = SimpleDbV2Client.builder()
            .region(region)
            .build();
    }

    /**
     * Retrieves information about a domain export.
     *
     * @param exportArn the ARN of the export to retrieve
     * @return the export response containing export details
     * @throws SimpleDbV2Exception if the operation fails
     */
    public GetExportResponse getExport(String exportArn) {
        try {
            GetExportRequest request = GetExportRequest.builder()
                .exportArn(exportArn)
                .build();

            GetExportResponse response = simpleDbClient.getExport(request);

            System.out.println("Export ARN: " + response.exportArn());
            System.out.println("Export Status: " + response.exportStatus());
            System.out.println("Domain Name: " + response.domainName());
            System.out.println("Requested At: " + response.requestedAt());

            return response;

        } catch (SimpleDbV2Exception e) {
            System.err.println("Error Code: " + e.awsErrorDetails().errorCode());
            System.err.println("Error Message: " + e.awsErrorDetails().errorMessage());
            System.err.println("HTTP Status Code: " + e.statusCode());
            throw e;
        }
    }
}
```

## Related Actions
<a name="SDB_API_GetExport_Related_Actions"></a>
+  [StartDomainExport](SDB_API_StartDomainExport.md) 
+  [ListExports](SDB_API_ListExports.md) 