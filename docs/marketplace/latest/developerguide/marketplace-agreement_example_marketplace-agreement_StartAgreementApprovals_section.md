

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Start the approval of an agreement request using an AWS SDK

The following code examples show how to start the approval of an agreement request, optionally with purchase orders.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalPlanInput;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalPurchaseOrder;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalPlanInput;
import software.amazon.awssdk.services.marketplaceagreement.model.StartAgreementApprovalsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.StartAgreementApprovalsResponse;

public class StartAgreementApprovals {

    private static final String AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";
    // planReference of a plan returned by GetAgreementRequestApprovalPlans for this agreement request.
    private static final String PLAN_REFERENCE = "<PLAN REFERENCE HERE>";
    private static final String REQUESTER_NOTE = "<NOTE FOR THE APPROVERS HERE>";
    // Optional: a purchase order for an expected charge, by its id from GetAgreementRequest chargeSummary.
    private static final String CHARGE_ID = null;
    private static final String PURCHASE_ORDER_REFERENCE = "<PURCHASE ORDER REFERENCE HERE>";

    public static void main(String[] args) {
        startAgreementApprovals();
    }

    private static void startAgreementApprovals() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        StartAgreementApprovalsRequest.Builder requestBuilder =
                StartAgreementApprovalsRequest.builder()
                        .agreementRequestId(AGREEMENT_REQUEST_ID)
                        .planInputs(AgreementApprovalPlanInput.fromBuyerAgreementApprovalPlanInput(
                                BuyerAgreementApprovalPlanInput.builder()
                                        .planReference(PLAN_REFERENCE)
                                        .requesterNote(REQUESTER_NOTE)
                                        .build()));
        if (CHARGE_ID != null) {
            requestBuilder.purchaseOrders(AgreementApprovalPurchaseOrder.builder()
                    .chargeId(CHARGE_ID)
                    .purchaseOrderReference(PURCHASE_ORDER_REFERENCE)
                    .build());
        }
        StartAgreementApprovalsRequest request = requestBuilder.build();

        StartAgreementApprovalsResponse response = marketplaceAgreementClient.startAgreementApprovals(request);

        for (AgreementApprovalSummary summary : response.approvalSummaries()) {
            System.out.println("Approval Type: " + summary.approvalTypeAsString());
            System.out.println("Agreement Request ID: " + summary.agreementRequestId());
            System.out.println("Agreement Approval ID: " + summary.agreementApprovalId());
            System.out.println("Name: " + summary.name());
            System.out.println("Status: " + summary.statusAsString());
            System.out.println("Created At: " + summary.createdAt());
            System.out.println("Updated At: " + summary.updatedAt());
            System.out.println("Started At: " + summary.startedAt());
            System.out.println("Expires At: " + summary.expiresAt());
            System.out.println("Approval Needed By: " + summary.approvalNeededBy());
            System.out.println("---");
        }
    }
}
```
+  For API details, see [StartAgreementApprovals](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/StartAgreementApprovals) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    StartAgreementApprovalsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";
// planReference of a plan returned by GetAgreementRequestApprovalPlans for this agreement request.
const PLAN_REFERENCE = "<PLAN REFERENCE HERE>";
const REQUESTER_NOTE = "<NOTE FOR THE APPROVERS HERE>";
// Optional: a purchase order for an expected charge, by its id from GetAgreementRequest chargeSummary.
const CHARGE_ID = undefined;
const PURCHASE_ORDER_REFERENCE = "<PURCHASE ORDER REFERENCE HERE>";

async function startAgreementApprovals() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new StartAgreementApprovalsCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
            planInputs: [
                {
                    buyerAgreementApprovalPlanInput: {
                        planReference: PLAN_REFERENCE,
                        requesterNote: REQUESTER_NOTE,
                    },
                },
            ],
            purchaseOrders: CHARGE_ID
                ? [{ chargeId: CHARGE_ID, purchaseOrderReference: PURCHASE_ORDER_REFERENCE }]
                : undefined,
        })
    );

    for (const summary of response.approvalSummaries) {
        console.log("Approval Type: " + summary.approvalType);
        console.log("Agreement Request ID: " + summary.agreementRequestId);
        console.log("Agreement Approval ID: " + summary.agreementApprovalId);
        console.log("Name: " + summary.name);
        console.log("Status: " + summary.status);
        console.log("Created At: " + summary.createdAt);
        console.log("Updated At: " + summary.updatedAt);
        console.log("Started At: " + summary.startedAt);
        console.log("Expires At: " + summary.expiresAt);
        console.log("Approval Needed By: " + summary.approvalNeededBy);
        console.log("---");
    }
}

startAgreementApprovals();
```
+  For API details, see [StartAgreementApprovals](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/StartAgreementApprovalsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class StartAgreementApprovals:

    AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>"
    # planReference of a plan returned by GetAgreementRequestApprovalPlans for this agreement request.
    PLAN_REFERENCE = "<PLAN REFERENCE HERE>"
    REQUESTER_NOTE = "<NOTE FOR THE APPROVERS HERE>"
    # Optional: a purchase order for an expected charge, by its id from GetAgreementRequest chargeSummary.
    CHARGE_ID = None
    PURCHASE_ORDER_REFERENCE = "<PURCHASE ORDER REFERENCE HERE>"

    @staticmethod
    def start_agreement_approvals():
        client = boto3.client("marketplace-agreement")

        kwargs = {
            "agreementRequestId": StartAgreementApprovals.AGREEMENT_REQUEST_ID,
            "planInputs": [
                {
                    "buyerAgreementApprovalPlanInput": {
                        "planReference": StartAgreementApprovals.PLAN_REFERENCE,
                        "requesterNote": StartAgreementApprovals.REQUESTER_NOTE,
                    }
                }
            ],
        }
        if StartAgreementApprovals.CHARGE_ID:
            kwargs["purchaseOrders"] = [
                {
                    "chargeId": StartAgreementApprovals.CHARGE_ID,
                    "purchaseOrderReference": StartAgreementApprovals.PURCHASE_ORDER_REFERENCE,
                }
            ]

        response = client.start_agreement_approvals(**kwargs)

        for summary in response["approvalSummaries"]:
            print("Approval Type: " + summary["approvalType"])
            print("Agreement Request ID: " + summary["agreementRequestId"])
            print("Agreement Approval ID: " + summary["agreementApprovalId"])
            print("Name: " + summary["name"])
            print("Status: " + summary["status"])
            print("Created At: " + str(summary["createdAt"]))
            print("Updated At: " + str(summary["updatedAt"]))
            print("Started At: " + str(summary.get("startedAt", "")))
            print("Expires At: " + str(summary.get("expiresAt", "")))
            print("Approval Needed By: " + str(summary["approvalNeededBy"]))
            print("---")


if __name__ == "__main__":
    StartAgreementApprovals.start_agreement_approvals()
```
+  For API details, see [StartAgreementApprovals](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/StartAgreementApprovals) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.