

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get details of an agreement request using an AWS SDK

The following code examples show how to get details of an agreement request, including whether it requires approval and its expected charges.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.ChargeSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.ExpectedCharge;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.ItemizedCharge;
import software.amazon.awssdk.services.marketplaceagreement.model.Resource;

public class GetAgreementRequest {

    private static final String AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

    public static void main(String[] args) {
        getAgreementRequest();
    }

    private static void getAgreementRequest() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        GetAgreementRequestRequest request =
                GetAgreementRequestRequest.builder()
                        .agreementRequestId(AGREEMENT_REQUEST_ID)
                        .build();

        GetAgreementRequestResponse response = marketplaceAgreementClient.getAgreementRequest(request);

        System.out.println("Agreement Request ID: " + response.agreementRequestId());
        System.out.println("Agreement Type: " + response.agreementType());
        System.out.println("Status: " + response.statusAsString());
        System.out.println("Approval Requirement: " + response.approvalRequirementAsString());
        if (response.agreementId() != null) {
            System.out.println("Agreement ID: " + response.agreementId());
        }
        System.out.println("Intent: " + response.intentAsString());
        System.out.println("Created At: " + response.createdAt());

        ChargeSummary chargeSummary = response.chargeSummary();
        System.out.println("Currency Code: " + chargeSummary.currencyCode());
        System.out.println("New Agreement Value: " + chargeSummary.newAgreementValue());
        // Tax fields are returned only when the request was created with tax estimation enabled.
        if (chargeSummary.estimatedTaxes() != null) {
            System.out.println("New Agreement Value After Tax: " + chargeSummary.newAgreementValueAfterTax());
            System.out.println("Estimated Taxes: " + chargeSummary.estimatedTaxes().totalAmount());
            System.out.println("Invoicing Entity: " + chargeSummary.invoicingEntity());
        }
        for (ExpectedCharge charge : chargeSummary.expectedCharges()) {
            System.out.println("Expected Charge ID: " + charge.id());
            System.out.println("  Amount: " + charge.amount());
            if (charge.amountAfterTax() != null) {
                System.out.println("  Amount After Tax: " + charge.amountAfterTax());
            }
            System.out.println("  Timing: " + charge.timingAsString());
            // Recurring charges of usage-based and recurring payment terms have no time.
            if (charge.time() != null) {
                System.out.println("  Time: " + charge.time());
            }
            if (charge.purchaseOrderReference() != null) {
                System.out.println("  Purchase Order Reference: " + charge.purchaseOrderReference());
            }
        }
        for (ItemizedCharge itemizedCharge : chargeSummary.itemizedCharges()) {
            System.out.println("Itemized Charge: " + itemizedCharge.dimensionKey() + ", quantity "
                    + itemizedCharge.oldQuantity() + " -> " + itemizedCharge.newQuantity() + ", amount "
                    + itemizedCharge.incrementalChargeAmount());
        }

