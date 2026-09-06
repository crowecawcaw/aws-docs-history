

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Use `ListEngagementInvitations` with an AWS SDK
<a name="example_partnercentral-selling_ListEngagementInvitations_section"></a>

The following code examples show how to use `ListEngagementInvitations`.

------
#### [ Java ]

**SDK for Java 2.x**  
Retrieves a list of engagement invitations sent to the partner.  

```
package org.example;

import java.util.ArrayList;
import java.util.List;

import org.example.utils.ReferenceCodesUtils;
import static org.example.utils.Constants.*;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.ListEngagementInvitationsRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListEngagementInvitationsResponse;
import software.amazon.awssdk.services.partnercentralselling.model.ParticipantType;
import software.amazon.awssdk.services.partnercentralselling.model.EngagementInvitationSummary;

public class ListEngagementInvitations {
	
	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();
	
    public static void main(String[] args) {
    	
    	List<EngagementInvitationSummary> opportunitySummaries = getResponse();
        ReferenceCodesUtils.formatOutput(opportunitySummaries);
    }
    
    static List<EngagementInvitationSummary> getResponse() {
		
		List<EngagementInvitationSummary> opportunitySummaries = new ArrayList<EngagementInvitationSummary>();
		
		ListEngagementInvitationsRequest listOpportunityRequest = ListEngagementInvitationsRequest.builder()
                .catalog(CATALOG_TO_USE)
                .participantType(ParticipantType.RECEIVER)
        		.maxResults(5)
        		.build();
        
		ListEngagementInvitationsResponse response = client.listEngagementInvitations(listOpportunityRequest);
    	
    	opportunitySummaries.addAll(response.engagementInvitationSummaries());
    	
    	client.close();
    	
        return opportunitySummaries;
	}
}
```
+  For API details, see [ListEngagementInvitations](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementInvitations) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Retrieves a list of engagement invitations sent to the partner.  

```
#!/usr/bin/env python

"""
Purpose
PC-API-21 ListEngagementInvitations - Retrieves a list of engagement invitations based on specified criteria. 
This operation allows partners to view all invitations to engagement.
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

def list_engagement_invitations():
    list_engagement_invitations_request ={
        "Catalog": CATALOG_TO_USE,
        "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_engagement_invitations(**list_engagement_invitations_request)
        return response

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Retrieve list of Engagement Invitations.")
    print("-" * 88)

    helper.pretty_print_datetime(list_engagement_invitations())

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [ListEngagementInvitations](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementInvitations) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.