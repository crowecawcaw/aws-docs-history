

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List all CPPOs created by a channel partner using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ListAllCppoOffers_section"></a>

The following code examples show how to list all CPPOs created by a channel partner.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code) repository. 

```
package com.example.awsmarketplace.catalogapi;

import java.util.ArrayList;
import java.util.List;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.document.Document;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.EntitySummary;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesResponse;

public class ListAllCppoOffers {

	/*
	 * List all CPPOs created by a channel partner
	 */
	public static void main(String[] args) {
		
		List<String> cppoOfferIds = getAllCppoOfferIds();

		ReferenceCodesUtils.formatOutput(cppoOfferIds);
	}

	public static List<String> getAllCppoOfferIds() {
		MarketplaceCatalogClient marketplaceCatalogClient = 
				MarketplaceCatalogClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();
		
		// get all offer entity ids
		List<String> entityIdList = new ArrayList<String>();

		ListEntitiesRequest listEntitiesRequest = 
				ListEntitiesRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityType(ENTITY_TYPE_OFFER)
				.maxResults(10)
				.nextToken(null)
				.build();

		ListEntitiesResponse listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);

		for (EntitySummary entitySummary : listEntitiesResponse.entitySummaryList()) {
			entityIdList.add(entitySummary.entityId());
		}

		while (listEntitiesResponse.nextToken() != null) {
			listEntitiesRequest = 
					ListEntitiesRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityType(ENTITY_TYPE_OFFER)
					.maxResults(10)
					.nextToken(listEntitiesResponse.nextToken())
					.build();
			listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);

			for (EntitySummary entitySummary : listEntitiesResponse.entitySummaryList()) {
				entityIdList.add(entitySummary.entityId());
			}
		}

		// filter for CPPO offers: ResaleAuthorizationId exists in Details

		List<String> cppoOfferIds = new ArrayList<String>();
		
		for (String entityId : entityIdList) {
			DescribeEntityRequest describeEntityRequest = 
					DescribeEntityRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityId(entityId)
					.build();
			DescribeEntityResponse describeEntityResponse = marketplaceCatalogClient.describeEntity(describeEntityRequest);
			
			Document resaleAuthorizationDocument = describeEntityResponse.detailsDocument().asMap().get(ATTRIBUTE_RESALE_AUTHORIZATION_ID);
			String resaleAuthorizationId = resaleAuthorizationDocument != null ? resaleAuthorizationDocument.asString() : "";

			if (!resaleAuthorizationId.isEmpty()) {
			    cppoOfferIds.add(resaleAuthorizationId);
			}
		}
		return cppoOfferIds;
	}

}
```
+  For API details, see [ListEntities](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListEntities) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python##catalog-api-reference-code) repository. 

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to list all Channel Partner Offers
in an account

Program executed with no arguments:
ie. python3 list_all_cppo_offers.py

CAPI-93
"""

import json
import logging

import boto3
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-catalog")


def get_offer_entities():
    """
    Returns a list of all offers in the account
    """

    next_token = ""  # nosec: B105
    response_list = []

    try:
        response = mp_client.list_entities(Catalog="AWSMarketplace", EntityType="Offer")
    except ClientError as e:
        logging.exception(f"Couldn't list entities. {e}")
        raise

    response_list.append(response)

    # Results are paginated depending on number of entities returned
    while "NextToken" in response:
        next_token = response["NextToken"]

        try:
            response = mp_client.list_entities(
                Catalog="AWSMarketplace",
                EntityType="Offer",
                NextToken=next_token,
            )
        except ClientError as e:
            logging.exception(f"Couldn't list entities. {e}")
            raise

        if "NextToken" in response:
            response_list.append(response)

    return response_list


def build_offer_list(response_list):
    """
    Cleans up list_entities response list with just list of offer IDs
    """
    offer_list = []

    for response in response_list:
        for entity in response["EntitySummaryList"]:
            offer_list.append(entity["EntityId"])

    return offer_list


def check_offer_resaleauth(offer_id):
    """
    Checks to see if an offer is based on a resale authorization
    """
    offer_response = describe_entity(offer_id)
    offer_details = json.loads(offer_response["Details"])
    if offer_details is None:
        offer_details = offer_response["DetailsDocument"]
    if "ResaleAuthorizationId" in offer_details and offer_details["ResaleAuthorizationId"] is not None:
        return offer_id
    else:
        return None


def describe_entity(entity_id):
    """
    General purpose describe entity call
    """
    try:
        response = mp_client.describe_entity(
            Catalog="AWSMarketplace",
            EntityId=entity_id,
        )
    except ClientError as e:
        logging.exception(f"Couldn't describe entity. {e}")
        raise

    return response


def get_resaleauth_offers():
    """
    Returns a list of all offers in the account that are
    based on a resale authorization
    """
    resale_offer_list = []

    response_list = get_offer_entities()
    offer_list = build_offer_list(response_list)
    for offer in offer_list:
        print ("offer id " + offer)
        offer_info = check_offer_resaleauth(offer)
        if offer_info is not None:
            resale_offer_list.append(offer_info)

    return resale_offer_list


if __name__ == "__main__":
    print(get_resaleauth_offers())
```
+  For API details, see [ListEntities](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListEntities) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.