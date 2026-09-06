

# StartDomainExport
<a name="SDB_API_StartDomainExport"></a>

## Description
<a name="SDB_API_StartDomainExport_Description"></a>

Initiates an export of data from an Amazon SimpleDB domain to an Amazon S3 bucket. The export process runs in the background and does not affect the performance of your active database. The exported data is stored in standard JSON format.

You can optionally encrypt the exported data in Amazon S3 by providing a customer managed AWS KMS key, or use the default encryption. The KMS key only encrypts the exported data artifacts in Amazon S3, not the Amazon S3 bucket or Amazon SimpleDB internal data storage.

**Note**  
If the export fails mid-process, no automatic cleanup occurs. Partial data may remain in the Amazon S3 bucket and must be manually removed.

## Request Parameters
<a name="SDB_API_StartDomainExport_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  clientToken  | A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon SimpleDB ignores the request, but does not return an error.<br />Type: String |  Yes  | 
|  domainName  | The name of the Amazon SimpleDB domain to export.<br />Type: String |  Yes  | 
|  s3Bucket  | The name of the Amazon S3 bucket where the exported data will be stored.<br />Type: String |  Yes  | 
|  s3KeyPrefix  | The prefix for Amazon S3 object keys of the export artifacts. If specified, data is written to `s3KeyPrefix/AWSSimpleDB/<exportId>/<domainName>/`.<br />Type: String |  No  | 
|  s3BucketOwner  | The AWS account ID that owns the Amazon S3 bucket. Required for cross-account exports.<br />Type: String |  No  | 
|  s3SseAlgorithm  | The server-side encryption algorithm to use for the exported data in Amazon S3.<br />Type: String<br />Valid values: `AES256` \| `KMS` |  No  | 
|  s3SseKmsKeyId  | The AWS KMS key ID to use for encryption. Required when `s3SseAlgorithm` is set to `KMS` and using a customer managed key.<br />Type: String |  No  | 

## Response Elements
<a name="SDB_API_StartDomainExport_ResponseElements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  clientToken  | The client token provided in the request. | 
|  exportArn  | The unique Amazon Resource Name (ARN) for the export. | 
|  requestedAt  | The timestamp when the export was requested. | 

## Special Errors
<a name="SDB_API_StartDomainExport_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  MissingParameter  | The request must contain the required parameters. | 
|  NoSuchDomain  | The specified domain does not exist. | 
|  InvalidParameterValue  | One or more parameter values are invalid. | 

## Examples
<a name="SDB_API_StartDomainExport_Examples"></a>

**Note**  
The new Export APIs don't support sending requests using `query parameters`. This is shown in the following code example.

```
import software.amazon.awssdk.services.simpledbv2.SimpleDbV2Client;
import software.amazon.awssdk.services.simpledbv2.model.StartDomainExportRequest;
import software.amazon.awssdk.services.simpledbv2.model.StartDomainExportResponse;
import software.amazon.awssdk.services.simpledbv2.model.SimpleDbV2Exception;
import software.amazon.awssdk.regions.Region;

public class SimpleDBDomainExportExample {
    
    private SimpleDbV2Client simpleDbClient;
    
    public SimpleDBDomainExportExample(Region region) {
        this.simpleDbClient = SimpleDbV2Client.builder()
            .region(region)
            .build();
    }
    
    /**
     * Starts a domain export to S3 bucket.
     *
     * @param domainName the name of the SimpleDB domain to export
     * @param s3BucketName the S3 bucket name where export will be stored
     * @param s3BucketOwner the AWS account ID that owns the S3 bucket
     * @return the export ARN
     * @throws SimpleDbV2Exception if the export operation fails
     */
    public String startDomainExport(String domainName, String s3BucketName, String s3BucketOwner) {
        try {
            StartDomainExportRequest request = StartDomainExportRequest.builder()
                .domainName(domainName)
                .s3Bucket(s3BucketName)
                .s3BucketOwner(s3BucketOwner)
                .build();
            
            StartDomainExportResponse response = simpleDbClient.startDomainExport(request);
        
            System.out.println("Export ARN: " + response.exportArn());
            System.out.println("Requested At: " + response.requestedAt());
            
            return response.exportArn();
            
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
<a name="SDB_API_StartDomainExport_Related_Actions"></a>
+  [GetExport](SDB_API_GetExport.md) 
+  [ListExports](SDB_API_ListExports.md) 