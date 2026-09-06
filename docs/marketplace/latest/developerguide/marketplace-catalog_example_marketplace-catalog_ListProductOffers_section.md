

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List and describe all offers associated with a product using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ListProductOffers_section"></a>

The following code examples show how to list and describe all offers associated with a product.

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
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.EntitySummary;
import software.amazon.awssdk.services.marketplacecatalog.model.EntityTypeFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferProductIdFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferTargetingFilter;

public class ListProductPrivateOffers {

	private static MarketplaceCatalogClient marketplaceCatalogClient = 
			MarketplaceCatalogClient.builder()
			.httpClient(ApacheHttpClient.builder().build())
			.credentialsProvider(ProfileCredentialsProvider.create())
			.build();
	/*
	 * retrieve all private offer information related to a single product
	 */
	public static void main(String[] args) {

		List<EntitySummary> entitySummaryList = getEntitySummaryList();
		
		// for each offer id, output the offer detail using DescribeEntity API
		
		for (EntitySummary entitySummary : entitySummaryList) {
			DescribeEntityRequest describeEntityRequest = 
					DescribeEntityRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityId(entitySummary.entityId())
					.build();
			DescribeEntityResponse describeEntityResponse = marketplaceCatalogClient.describeEntity(describeEntityRequest);
			ReferenceCodesUtils.formatOutput(describeEntityResponse);
		}
	}
	public static List<EntitySummary> getEntitySummaryList() {
		// define list entities filters
		
		EntityTypeFilters entityTypeFilters = 
				EntityTypeFilters.builder()
				.offerFilters(OfferFilters.builder()
						.targeting(OfferTargetingFilter.builder()
								.valueListWithStrings(OFFER_TARGETING_BUYERACCOUNTS)
								.build())
						.productId(OfferProductIdFilter.builder()
								.valueList(PRODUCT_ID)
								.build())
						.build())
				.build();
		
		ListEntitiesRequest listEntitiesRequest = 
				ListEntitiesRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityType(ENTITY_TYPE_OFFER).maxResults(50)
				.entityTypeFilters(entityTypeFilters)
				.nextToken(null)
				.build();
		
		ListEntitiesResponse listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
		
		// save all entitySummary of the results into entitySummaryList
		
		List<EntitySummary> entitySummaryList = new ArrayList<EntitySummary>();
		
		entitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
		
		while ( listEntitiesResponse.nextToken() != null && listEntitiesResponse.nextToken().length() > 0) {
			listEntitiesRequest = 
					ListEntitiesRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityType(ENTITY_TYPE_OFFER).maxResults(50)
					.entityTypeFilters(entityTypeFilters)
					.nextToken(listEntitiesResponse.nextToken())
					.build();
			listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
			entitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
		}
		return entitySummaryList;
	}

}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [DescribeEntity](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/DescribeEntity)
  + [ListEntities](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListEntities)

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python##catalog-api-reference-code) repository. 

```
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to retrieve all offer information
related to a single product
CAPI-97
"""

import argparse
import logging

import boto3
from botocore.exceptions import ClientError
from utils import helpers

logger = logging.getLogger(__name__)

mp_client = boto3.client("marketplace-catalog")


def get_entity_information(entity_id):
    """
    Returns information about a given entity
    Args: entity_id str: Entity to return
    Returns: dict: Dictionary of entity information
    """

    try:
        response = mp_client.describe_entity(
            Catalog="AWSMarketplace",
            EntityId=entity_id,
        )

        return response

    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Entity with ID %s not found.", entity_id)
        else:
            logger.error("Unexpected error: %s", e)


def list_entity_details(entity_type, entity_id):
    """
    Returns details about a given entity and entity type
    """

    entity_summary_list = []

    # filter will return details for given entity_id with BuyerAccounts targeting
    filter_list_param = {
        'OfferFilters':{
            'ProductId':{
                'ValueList':[entity_id]
            },
            'Targeting': {
                'ValueList': ["BuyerAccounts"]
            }
        }
    }

    try:
        response = mp_client.list_entities(
            Catalog="AWSMarketplace",
            EntityType=entity_type,
            EntityTypeFilters = filter_list_param,
            MaxResults=10
        )

    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Entity ID %s not found.", entity_id)
        else:
            logger.error("Unexpected error: %s", e)

    # add results to entity_summary_list
    entity_summary_list.extend(response["EntitySummaryList"])

    # if there are more than 10 offers, paginate through the results
    while "NextToken" in response and response["NextToken"] is not None:
        try:
            response = mp_client.list_entities(
                Catalog="AWSMarketplace",
                EntityType=entity_type,
                EntityTypeFilters = filter_list_param,
                NextToken=response["NextToken"],
                MaxResults=10
            )

        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Entity ID %s not found.", entity_id)
            else:
                logger.error("Unexpected error: %s", e)

        # add results to entity_summary_list
        entity_summary_list.extend(response["EntitySummaryList"])

        return entity_summary_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--entity-id",
        "-eid",
        help="Provide Entity ID corresponding to a product to filter offers on",
        required=True,
    )

    args = parser.parse_args()

    # Gets a offers associated with the entity_id
    response = list_entity_details(
        "Offer",
        entity_id=args.entity_id
    )

    if response: # if response is not empty

        # list_entity_details returns a list of offers
        for offer in response:

            print("-"*128)
            print(f"Terms for Offer ID: {offer['EntityId']}")
            print("-"*128)

            #retrieve offer information for each offer
            entity_information = get_entity_information(offer["EntityId"])

            helpers.pretty_print_datetime(entity_information)

    else:
        print(f"No information found for Entity ID: {args.entity_id}")
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [DescribeEntity](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/DescribeEntity)
  + [ListEntities](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListEntities)

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.