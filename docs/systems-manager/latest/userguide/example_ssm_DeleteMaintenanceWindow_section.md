

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeleteMaintenanceWindow` with an AWS SDK or CLI
<a name="example_ssm_DeleteMaintenanceWindow_section"></a>

The following code examples show how to use `DeleteMaintenanceWindow`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_ssm_Scenario_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a maintenance window**  
This `delete-maintenance-window` example removes the specified maintenance window.  

```
aws ssm delete-maintenance-window \
    --window-id {{"mw-1a2b3c4d5e6f7g8h9"}}
```
Output:  

```
{
    "WindowId":"mw-1a2b3c4d5e6f7g8h9"
}
```
For more information, see [Delete a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-delete-mw.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeleteMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-maintenance-window.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples). 

```
    /**
     * Deletes an AWS SSM Maintenance Window asynchronously.
     *
     * @param winId The ID of the Maintenance Window to delete.
     * <p>
     * This method initiates an asynchronous request to delete an SSM Maintenance Window.
     * If an exception occurs, it handles the error appropriately.
     */
    public void deleteMaintenanceWindow(String winId) {
        DeleteMaintenanceWindowRequest windowRequest = DeleteMaintenanceWindowRequest.builder()
                .windowId(winId)
                .build();

        CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
            getAsyncClient().deleteMaintenanceWindow(windowRequest)
                    .thenAccept(response -> {
                        System.out.println("The maintenance window was successfully deleted.");
                    })
                    .exceptionally(ex -> {
                        throw new CompletionException(ex);
                    }).join();
        }).exceptionally(ex -> {
            Throwable cause = (ex instanceof CompletionException) ? ex.getCause() : ex;
            if (cause instanceof SsmException) {
                throw new RuntimeException("SSM error: " + cause.getMessage(), cause);
            } else {
                throw new RuntimeException("Unexpected error: " + cause.getMessage(), cause);
            }
        });

        try {
            future.join();
        } catch (CompletionException ex) {
            throw ex.getCause() instanceof RuntimeException ? (RuntimeException) ex.getCause() : ex;
        }
    }
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteMaintenanceWindow) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples). 

```
import { DeleteMaintenanceWindowCommand, SSMClient } from "@aws-sdk/client-ssm";
import { parseArgs } from "node:util";

/**
 * Delete an SSM maintenance window.
 * @param {{ windowId: string }}
 */
export const main = async ({ windowId }) => {
  const client = new SSMClient({});
  try {
    await client.send(
      new DeleteMaintenanceWindowCommand({ WindowId: windowId }),
    );
    console.log(`Maintenance window '${windowId}' deleted.`);
    return { Deleted: true };
  } catch (caught) {
    if (caught instanceof Error && caught.name === "MissingParameter") {
      console.warn(`${caught.message}. Did you provide this value?`);
    } else {
      throw caught;
    }
  }
};
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/DeleteMaintenanceWindowCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example removes a maintenance window.**  

```
Remove-SSMMaintenanceWindow -WindowId "mw-06d59c1a07c022145"
```
**Output:**  

```
mw-06d59c1a07c022145
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example removes a maintenance window.**  

```
Remove-SSMMaintenanceWindow -WindowId "mw-06d59c1a07c022145"
```
**Output:**  

```
mw-06d59c1a07c022145
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples). 

```
class MaintenanceWindowWrapper:
    """Encapsulates AWS Systems Manager maintenance window actions."""

    def __init__(self, ssm_client):
        """
        :param ssm_client: A Boto3 Systems Manager client.
        """
        self.ssm_client = ssm_client
        self.window_id = None
        self.name = None

    @classmethod
    def from_client(cls):
        ssm_client = boto3.client("ssm")
        return cls(ssm_client)


    def delete(self):
        """
        Delete the associated AWS Systems Manager maintenance window.
        """
        if self.window_id is None:
            return

        try:
            self.ssm_client.delete_maintenance_window(WindowId=self.window_id)
            logger.info("Deleted maintenance window %s.", self.window_id)
            print(f"Deleted maintenance window {self.name}")
            self.window_id = None
        except ClientError as err:
            logger.error(
                "Couldn't delete maintenance window %s. Here's why: %s: %s",
                self.window_id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteMaintenanceWindow) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples). 

```
    TRY.
        lo_ssm->deletemaintenancewindow( iv_windowid = iv_window_id ).
        MESSAGE 'Maintenance window deleted.' TYPE 'I'.
      CATCH /aws1/cx_ssminternalservererr.
        MESSAGE 'Internal server error occurred.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DeleteMaintenanceWindow](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.