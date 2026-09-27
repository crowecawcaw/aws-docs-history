

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the end time behavior of an agreement using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_GetAgreementEndTimeBehavior_section"></a>

The following code examples show how to find out whether an agreement will renew, be replaced, or expire at its end date.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```
package com.example.awsmarketplace.agreementapi.seller;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.EndTimeBehavior;

public class GetAgreementEndTimeBehavior {

	/*
	 * Find out whether the agreement will renew, be replaced, or expire at its end date, and why
	 */

	public static void main(String[] args) {

		String agreementId = args.length > 0 ? args[0] : AGREEMENT_ID;

		EndTimeBehavior endTimeBehavior = getEndTimeBehavior(agreementId);

		// endTimeBehavior is absent for agreements that have no end date, such as pay-as-you-go.
		if (endTimeBehavior == null) {
			System.out.println("Agreement " + agreementId + " has no end date, so it has no end time behavior.");
			return;
		}

		System.out.println("End time behavior is " + endTimeBehavior.typeAsString());

		// reasonCode is null when type is RENEW, otherwise the reason the agreement does not renew.
		if (endTimeBehavior.reasonCodeAsString() != null) {
			System.out.println("Reason is " + endTimeBehavior.reasonCodeAsString());
		}

		// renewalSummary is present whenever type is RENEW, but offerId inside it is absent
		// until a renewal offer is created.
		if (endTimeBehavior.renewalSummary() != null && endTimeBehavior.renewalSummary().offerId() != null) {
			System.out.println("Next renewal will use offer " + endTimeBehavior.renewalSummary().offerId());
		}
	}

	public static EndTimeBehavior getEndTimeBehavior(String agreementId) {

		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		DescribeAgreementRequest describeAgreementRequest =
				DescribeAgreementRequest.builder()
				.agreementId(agreementId)
				.build();

		DescribeAgreementResponse describeAgreementResponse =
				marketplaceAgreementClient.describeAgreement(describeAgreementRequest);

		return describeAgreementResponse.endTimeBehavior();
	}

}
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Obtain what will happen to the agreement when it reaches its end date, and the reason for that outcome
AG-32
"""

import logging

import boto3
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

logger = logging.getLogger(__name__)

# agreement id
AGREEMENT_ID = "agmt-11111111111111111111"

# attribute names
ATTRIBUTE_END_TIME_BEHAVIOR = "endTimeBehavior"
ATTRIBUTE_TYPE = "type"
ATTRIBUTE_REASON_CODE = "reasonCode"
ATTRIBUTE_RENEWAL_SUMMARY = "renewalSummary"
ATTRIBUTE_OFFER_ID = "offerId"


def get_end_time_behavior(entity_id):
    """
    Returns the end time behavior of a given agreement
    Args: entity_id str: Agreement to describe
    Returns: dict: The endTimeBehavior of the agreement, or None if it has no end date
    """

    try:
        agreement = mp_client.describe_agreement(agreementId=entity_id)

        # endTimeBehavior is absent for agreements that have no end date, because those
        # agreements never reach an end time. Pay-as-you-go agreements are the most
        # common example.
        return agreement.get(ATTRIBUTE_END_TIME_BEHAVIOR)

    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Agreement with ID %s not found.", entity_id)
        else:
            logger.error("Unexpected error: %s", e)


def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Looking for an agreement in the AWS Marketplace.")
    print("-" * 88)

    end_time_behavior = get_end_time_behavior(AGREEMENT_ID)

    if end_time_behavior is None:
        print(
            "Agreement "
            + AGREEMENT_ID
            + " was not found, or it has no end date and therefore no end time behavior."
        )
        return

    print(f"End time behavior is {end_time_behavior[ATTRIBUTE_TYPE]}")

    # reasonCode is only populated when type is EXPIRE or REPLACE. It is absent when type is RENEW.
    if ATTRIBUTE_REASON_CODE in end_time_behavior:
        print(f"Reason is {end_time_behavior[ATTRIBUTE_REASON_CODE]}")

    # renewalSummary carries the offer that the next renewal will use. It is present whenever
    # type is RENEW, but offerId inside it is absent until a renewal offer is created.
    offer_id = end_time_behavior.get(ATTRIBUTE_RENEWAL_SUMMARY, {}).get(ATTRIBUTE_OFFER_ID)
    if offer_id:
        print(f"Next renewal will use offer {offer_id}")


if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.