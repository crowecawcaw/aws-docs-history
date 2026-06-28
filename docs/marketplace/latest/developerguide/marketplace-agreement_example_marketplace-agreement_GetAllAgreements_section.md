The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Get all agreements using an AWS SDK

The following code examples show how to get all agreements.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code")
repository.

```
package com.example.awsmarketplace.agreementapi.seller;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementViewSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.Filter;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsResponse;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;

import com.example.awsmarketplace.utils.ReferenceCodesUtils;

public class GetAllAgreements {

	/*
	 * Get all purchase agreements for your PartyType (Proposer, or Acceptor)
	 * Depend on the number of agreements in your account, this code may take some time to finish.
	 */
	public static void main(String[] args) {

		List<AgreementViewSummary> agreementSummaryList = getAllAgreements();

		ReferenceCodesUtils.formatOutput(agreementSummaryList);
	}

	public static List<AgreementViewSummary> getAllAgreements() {
		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

        // Set PartyType filter to PARTY_TYPE_FILTER_VALUE_ACCEPTOR to return agreements where you are the acceptor.
        // Change to PARTY_TYPE_FILTER_VALUE_PROPOSER to return agreements where you are the proposer.
		Filter partyType = Filter.builder().name(PARTY_TYPE_FILTER_NAME)
				.values(PARTY_TYPE_FILTER_VALUE_ACCEPTOR).build();

		Filter agreementType = Filter.builder().name(AGREEMENT_TYPE_FILTER_NAME)
				.values(AGREEMENT_TYPE_FILTER_VALUE_PURCHASEAGREEMENT).build();

		List<Filter> searchFilters = new ArrayList<Filter>();

		searchFilters.addAll(Arrays.asList(partyType, agreementType));

		// Save all results in a list array

		List<AgreementViewSummary> agreementSummaryList = new ArrayList<AgreementViewSummary>();

		SearchAgreementsRequest searchAgreementsRequest =
				SearchAgreementsRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.filters(searchFilters)
				.build();

		SearchAgreementsResponse searchAgreementsResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);

		agreementSummaryList.addAll(searchAgreementsResponse.agreementViewSummaries());

		while (searchAgreementsResponse.nextToken() != null && searchAgreementsResponse.nextToken().length() > 0) {
			searchAgreementsRequest =
					SearchAgreementsRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.nextToken(searchAgreementsResponse.nextToken())
					.filters(searchFilters).build();
			searchAgreementsResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);
			agreementSummaryList.addAll(searchAgreementsResponse.agreementViewSummaries());
		}
		return agreementSummaryList;
	}

}


```

- For API details, see
  [SearchAgreements](../../../goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SearchAgreements.md "../../../goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SearchAgreements.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code "https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code")
repository.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to get all agreements
AG-01
"""

import logging

import boto3
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import utils.helpers as helper
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

logger = logging.getLogger(__name__)

MAX_PAGE_RESULTS = 10

party_type_list = ["Acceptor"]
agreement_type_list = ["PurchaseAgreement"]

filter_list = [
    {"name": "PartyType", "values": party_type_list},
    {"name": "AgreementType", "values": agreement_type_list},
]

agreement_results_list = []


def get_agreements(filter_list=filter_list):
    try:
        agreements = mp_client.search_agreements(
            catalog="AWSMarketplace",
            maxResults=MAX_PAGE_RESULTS,
            filters=filter_list,
        )
    except ClientError as e:
        logger.error("Could not complete search_agreements request.")
        raise e

    agreement_results_list.extend(agreements["agreementViewSummaries"])

    while "nextToken" in agreements and agreements["nextToken"] is not None:
        try:
            agreements = mp_client.search_agreements(
                catalog="AWSMarketplace",
                maxResults=MAX_PAGE_RESULTS,
                nextToken=agreements["nextToken"],
                filters=filter_list,
            )
        except ClientError as e:
            logger.error("Could not complete search_agreements request.")
            raise e

        agreement_results_list.extend(agreements["agreementViewSummaries"])

    return agreement_results_list


if __name__ == "__main__":
    agreements_list = get_agreements(filter_list)
    helper.pretty_print_datetime(agreements_list)


```

- For API details, see
  [SearchAgreements](../../../goto/boto3/marketplace-agreement-2020-03-01/SearchAgreements.md "../../../goto/boto3/marketplace-agreement-2020-03-01/SearchAgreements.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
