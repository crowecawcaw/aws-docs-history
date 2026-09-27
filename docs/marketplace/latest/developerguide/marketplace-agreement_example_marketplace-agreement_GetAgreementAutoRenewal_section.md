

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Get the auto renewal terms of an agreement using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_GetAgreementAutoRenewal_section"></a>

The following code examples show how to get the auto renewal terms of an agreement.

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
import software.amazon.awssdk.services.marketplaceagreement.model.AcceptedTerm;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.EndTimeBehavior;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.GetAgreementTermsResponse;
import software.amazon.awssdk.services.marketplaceagreement.model.PaymentScheduleEntry;
import software.amazon.awssdk.services.marketplaceagreement.model.PriceIncrease;
import software.amazon.awssdk.services.marketplaceagreement.model.RenewalTerm;
import software.amazon.awssdk.services.marketplaceagreement.model.TermTemplate;

public class GetAgreementAutoRenewal {

	/*
	 * Obtain the auto-renewal status of the agreement
	 */

	public static void main(String[] args) {

		String agreementId = args.length > 0 ? args[0] : AGREEMENT_ID;

		RenewalTerm renewalTerm = getRenewalTerm(agreementId);

		printRenewalTerm(renewalTerm);

		printEndTimeBehavior(agreementId);
	}

	/*
	 * Returns whether the agreement is set to auto renew, or "No Auto Renewal" when there is no
	 * renewal term or the flag is not set. Delegates to getRenewalTerm so there is a single API path.
	 */
	public static String getAutoRenewal(String agreementId) {

		RenewalTerm renewalTerm = getRenewalTerm(agreementId);

		if (renewalTerm != null && renewalTerm.configuration() != null
				&& renewalTerm.configuration().enableAutoRenew() != null) {
			return String.valueOf(renewalTerm.configuration().enableAutoRenew().booleanValue());
		}
		return "No Auto Renewal";
	}

	/*
	 * Reads the agreement's renewal term. These values come from the offer and are read-only here.
	 * Returns the first renewal term found, or null when the agreement has none.
	 */
	public static RenewalTerm getRenewalTerm(String agreementId) {

		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		String nextToken = null;

		do {
			GetAgreementTermsResponse getAgreementTermsResponse =
					marketplaceAgreementClient.getAgreementTerms(
							GetAgreementTermsRequest.builder()
							.agreementId(agreementId)
							.nextToken(nextToken)
							.build());

			for (AcceptedTerm acceptedTerm : getAgreementTermsResponse.acceptedTerms()) {
				// AcceptedTerm is a union. Only the renewal term is of interest here.
				if (acceptedTerm.renewalTerm() != null) {
					return acceptedTerm.renewalTerm();
				}
			}

			nextToken = getAgreementTermsResponse.nextToken();
		} while (nextToken != null);

		return null;
	}

	/*
	 * Prints the fields of a renewal term.
	 */
	public static void printRenewalTerm(RenewalTerm renewalTerm) {

		if (renewalTerm == null) {
			System.out.println("No Auto Renewal");
			return;
		}

		System.out.println("Renewal Term ID: " + renewalTerm.id());

		if (renewalTerm.configuration() != null) {
			System.out.println("Auto Renew Enabled: " + renewalTerm.configuration().enableAutoRenew());
		}

		// ISO 8601 duration. The customer can no longer change enableAutoRenew once the
		// agreement is within this duration of its end date. Absent when the offer sets no deadline,
		// which leaves the customer free to change enableAutoRenew up to the end date.
		if (renewalTerm.lockoutPeriod() != null) {
			System.out.println("Lockout Period: " + renewalTerm.lockoutPeriod());
		} else {
			System.out.println("Lockout Period: none");
		}

		// Absent means the agreement can renew without limit.
		if (renewalTerm.maxRenewals() != null) {
			System.out.println("Max Renewals: " + renewalTerm.maxRenewals());
		} else {
			System.out.println("Max Renewals: unlimited");
		}

		// Absent unless the offer sets a separate deadline for adjusting the renewal price.
		if (renewalTerm.adjustmentDeadline() != null) {
			System.out.println("Adjustment Deadline: " + renewalTerm.adjustmentDeadline());
		}

		printPriceIncrease(renewalTerm.priceIncrease());

		for (TermTemplate termTemplate : renewalTerm.termTemplates()) {
			printTermTemplate(termTemplate);
		}
	}

	/*
	 * Reads the price change that applies when the agreement renews.
	 */
	public static void printPriceIncrease(PriceIncrease priceIncrease) {

		if (priceIncrease == null) {
			System.out.println("Price Increase: none (the price does not change at renewal)");
			return;
		}

		// PriceIncrease is a union. Exactly one variant is set.
		if (priceIncrease.fixedPercentage() != null) {
			System.out.println("Fixed Price Increase Percentage: " + priceIncrease.fixedPercentage().value());
		} else if (priceIncrease.percentageRange() != null) {
			// The uplift is open within this range; defaultValue applies if you take no action.
			System.out.println("Price Increase Min Percentage: " + priceIncrease.percentageRange().minValue());
			System.out.println("Price Increase Max Percentage: " + priceIncrease.percentageRange().maxValue());
			System.out.println("Price Increase Default Percentage: " + priceIncrease.percentageRange().defaultValue());
		}
	}

