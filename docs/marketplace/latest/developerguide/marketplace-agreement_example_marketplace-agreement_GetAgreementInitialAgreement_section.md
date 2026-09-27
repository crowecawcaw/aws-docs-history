

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the initial agreement of an agreement using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_GetAgreementInitialAgreement_section"></a>

The following code examples show how to identify the first agreement in an agreement's chain.

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

public class GetAgreementInitialAgreement {

	/*
	 * Identify the first agreement in my agreement's chain
	 */

	public static void main(String[] args) {

		String agreementId = args.length > 0 ? args[0] : AGREEMENT_ID;

		// A renewal or replacement carries forward the same initialAgreementId, so this value
		// identifies the whole chain. It equals agreementId when this agreement starts the chain.
		System.out.println("Initial Agreement ID: " + getInitialAgreementId(agreementId));
	}

	public static String getInitialAgreementId(String agreementId) {
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

		return describeAgreementResponse.initialAgreementId();
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
Obtain the first agreement in this agreement's chain
AG-33
"""

import logging

import boto3
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

logger = logging.getLogger(__name__)

# agreement id
AGREEMENT_ID = "agmt-11111111111111111111"

# attribute name
ATTRIBUTE_INITIAL_AGREEMENT_ID = "initialAgreementId"


def get_initial_agreement_id(entity_id):
    """
    Returns the first agreement in the chain that the given agreement belongs to
    Args: entity_id str: Agreement to describe
    Returns: str: The initial agreement id. Equals entity_id when this agreement starts the chain.
    """

    try:
        agreement = mp_client.describe_agreement(agreementId=entity_id)
        return agreement.get(ATTRIBUTE_INITIAL_AGREEMENT_ID)

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

    # A renewal or replacement carries forward the same initialAgreementId, so this value
    # identifies the whole chain. It equals AGREEMENT_ID when this agreement starts the chain.
    print("Initial Agreement ID: " + str(get_initial_agreement_id(AGREEMENT_ID)))


if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.