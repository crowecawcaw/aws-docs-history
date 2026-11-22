

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Cancel an agreement request using an AWS SDK

The following code examples show how to cancel an agreement request that is pending approval.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.CancelAgreementRequestRequest;

// Cancels an agreement request that is pending approval, and its approval.
public class CancelAgreementRequest {

    private static final String AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

    public static void main(String[] args) {
        cancelAgreementRequest();
    }

    private static void cancelAgreementRequest() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        CancelAgreementRequestRequest request =
                CancelAgreementRequestRequest.builder()
                        .agreementRequestId(AGREEMENT_REQUEST_ID)
                        .build();

        marketplaceAgreementClient.cancelAgreementRequest(request);

        System.out.println("Cancelled Agreement Request ID: " + AGREEMENT_REQUEST_ID);
    }
}
```
+  For API details, see [CancelAgreementRequest](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/CancelAgreementRequest) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    CancelAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Cancels an agreement request that is pending approval, and its approval.
const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function cancelAgreementRequest() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new CancelAgreementRequestCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
        })
    );

    console.log("Cancelled Agreement Request ID: " + AGREEMENT_REQUEST_ID);
}

cancelAgreementRequest();
```
+  For API details, see [CancelAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CancelAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


# Cancels an agreement request that is pending approval, and its approval.
class CancelAgreementRequest:

    AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>"

    @staticmethod
    def cancel_agreement_request():
        client = boto3.client("marketplace-agreement")

        client.cancel_agreement_request(
            agreementRequestId=CancelAgreementRequest.AGREEMENT_REQUEST_ID,
        )

        print("Cancelled Agreement Request ID: " + CancelAgreementRequest.AGREEMENT_REQUEST_ID)


if __name__ == "__main__":
    CancelAgreementRequest.cancel_agreement_request()
```
+  For API details, see [CancelAgreementRequest](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/CancelAgreementRequest) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.