	/*
	 * Reads the term template that applies when the agreement renews.
	 */
	public static void printTermTemplate(TermTemplate termTemplate) {

		// TermTemplate is a union. Only payment schedule templates are supported today.
		if (termTemplate.paymentScheduleTermTemplate() == null) {
			System.out.println("Term Template: not a payment schedule template");
			return;
		}

		System.out.println("Payment Schedule Template:");
		for (PaymentScheduleEntry entry : termTemplate.paymentScheduleTermTemplate().schedule()) {
			// chargeDateOffset is relative to the start of the renewed agreement, e.g. "P3M".
			String line = "  Charge Date Offset: " + entry.chargeDateOffset()
					+ ", Charge Percentage: " + entry.chargePercentage();

			// Absent unless the schedule pins charges to a day of the month.
			if (entry.dayOfMonth() != null) {
				line += ", Day Of Month: " + entry.dayOfMonth();
			}

			System.out.println(line);
		}
	}

	/*
	 * Reads the agreement's end time behavior: whether it will renew, be replaced, or expire, and why.
	 */
	public static void printEndTimeBehavior(String agreementId) {

		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		DescribeAgreementResponse describeAgreementResponse =
				marketplaceAgreementClient.describeAgreement(
						DescribeAgreementRequest.builder().agreementId(agreementId).build());

		EndTimeBehavior endTimeBehavior = describeAgreementResponse.endTimeBehavior();
		if (endTimeBehavior == null) {
			System.out.println("End Time Behavior: none (this agreement has no end date)");
			return;
		}

		System.out.println("End Time Behavior Type: " + endTimeBehavior.typeAsString());

		// The reason the agreement does not renew, and absent when it does. My own PROPOSER_RENEW_OPTED_OUT
		// leaves enableAutoRenew untouched, so the flag can read true even when this says it will not renew.
		if (endTimeBehavior.reasonCodeAsString() != null) {
			System.out.println("End Time Behavior Reason Code: " + endTimeBehavior.reasonCodeAsString());
		}

		// renewalSummary is present whenever type is RENEW, but offerId inside it is absent
		// until a renewal offer is created.
		if (endTimeBehavior.renewalSummary() != null && endTimeBehavior.renewalSummary().offerId() != null) {
			System.out.println("Renewal Offer ID: " + endTimeBehavior.renewalSummary().offerId());
		}
	}

}
```
+  For API details, see [GetAgreementTerms](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementTerms) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository. 

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Obtain the auto-renewal status of the agreement
AG-15
"""

import json
import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import utils.helpers as helper


import boto3
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

logger = logging.getLogger(__name__)

# agreement id
AGREEMENT_ID = "agmt-11111111111111111111"

# to use sample file or not
USE_SAMPLE_FILE = False
SAMPLE_FILE_NAME = "mockup_agreement_terms.json"

# attribute name
ROOT_ELEM = "acceptedTerms"
TERM_NAME = "renewalTerm"
CONFIG_ELEM = "configuration"
ATTRIBUTE_NAME = "enableAutoRenew"


def get_renewal_term(entity_id):
    """
    Reads the agreement's renewal term. These values come from the offer and are read-only here.
    Args: entity_id str: Agreement to read the terms of
    Returns: dict: The first renewal term found, or None when the agreement has none
    """

    try:
        next_token = None

        while True:
            if USE_SAMPLE_FILE:
                sample_file = os.path.join(os.path.dirname(__file__), SAMPLE_FILE_NAME)
                terms = open_json_file(sample_file)
            elif next_token is None:
                terms = mp_client.get_agreement_terms(agreementId=entity_id)
            else:
                terms = mp_client.get_agreement_terms(
                    agreementId=entity_id, nextToken=next_token
                )

            for term in terms[ROOT_ELEM]:
                # acceptedTerms is a union. Only the renewal term is of interest here.
                if TERM_NAME in term:
                    return term[TERM_NAME]

            if USE_SAMPLE_FILE:
                break

            next_token = terms.get("nextToken")
            if not next_token:
                break

    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Agreement with ID %s not found.", entity_id)
        else:
            logger.error("Unexpected error: %s", e)

    return None


def get_auto_renewal(entity_id):
    """
    Returns whether the agreement is set to auto renew, or "No Auto Renewal" when there is no
    renewal term or the flag is not set. Delegates to get_renewal_term so there is a single API path.
    Args: entity_id str: Agreement to read the terms of
    Returns: str: "True"/"False", or "No Auto Renewal"
    """

    renewal_term = get_renewal_term(entity_id)

    if (
        renewal_term is not None
        and CONFIG_ELEM in renewal_term
        and renewal_term[CONFIG_ELEM].get(ATTRIBUTE_NAME) is not None
    ):
        return str(renewal_term[CONFIG_ELEM].get(ATTRIBUTE_NAME))
    return "No Auto Renewal"


def print_renewal_term(renewal_term):
    """
    Prints the fields of a renewal term.
    Args: renewal_term dict: A renewal term, or None
    """

    if renewal_term is None:
        print("No Auto Renewal")
        return

    print("Renewal Term ID: " + str(renewal_term.get("id")))

    if CONFIG_ELEM in renewal_term:
        print(
            "Auto Renew Enabled: "
            + str(renewal_term[CONFIG_ELEM].get(ATTRIBUTE_NAME))
        )

    # ISO 8601 duration. The customer can no longer change enableAutoRenew once the
    # agreement is within this duration of its end date. Absent when the offer sets no deadline,
    # which leaves the customer free to change enableAutoRenew up to the end date.
    if "lockoutPeriod" in renewal_term:
        print("Lockout Period: " + str(renewal_term["lockoutPeriod"]))
    else:
        print("Lockout Period: none")

    # Absent means the agreement can renew without limit.
    if "maxRenewals" in renewal_term:
        print("Max Renewals: " + str(renewal_term["maxRenewals"]))
    else:
        print("Max Renewals: unlimited")

    # Absent unless the offer sets a separate deadline for adjusting the renewal price.
    if "adjustmentDeadline" in renewal_term:
        print("Adjustment Deadline: " + str(renewal_term["adjustmentDeadline"]))

    print_price_increase(renewal_term.get("priceIncrease"))

    for term_template in renewal_term.get("termTemplates", []):
        print_term_template(term_template)


def print_price_increase(price_increase):
    """
    Prints the price change that applies when the agreement renews.
    Args: price_increase dict: The priceIncrease union from the renewal term
    """

    if price_increase is None:
        print("Price Increase: none (the price does not change at renewal)")
        return

    # priceIncrease is a union. Exactly one variant is set.
    if "fixedPercentage" in price_increase:
        print(
            "Fixed Price Increase Percentage: "
            + str(price_increase["fixedPercentage"].get("value"))
        )
    elif "percentageRange" in price_increase:
        # The uplift is open within this range; defaultValue applies if you take no action.
        percentage_range = price_increase["percentageRange"]
        print("Price Increase Min Percentage: " + str(percentage_range.get("minValue")))
        print("Price Increase Max Percentage: " + str(percentage_range.get("maxValue")))
        print(
            "Price Increase Default Percentage: "
            + str(percentage_range.get("defaultValue"))
        )


def print_term_template(term_template):
    """
    Prints the term template that applies when the agreement renews.
    Args: term_template dict: A termTemplates entry from the renewal term
    """

    # termTemplates entries are a union. Only payment schedule templates are supported today.
    if "paymentScheduleTermTemplate" not in term_template:
        print("Term Template: not a payment schedule template")
        return

    print("Payment Schedule Template:")
    for entry in term_template["paymentScheduleTermTemplate"].get("schedule", []):
        # chargeDateOffset is relative to the start of the renewed agreement, e.g. "P3M".
        line = (
            "  Charge Date Offset: "
            + str(entry.get("chargeDateOffset"))
            + ", Charge Percentage: "
            + str(entry.get("chargePercentage"))
        )

        # Absent unless the schedule pins charges to a day of the month.
        if "dayOfMonth" in entry:
            line += ", Day Of Month: " + str(entry["dayOfMonth"])

        print(line)


def print_end_time_behavior(entity_id):
    """
    Prints the agreement's end time behavior: whether it will renew, be replaced, or expire, and why.
    Args: entity_id str: Agreement to describe
    """

    try:
        agreement = mp_client.describe_agreement(agreementId=entity_id)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Agreement with ID %s not found.", entity_id)
        else:
            logger.error("Unexpected error: %s", e)
        return

    end_time_behavior = agreement.get("endTimeBehavior")
    if end_time_behavior is None:
        print("End Time Behavior: none (this agreement has no end date)")
        return

    print("End Time Behavior Type: " + str(end_time_behavior.get("type")))

    # The reason the agreement does not renew, and absent when it does. My own PROPOSER_RENEW_OPTED_OUT
    # leaves enableAutoRenew untouched, so the flag can read True even when this says it will not renew.
    if "reasonCode" in end_time_behavior:
        print("End Time Behavior Reason Code: " + str(end_time_behavior["reasonCode"]))

    # renewalSummary is present whenever type is RENEW, but offerId inside it is absent
    # until a renewal offer is created.
    offer_id = end_time_behavior.get("renewalSummary", {}).get("offerId")
    if offer_id:
        print("Renewal Offer ID: " + offer_id)


def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Looking for an agreement in the AWS Marketplace.")
    print("-" * 88)

    print_renewal_term(get_renewal_term(AGREEMENT_ID))

    # USE_SAMPLE_FILE only mocks the GetAgreementTerms response. endTimeBehavior comes from
    # DescribeAgreement, which has no sample file, so skip it when running from the sample.
    if not USE_SAMPLE_FILE:
        print_end_time_behavior(AGREEMENT_ID)


# open json file from path
def open_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [GetAgreementTerms](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementTerms) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.