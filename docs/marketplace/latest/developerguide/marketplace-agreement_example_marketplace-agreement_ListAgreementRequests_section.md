

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List agreement requests using an AWS SDK

The following code examples show how to list my agreement requests, filtered by status.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementRequestSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.ListAgreementRequestsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.ListAgreementRequestsResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.Resource;

public class ListAgreementRequests {

    private static final String STATUS = "PENDING_APPROVAL";

    public static void main(String[] args) {
        listAgreementRequests();
    }

    private static void listAgreementRequests() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        String nextToken = null;

        do {
            ListAgreementRequestsRequest request =
                    ListAgreementRequestsRequest.builder()
                            .status(STATUS)
                            .nextToken(nextToken)
                            .build();

            ListAgreementRequestsResponse response = marketplaceAgreementClient.listAgreementRequests(request);

            for (AgreementRequestSummary summary : response.items()) {
                System.out.println("Agreement Request ID: " + summary.agreementRequestId());
                System.out.println("Agreement Type: " + summary.agreementType());
                System.out.println("Status: " + summary.statusAsString());
                if (summary.agreementId() != null) {
                    System.out.println("Agreement ID: " + summary.agreementId());
                }
                System.out.println("Offer ID: " + summary.proposalSummary().offerId());
                if (summary.proposalSummary().offerSetId() != null) {
                    System.out.println("Offer Set ID: " + summary.proposalSummary().offerSetId());
                }
                for (Resource resource : summary.proposalSummary().resources()) {
                    System.out.println("Resource: " + resource.id() + " (" + resource.type() + ")");
                }
                System.out.println("---");
            }

            nextToken = response.nextToken();
        } while (nextToken != null);
    }
}
```
+  For API details, see [ListAgreementRequests](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/ListAgreementRequests) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementRequestsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const STATUS = "PENDING_APPROVAL";

async function listAgreementRequests() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementRequestsCommand({
                status: STATUS,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items ?? []) {
            console.log("Agreement Request ID: " + summary.agreementRequestId);
            console.log("Agreement Type: " + summary.agreementType);
            console.log("Status: " + summary.status);
            if (summary.agreementId) {
                console.log("Agreement ID: " + summary.agreementId);
            }
            console.log("Offer ID: " + summary.proposalSummary.offerId);
            if (summary.proposalSummary.offerSetId !== undefined) {
                console.log("Offer Set ID: " + summary.proposalSummary.offerSetId);
            }
            for (const resource of summary.proposalSummary.resources ?? []) {
                console.log("Resource: " + resource.id + " (" + resource.type + ")");
            }
            console.log("---");
        }

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementRequests();
```
+  For API details, see [ListAgreementRequests](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementRequestsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class ListAgreementRequests:

    STATUS = "PENDING_APPROVAL"

    @staticmethod
    def list_agreement_requests():
        client = boto3.client("marketplace-agreement")

        next_token = None

        while True:
            kwargs = {"status": ListAgreementRequests.STATUS}
            if next_token:
                kwargs["nextToken"] = next_token

            response = client.list_agreement_requests(**kwargs)

            for summary in response.get("items", []):
                print("Agreement Request ID: " + summary["agreementRequestId"])
                print("Agreement Type: " + str(summary.get("agreementType", "")))
                print("Status: " + str(summary.get("status", "")))
                if "agreementId" in summary:
                    print("Agreement ID: " + summary["agreementId"])
                proposal_summary = summary["proposalSummary"]
                print("Offer ID: " + str(proposal_summary.get("offerId", "")))
                if "offerSetId" in proposal_summary:
                    print("Offer Set ID: " + proposal_summary["offerSetId"])
                for resource in proposal_summary.get("resources", []):
                    print("Resource: " + resource["id"] + " (" + resource["type"] + ")")
                print("---")

            next_token = response.get("nextToken")
            if not next_token:
                break


if __name__ == "__main__":
    ListAgreementRequests.list_agreement_requests()
```
+  For API details, see [ListAgreementRequests](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/ListAgreementRequests) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.