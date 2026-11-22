

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the terms of an agreement request using an AWS SDK

The following code examples show how to get the terms requested in an agreement request.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementRequestTerm;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestTermsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestTermsResponse;

public class GetAgreementRequestTerms {

    private static final String AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

    public static void main(String[] args) {
        getAgreementRequestTerms();
    }

    private static void getAgreementRequestTerms() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        GetAgreementRequestTermsRequest request =
                GetAgreementRequestTermsRequest.builder()
                        .agreementRequestId(AGREEMENT_REQUEST_ID)
                        .build();

        for (GetAgreementRequestTermsResponse page :
                marketplaceAgreementClient.getAgreementRequestTermsPaginator(request)) {
            for (AgreementRequestTerm term : page.terms()) {
                System.out.println("Term Type: " + term.type());
                System.out.println(term);
                System.out.println("---");
            }
        }
    }
}
```
+  For API details, see [GetAgreementRequestTerms](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequestTerms) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    paginateGetAgreementRequestTerms,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequestTerms() {
    const client = new MarketplaceAgreementClient();

    for await (const page of paginateGetAgreementRequestTerms(
        { client },
        { agreementRequestId: AGREEMENT_REQUEST_ID }
    )) {
        for (const term of page.terms) {
            const [termType, termValue] = Object.entries(term)[0];
            console.log("Term Type: " + termType);
            console.log(JSON.stringify(termValue, null, 2));
            console.log("---");
        }
    }
}

getAgreementRequestTerms();
```
+  For API details, see [GetAgreementRequestTerms](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestTermsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3

import json


class GetAgreementRequestTerms:

    AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>"

    @staticmethod
    def get_agreement_request_terms():
        client = boto3.client("marketplace-agreement")

        paginator = client.get_paginator("get_agreement_request_terms")
        for page in paginator.paginate(agreementRequestId=GetAgreementRequestTerms.AGREEMENT_REQUEST_ID):
            for term in page["terms"]:
                term_type, term_value = next(iter(term.items()))
                print("Term Type: " + term_type)
                print(json.dumps(term_value, indent=2, default=str))
                print("---")


if __name__ == "__main__":
    GetAgreementRequestTerms.get_agreement_request_terms()
```
+  For API details, see [GetAgreementRequestTerms](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequestTerms) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.