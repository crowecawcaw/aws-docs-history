

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `UpdateOpsItem` with an AWS SDK or CLI
<a name="example_ssm_UpdateOpsItem_section"></a>

The following code examples show how to use `UpdateOpsItem`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_ssm_Scenario_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To update an OpsItem**  
The following `update-ops-item` example updates the description, priority, and category for an OpsItem. In addition, the command specifies an SNS topic where the notifications are sent when this OpsItem is edited or changed.  

```
aws ssm update-ops-item \
    --ops-item-id {{"oi-287b5EXAMPLE"}} \
    --description {{"Primary OpsItem for failover event 2020-01-01-fh398yf"}} \
    --priority {{2}} \
    --category {{"Security"}} \
    --notifications {{"Arn=arn:aws:sns:us-east-2:111222333444:my-us-east-2-topic"}}
```
Output:  

```
This command produces no output.
```
For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [UpdateOpsItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-ops-item.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples). 

```
    /**
     * Resolves an AWS SSM OpsItem asynchronously.
     *
     * @param opsID The ID of the OpsItem to resolve.
     * <p>
     * This method initiates an asynchronous request to resolve an SSM OpsItem.
     * If an exception occurs, it handles the error appropriately.
     */
    public void resolveOpsItem(String opsID) {
        UpdateOpsItemRequest opsItemRequest = UpdateOpsItemRequest.builder()
                .opsItemId(opsID)
                .status(OpsItemStatus.RESOLVED)
                .build();

        CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
            getAsyncClient().updateOpsItem(opsItemRequest)
                    .thenAccept(response -> {
                        System.out.println("OpsItem resolved successfully.");
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
+  For API details, see [UpdateOpsItem](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateOpsItem) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples). 

```
import { UpdateOpsItemCommand, SSMClient } from "@aws-sdk/client-ssm";
import { parseArgs } from "node:util";

/**
 * Update an SSM OpsItem.
 * @param {{ opsItemId: string, status?: OpsItemStatus }}
 */
export const main = async ({
  opsItemId,
  status = undefined, // The OpsItem status. Status can be Open, In Progress, or Resolved
}) => {
  const client = new SSMClient({});
  try {
    await client.send(
      new UpdateOpsItemCommand({
        OpsItemId: opsItemId,
        Status: status,
      }),
    );
    console.log("Ops item updated.");
    return { Success: true };
  } catch (caught) {
    if (
      caught instanceof Error &&
      caught.name === "OpsItemLimitExceededException"
    ) {
      console.warn(
        `Couldn't create ops item because you have exceeded your open OpsItem limit. ${caught.message}.`,
      );
    } else {
      throw caught;
    }
  }
};
```
+  For API details, see [UpdateOpsItem](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/ssm/command/UpdateOpsItemCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples). 

```
class OpsItemWrapper:
    """Encapsulates AWS Systems Manager OpsItem actions."""

    def __init__(self, ssm_client):
        """
        :param ssm_client: A Boto3 Systems Manager client.
        """
        self.ssm_client = ssm_client
        self.id = None

    @classmethod
    def from_client(cls):
        """
        :return: A OpsItemWrapper instance.
        """
        ssm_client = boto3.client("ssm")
        return cls(ssm_client)


    def update(self, title=None, description=None, status=None):
        """
        Update an OpsItem.

        :param title: The new OpsItem title.
        :param description: The new OpsItem description.
        :param status: The new OpsItem status.
        :return:
        """
        args = dict(OpsItemId=self.id)
        if title is not None:
            args["Title"] = title
        if description is not None:
            args["Description"] = description
        if status is not None:
            args["Status"] = status
        try:
            self.ssm_client.update_ops_item(**args)
        except ClientError as err:
            logger.error(
                "Couldn't update ops item %s. Here's why: %s: %s",
                self.id,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [UpdateOpsItem](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateOpsItem) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples). 

```
    TRY.
        lo_ssm->updateopsitem(
            iv_opsitemid = iv_ops_item_id
            iv_title = iv_title
            iv_description = iv_description
            iv_status = iv_status ).
        MESSAGE 'OpsItem updated.' TYPE 'I'.
      CATCH /aws1/cx_ssmopsitemnotfoundex.
        MESSAGE 'OpsItem not found.' TYPE 'I'.
      CATCH /aws1/cx_ssmopsiteminvparamex.
        MESSAGE 'Invalid OpsItem parameter.' TYPE 'I'.
    ENDTRY.
```
+  For API details, see [UpdateOpsItem](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.