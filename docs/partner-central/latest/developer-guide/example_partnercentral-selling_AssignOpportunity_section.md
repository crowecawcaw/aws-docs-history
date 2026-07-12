The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `AssignOpportunity` with an AWS SDK

The following code examples show how to use `AssignOpportunity`.

Java

**SDK for Java 2.x**

Reassign an existing Opportunity to another user.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AssignOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.AssignOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.AssigneeContact;

/*
Purpose
PC-API-07 Assigning a new owner
*/

public class AssignOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String assigneeFirstName = "John";

    	String assigneeLastName = "Doe";

    	String assigneeEmail = "test@test.com";

    	String businessTitle = "PartnerAccountManager";

    	AssignOpportunityResponse response = getResponse(opportunityId, assigneeFirstName, assigneeLastName, assigneeEmail, businessTitle);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static AssignOpportunityResponse getResponse(String opportunityId, String assigneeFirstName, String assigneeLastName, String assigneeEmail, String businessTitle) {

		AssignOpportunityRequest assignOpportunityRequest = AssignOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.assignee(AssigneeContact.builder()
        				.firstName(assigneeFirstName)
        				.lastName(assigneeLastName)
        				.email(assigneeEmail)
        				.businessTitle(businessTitle)
        				.build())
        		.build();

        AssignOpportunityResponse response = client.assignOpportunity(assignOpportunityRequest);

        return response;
	}
}


```

- For API details, see
  [AssignOpportunity](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssignOpportunity.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssignOpportunity.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

Reassign an existing Opportunity to another user.

```

#!/usr/bin/env python

"""
Purpose
PC-API-07 Assigning a new owner
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

def assign_opportunity(identifier):
    assign_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier,
        "Assignee": {
            "BusinessTitle": "OpportunityOwner",
            "Email": "test@test.com",
            "FirstName": "John",
            "LastName": "Doe"
        }
    }
    try:
        # Perform an API call
        response = partner_central_client.assign_opportunity(**assign_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O4236468"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Assigning a new owner to an opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(assign_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [AssignOpportunity](../../../goto/boto3/partnercentral-selling-2022-07-26/AssignOpportunity.md "../../../goto/boto3/partnercentral-selling-2022-07-26/AssignOpportunity.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
