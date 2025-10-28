# Code examples for Systems Manager using AWS SDKs

The following code examples show how to use Systems Manager with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Systems Manager.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/ssm#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ssm.SsmClient;
import software.amazon.awssdk.services.ssm.model.DocumentFilter;
import software.amazon.awssdk.services.ssm.model.ListDocumentsRequest;
import software.amazon.awssdk.services.ssm.model.ListDocumentsResponse;

public class HelloSSM {

    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <awsAccount>

                Where:
                    awsAccount - Your AWS Account number.
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String awsAccount = args[0] ;
        Region region = Region.US_EAST_1;
        SsmClient ssmClient = SsmClient.builder()
            .region(region)
            .build();

        listDocuments(ssmClient, awsAccount);
    }

    /*
    This code automatically fetches the next set of results using the `nextToken` and
    stops once the desired maxResults (20 in this case) have been reached.
    */
    public static void listDocuments(SsmClient ssmClient, String awsAccount) {
        String nextToken = null;
        int totalDocumentsReturned = 0;
        int maxResults = 20;
        do {
            ListDocumentsRequest request = ListDocumentsRequest.builder()
                .documentFilterList(
                    DocumentFilter.builder()
                        .key("Owner")
                        .value(awsAccount)
                        .build()
                    )
                .maxResults(maxResults)
                .nextToken(nextToken)
                .build();

            ListDocumentsResponse response = ssmClient.listDocuments(request);
            response.documentIdentifiers().forEach(identifier -> System.out.println("Document Name: " + identifier.name()));
            nextToken = response.nextToken();
            totalDocumentsReturned += response.documentIdentifiers().size();
        } while (nextToken != null && totalDocumentsReturned < maxResults);
    }
}


```

- For API details, see
  [ListDocuments](../../../goto/SdkForJavaV2/ssm-2014-11-06/ListDocuments.md "../../../goto/SdkForJavaV2/ssm-2014-11-06/ListDocuments.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/ssm#code-examples").

```
import { paginateListDocuments, SSMClient } from "@aws-sdk/client-ssm";

// Call ListDocuments and display the result.
export const main = async () => {
  const client = new SSMClient();
  const listDocumentsPaginated = [];
  console.log(
    "Hello, AWS Systems Manager! Let's list some of your documents:\n",
  );
  try {
    // The paginate function is a wrapper around the base command.
    const paginator = paginateListDocuments({ client }, { MaxResults: 5 });
    for await (const page of paginator) {
      listDocumentsPaginated.push(...page.DocumentIdentifiers);
    }
  } catch (caught) {
    console.error(`There was a problem saying hello: ${caught.message}`);
    throw caught;
  }

  for (const { Name, DocumentFormat, CreatedDate } of listDocumentsPaginated) {
    console.log(`${Name} - ${DocumentFormat} - ${CreatedDate}`);
  }
};

// Call function if run directly.
import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main();
}


```

- For API details, see
  [ListDocuments](../../../AWSJavaScriptSDK/v3/latest/client/ssm/command/ListDocumentsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/ssm/command/ListDocumentsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/ssm#code-examples").

```
import boto3
from botocore.exceptions import ClientError


def hello_systems_manager(ssm_client):
    """
    Use the AWS SDK for Python (Boto3) to create an AWS Systems Manager
    client and list the first 5 documents in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param ssm_client: A Boto3 AWS Systems Manager Client object. This object wraps
                             the low-level AWS Systems Manager service API.
    """
    print("Hello, AWS Systems Manager! Let's list some of your documents:\n")

    paginator = ssm_client.get_paginator("list_documents")
    page_iterator = paginator.paginate(PaginationConfig={"MaxItems": 5})
    for page in page_iterator:
        for document in page["DocumentIdentifiers"]:
            print(f"  {document['Name']}")


if __name__ == "__main__":
    try:
        hello_systems_manager(boto3.client("ssm"))
    except ClientError as err:
        print("Hello systems manager had an error.")
        print(err.response["Error"]["Code"])
        print(err.response["Error"]["Message"])


