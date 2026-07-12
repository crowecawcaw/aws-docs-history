The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `RejectEngagementInvitation` with an AWS SDK

The following code examples show how to use `RejectEngagementInvitation`.

Java

**SDK for Java 2.x**

Rejects an EngagementInvitation that AWS shared.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.RejectEngagementInvitationRequest;
import software.amazon.awssdk.services.partnercentralselling.model.RejectEngagementInvitationResponse;

/*
 * Purpose
 * PC-API-05 AWS Originated(AO) rejection
 */

public class RejectEngagementInvitation {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

		RejectEngagementInvitationResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static RejectEngagementInvitationResponse getResponse(String invitationId) {

        RejectEngagementInvitationRequest rejectOpportunityRequest = RejectEngagementInvitationRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(invitationId)
        		.rejectionReason("Unable to support")
        		.build();

		RejectEngagementInvitationResponse response = client.rejectEngagementInvitation(rejectOpportunityRequest);

        return response;
	}
}


```

- For API details, see
  [RejectEngagementInvitation](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/RejectEngagementInvitation.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/RejectEngagementInvitation.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

Rejects an EngagementInvitation that AWS shared.

```

#!/usr/bin/env python

"""
Purpose
PC-API-05 AWS Originated AO rejection - RejectOpportunityEngagementInvitation - Rejects a engagement invitation.
This action indicates that the partner does not wish to participate in the engagement and
provides a reason for the rejection.
Upon rejection, a OpportunityEngagementInvitationRejected event is triggered.
Subsequently, the invitation will no longer be available for the partner to act on.
"""
import json
import logging
import boto3
import utils.helpers as helper

from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
)

def reject_opportunity_engagement_invitation(identifier, reject_reason):
    reject_opportunity_engagement_invitation_request ={
        "Catalog": CATALOG_TO_USE,
	    "Identifier": identifier,
        "RejectionReason": reject_reason
    }
    try:
        # Perform an API call
        response = partner_central_client.reject_engagement_invitation(**reject_opportunity_engagement_invitation_request)
        return response

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    identifier = "arn:aws:partnercentral:us-east-1::catalog/Sandbox/engagement-invitation/engi-0000002isviga"
    reject_reason = "Customer problem unclear"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Given the ARN identifier and reject reason, reject the Opportunity Engagement Invitation.")
    print("-" * 88)

    helper.pretty_print_datetime(reject_opportunity_engagement_invitation(identifier, reject_reason))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [RejectEngagementInvitation](../../../goto/boto3/partnercentral-selling-2022-07-26/RejectEngagementInvitation.md "../../../goto/boto3/partnercentral-selling-2022-07-26/RejectEngagementInvitation.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
