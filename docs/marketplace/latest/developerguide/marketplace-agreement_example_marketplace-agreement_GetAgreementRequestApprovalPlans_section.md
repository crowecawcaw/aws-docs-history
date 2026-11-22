

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the approval plans of an agreement request using an AWS SDK

The following code examples show how to get the approval plans that apply to an agreement request.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```java
package com.example.awsmarketplace.agreementapi.buyer.agreementRequest;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementApprovalPlan;
import software.amazon.awssdk.services.marketplaceagreement.model.Approver;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalPlan;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalPlanGroup;
import software.amazon.awssdk.services.marketplaceagreement.model.BuyerAgreementApprovalPlanLevel;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestApprovalPlansRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementRequestApprovalPlansResponse;

public class GetAgreementRequestApprovalPlans {

    private static final String AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

    public static void main(String[] args) {
        getAgreementRequestApprovalPlans();
    }

    private static void getAgreementRequestApprovalPlans() {
        MarketplaceAgreementClient marketplaceAgreementClient =
                MarketplaceAgreementClient.builder()
                        .httpClient(ApacheHttpClient.builder().build())
                        .credentialsProvider(ProfileCredentialsProvider.create())
                        .build();

        GetAgreementRequestApprovalPlansRequest request =
                GetAgreementRequestApprovalPlansRequest.builder()
                        .agreementRequestId(AGREEMENT_REQUEST_ID)
                        .build();

        for (GetAgreementRequestApprovalPlansResponse page :
                marketplaceAgreementClient.getAgreementRequestApprovalPlansPaginator(request)) {
            for (AgreementApprovalPlan item : page.items()) {
                BuyerAgreementApprovalPlan plan = item.buyerAgreementApprovalPlan();
                System.out.println("Plan Reference: " + plan.planReference());
                System.out.println("Plan Name: " + plan.name());
                for (BuyerAgreementApprovalPlanLevel level : plan.levels()) {
                    System.out.println("  Level: " + level.name());
                    for (BuyerAgreementApprovalPlanGroup group : level.groups()) {
                        System.out.println("    Required Approvals: " + group.approvalCriteria().requiredApprovalCount());
                        for (Approver approver : group.approvers()) {
                            System.out.println("    Approver: " + approver);
                        }
                    }
                }
                System.out.println("---");
            }
        }
    }
}
```
+  For API details, see [GetAgreementRequestApprovalPlans](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository. 

```javascript
const {
    MarketplaceAgreementClient,
    paginateGetAgreementRequestApprovalPlans,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequestApprovalPlans() {
    const client = new MarketplaceAgreementClient();

    for await (const page of paginateGetAgreementRequestApprovalPlans(
        { client },
        { agreementRequestId: AGREEMENT_REQUEST_ID }
    )) {
        for (const item of page.items) {
            const plan = item.buyerAgreementApprovalPlan;
            console.log("Plan Reference: " + plan.planReference);
            console.log("Plan Name: " + plan.name);
            for (const level of plan.levels) {
                console.log("  Level: " + level.name);
                for (const group of level.groups) {
                    console.log("    Required Approvals: " + group.approvalCriteria.requiredApprovalCount);
                    for (const approver of group.approvers) {
                        console.log("    Approver: " + JSON.stringify(approver));
                    }
                }
            }
            console.log("---");
        }
    }
}

getAgreementRequestApprovalPlans();
```
+  For API details, see [GetAgreementRequestApprovalPlans](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestApprovalPlansCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import boto3


class GetAgreementRequestApprovalPlans:

    AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>"

    @staticmethod
    def get_agreement_request_approval_plans():
        client = boto3.client("marketplace-agreement")

        paginator = client.get_paginator("get_agreement_request_approval_plans")
        for page in paginator.paginate(agreementRequestId=GetAgreementRequestApprovalPlans.AGREEMENT_REQUEST_ID):
            for item in page["items"]:
                plan = item["buyerAgreementApprovalPlan"]
                print("Plan Reference: " + plan["planReference"])
                print("Plan Name: " + str(plan.get("name", "")))
                for level in plan["levels"]:
                    print("  Level: " + str(level.get("name", "")))
                    for group in level["groups"]:
                        print("    Required Approvals: " + str(group["approvalCriteria"]["requiredApprovalCount"]))
                        for approver in group["approvers"]:
                            print("    Approver: " + str(approver))
                print("---")


if __name__ == "__main__":
    GetAgreementRequestApprovalPlans.get_agreement_request_approval_plans()
```
+  For API details, see [GetAgreementRequestApprovalPlans](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequestApprovalPlans) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.