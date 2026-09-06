

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeleteDocument` with an AWS SDK or CLI
<a name="example_ssm_DeleteDocument_section"></a>

The following code examples show how to use `DeleteDocument`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a document**  
The following `delete-document` example deletes a Systems Manager document.  

```
aws ssm delete-document \
    --name {{"Example"}}
```
This command produces no output.  
For more information, see [Creating Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeleteDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-document.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples). 

```
    /**
     * Deletes an AWS SSM document asynchronously.
     *
     * @param documentName The name of the document to delete.
     * <p>
     * This method initiates an asynchronous request to delete an SSM document.
     * If an exception occurs, it handles the error appropriately.
     */
    public void deleteDoc(String documentName) {
        DeleteDocumentRequest documentRequest = DeleteDocumentRequest.builder()
                .name(documentName)
                .build();

        CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
            getAsyncClient().deleteDocument(documentRequest)
                    .thenAccept(response -> {
                        System.out.println("The SSM document was successfully deleted.");
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
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteDocument) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples). 

```
import { DeleteDocumentCommand, SSMClient } from "@aws-sdk/client-ssm";
import { parseArgs } from "node:util";

/**
 * Delete an SSM document.
 * @param {{ documentName: string }}
 */
export const main = async ({ documentName }) => {
  const client = new SSMClient({});
  try {
    await client.send(new DeleteDocumentCommand({ Name: documentName }));
    console.log(`Document '${documentName}' deleted.`);
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
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/DeleteDocumentCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes a document. There is no output if the command succeeds.**  

```
Remove-SSMDocument -Name "RunShellScript"
```
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes a document. There is no output if the command succeeds.**  

```
Remove-SSMDocument -Name "RunShellScript"
```
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples). 

```
class DocumentWrapper:
    """Encapsulates AWS Systems Manager Document actions."""

    def __init__(self, ssm_client):
        """
        :param ssm_client: A Boto3 Systems Manager client.
        """
        self.ssm_client = ssm_client
        self.name = None

    @classmethod
    def from_client(cls):
        ssm_client = boto3.client("ssm")
        return cls(ssm_client)


    def delete(self):
        """
        Deletes an AWS Systems Manager document.
        """
        if self.name is None:
            return

        try:
            self.ssm_client.delete_document(Name=self.name)
            print(f"Deleted document {self.name}.")
            self.name = None
        except ClientError as err:
            logger.error(
                "Couldn't delete %s. Here's why: %s: %s",
                self.name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteDocument) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples). 

```
    TRY.
        lo_ssm->deletedocument( iv_name = iv_name ).
        MESSAGE 'Document deleted.' TYPE 'I'.
      CATCH /aws1/cx_ssminvaliddocument.
        MESSAGE 'Invalid document.' TYPE 'I'.
      CATCH /aws1/cx_ssmassocdinstances.
        MESSAGE 'Document has associated instances.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DeleteDocument](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.