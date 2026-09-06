

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the pricing type of an agreement using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_GetAgreementPricingType_section"></a>

The following code examples show how to get the pricing type of an agreement.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository. 

```
package com.example.awsmarketplace.agreementapi.seller;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.AcceptedTerm;
import software.amazon.awssdk.services.marketplaceagreement.model.AgreementViewSummary;
import software.amazon.awssdk.services.marketplaceagreement.model.Filter;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.SearchAgreementsResponse;

import com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

import org.apache.commons.lang3.tuple.Triple;

import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityResponse;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;

/*
 * Obtain the pricing type of the agreement (contract, FPS, metered, free etc.)
 */
public class GetAgreementPricingType {

	private static final String FILTER_NAME = "OfferId";

	private static final String FILTER_VALUE = OFFER_ID;
	
	// Product types
	private static final String SAAS_PRODUCT = "SaaSProduct";
	private static final String AMI_PRODUCT = "AmiProduct";
	private static final String ML_PRODUCT = "MachineLearningProduct";
	private static final String CONTAINER_PRODUCT = "ContainerProduct";
	private static final String DATA_PRODUCT = "DataProduct";
	private static final String PROSERVICE_PRODUCT = "ProfessionalServicesProduct";
	private static final String AIQ_PRODUCT = "AiqProduct";

	// Pricing types
	private static final String CCP = "CCP";
	private static final String ANNUAL = "Annual";
	private static final String CONTRACT = "Contract";
	private static final String SFT = "SaaS Free Trial";
	private static final String HMA = "Hourly and Monthly Agreements";
	private static final String HOURLY = "Hourly";
	private static final String MONTHLY = "Monthly";
	private static final String AFPS = "Annual FPS";
	private static final String CFPS = "Contract FPS";
	private static final String CCPFPS = "CCP with FPS";
	private static final String BYOL = "BYOL";
	private static final String FREE = "Free";
	private static final String FTH = "Free Trials and Hourly";

	// Agreement term pricing types
	private static final Set<String> LEGAL = Set.of("LegalTerm");
	private static final Set<String> CONFIGURABLE_UPFRONT = Set.of("ConfigurableUpfrontPricingTerm");
	private static final Set<String> USAGE_BASED = Set.of("UsageBasedPricingTerm");
	private static final Set<String> CONFIGURABLE_UPFRONT_AND_USAGE_BASED = Set.of("ConfigurableUpfrontPricingTerm", "UsageBasedPricingTerm");
	private static final Set<String> FREE_TRIAL = Set.of("FreeTrialPricingTerm");
	private static final Set<String> RECURRING_PAYMENT = Set.of("RecurringPaymentTerm");
	private static final Set<String> USAGE_BASED_AND_RECURRING_PAYMENT = Set.of("UsageBasedPricingTerm", "RecurringPaymentTerm");
	private static final Set<String> FIXED_UPFRONT_AND_PAYMENT_SCHEDULE = Set.of("FixedUpfrontPricingTerm", "PaymentScheduleTerm");
	private static final Set<String> FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED = Set.of("FixedUpfrontPricingTerm", "PaymentScheduleTerm", "UsageBasedPricingTerm");
	private static final Set<String> BYOL_PRICING = Set.of("ByolPricingTerm");
	private static final Set<String> FREE_TRIAL_AND_USAGE_BASED = Set.of("FreeTrialPricingTerm", "UsageBasedPricingTerm");

	private static final List<Set<String>> ALL_AGREEMENT_TERM_TYPES_COMBINATION = Arrays.asList(LEGAL, CONFIGURABLE_UPFRONT, USAGE_BASED, CONFIGURABLE_UPFRONT_AND_USAGE_BASED,
			FREE_TRIAL, RECURRING_PAYMENT, USAGE_BASED_AND_RECURRING_PAYMENT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED, BYOL_PRICING, FREE_TRIAL_AND_USAGE_BASED);
	
	private static  MarketplaceAgreementClient marketplaceAgreementClient = 
			MarketplaceAgreementClient.builder()
			.httpClient(ApacheHttpClient.builder().build())
			.credentialsProvider(ProfileCredentialsProvider.create())
			.build();

	private static MarketplaceCatalogClient marketplaceCatalogClient = 
			MarketplaceCatalogClient.builder()
			.httpClient(ApacheHttpClient.builder().build())
			.credentialsProvider(ProfileCredentialsProvider.create())
			.build();

    /*
     * Get agreement Pricing Type given product type, agreement term types and offer types if needed
     */
	public static String getPricingType(String productType, Set<String> agreementTermType, Set<String> offerType) {
		Map<Triple<String, Set<String>, Set<String>>, String> pricingTypes = new HashMap<>();

		pricingTypes.put(Triple.of(SAAS_PRODUCT, CONFIGURABLE_UPFRONT_AND_USAGE_BASED, new HashSet<>()), CCP);
		pricingTypes.put(Triple.of(DATA_PRODUCT, CONFIGURABLE_UPFRONT_AND_USAGE_BASED, new HashSet<>()), CCP);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, CONFIGURABLE_UPFRONT, CONFIGURABLE_UPFRONT_AND_USAGE_BASED), ANNUAL);
		pricingTypes.put(Triple.of(AMI_PRODUCT, CONFIGURABLE_UPFRONT, CONFIGURABLE_UPFRONT_AND_USAGE_BASED), ANNUAL);
		pricingTypes.put(Triple.of(ML_PRODUCT, CONFIGURABLE_UPFRONT, CONFIGURABLE_UPFRONT_AND_USAGE_BASED), ANNUAL);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, CONFIGURABLE_UPFRONT, CONFIGURABLE_UPFRONT), CONTRACT);
		pricingTypes.put(Triple.of(AMI_PRODUCT, CONFIGURABLE_UPFRONT, CONFIGURABLE_UPFRONT), CONTRACT);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, CONFIGURABLE_UPFRONT, new HashSet<>()), CONTRACT);
		pricingTypes.put(Triple.of(DATA_PRODUCT, CONFIGURABLE_UPFRONT, new HashSet<>()), CONTRACT);
		pricingTypes.put(Triple.of(AIQ_PRODUCT, CONFIGURABLE_UPFRONT, new HashSet<>()), CONTRACT);
		pricingTypes.put(Triple.of(PROSERVICE_PRODUCT, CONFIGURABLE_UPFRONT, new HashSet<>()), CONTRACT);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, FREE_TRIAL, new HashSet<>()), SFT);
		pricingTypes.put(Triple.of(AMI_PRODUCT, USAGE_BASED_AND_RECURRING_PAYMENT, new HashSet<>()), HMA);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, USAGE_BASED, new HashSet<>()), HOURLY);
		pricingTypes.put(Triple.of(AMI_PRODUCT, USAGE_BASED, new HashSet<>()), HOURLY);
		pricingTypes.put(Triple.of(ML_PRODUCT, USAGE_BASED, new HashSet<>()), HOURLY);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, RECURRING_PAYMENT, new HashSet<>()), MONTHLY);
		pricingTypes.put(Triple.of(AMI_PRODUCT, RECURRING_PAYMENT, new HashSet<>()), MONTHLY);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED), AFPS);
		pricingTypes.put(Triple.of(AMI_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED), AFPS);
		pricingTypes.put(Triple.of(ML_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), AFPS);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), CFPS);
		pricingTypes.put(Triple.of(AMI_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE), CFPS);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), CFPS);
		pricingTypes.put(Triple.of(DATA_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), CFPS);
		pricingTypes.put(Triple.of(AIQ_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), CFPS);
		pricingTypes.put(Triple.of(PROSERVICE_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE, new HashSet<>()), CFPS);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED, new HashSet<>()), CCPFPS);
		pricingTypes.put(Triple.of(DATA_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED, new HashSet<>()), CCPFPS);
		pricingTypes.put(Triple.of(AIQ_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED, new HashSet<>()), CCPFPS);
		pricingTypes.put(Triple.of(PROSERVICE_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE_AND_USAGE_BASED, new HashSet<>()), CCPFPS);
		pricingTypes.put(Triple.of(AMI_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(SAAS_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(PROSERVICE_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(AIQ_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(ML_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(DATA_PRODUCT, BYOL_PRICING, new HashSet<>()), BYOL);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, LEGAL, new HashSet<>()), FREE);
		pricingTypes.put(Triple.of(AMI_PRODUCT, FREE_TRIAL_AND_USAGE_BASED, new HashSet<>()), FTH);
		pricingTypes.put(Triple.of(CONTAINER_PRODUCT, FREE_TRIAL_AND_USAGE_BASED, new HashSet<>()), FTH);
		pricingTypes.put(Triple.of(ML_PRODUCT, FREE_TRIAL_AND_USAGE_BASED, new HashSet<>()), FTH);

		Triple<String, Set<String>, Set<String>> key = Triple.of(productType, agreementTermType, offerType);

		if (pricingTypes.containsKey(key)) {
			return pricingTypes.get(key);
		} else {
			return "Unknown";
		}
	}

	/*
	 * Given product type and agreement term types, some combinations need to check offer term types as well.
	 */
	public static String needToCheckOfferTermsType(String productType, Set<String> agreementTermTypes) {
		Map<KeyPair, String> offerTermTypes = new HashMap<>();
		offerTermTypes.put(new KeyPair(CONTAINER_PRODUCT, CONFIGURABLE_UPFRONT), "Y");
		offerTermTypes.put(new KeyPair(AMI_PRODUCT, CONFIGURABLE_UPFRONT), "Y");
		offerTermTypes.put(new KeyPair(CONTAINER_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE), "Y");
		offerTermTypes.put(new KeyPair(AMI_PRODUCT, FIXED_UPFRONT_AND_PAYMENT_SCHEDULE), "Y");

		KeyPair key = new KeyPair(productType, agreementTermTypes);
		if (offerTermTypes.containsKey(key)) {
			return offerTermTypes.get(key);
		} else {
			return null;
		}
	}

	public static List<AgreementViewSummary> getAgreementsById() {
		
		List<AgreementViewSummary> agreementSummaryList = new ArrayList<AgreementViewSummary>();

		// Set PartyType filter to PARTY_TYPE_FILTER_VALUE_PROPOSER to return agreements where you are the proposer.
		// Change to PARTY_TYPE_FILTER_VALUE_ACCEPTOR to return agreements where you are the acceptor.
		Filter partyType = Filter.builder().name(PARTY_TYPE_FILTER_NAME).values(PARTY_TYPE_FILTER_VALUE_PROPOSER).build();

		Filter agreementType = Filter.builder().name(AGREEMENT_TYPE_FILTER_NAME).values(AGREEMENT_TYPE_FILTER_VALUE_PURCHASEAGREEMENT).build();

		Filter customizeFilter = Filter.builder().name(FILTER_NAME).values(FILTER_VALUE).build();

		SearchAgreementsRequest searchAgreementsRequest = 
				SearchAgreementsRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.filters(partyType, agreementType, customizeFilter).build();

		SearchAgreementsResponse searchResultResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);

		agreementSummaryList.addAll(searchResultResponse.agreementViewSummaries());

		while (searchResultResponse.nextToken() != null && searchResultResponse.nextToken().length() > 0) {
			searchAgreementsRequest = SearchAgreementsRequest.builder().catalog(AWS_MP_CATALOG)
					.filters(partyType, agreementType).nextToken(searchResultResponse.nextToken()).build();
			searchResultResponse = marketplaceAgreementClient.searchAgreements(searchAgreementsRequest);
			agreementSummaryList.addAll(searchResultResponse.agreementViewSummaries());
		}
		return agreementSummaryList;

	}

	static class KeyPair {
		private final String first;
		private final Set<String> second;

		public KeyPair(String productType, Set<String> second) {
			this.first = productType;
			this.second = second;
		}

		@Override
		public int hashCode() {
			return Objects.hash(first, second);
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null || getClass() != obj.getClass())
				return false;
			KeyPair other = (KeyPair) obj;
			return Objects.equals(first, other.first) && Objects.equals(second, other.second);
		}
	}

	/*
	 * Get all the term types for the offer
	 */
	public static Set<String> getOfferTermTypes(String offerId) {

		Set<String> offerTermTypes = new HashSet<String>();

		DescribeEntityRequest request = 
				DescribeEntityRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityId(offerId)
				.build();

		DescribeEntityResponse result = marketplaceCatalogClient.describeEntity(request);

		String details = result.details();
		
		try {
			ObjectMapper objectMapper = new ObjectMapper();
			JsonNode rootNode = objectMapper.readTree(details);
			JsonNode termsNode = rootNode.get(ATTRIBUTE_TERMS);

			for (JsonNode termNode : termsNode) {
				if (termNode.get(ATTRIBUTE_TYPE_ENTITY) != null ) {
					offerTermTypes.add(termNode.get(ATTRIBUTE_TYPE_ENTITY).asText());
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		return offerTermTypes;

	}

	/*
	 * Get all the agreement term types
	 */
	public static Set<String> getAgreementTermTypes(GetAgreementTermsResponse agreementTerm) {
		Set<String> agreementTermTypes = new HashSet<String>();
		try {
			for (AcceptedTerm term : agreementTerm.acceptedTerms()) {
				ObjectMapper objectMapper = new ObjectMapper();
				JsonNode termNode = objectMapper.readTree(getJson(term));
				Iterator<Map.Entry<String, JsonNode>> fieldsIterator = termNode.fields();
				while (fieldsIterator.hasNext()) {
					Map.Entry<String, JsonNode> entry = fieldsIterator.next();
					JsonNode value = entry.getValue();
					if (value.isObject() && value.has(ATTRIBUTE_TYPE_AGREEMENT)) {
						agreementTermTypes.add(value.get(ATTRIBUTE_TYPE_AGREEMENT).asText());
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return agreementTermTypes;

	}

	/*
	 * make sure all elements in array2 exist in array1
	 */
	public static boolean allElementsExist(Set<String> array1, Set<String> array2) {
		for (String element : array2) {
			boolean found = false;
			for (String str : array1) {
				if (element.equals(str)) {
					found = true;
					break;
				}
			}
			if (!found) {
				return false;
			}
		}
		return true;
	}

	/*
	 * Find the combinations of the agreement term types for the agreement
	 */
	public static Set<String> getMatchedTermTypesCombination(Set<String> agreementTermTypes) {
		Set<String> matchedCombination = new HashSet<String>();
		for (Set<String> element : ALL_AGREEMENT_TERM_TYPES_COMBINATION) {
			if (allElementsExist(agreementTermTypes, element)) {
				matchedCombination = element;
			}
		}
		return matchedCombination;
	}

	public static void main(String[] args) {

		List<AgreementViewSummary> agreements = getAgreementsById();

		for (AgreementViewSummary summary : agreements) {
			String pricingType = "";
			String agreementId = summary.agreementId();
			System.out.println(agreementId);
			String offerId = summary.proposalSummary().offerId();
			
			//get all pricing term types for the offer in the agreement
			Set<String> offerTermTypes = getOfferTermTypes(offerId);
			String productType = summary.proposalSummary().resources().get(0).type();
			
			//get all pricing term types for the agreement
			GetAgreementTermsRequest getAgreementTermsRequest = 
					GetAgreementTermsRequest.builder().agreementId(agreementId)
					.build();
			GetAgreementTermsResponse getAgreementTermsResponse = marketplaceAgreementClient.getAgreementTerms(getAgreementTermsRequest);
			Set<String> agreementTermTypes = getAgreementTermTypes(getAgreementTermsResponse);
			
			//get matched pricing term type combination set
			Set<String> agreementMatchedTermType = getMatchedTermTypesCombination(agreementTermTypes);
			
			//check to see if this agreement pricing term combination needs additional check on offer pricing terms
			String needToCheckOfferType = needToCheckOfferTermsType(productType, agreementMatchedTermType);
			
			// get the pricing type for the agreement based on the product type, agreement term types and offer term types if needed
			if (needToCheckOfferType != null) {
				Set<String> offerMatchedTermType = getMatchedTermTypesCombination(offerTermTypes);
				pricingType = getPricingType(productType, agreementMatchedTermType, offerMatchedTermType);
			} else if (agreementMatchedTermType == LEGAL) {
				pricingType = FREE;
			} else {
				pricingType = getPricingType(productType, agreementMatchedTermType, new HashSet());
			}
			System.out.println("Pricing type is " + pricingType);
		}
	}

	private static String getJson(Object result) {
		String json = "";

		try {
			ObjectMapper om = new ObjectMapper();
			om.setVisibility(PropertyAccessor.FIELD, Visibility.ANY);
			om.registerModule(new JavaTimeModule());
			ObjectWriter ow = om.writer().withDefaultPrettyPrinter();

			json = ow.writeValueAsString(result);
		} catch (JsonProcessingException e) {
			e.printStackTrace();
		}
		return json;
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
Obtain the pricing type of the agreement (contract, FPS, metered, free etc.)
AG-16
"""

import json
import logging

import boto3
from botocore.exceptions import ClientError

# To search by offer id: OfferId; by product id: ResourceIdentifier; by product type: ResourceType
idType = "OfferId"

# replace id value as needed
idValue = "offer-1111111111111"

MAX_PAGE_RESULTS = 10

# catalog; switch to AWSMarketplace for release
AWSMPCATALOG = "AWSMarketplace"

# product types

SaaSProduct = "SaaSProduct"
AmiProduct = "AmiProduct"
MLProduct = "MachineLearningProduct"
ContainerProduct = "ContainerProduct"
DataProduct = "DataProduct"
ProServiceProduct = "ProfessionalServicesProduct"
AiqProduct = "AiqProduct"

# Define pricing types
CCP = "CCP"
Annual = "Annual"
Contract = "Contract"
SFT = "SaaS Free Trial"
HMA = "Hourly and Monthly Agreements"
Hourly = "Hourly"
Monthly = "Monthly"
AFPS = "Annual FPS"
CFPS = "Contract FPS"
CCPFPS = "CCP with FPS"
BYOL = "BYOL"
Free = "Free"
FTH = "Free Trials and Hourly"

# Define Agreement Term Types
legal = ["LegalTerm"]
config = ["ConfigurableUpfrontPricingTerm"]
usage = ["UsageBasedPricingTerm"]
config_usage = ["ConfigurableUpfrontPricingTerm", "UsageBasedPricingTerm"]
freeTrial = ["FreeTrialPricingTerm"]
recur = ["RecurringPaymentTerm"]
usage_recur = ("UsageBasedPricingTerm", "RecurringPaymentTerm")
fixed_payment = ["FixedUpfrontPricingTerm", "PaymentScheduleTerm"]
fixed_payment_usage = [
    "FixedUpfrontPricingTerm",
    "PaymentScheduleTerm",
    "UsageBasedPricingTerm",
]
byol = ["ByolPricingTerm"]
freeTrial_usage = ("FreeTrialPricingTerm", "UsageBasedPricingTerm")
all_agreement_types_combination = (
    legal,
    config,
    usage,
    config_usage,
    freeTrial,
    recur,
    usage_recur,
    fixed_payment,
    fixed_payment_usage,
    byol,
    freeTrial_usage,
)


# get pricing type method given product type, agreement temr type and offer type if needed
def get_pricing_type(product_type, agreement_term_type, offer_type):
    pricing_types = {
        (SaaSProduct, frozenset(config_usage), frozenset("")): CCP,
        (DataProduct, frozenset(config_usage), frozenset("")): CCP,
        (ContainerProduct, frozenset(config), frozenset(config_usage)): Annual,
        (AmiProduct, frozenset(config), frozenset(config_usage)): Annual,
        (MLProduct, frozenset(config), frozenset(config_usage)): Annual,
        (ContainerProduct, frozenset(config), frozenset(config)): Contract,
        (AmiProduct, frozenset(config), frozenset(config)): Contract,
        (SaaSProduct, frozenset(config), frozenset("")): Contract,
        (DataProduct, frozenset(config), frozenset("")): Contract,
        (AiqProduct, frozenset(config), frozenset("")): Contract,
        (ProServiceProduct, frozenset(config), frozenset("")): Contract,
        (SaaSProduct, frozenset(freeTrial), frozenset("")): SFT,
        (AmiProduct, frozenset(usage_recur), frozenset("")): HMA,
        (SaaSProduct, frozenset(usage), frozenset("")): Hourly,
        (AmiProduct, frozenset(usage), frozenset("")): Hourly,
        (ContainerProduct, frozenset(usage), frozenset("")): Hourly,
        (MLProduct, frozenset(usage), frozenset("")): Hourly,
        (ContainerProduct, frozenset(recur), frozenset("")): Monthly,
        (AmiProduct, frozenset(recur), frozenset("")): Monthly,
        (
            ContainerProduct,
            frozenset(fixed_payment),
            frozenset(fixed_payment_usage),
        ): AFPS,
        (AmiProduct, frozenset(fixed_payment), frozenset(fixed_payment_usage)): AFPS,
        (MLProduct, frozenset(fixed_payment), frozenset("")): AFPS,
        (ContainerProduct, frozenset(fixed_payment), frozenset(fixed_payment)): CFPS,
        (AmiProduct, frozenset(fixed_payment), frozenset(fixed_payment)): CFPS,
        (SaaSProduct, frozenset(fixed_payment), frozenset("")): CFPS,
        (DataProduct, frozenset(fixed_payment), frozenset("")): CFPS,
        (AiqProduct, frozenset(fixed_payment), frozenset("")): CFPS,
        (ProServiceProduct, frozenset(fixed_payment), frozenset("")): CFPS,
        (SaaSProduct, frozenset(fixed_payment_usage), frozenset("")): CCPFPS,
        (DataProduct, frozenset(fixed_payment_usage), frozenset("")): CCPFPS,
        (AiqProduct, frozenset(fixed_payment_usage), frozenset("")): CCPFPS,
        (ProServiceProduct, frozenset(fixed_payment_usage), frozenset("")): CCPFPS,
        (AmiProduct, frozenset(byol), frozenset("")): BYOL,
        (SaaSProduct, frozenset(byol), frozenset("")): BYOL,
        (ProServiceProduct, frozenset(byol), frozenset("")): BYOL,
        (AiqProduct, frozenset(byol), frozenset("")): BYOL,
        (MLProduct, frozenset(byol), frozenset("")): BYOL,
        (ContainerProduct, frozenset(byol), frozenset("")): BYOL,
        (DataProduct, frozenset(byol), frozenset("")): BYOL,
        (ContainerProduct, frozenset(legal), frozenset("")): Free,
        (AmiProduct, frozenset(freeTrial_usage), frozenset("")): FTH,
        (ContainerProduct, frozenset(freeTrial_usage), frozenset("")): FTH,
        (MLProduct, frozenset(freeTrial_usage), frozenset("")): FTH,
    }

    key = (product_type, agreement_term_type, offer_type)
    if key in pricing_types:
        return pricing_types[key]
    else:
        return "Unknown"


# Example usage for testing purpose
"""
product_type = SaaSProduct
agreement_term_type = frozenset(config_usage)
offer_type = frozenset('')
pricing_type = get_pricing_type(product_type, agreement_term_type, offer_type)
print("pricing type = " + pricing_type)  # Output: CCP
"""


# check if offer term types are needed; if Y, needed
def get_offer_term_type(product_type, agreement_term_type):
    offer_term_types = {
        (ContainerProduct, frozenset(config)): "Y",
        (AmiProduct, frozenset(config)): "Y",
        (ContainerProduct, frozenset(fixed_payment)): "Y",
        (AmiProduct, frozenset(fixed_payment)): "Y",
        (AmiProduct, frozenset(fixed_payment), frozenset(fixed_payment)): "Y",
    }

    key = (product_type, agreement_term_type)
    if key in offer_term_types:
        return offer_term_types[key]
    else:
        return


logger = logging.getLogger(__name__)


def get_agreements(mp_client):
    AgreementSummaryList = []
    # Set PartyType to "Proposer" to return agreements where you are the proposer.
    # Change to "Acceptor" to return agreements where you are the acceptor.
    partyTypes = ["Proposer"]
    for value in partyTypes:
        try:
            agreement = mp_client.search_agreements(
                catalog=AWSMPCATALOG,
                maxResults=MAX_PAGE_RESULTS,
                filters=[
                    {"name": "PartyType", "values": [value]},
                    {"name": idType, "values": [idValue]},
                    {"name": "AgreementType", "values": ["PurchaseAgreement"]},
                ],
            )
        except ClientError as e:
            logger.error("Could not complete search_agreements request.")
            raise

        AgreementSummaryList.extend(agreement["agreementViewSummaries"])

        while "nextToken" in agreement and agreement["nextToken"] is not None:
            try:
                agreement = mp_client.search_agreements(
                    catalog=AWSMPCATALOG,
                    maxResults=MAX_PAGE_RESULTS,
                    nextToken=agreement["nextToken"],
                    filters=[
                        {"name": "PartyType", "values": [value]},
                        {"name": idType, "values": [idValue]},
                        {"name": "AgreementType", "values": ["PurchaseAgreement"]},
                    ],
                )
            except ClientError as e:
                logger.error("Could not complete search_agreements request.")
                raise

            AgreementSummaryList.extend(agreement["agreementViewSummaries"])

    return AgreementSummaryList


def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Looking for an agreement in the AWS Marketplace Catalog.")
    print("-" * 88)

    mp_client = boto3.client("marketplace-agreement")

    # find all agreements matching the specified idType and idValue
    agreements = get_agreements(mp_client)

    for item in agreements:
        pricingType = ""
        agreement_id = item["agreementId"]

        # get term types inside offer
        offer_term_types = get_offer_term_types(item)

        # even though multiple product types are allowed for one agreement, only need the first one
        productType = item["proposalSummary"]["resources"][0]["type"]

        # get agreement terms types
        agreementTerm = mp_client.get_agreement_terms(agreementId=agreement_id)

        agreementTermTypes = get_agreement_term_types(agreementTerm)

        # match with agreement term type group
        matchedTermType = getMatchedTermTypesCombination(agreementTermTypes)

        # check if offer term type is needed.
        offer_term_type_needed = get_offer_term_type(
            productType, frozenset(matchedTermType)
        )

        # get pricing type given product type, agreement term types and offer type if needed;
        # one excpetion is Container with Legal term. LegalTerm needs to be the only term present
        if offer_term_type_needed is not None:
            matchedOfferTermTypes = getMatchedTermTypesCombination(offer_term_types)
            print(f"matchedOfferTermType = {matchedOfferTermTypes}")
            pricingType = get_pricing_type(
                productType,
                frozenset(matchedTermType),
                frozenset(matchedOfferTermTypes),
            )
        elif set(matchedTermType) == set(legal):
            pricingType = Free
        else:
            pricingType = get_pricing_type(
                productType, frozenset(matchedTermType), frozenset("")
            )

        print(
            f"agreementId={agreement_id};productType={productType}; agreementTermTypes={agreementTermTypes}; matchedTermType={matchedTermType}; offerTermTypeNeeded={offer_term_type_needed}; offer_term_types={offer_term_types}"
        )
        print(f"pricing type={pricingType}")


def getMatchedTermTypesCombination(agreementTermTypes):
    matchedCombination = ()
    for element in all_agreement_types_combination:
        if check_elements(agreementTermTypes, element):
            matchedCombination = element
    return matchedCombination


def get_offer_term_types(item):
    offer_id = item["proposalSummary"]["offerId"]
    mp_catalogAPI_client = boto3.client("marketplace-catalog")
    offer_document = get_entity_information(mp_catalogAPI_client, offer_id)
    offerDetail = offer_document["Details"]
    offerDetail_json_object = json.loads(offerDetail)
    offer_term_types = [term["Type"] for term in offerDetail_json_object["Terms"]]
    return offer_term_types


# make sure all elements in array2 exist in array1
def check_elements(array1, array2):
    for element in array2:
        if element not in array1:
            return False
    return True


def get_entity_information(mp_client, entity_id):
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


def get_agreement_term_types(agreementTerm):
    types = []
    for term in agreementTerm["acceptedTerms"]:
        for value in term.values():
            if isinstance(value, dict) and "type" in value:
                types.append(value["type"])
    return types


if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.