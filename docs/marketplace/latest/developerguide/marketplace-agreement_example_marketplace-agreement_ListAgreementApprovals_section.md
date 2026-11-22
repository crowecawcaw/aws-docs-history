

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List agreement approvals using an AWS SDK

The following code examples show how to list the agreement approvals I requested, or that I decide as the administrator of my organization.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementApproval;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.ListAgreementApprovalsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.ListAgreementApprovalsResponse;

public class ListAgreementApprovals {

    // REQUESTER lists the approvals the caller started. AWS_ORGANIZATION_ADMIN lists the approvals the caller
    // decides as the administrator of its AWS Organization.
    private static final String PARTY_TYPE = "AWS_ORGANIZATION_ADMIN";
    private static final String STATUS = "PENDING_APPROVAL";

    public static void main(String[] args) {
        listAgreementApprovals();
    }

    private static void listAgreementApprovals() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        String nextToken = null;

        do {
            ListAgreementApprovalsRequest request =
                    ListAgreementApprovalsRequest.builder()
                            .partyType(PARTY_TYPE)
                            .status(STATUS)
                            .nextToken(nextToken)
                            .build();

            ListAgreementApprovalsResponse response = marketplaceAgreementClient.listAgreementApprovals(request);

            for (AgreementApprovalSummary summary : response.items()) {
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

            nextToken = response.nextToken();
        } while (nextToken != null);
    }
}
```
+  For API details, see [ListAgreementApprovals](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementApprovals) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementApprovalsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// REQUESTER lists the approvals the caller started. AWS_ORGANIZATION_ADMIN lists the approvals the caller
// decides as the administrator of its AWS Organization.
const PARTY_TYPE = "AWS_ORGANIZATION_ADMIN";
const STATUS = "PENDING_APPROVAL";

async function listAgreementApprovals() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementApprovalsCommand({
                partyType: PARTY_TYPE,
                status: STATUS,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items) {
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

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementApprovals();
```
+  For API details, see [ListAgreementApprovals](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementApprovalsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class ListAgreementApprovals:

    # REQUESTER lists the approvals the caller started. AWS_ORGANIZATION_ADMIN lists the approvals the caller
    # decides as the administrator of its AWS Organization.
    PARTY_TYPE = "AWS_ORGANIZATION_ADMIN"
    STATUS = "PENDING_APPROVAL"

    @staticmethod
    def list_agreement_approvals():
        client = boto3.client("marketplace-agreement")

        next_token = None

        while True:
            kwargs = {"partyType": ListAgreementApprovals.PARTY_TYPE, "status": ListAgreementApprovals.STATUS}
            if next_token:
                kwargs["nextToken"] = next_token

            response = client.list_agreement_approvals(**kwargs)

            for summary in response["items"]:
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

            next_token = response.get("nextToken")
            if not next_token:
                break


if __name__ == "__main__":
    ListAgreementApprovals.list_agreement_approvals()
```
+  For API details, see [ListAgreementApprovals](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementApprovals) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.