

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Search for the agreements that will renew using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_SearchAgreementsRenewing_section"></a>

The following code examples show how to search for the agreements that will renew.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```
package com.example.awsmarketplace.agreementapi.seller;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementViewSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.EndTimeBehaviorType;
import software.amazon.awssdk.services.marketplaceagreement.model.Filter;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsResponse;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

/**
 * This filter is supported only when PartyType is Proposer, so only sellers can use it. An
 * unsupported combination fails with a ValidationException whose reason is UNSUPPORTED_FILTERS.
 * All filter combinations we support for Proposer and Acceptor:
 * https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html
 */

public class SearchAgreementsRenewing {

	/*
	 * Obtain the agreements that will renew at their end date
	 */

	// change to REPLACE or EXPIRE to find the agreements that will not renew
	static String endTimeBehaviorTypeFilterValue = EndTimeBehaviorType.RENEW.toString();

	static String partyTypeFilterValue = PARTY_TYPE_FILTER_VALUE_PROPOSER;

	public static void main(String[] args) {

		List<AgreementViewSummary> agreementSummaryList = getAgreements();

		ReferenceCodesUtils.formatOutput(agreementSummaryList);
	}

	public static List<AgreementViewSummary> getAgreements() {
		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		// This filter is supported only for the proposer, so leave PartyType set to
		// PARTY_TYPE_FILTER_VALUE_PROPOSER. PARTY_TYPE_FILTER_VALUE_ACCEPTOR fails with a
		// ValidationException whose reason is UNSUPPORTED_FILTERS.
		Filter partyTypeFilter = Filter.builder().name(PARTY_TYPE_FILTER_NAME)
				.values(partyTypeFilterValue).build();

		Filter agreementTypeFilter = Filter.builder().name(AGREEMENT_TYPE_FILTER_NAME)
				.values(AGREEMENT_TYPE_FILTER_VALUE_PURCHASEAGREEMENT).build();

		Filter customizeFilter = Filter.builder().name(END_TIME_BEHAVIOR_TYPE_FILTER_NAME)
				.values(endTimeBehaviorTypeFilterValue).build();

		List<Filter> filters = new ArrayList<Filter>();

		filters.addAll(Arrays.asList(partyTypeFilter, agreementTypeFilter, customizeFilter));

		// search agreement with filters

		SearchAgreementsRequest searchAgreementsRequest =
				SearchAgreementsRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.filters(filters)
				.build();

		SearchAgreementsResponse searchAgreementResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);

		List<AgreementViewSummary> agreementSummaryList = new ArrayList<AgreementViewSummary>();

		agreementSummaryList.addAll(searchAgreementResponse.agreementViewSummaries());

		while (searchAgreementResponse.nextToken() != null && searchAgreementResponse.nextToken().length() > 0) {
			searchAgreementsRequest =
					SearchAgreementsRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.filters(filters)
					.nextToken(searchAgreementResponse.nextToken())
					.build();
			searchAgreementResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);
			agreementSummaryList.addAll(searchAgreementResponse.agreementViewSummaries());
		}
		return agreementSummaryList;
	}

}
```
+  For API details, see [SearchAgreements](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SearchAgreements) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to search for the agreements that will renew
AG-31

This filter is supported only when PartyType is Proposer, so only sellers can use it. An
unsupported combination fails with a ValidationException whose reason is UNSUPPORTED_FILTERS.
All filter combinations we support for Proposer and Acceptor:
https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SearchAgreements.html
"""

import logging

import boto3
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import utils.helpers as helper
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

# change to 'REPLACE' or 'EXPIRE' to find the agreements that will not renew
endTimeBehaviorTypeFilterValue = "RENEW"

MAX_PAGE_RESULTS = 10

logger = logging.getLogger(__name__)


def get_agreements():
    AgreementSummaryList = []

    try:
        agreement = mp_client.search_agreements(
            catalog="AWSMarketplace",
            maxResults=MAX_PAGE_RESULTS,
            # This filter is supported only for the proposer, so leave PartyType set to
            # "Proposer". "Acceptor" fails with a ValidationException whose reason is
            # UNSUPPORTED_FILTERS.
            filters=[
                {"name": "PartyType", "values": ["Proposer"]},
                {"name": "EndTimeBehaviorType", "values": [endTimeBehaviorTypeFilterValue]},
                {"name": "AgreementType", "values": ["PurchaseAgreement"]},
            ],
        )
    except ClientError as e:
        logger.error("Could not complete search_agreements request.")
        raise

    AgreementSummaryList.extend(agreement["agreementViewSummaries"])

    while "nextToken" in agreement:
        try:
            agreement = mp_client.search_agreements(
                catalog="AWSMarketplace",
                maxResults=MAX_PAGE_RESULTS,
                nextToken=agreement["nextToken"],
                filters=[
                    {"name": "PartyType", "values": ["Proposer"]},
                    {
                        "name": "EndTimeBehaviorType",
                        "values": [endTimeBehaviorTypeFilterValue],
                    },
                    {"name": "AgreementType", "values": ["PurchaseAgreement"]},
                ],
            )
        except ClientError as e:
            logger.error("Could not complete search_agreements request.")
            raise

        AgreementSummaryList.extend(agreement["agreementViewSummaries"])

    return AgreementSummaryList


if __name__ == "__main__":
    agreements = get_agreements()
    helper.pretty_print_datetime(agreements)
```
+  For API details, see [SearchAgreements](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/SearchAgreements) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.