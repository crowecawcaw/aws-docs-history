

# ListExports
<a name="SDB_API_ListExports"></a>

## Description
<a name="SDB_API_ListExports_Description"></a>

Lists all exports created in an AWS account. Results are paginated and can be filtered by domain name. Returns exports created within the past 3 months.

## Request Parameters
<a name="SDB_API_ListExports_RequestParameters"></a>


|  Name  |  Description  |  Required | 
| --- | --- | --- | 
|  domainName  | Filter exports by domain name. If not specified, returns exports for all domains.<br />Type: String |  No  | 
|  maxResults  | The maximum number of exports to return in a single call.<br />Type: Integer |  No  | 
|  nextToken  | The pagination token from a previous ListExports response. Use this to retrieve the next page of results.<br />Type: String |  No  | 

## Response Elements
<a name="SDB_API_ListExports_ResponseElements"></a>


|  Name  |  Description  | 
| --- | --- | 
|  exportSummaries  | A list of export summaries. | 
|  exportSummaries[].exportArn  | The unique Amazon Resource Name (ARN) of the export. | 
|  exportSummaries[].exportStatus  | The current state of the export. Valid values: PENDING \| IN\_PROGRESS \| SUCCEEDED \| FAILED | 
|  exportSummaries[].domainName  | The name of the Amazon SimpleDB domain. | 
|  nextToken  | The token to use for retrieving the next page of results. Present only if more results are available. | 

## Special Errors
<a name="SDB_API_ListExports_SpecialErrors"></a>


|  Error  |  Description  | 
| --- | --- | 
|  InvalidParameterValue  | One or more parameter values are invalid. | 

## Examples
<a name="SDB_API_ListExports_Examples"></a>

**Note**  
The new Export APIs don't support sending requests using `query parameters`. This is shown in the following code example.

```
import software.amazon.awssdk.services.simpledbv2.SimpleDbV2Client;
import software.amazon.awssdk.services.simpledbv2.model.ListExportsRequest;
import software.amazon.awssdk.services.simpledbv2.model.ListExportsResponse;
import software.amazon.awssdk.services.simpledbv2.model.ExportSummary;
import software.amazon.awssdk.services.simpledbv2.model.SimpleDbV2Exception;
import software.amazon.awssdk.regions.Region;

public class SimpleDBListExportsExample {

    private SimpleDbV2Client simpleDbClient;

    public SimpleDBListExportsExample(Region region) {
        this.simpleDbClient = SimpleDbV2Client.builder()
            .region(region)
            .build();
    }

    /**
     * Lists all exports in the account.
     *
     * @param domainName optional domain name to filter exports (can be null)
     * @param maxResults optional maximum number of results to return (can be null)
     * @param nextToken optional pagination token from previous response (can be null)
     * @return the list exports response
     * @throws SimpleDbV2Exception if the operation fails
     */
    public ListExportsResponse listExports(String domainName, Integer maxResults, String nextToken) {
        try {
            ListExportsRequest.Builder requestBuilder = ListExportsRequest.builder();

            if (domainName != null && !domainName.isEmpty()) {
                requestBuilder.domainName(domainName);
            }
            if (maxResults != null) {
                requestBuilder.maxResults(maxResults);
            }
            if (nextToken != null && !nextToken.isEmpty()) {
                requestBuilder.nextToken(nextToken);
            }

            ListExportsRequest request = requestBuilder.build();
            ListExportsResponse response = simpleDbClient.listExports(request);

            System.out.println("Exports found: " + response.exportSummaries().size());
            for (ExportSummary summary : response.exportSummaries()) {
                System.out.println("Export ARN: " + summary.exportArn());
                System.out.println("Status: " + summary.exportStatus());
                System.out.println("Domain: " + summary.domainName());
                System.out.println("---");
            }

            if (response.nextToken() != null) {
                System.out.println("More results available. Next token: " + response.nextToken());
            }

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
<a name="SDB_API_ListExports_Related_Actions"></a>
+  [StartDomainExport](SDB_API_StartDomainExport.md) 
+  [GetExport](SDB_API_GetExport.md) 