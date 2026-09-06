

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List all AMI, SaaS, or Container products and associated public offers using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ListProducts_section"></a>

The following code examples show how to list all AMI, SaaS, or Container products and associated public offers.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code) repository. 

```
package com.example.awsmarketplace.catalogapi;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.EntitySummary;
import software.amazon.awssdk.services.marketplacecatalog.model.EntityTypeFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferProductIdFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferStateFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferTargetingFilter;

public class ListEntities {

	/*
	 * List all my AMI or SaaS or Container products and associated public offers
	 */
	public static void main(String[] args) {
		
		Map<String, List<EntitySummary>> allProductsWithOffers = getAllProductsWithOffers();
	
		ReferenceCodesUtils.formatOutput(allProductsWithOffers);
	}

	public static Map<String, List<EntitySummary>> getAllProductsWithOffers() {
		MarketplaceCatalogClient marketplaceCatalogClient = 
				MarketplaceCatalogClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();
		
		Map<String, List<EntitySummary>> allProductsWithOffers = new HashMap<String, List<EntitySummary>> ();

		// get all product entities
		List<EntitySummary> productEntityList = new ArrayList<EntitySummary>();

		ListEntitiesRequest listEntitiesRequest = 
				ListEntitiesRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityType(PRODUCT_TYPE_AMI)
				.maxResults(10)
				.nextToken(null)
				.build();
		
	 
		ListEntitiesResponse listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);

		productEntityList.addAll(listEntitiesResponse.entitySummaryList());


		while (listEntitiesResponse.nextToken() != null) {
			listEntitiesRequest = 
					ListEntitiesRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityType(PRODUCT_TYPE_AMI)
					.maxResults(10)
					.nextToken(listEntitiesResponse.nextToken())
					.build();
			listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
			productEntityList.addAll(listEntitiesResponse.entitySummaryList());
		}
		
		// loop through each product entity and get the public released offers associated using product id filter
		
		for ( EntitySummary productEntitySummary : productEntityList) {
			EntityTypeFilters entityTypeFilters = 
					EntityTypeFilters.builder()
					.offerFilters(OfferFilters.builder()
							.targeting(OfferTargetingFilter.builder()
									.valueListWithStrings(OFFER_TARGETING_NONE)
									.build())
							.state(OfferStateFilter.builder()
									.valueListWithStrings(OFFER_STATE_RELEASED)
									.build())
							.productId(OfferProductIdFilter.builder()
									.valueList(productEntitySummary.entityId())
									.build())
							.build())
					.build();
			
			listEntitiesRequest = 
					ListEntitiesRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityType(ENTITY_TYPE_OFFER)
					.maxResults(10)
					.entityTypeFilters(entityTypeFilters)
					.nextToken(null)
					.build();
			
			listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
			
			// save all entitySummary of the results into entitySummaryList
			
			List<EntitySummary> offerEntitySummaryList = new ArrayList<EntitySummary>();
			
			offerEntitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
			
			while ( listEntitiesResponse.nextToken() != null && listEntitiesResponse.nextToken().length() > 0) {
				listEntitiesRequest = 
						ListEntitiesRequest.builder()
						.catalog(AWS_MP_CATALOG)
						.entityType(ENTITY_TYPE_OFFER)
						.maxResults(10)
						.entityTypeFilters(entityTypeFilters)
						.nextToken(listEntitiesResponse.nextToken())
						.build();
				listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
				offerEntitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
			}
			
			// save final results into map; key = product id; value = offer entity summary list
			
			allProductsWithOffers.put(productEntitySummary.entityId(), offerEntitySummaryList);
		}
		return allProductsWithOffers;
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
Shows how to use the AWS SDK for Python (Boto3) to display information about AMI products and their associated offers in the AWS Marketplace Catalog
CAPI-27
"""

import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

MAX_PAGE_RESULTS = 10

try:
    mp_client = boto3.client("marketplace-catalog")
except ClientError as e:
    logger.error("Could not create boto3 client.")
    raise


def pretty_print(response):
    json_object = json.dumps(response, indent=4)
    print(json_object)


def describe_entity(entity_id):
    """
    Returns entity details
    Args: entity_id str: The entity ID of the product or offer
    Returns: dict: The entity details
    """
    try:
        response = mp_client.describe_entity(
            Catalog="AWSMarketplace", EntityId=entity_id
        )
    except ClientError as e:
        logger.error("Could not complete describe_entity request.")
        raise

    # De-stringify the details
    response["Details"] = json.loads(response["Details"])

    return response


def get_entities(entity_type, visibility=None):
    """
    Returns list of entities for provided entity_type
    Args: entity_type str: Type of entity list to return, in our case AmiProduct or Offer
    Returns: list: Abbreviated list of entity information
    """
    EntitySummaryList = []

    # Get the first page of results
    try:
        response = mp_client.list_entities(
            Catalog="AWSMarketplace",
            EntityType=entity_type,
            MaxResults=MAX_PAGE_RESULTS,
        )
    except ClientError as e:
        logger.error("Could not complete list_entities request.")
        raise

    EntitySummaryList.extend(response["EntitySummaryList"])

    # Get subsequent pages of results if previous response contained a NextToken
    while "NextToken" in response:
        try:
            response = mp_client.list_entities(
                Catalog="AWSMarketplace",
                EntityType=entity_type,
                MaxResults=MAX_PAGE_RESULTS,
                NextToken=response["NextToken"],
            )
        except ClientError as e:
            logger.error("Could not complete list_entities request.")
            raise

        EntitySummaryList.extend(response["EntitySummaryList"])

    # if visibility is provided, filter the list to only include entities with that visibility
    if visibility is not None:
        EntitySummaryList = [
            entity for entity in EntitySummaryList if entity["Visibility"] == visibility
        ]

    return EntitySummaryList


def get_enhanced_product_list(entity_type):
    """
    Returns an enhanced list of products with product details and offer details
    Args: entity_type str: Type of entity list to return, in our case AmiProduct
    Returns: list: Enhanced list of dictionary objects containing product and offer details
    """

    product_list = get_entities(entity_type)

    # Loop through product list and append product details to each product
    for product in product_list:
        # appends product details to product dictionary
        product["ProductDetails"] = describe_entity(product["EntityId"])["Details"]
        # creating an empty list for offer details
        product["OfferDetailsList"] = []

    return product_list


def attach_offer_details(product_list):
    """
    Loops through offer information and appends offer details to product list
    Args: product_list list: List of product dictionaries
    Returns: list: Enhanced list of dictionary objects containing product and offer details
    """
    offer_list = get_entities("Offer", "Public")

    # Loop through offer list and append offer details to each product
    for offer in offer_list:
        offer["OfferDetails"] = describe_entity(offer["EntityId"])["Details"]

        # Extracts product-id from offer
        product_id = offer["OfferDetails"]["ProductId"]

        # Determines if product-id referenced in offer matches product-id in product list
        product_dict = next(
            filter(lambda product: product["EntityId"] == product_id, product_list),
            None,
        )

        # If product-id matches, appends offer details to product dictionary
        if product_dict is not None:
            # logger.info(f"Offer product Id {offer['OfferDetails']['ProductId']} found in product dictionary. Updating product dictionary with offer details")
            product_dict["OfferDetailsList"].append(offer["OfferDetails"])

        else:
            # logger.info("Offer product Id {offer['OfferDetails']['ProductId']} not found. Skipping offer details update")
            pass

    return product_list


def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Retrieving products and public offer information....")
    print("-" * 88)

    # Builds a list of products and their details
    product_list = get_enhanced_product_list("AmiProduct")

    # Queries offer information and attaches it to the product list
    product_offer_list = attach_offer_details(product_list)

    pretty_print(product_offer_list)
    return product_offer_list


if __name__ == "__main__":
    usage_demo()
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [DescribeEntity](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/DescribeEntity)
  + [ListEntities](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/ListEntities)

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.