```

- For API details, see
  [ListDocuments](../../../goto/boto3/ssm-2014-11-06/ListDocuments.md "../../../goto/boto3/ssm-2014-11-06/ListDocuments.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Systems Manager](example_ssm_Hello_section.md "example_ssm_Hello_section.md")
  - [Learn the basics](example_ssm_Scenario_section.md "example_ssm_Scenario_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [AddTagsToResource](example_ssm_AddTagsToResource_section.md "example_ssm_AddTagsToResource_section.md")
    - [CancelCommand](example_ssm_CancelCommand_section.md "example_ssm_CancelCommand_section.md")
    - [CreateActivation](example_ssm_CreateActivation_section.md "example_ssm_CreateActivation_section.md")
    - [CreateAssociation](example_ssm_CreateAssociation_section.md "example_ssm_CreateAssociation_section.md")
    - [CreateAssociationBatch](example_ssm_CreateAssociationBatch_section.md "example_ssm_CreateAssociationBatch_section.md")
    - [CreateDocument](example_ssm_CreateDocument_section.md "example_ssm_CreateDocument_section.md")
    - [CreateMaintenanceWindow](example_ssm_CreateMaintenanceWindow_section.md "example_ssm_CreateMaintenanceWindow_section.md")
    - [CreateOpsItem](example_ssm_CreateOpsItem_section.md "example_ssm_CreateOpsItem_section.md")
    - [CreatePatchBaseline](example_ssm_CreatePatchBaseline_section.md "example_ssm_CreatePatchBaseline_section.md")
    - [DeleteActivation](example_ssm_DeleteActivation_section.md "example_ssm_DeleteActivation_section.md")
    - [DeleteAssociation](example_ssm_DeleteAssociation_section.md "example_ssm_DeleteAssociation_section.md")
    - [DeleteDocument](example_ssm_DeleteDocument_section.md "example_ssm_DeleteDocument_section.md")
    - [DeleteMaintenanceWindow](example_ssm_DeleteMaintenanceWindow_section.md "example_ssm_DeleteMaintenanceWindow_section.md")
    - [DeleteOpsItem](example_ssm_DeleteOpsItem_section.md "example_ssm_DeleteOpsItem_section.md")
    - [DeleteParameter](example_ssm_DeleteParameter_section.md "example_ssm_DeleteParameter_section.md")
    - [DeletePatchBaseline](example_ssm_DeletePatchBaseline_section.md "example_ssm_DeletePatchBaseline_section.md")
    - [DeregisterManagedInstance](example_ssm_DeregisterManagedInstance_section.md "example_ssm_DeregisterManagedInstance_section.md")
    - [DeregisterPatchBaselineForPatchGroup](example_ssm_DeregisterPatchBaselineForPatchGroup_section.md "example_ssm_DeregisterPatchBaselineForPatchGroup_section.md")
    - [DeregisterTargetFromMaintenanceWindow](example_ssm_DeregisterTargetFromMaintenanceWindow_section.md "example_ssm_DeregisterTargetFromMaintenanceWindow_section.md")
    - [DeregisterTaskFromMaintenanceWindow](example_ssm_DeregisterTaskFromMaintenanceWindow_section.md "example_ssm_DeregisterTaskFromMaintenanceWindow_section.md")
    - [DescribeActivations](example_ssm_DescribeActivations_section.md "example_ssm_DescribeActivations_section.md")
    - [DescribeAssociation](example_ssm_DescribeAssociation_section.md "example_ssm_DescribeAssociation_section.md")
    - [DescribeAssociationExecutionTargets](example_ssm_DescribeAssociationExecutionTargets_section.md "example_ssm_DescribeAssociationExecutionTargets_section.md")
    - [DescribeAssociationExecutions](example_ssm_DescribeAssociationExecutions_section.md "example_ssm_DescribeAssociationExecutions_section.md")
    - [DescribeAutomationExecutions](example_ssm_DescribeAutomationExecutions_section.md "example_ssm_DescribeAutomationExecutions_section.md")
    - [DescribeAutomationStepExecutions](example_ssm_DescribeAutomationStepExecutions_section.md "example_ssm_DescribeAutomationStepExecutions_section.md")
    - [DescribeAvailablePatches](example_ssm_DescribeAvailablePatches_section.md "example_ssm_DescribeAvailablePatches_section.md")
    - [DescribeDocument](example_ssm_DescribeDocument_section.md "example_ssm_DescribeDocument_section.md")
    - [DescribeDocumentPermission](example_ssm_DescribeDocumentPermission_section.md "example_ssm_DescribeDocumentPermission_section.md")
    - [DescribeEffectiveInstanceAssociations](example_ssm_DescribeEffectiveInstanceAssociations_section.md "example_ssm_DescribeEffectiveInstanceAssociations_section.md")
    - [DescribeEffectivePatchesForPatchBaseline](example_ssm_DescribeEffectivePatchesForPatchBaseline_section.md "example_ssm_DescribeEffectivePatchesForPatchBaseline_section.md")
    - [DescribeInstanceAssociationsStatus](example_ssm_DescribeInstanceAssociationsStatus_section.md "example_ssm_DescribeInstanceAssociationsStatus_section.md")
    - [DescribeInstanceInformation](example_ssm_DescribeInstanceInformation_section.md "example_ssm_DescribeInstanceInformation_section.md")
    - [DescribeInstancePatchStates](example_ssm_DescribeInstancePatchStates_section.md "example_ssm_DescribeInstancePatchStates_section.md")
    - [DescribeInstancePatchStatesForPatchGroup](example_ssm_DescribeInstancePatchStatesForPatchGroup_section.md "example_ssm_DescribeInstancePatchStatesForPatchGroup_section.md")
    - [DescribeInstancePatches](example_ssm_DescribeInstancePatches_section.md "example_ssm_DescribeInstancePatches_section.md")
    - [DescribeMaintenanceWindowExecutionTaskInvocations](example_ssm_DescribeMaintenanceWindowExecutionTaskInvocations_section.md "example_ssm_DescribeMaintenanceWindowExecutionTaskInvocations_section.md")
    - [DescribeMaintenanceWindowExecutionTasks](example_ssm_DescribeMaintenanceWindowExecutionTasks_section.md "example_ssm_DescribeMaintenanceWindowExecutionTasks_section.md")
    - [DescribeMaintenanceWindowExecutions](example_ssm_DescribeMaintenanceWindowExecutions_section.md "example_ssm_DescribeMaintenanceWindowExecutions_section.md")
    - [DescribeMaintenanceWindowTargets](example_ssm_DescribeMaintenanceWindowTargets_section.md "example_ssm_DescribeMaintenanceWindowTargets_section.md")
    - [DescribeMaintenanceWindowTasks](example_ssm_DescribeMaintenanceWindowTasks_section.md "example_ssm_DescribeMaintenanceWindowTasks_section.md")
    - [DescribeMaintenanceWindows](example_ssm_DescribeMaintenanceWindows_section.md "example_ssm_DescribeMaintenanceWindows_section.md")
    - [DescribeOpsItems](example_ssm_DescribeOpsItems_section.md "example_ssm_DescribeOpsItems_section.md")
    - [DescribeParameters](example_ssm_DescribeParameters_section.md "example_ssm_DescribeParameters_section.md")
    - [DescribePatchBaselines](example_ssm_DescribePatchBaselines_section.md "example_ssm_DescribePatchBaselines_section.md")
    - [DescribePatchGroupState](example_ssm_DescribePatchGroupState_section.md "example_ssm_DescribePatchGroupState_section.md")
    - [DescribePatchGroups](example_ssm_DescribePatchGroups_section.md "example_ssm_DescribePatchGroups_section.md")
    - [GetAutomationExecution](example_ssm_GetAutomationExecution_section.md "example_ssm_GetAutomationExecution_section.md")
    - [GetCommandInvocation](example_ssm_GetCommandInvocation_section.md "example_ssm_GetCommandInvocation_section.md")
    - [GetConnectionStatus](example_ssm_GetConnectionStatus_section.md "example_ssm_GetConnectionStatus_section.md")
    - [GetDefaultPatchBaseline](example_ssm_GetDefaultPatchBaseline_section.md "example_ssm_GetDefaultPatchBaseline_section.md")
    - [GetDeployablePatchSnapshotForInstance](example_ssm_GetDeployablePatchSnapshotForInstance_section.md "example_ssm_GetDeployablePatchSnapshotForInstance_section.md")
    - [GetDocument](example_ssm_GetDocument_section.md "example_ssm_GetDocument_section.md")
    - [GetInventory](example_ssm_GetInventory_section.md "example_ssm_GetInventory_section.md")
    - [GetInventorySchema](example_ssm_GetInventorySchema_section.md "example_ssm_GetInventorySchema_section.md")
    - [GetMaintenanceWindow](example_ssm_GetMaintenanceWindow_section.md "example_ssm_GetMaintenanceWindow_section.md")
    - [GetMaintenanceWindowExecution](example_ssm_GetMaintenanceWindowExecution_section.md "example_ssm_GetMaintenanceWindowExecution_section.md")
    - [GetMaintenanceWindowExecutionTask](example_ssm_GetMaintenanceWindowExecutionTask_section.md "example_ssm_GetMaintenanceWindowExecutionTask_section.md")
    - [GetParameter](example_ssm_GetParameter_section.md "example_ssm_GetParameter_section.md")
    - [GetParameterHistory](example_ssm_GetParameterHistory_section.md "example_ssm_GetParameterHistory_section.md")
    - [GetParameters](example_ssm_GetParameters_section.md "example_ssm_GetParameters_section.md")
    - [GetPatchBaseline](example_ssm_GetPatchBaseline_section.md "example_ssm_GetPatchBaseline_section.md")
    - [GetPatchBaselineForPatchGroup](example_ssm_GetPatchBaselineForPatchGroup_section.md "example_ssm_GetPatchBaselineForPatchGroup_section.md")
    - [ListAssociationVersions](example_ssm_ListAssociationVersions_section.md "example_ssm_ListAssociationVersions_section.md")
    - [ListAssociations](example_ssm_ListAssociations_section.md "example_ssm_ListAssociations_section.md")
    - [ListCommandInvocations](example_ssm_ListCommandInvocations_section.md "example_ssm_ListCommandInvocations_section.md")
    - [ListCommands](example_ssm_ListCommands_section.md "example_ssm_ListCommands_section.md")
    - [ListComplianceItems](example_ssm_ListComplianceItems_section.md "example_ssm_ListComplianceItems_section.md")
    - [ListComplianceSummaries](example_ssm_ListComplianceSummaries_section.md "example_ssm_ListComplianceSummaries_section.md")
    - [ListDocumentVersions](example_ssm_ListDocumentVersions_section.md "example_ssm_ListDocumentVersions_section.md")
    - [ListDocuments](example_ssm_ListDocuments_section.md "example_ssm_ListDocuments_section.md")
    - [ListInventoryEntries](example_ssm_ListInventoryEntries_section.md "example_ssm_ListInventoryEntries_section.md")
    - [ListResourceComplianceSummaries](example_ssm_ListResourceComplianceSummaries_section.md "example_ssm_ListResourceComplianceSummaries_section.md")
    - [ListTagsForResource](example_ssm_ListTagsForResource_section.md "example_ssm_ListTagsForResource_section.md")
    - [ModifyDocumentPermission](example_ssm_ModifyDocumentPermission_section.md "example_ssm_ModifyDocumentPermission_section.md")
    - [PutComplianceItems](example_ssm_PutComplianceItems_section.md "example_ssm_PutComplianceItems_section.md")
    - [PutInventory](example_ssm_PutInventory_section.md "example_ssm_PutInventory_section.md")
    - [PutParameter](example_ssm_PutParameter_section.md "example_ssm_PutParameter_section.md")
    - [RegisterDefaultPatchBaseline](example_ssm_RegisterDefaultPatchBaseline_section.md "example_ssm_RegisterDefaultPatchBaseline_section.md")
    - [RegisterPatchBaselineForPatchGroup](example_ssm_RegisterPatchBaselineForPatchGroup_section.md "example_ssm_RegisterPatchBaselineForPatchGroup_section.md")
    - [RegisterTargetWithMaintenanceWindow](example_ssm_RegisterTargetWithMaintenanceWindow_section.md "example_ssm_RegisterTargetWithMaintenanceWindow_section.md")
    - [RegisterTaskWithMaintenanceWindow](example_ssm_RegisterTaskWithMaintenanceWindow_section.md "example_ssm_RegisterTaskWithMaintenanceWindow_section.md")
    - [RemoveTagsFromResource](example_ssm_RemoveTagsFromResource_section.md "example_ssm_RemoveTagsFromResource_section.md")
    - [SendCommand](example_ssm_SendCommand_section.md "example_ssm_SendCommand_section.md")
    - [StartAutomationExecution](example_ssm_StartAutomationExecution_section.md "example_ssm_StartAutomationExecution_section.md")
    - [StartSession](example_ssm_StartSession_section.md "example_ssm_StartSession_section.md")
    - [StopAutomationExecution](example_ssm_StopAutomationExecution_section.md "example_ssm_StopAutomationExecution_section.md")
    - [UpdateAssociation](example_ssm_UpdateAssociation_section.md "example_ssm_UpdateAssociation_section.md")
    - [UpdateAssociationStatus](example_ssm_UpdateAssociationStatus_section.md "example_ssm_UpdateAssociationStatus_section.md")
    - [UpdateDocument](example_ssm_UpdateDocument_section.md "example_ssm_UpdateDocument_section.md")
    - [UpdateDocumentDefaultVersion](example_ssm_UpdateDocumentDefaultVersion_section.md "example_ssm_UpdateDocumentDefaultVersion_section.md")
    - [UpdateMaintenanceWindow](example_ssm_UpdateMaintenanceWindow_section.md "example_ssm_UpdateMaintenanceWindow_section.md")
    - [UpdateManagedInstanceRole](example_ssm_UpdateManagedInstanceRole_section.md "example_ssm_UpdateManagedInstanceRole_section.md")
    - [UpdateOpsItem](example_ssm_UpdateOpsItem_section.md "example_ssm_UpdateOpsItem_section.md")
    - [UpdatePatchBaseline](example_ssm_UpdatePatchBaseline_section.md "example_ssm_UpdatePatchBaseline_section.md")
