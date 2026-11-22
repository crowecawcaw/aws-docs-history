

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get details of an agreement approval using an AWS SDK

The following code examples show how to get details of an agreement approval, including its approver outcomes.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementApproval;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalResource;
import software.amazon.awssdk.services.marketplaceagreement.model.ApproverOutcome;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApproval;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalGroup;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalLevel;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementApprovalRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementApprovalResponse;

public class GetAgreementApproval {

    private static final String AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";

    public static void main(String[] args) {
        getAgreementApproval();
    }

    private static void getAgreementApproval() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        GetAgreementApprovalRequest request =
                GetAgreementApprovalRequest.builder()
                        .agreementApprovalId(AGREEMENT_APPROVAL_ID)
                        .build();

        GetAgreementApprovalResponse response = marketplaceAgreementClient.getAgreementApproval(request);
        BuyerAgreementApproval approval = response.buyerAgreementApproval();

        System.out.println("Approval Type: " + approval.approvalTypeAsString());
        System.out.println("Agreement Approval ID: " + approval.agreementApprovalId());
        System.out.println("Agreement Request ID: " + approval.agreementRequestId());
        System.out.println("Name: " + approval.name());
        System.out.println("Status: " + approval.statusAsString());
        System.out.println("Requester Account ID: " + approval.requester().accountId());
        System.out.println("Proposer: " + approval.proposer().legalName() + " (" + approval.proposer().accountId() + ")");
        System.out.println("Offer ID: " + approval.proposalSummary().offerId());
        if (approval.proposalSummary().offerSetId() != null) {
            System.out.println("Offer Set ID: " + approval.proposalSummary().offerSetId());
        }
        System.out.println("Visibility Scope: " + approval.proposalSummary().visibilityScopeAsString());
        for (AgreementApprovalResource resource : approval.proposalSummary().resources()) {
            System.out.println("Resource: " + resource.name() + " (" + resource.id() + ", " + resource.type() + ")");
        }
        System.out.println("Plan Reference: " + approval.planInput().planReference());
        if (approval.planInput().requesterNote() != null) {
            System.out.println("Requester Note: " + approval.planInput().requesterNote());
        }
        System.out.println("Created At: " + approval.createdAt());
        System.out.println("Updated At: " + approval.updatedAt());
        System.out.println("Started At: " + approval.startedAt());
        System.out.println("Expires At: " + approval.expiresAt());
        System.out.println("Approval Needed By: " + approval.approvalNeededBy());
        for (BuyerAgreementApprovalLevel level : approval.levels()) {
            System.out.println("  Level: " + level.name());
            for (BuyerAgreementApprovalGroup group : level.groups()) {
                System.out.println("    Required Approvals: " + group.approvalCriteria().requiredApprovalCount());
                for (ApproverOutcome outcome : group.approvers()) {
                    printApproverOutcome(outcome);
                }
            }
        }
    }

    private static void printApproverOutcome(ApproverOutcome outcome) {
        switch (outcome.type()) {
            case AWS_ORGANIZATION_APPROVER_OUTCOME:
                System.out.println("    Organization admin: " + outcome.awsOrganizationApproverOutcome().statusAsString()
                        + ", approverOutcomeId " + outcome.awsOrganizationApproverOutcome().approverOutcomeId());
                break;
            case EMAIL_APPROVER_OUTCOME:
                System.out.println("    Email approver " + outcome.emailApproverOutcome().emailAddress() + ": "
                        + outcome.emailApproverOutcome().statusAsString()
                        + ", approverOutcomeId " + outcome.emailApproverOutcome().approverOutcomeId());
                break;
            case PROCUREMENT_TOOL_APPROVER_OUTCOME:
                System.out.println("    Procurement tool " + outcome.procurementToolApproverOutcome().name() + ": "
                        + outcome.procurementToolApproverOutcome().statusAsString()
                        + ", approverOutcomeId " + outcome.procurementToolApproverOutcome().approverOutcomeId());
                break;
            default:
                System.out.println("    Approver: " + outcome);
        }
    }
}
```
+  For API details, see [GetAgreementApproval](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementApproval) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";

async function getAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementApprovalCommand({
            agreementApprovalId: AGREEMENT_APPROVAL_ID,
        })
    );
    const approval = response.buyerAgreementApproval;

    console.log("Approval Type: " + approval.approvalType);
    console.log("Agreement Approval ID: " + approval.agreementApprovalId);
    console.log("Agreement Request ID: " + approval.agreementRequestId);
    console.log("Name: " + approval.name);
    console.log("Status: " + approval.status);
    console.log("Requester Account ID: " + approval.requester.accountId);
    console.log("Proposer: " + approval.proposer.legalName + " (" + approval.proposer.accountId + ")");
    console.log("Offer ID: " + approval.proposalSummary.offerId);
    if (approval.proposalSummary.offerSetId !== undefined) {
        console.log("Offer Set ID: " + approval.proposalSummary.offerSetId);
    }
    console.log("Visibility Scope: " + approval.proposalSummary.visibilityScope);
    for (const resource of approval.proposalSummary.resources ?? []) {
        console.log("Resource: " + resource.name + " (" + resource.id + ", " + resource.type + ")");
    }
    console.log("Plan Reference: " + approval.planInput.planReference);
    if (approval.planInput.requesterNote !== undefined) {
        console.log("Requester Note: " + approval.planInput.requesterNote);
    }
    console.log("Created At: " + approval.createdAt);
    console.log("Updated At: " + approval.updatedAt);
    console.log("Started At: " + approval.startedAt);
    console.log("Expires At: " + approval.expiresAt);
    console.log("Approval Needed By: " + approval.approvalNeededBy);
    for (const level of approval.levels) {
        console.log("  Level: " + level.name);
        for (const group of level.groups) {
            console.log("    Required Approvals: " + group.approvalCriteria.requiredApprovalCount);
            for (const outcome of group.approvers) {
                printApproverOutcome(outcome);
            }
        }
    }
}

function printApproverOutcome(outcome) {
    if (outcome.awsOrganizationApproverOutcome) {
        const admin = outcome.awsOrganizationApproverOutcome;
        console.log("    Organization admin: " + admin.status + ", approverOutcomeId " + admin.approverOutcomeId);
    } else if (outcome.emailApproverOutcome) {
        const email = outcome.emailApproverOutcome;
        console.log("    Email approver " + email.emailAddress + ": " + email.status
            + ", approverOutcomeId " + email.approverOutcomeId);
    } else if (outcome.procurementToolApproverOutcome) {
        const tool = outcome.procurementToolApproverOutcome;
        console.log("    Procurement tool " + tool.name + ": " + tool.status
            + ", approverOutcomeId " + tool.approverOutcomeId);
    } else {
        console.log("    Approver: " + JSON.stringify(outcome));
    }
}

getAgreementApproval();
```
+  For API details, see [GetAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class GetAgreementApproval:

    AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>"

    @staticmethod
    def get_agreement_approval():
        client = boto3.client("marketplace-agreement")

        response = client.get_agreement_approval(
            agreementApprovalId=GetAgreementApproval.AGREEMENT_APPROVAL_ID,
        )
        approval = response["buyerAgreementApproval"]

        print("Approval Type: " + approval["approvalType"])
        print("Agreement Approval ID: " + approval["agreementApprovalId"])
        print("Agreement Request ID: " + approval["agreementRequestId"])
        print("Name: " + approval["name"])
        print("Status: " + approval["status"])
        print("Requester Account ID: " + approval["requester"]["accountId"])
        print("Proposer: " + approval["proposer"]["legalName"] + " (" + approval["proposer"]["accountId"] + ")")
        proposal_summary = approval["proposalSummary"]
        print("Offer ID: " + proposal_summary["offerId"])
        if "offerSetId" in proposal_summary:
            print("Offer Set ID: " + proposal_summary["offerSetId"])
        print("Visibility Scope: " + proposal_summary["visibilityScope"])
        for resource in proposal_summary.get("resources", []):
            print("Resource: " + resource["name"] + " (" + resource["id"] + ", " + resource["type"] + ")")
        print("Plan Reference: " + approval["planInput"]["planReference"])
        if "requesterNote" in approval["planInput"]:
            print("Requester Note: " + approval["planInput"]["requesterNote"])
        print("Created At: " + str(approval["createdAt"]))
        print("Updated At: " + str(approval["updatedAt"]))
        print("Started At: " + str(approval.get("startedAt", "")))
        print("Expires At: " + str(approval.get("expiresAt", "")))
        print("Approval Needed By: " + str(approval["approvalNeededBy"]))
        for level in approval["levels"]:
            print("  Level: " + str(level.get("name", "")))
            for group in level["groups"]:
                print("    Required Approvals: " + str(group["approvalCriteria"]["requiredApprovalCount"]))
                for outcome in group["approvers"]:
                    GetAgreementApproval.print_approver_outcome(outcome)

    @staticmethod
    def print_approver_outcome(outcome):
        if "awsOrganizationApproverOutcome" in outcome:
            admin = outcome["awsOrganizationApproverOutcome"]
            print("    Organization admin: " + admin["status"]
                  + ", approverOutcomeId " + str(admin.get("approverOutcomeId", "")))
        elif "emailApproverOutcome" in outcome:
            email = outcome["emailApproverOutcome"]
            print("    Email approver " + email["emailAddress"] + ": " + email["status"]
                  + ", approverOutcomeId " + str(email.get("approverOutcomeId", "")))
        elif "procurementToolApproverOutcome" in outcome:
            tool = outcome["procurementToolApproverOutcome"]
            print("    Procurement tool " + str(tool.get("name", "")) + ": " + tool["status"]
                  + ", approverOutcomeId " + str(tool.get("approverOutcomeId", "")))
        else:
            print("    Approver: " + str(outcome))


if __name__ == "__main__":
    GetAgreementApproval.get_agreement_approval()
```
+  For API details, see [GetAgreementApproval](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementApproval) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.