The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `StartEngagementFromOpportunityTask` with an AWS SDK

The following code examples show how to use `StartEngagementFromOpportunityTask`.

Java

**SDK for Java 2.x**

Initiates the engagement process from an existing opportunity by accepting the engagement invitation and creating a corresponding opportunity in the partner’s system.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AwsSubmission;
import software.amazon.awssdk.services.partnercentralselling.model.SalesInvolvementType;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementFromOpportunityTaskRequest;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementFromOpportunityTaskResponse;
import software.amazon.awssdk.services.partnercentralselling.model.Visibility;

/*
 * Purpose
 * PC-API-01 Partner Originated (PO) opp submission(Start Engagement From Opportunity Task for AO Originated Opportunity)
 */

public class StartEngagementFromOpportunityTask {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	StartEngagementFromOpportunityTaskResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static StartEngagementFromOpportunityTaskResponse getResponse(String opportunityId) {

		StartEngagementFromOpportunityTaskRequest submitOpportunityRequest = StartEngagementFromOpportunityTaskRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.clientToken("test-annjqwesdsd99")
        		.awsSubmission(AwsSubmission.builder().involvementType(SalesInvolvementType.CO_SELL).visibility(Visibility.FULL).build())
        		.build();

		StartEngagementFromOpportunityTaskResponse response = client.startEngagementFromOpportunityTask(submitOpportunityRequest);

        return response;
	}
}


```

- For API details, see
  [StartEngagementFromOpportunityTask](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

Initiates the engagement process from an existing opportunity by accepting the engagement invitation and creating a corresponding opportunity in the partner’s system.

```

#!/usr/bin/env python

"""
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
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

def start_engagement_from_opportunity_task(identifier):

    start_engagement_from_opportunity_task_request ={
            "AwsSubmission": {
                "InvolvementType": "Co-Sell",
                "Visibility": "Full"
            },
            "Catalog": CATALOG_TO_USE,
	        "Identifier" : identifier,
            "ClientToken": "test-annjqwesdsd99"
    }
    try:
            # Perform an API call
            response = partner_central_client.start_engagement_from_opportunity_task(**start_engagement_from_opportunity_task_request)
            return response

    except ClientError as err:
            # Catch all client exceptions
            print(err.response)
            return None

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Start Engagement from Opportunity Task.")
    print("-" * 88)

    helper.pretty_print_datetime(start_engagement_from_opportunity_task(identifier))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [StartEngagementFromOpportunityTask](../../../goto/boto3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask.md "../../../goto/boto3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