        System.out.println("Proposer Account ID: " + response.proposer().accountId());
        System.out.println("Offer ID: " + response.proposalSummary().offerId());
        if (response.proposalSummary().offerSetId() != null) {
            System.out.println("Offer Set ID: " + response.proposalSummary().offerSetId());
        }
        for (Resource resource : response.proposalSummary().resources()) {
            System.out.println("Resource: " + resource.id() + " (" + resource.type() + ")");
        }
    }
}
```
+  For API details, see [GetAgreementRequest](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequest) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementRequestCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
        })
    );

    console.log("Agreement Request ID: " + response.agreementRequestId);
    console.log("Agreement Type: " + response.agreementType);
    console.log("Status: " + response.status);
    console.log("Approval Requirement: " + response.approvalRequirement);
    if (response.agreementId !== undefined) {
        console.log("Agreement ID: " + response.agreementId);
    }
    console.log("Intent: " + response.intent);
    console.log("Created At: " + response.createdAt);

    const chargeSummary = response.chargeSummary;
    console.log("Currency Code: " + chargeSummary.currencyCode);
    console.log("New Agreement Value: " + chargeSummary.newAgreementValue);
    // Tax fields are returned only when the request was created with tax estimation enabled.
    if (chargeSummary.estimatedTaxes !== undefined) {
        console.log("New Agreement Value After Tax: " + chargeSummary.newAgreementValueAfterTax);
        console.log("Estimated Taxes: " + chargeSummary.estimatedTaxes.totalAmount);
        console.log("Invoicing Entity: " + JSON.stringify(chargeSummary.invoicingEntity));
    }
    for (const charge of chargeSummary.expectedCharges ?? []) {
        console.log("Expected Charge ID: " + charge.id);
        console.log("  Amount: " + charge.amount);
        if (charge.amountAfterTax !== undefined) {
            console.log("  Amount After Tax: " + charge.amountAfterTax);
        }
        console.log("  Timing: " + charge.timing);
        // Recurring charges of usage-based and recurring payment terms have no time.
        if (charge.time !== undefined) {
            console.log("  Time: " + charge.time);
        }
        if (charge.purchaseOrderReference !== undefined) {
            console.log("  Purchase Order Reference: " + charge.purchaseOrderReference);
        }
    }
    for (const itemizedCharge of chargeSummary.itemizedCharges ?? []) {
        console.log("Itemized Charge: " + itemizedCharge.dimensionKey + ", quantity "
            + itemizedCharge.oldQuantity + " -> " + itemizedCharge.newQuantity + ", amount "
            + itemizedCharge.incrementalChargeAmount);
    }

    console.log("Proposer Account ID: " + response.proposer.accountId);
    console.log("Offer ID: " + response.proposalSummary.offerId);
    if (response.proposalSummary.offerSetId !== undefined) {
        console.log("Offer Set ID: " + response.proposalSummary.offerSetId);
    }
    for (const resource of response.proposalSummary.resources ?? []) {
        console.log("Resource: " + resource.id + " (" + resource.type + ")");
    }
}

getAgreementRequest();
```
+  For API details, see [GetAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class GetAgreementRequest:

    AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>"

    @staticmethod
    def get_agreement_request():
        client = boto3.client("marketplace-agreement")

        response = client.get_agreement_request(
            agreementRequestId=GetAgreementRequest.AGREEMENT_REQUEST_ID,
        )

        print("Agreement Request ID: " + response["agreementRequestId"])
        print("Agreement Type: " + str(response.get("agreementType", "")))
        print("Status: " + str(response.get("status", "")))
        print("Approval Requirement: " + str(response.get("approvalRequirement", "")))
        if "agreementId" in response:
            print("Agreement ID: " + response["agreementId"])
        print("Intent: " + str(response.get("intent", "")))
        print("Created At: " + str(response.get("createdAt", "")))

        charge_summary = response["chargeSummary"]
        print("Currency Code: " + str(charge_summary.get("currencyCode", "")))
        print("New Agreement Value: " + str(charge_summary.get("newAgreementValue", "")))
        # Tax fields are returned only when the request was created with tax estimation enabled.
        if "estimatedTaxes" in charge_summary:
            print("New Agreement Value After Tax: " + str(charge_summary.get("newAgreementValueAfterTax", "")))
            print("Estimated Taxes: " + str(charge_summary["estimatedTaxes"].get("totalAmount", "")))
            print("Invoicing Entity: " + str(charge_summary.get("invoicingEntity", "")))
        for charge in charge_summary.get("expectedCharges", []):
            print("Expected Charge ID: " + str(charge.get("id", "")))
            print("  Amount: " + str(charge.get("amount", "")))
            if "amountAfterTax" in charge:
                print("  Amount After Tax: " + charge["amountAfterTax"])
            print("  Timing: " + str(charge.get("timing", "")))
            # Recurring charges of usage-based and recurring payment terms have no time.
            if "time" in charge:
                print("  Time: " + str(charge["time"]))
            if "purchaseOrderReference" in charge:
                print("  Purchase Order Reference: " + charge["purchaseOrderReference"])
        for itemized_charge in charge_summary.get("itemizedCharges", []):
            print("Itemized Charge: " + str(itemized_charge.get("dimensionKey", "")) + ", quantity "
                  + str(itemized_charge.get("oldQuantity", "")) + " -> " + str(itemized_charge.get("newQuantity", ""))
                  + ", amount " + str(itemized_charge.get("incrementalChargeAmount", "")))

        print("Proposer Account ID: " + str(response["proposer"].get("accountId", "")))
        proposal_summary = response["proposalSummary"]
        print("Offer ID: " + str(proposal_summary.get("offerId", "")))
        if "offerSetId" in proposal_summary:
            print("Offer Set ID: " + proposal_summary["offerSetId"])
        for resource in proposal_summary.get("resources", []):
            print("Resource: " + resource["id"] + " (" + resource["type"] + ")")


if __name__ == "__main__":
    GetAgreementRequest.get_agreement_request()
```
+  For API details, see [GetAgreementRequest](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequest) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.