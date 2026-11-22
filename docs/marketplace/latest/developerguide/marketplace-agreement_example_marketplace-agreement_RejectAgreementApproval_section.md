

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Reject an agreement approval using an AWS SDK

The following code examples show how to reject an agreement approval as the administrator of my organization.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementApproval;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalRejectionInput;
import software.amazon.awssdk.services.marketplaceagreement.model.RejectAgreementApprovalRequest;

// Rejects an agreement approval as the administrator of the buyer's AWS Organization. The agreement request
// is rejected and no agreement is created.
public class RejectAgreementApproval {

    private static final String AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
    private static final String NOTE = "<REJECTION REASON HERE>";

    public static void main(String[] args) {
        rejectAgreementApproval();
    }

    private static void rejectAgreementApproval() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        RejectAgreementApprovalRequest request =
                RejectAgreementApprovalRequest.builder()
                        .buyerAgreementApprovalRejectionInput(BuyerAgreementApprovalRejectionInput.builder()
                                .agreementApprovalId(AGREEMENT_APPROVAL_ID)
                                .note(NOTE)
                                .build())
                        .build();

        marketplaceAgreementClient.rejectAgreementApproval(request);

        System.out.println("Rejected Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
    }
}
```
+  For API details, see [RejectAgreementApproval](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RejectAgreementApproval) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    RejectAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Rejects an agreement approval as the administrator of the buyer's AWS Organization. The agreement request
// is rejected and no agreement is created.
const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
const NOTE = "<REJECTION REASON HERE>";

async function rejectAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new RejectAgreementApprovalCommand({
            buyerAgreementApprovalRejectionInput: {
                agreementApprovalId: AGREEMENT_APPROVAL_ID,
                note: NOTE,
            },
        })
    );

    console.log("Rejected Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
}

rejectAgreementApproval();
```
+  For API details, see [RejectAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/RejectAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


# Rejects an agreement approval as the administrator of the buyer's AWS Organization. The agreement request
# is rejected and no agreement is created.
class RejectAgreementApproval:

    AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>"
    NOTE = "<REJECTION REASON HERE>"

    @staticmethod
    def reject_agreement_approval():
        client = boto3.client("marketplace-agreement")

        rejection_input = {
            "agreementApprovalId": RejectAgreementApproval.AGREEMENT_APPROVAL_ID,
            "note": RejectAgreementApproval.NOTE,
        }

        client.reject_agreement_approval(buyerAgreementApprovalRejectionInput=rejection_input)

        print("Rejected Agreement Approval ID: " + RejectAgreementApproval.AGREEMENT_APPROVAL_ID)


if __name__ == "__main__":
    RejectAgreementApproval.reject_agreement_approval()
```
+  For API details, see [RejectAgreementApproval](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/RejectAgreementApproval) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.