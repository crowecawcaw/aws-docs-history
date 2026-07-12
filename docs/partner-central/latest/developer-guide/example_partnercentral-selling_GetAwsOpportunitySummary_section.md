The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `GetAwsOpportunitySummary` with an AWS SDK

The following code examples show how to use `GetAwsOpportunitySummary`.

Java

**SDK for Java 2.x**

Retrieves a summary of an AWS Opportunity.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.GetAwsOpportunitySummaryRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetAwsOpportunitySummaryResponse;

/*
 * Purpose
 * PC-API-25 Retrieves a summary of an AWS Opportunity.
 */

public class GetAwsOpportunitySummary {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	GetAwsOpportunitySummaryResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	public static GetAwsOpportunitySummaryResponse getResponse(String opportunityId) {

		GetAwsOpportunitySummaryRequest getOpportunityRequest = GetAwsOpportunitySummaryRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.relatedOpportunityIdentifier(opportunityId)
        		.build();

		GetAwsOpportunitySummaryResponse response = client.getAwsOpportunitySummary(getOpportunityRequest);

        return response;
	}
}


```

- For API details, see
  [GetAwsOpportunitySummary](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

Retrieves a summary of an AWS Opportunity.

```

#!/usr/bin/env python

"""
Purpose
PC-API-25 Retrieves a summary of an AWS Opportunity. LifeCycle.ReviewStatus=Approved
"""
import logging
import boto3
import utils.helpers as helper
from botocore.client import ClientError

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def get_opportunity(identifier):
    get_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "RelatedOpportunityIdentifier": identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.get_aws_opportunity_summary(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get AWS Opportunity summary.")
    print("-" * 88)

    helper.pretty_print_datetime(get_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [GetAwsOpportunitySummary](../../../goto/boto3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary.md "../../../goto/boto3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
