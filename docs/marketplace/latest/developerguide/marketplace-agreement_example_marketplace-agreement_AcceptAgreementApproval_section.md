

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Approve an agreement approval using an AWS SDK

The following code examples show how to approve an agreement approval as the administrator of my organization.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementApproval;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AcceptAgreementApprovalRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalApproverInput;

// Approves an agreement approval as the administrator of the buyer's AWS Organization. When the approval
// is approved, the agreement request is accepted and the agreement is created; GetAgreementRequest returns its
// agreementId.
public class AcceptAgreementApproval {

    private static final String AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
    private static final String NOTE = "<APPROVAL NOTE HERE>";

    public static void main(String[] args) {
        acceptAgreementApproval();
    }

    private static void acceptAgreementApproval() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        AcceptAgreementApprovalRequest request =
                AcceptAgreementApprovalRequest.builder()
                        .buyerAgreementApprovalApproverInput(BuyerAgreementApprovalApproverInput.builder()
                                .agreementApprovalId(AGREEMENT_APPROVAL_ID)
                                .note(NOTE)
                                .build())
                        .build();

        marketplaceAgreementClient.acceptAgreementApproval(request);

        System.out.println("Approved Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
    }
}
```
+  For API details, see [AcceptAgreementApproval](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AcceptAgreementApproval) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    AcceptAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Approves an agreement approval as the administrator of the buyer's AWS Organization. When the approval
// is approved, the agreement request is accepted and the agreement is created; GetAgreementRequest returns its
// agreementId.
const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
const NOTE = "<APPROVAL NOTE HERE>";

async function acceptAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new AcceptAgreementApprovalCommand({
            buyerAgreementApprovalApproverInput: {
                agreementApprovalId: AGREEMENT_APPROVAL_ID,
                note: NOTE,
            },
        })
    );

    console.log("Approved Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
}

acceptAgreementApproval();
```
+  For API details, see [AcceptAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/AcceptAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


# Approves an agreement approval as the administrator of the buyer's AWS Organization. When the approval
# is approved, the agreement request is accepted and the agreement is created; GetAgreementRequest returns its
# agreementId.
class AcceptAgreementApproval:

    AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>"
    NOTE = "<APPROVAL NOTE HERE>"

    @staticmethod
    def accept_agreement_approval():
        client = boto3.client("marketplace-agreement")

        approver_input = {
            "agreementApprovalId": AcceptAgreementApproval.AGREEMENT_APPROVAL_ID,
            "note": AcceptAgreementApproval.NOTE,
        }

        client.accept_agreement_approval(buyerAgreementApprovalApproverInput=approver_input)

        print("Approved Agreement Approval ID: " + AcceptAgreementApproval.AGREEMENT_APPROVAL_ID)


if __name__ == "__main__":
    AcceptAgreementApproval.accept_agreement_approval()
```
+  For API details, see [AcceptAgreementApproval](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/AcceptAgreementApproval) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.