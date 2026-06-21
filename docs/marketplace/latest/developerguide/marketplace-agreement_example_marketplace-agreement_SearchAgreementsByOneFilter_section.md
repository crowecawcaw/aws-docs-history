The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Search for agreements with one custom filter using an AWS SDK

The following code example shows how to search for agreements with one custom filter.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code")
repository.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package com.example.awsmarketplace.agreementapi;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementViewSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.Filter;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsResponse;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.example.awsmarketplace.utils.ReferenceCodesUtils;

/**
 * To search by
 * offer id: OfferId;
 * product id: ResourceIdentifier;
 * customer AWS account id: AcceptorAccountId
 * product type: ResourceType (i.e. SaasProduct)
 * status: Status. status values can be: ACTIVE, CANCELED,
 * 		EXPIRED, RENEWED, REPLACED, ROLLED_BACK, SUPERSEDED, TERMINATED
 */

public class SearchAgreementsByOneFilter {

	private static final String FILTER_NAME = "ResourceType";

	private static final String FILTER_VALUE = "SaaSProduct";

	/*
	 * search agreements by one customize filter
	 */
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

		Filter partyTypeFilter = Filter.builder().name(PARTY_TYPE_FILTER_NAME)
				.values(PARTY_TYPE_FILTER_VALUE_PROPOSER).build();

		Filter agreementTypeFilter = Filter.builder().name(AGREEMENT_TYPE_FILTER_NAME)
				.values(AGREEMENT_TYPE_FILTER_VALUE_PURCHASEAGREEMENT).build();

		Filter customizeFilter = Filter.builder().name(FILTER_NAME).values(FILTER_VALUE).build();

		List<Filter> filters = new ArrayList<Filter>();

		filters.addAll(Arrays.asList(partyTypeFilter, agreementTypeFilter, customizeFilter));

		SearchAgreementsRequest searchAgreementsRequest =
				SearchAgreementsRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.filters(filters)
				.build();
		SearchAgreementsResponse searchAgreementsResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);

		List<AgreementViewSummary> agreementSummaryList = new ArrayList<AgreementViewSummary>();

		agreementSummaryList.addAll(searchAgreementsResponse.agreementViewSummaries());

		while (searchAgreementsResponse.nextToken() != null && searchAgreementsResponse.nextToken().length() > 0) {
			searchAgreementsRequest =
					SearchAgreementsRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.filters(filters)
					.nextToken(searchAgreementsResponse.nextToken())
					.build();
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

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
