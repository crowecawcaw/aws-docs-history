

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Use `DisassociateOpportunity` with an AWS SDK
<a name="example_partnercentral-selling_DisassociateOpportunity_section"></a>

The following code examples show how to use `DisassociateOpportunity`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Update associated entity of an opportunity](example_partnercentral-selling__UpdateAssociatedEntity_section.md) 

------
#### [ Java ]

**SDK for Java 2.x**  
Remove an existing association between an Opportunity and related entities.  

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityResponse;

/*
Purpose
PC-API -14 Removing a Solution
PC-API -15 Removing an offer
PC-API -16 Removing a product
entity_type = Solutions | AWSProducts | AWSMarketplaceOffers 
*/

public class DisassociateOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();
	
    public static void main(String[] args) {
    	
    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;
    	
    	String entityType = "Solutions";
    	
    	String entityIdentifier = "S-0000000";
    	
    	DisassociateOpportunityResponse response = getResponse(opportunityId, entityType, entityIdentifier );
    	
    	ReferenceCodesUtils.formatOutput(response);
    }

	static DisassociateOpportunityResponse getResponse(String opportunityId, String entityType, String entityIdentifier) {
		
		DisassociateOpportunityRequest disassociateOpportunityRequest = DisassociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();
        
        DisassociateOpportunityResponse response = client.disassociateOpportunity(disassociateOpportunityRequest);
        
        return response;
	}
}
```
+  For API details, see [DisassociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Remove an existing association between an Opportunity and related entities.  

```
#!/usr/bin/env python

"""
Purpose
PC-API -14 Removing a Solution
PC-API -15 Removing an offer
PC-API -16 Removing a product
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

def disassociate_opportunity(entity_type, entity_identifier, opportunityIdentifier):
    disassociate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier, 
        "RelatedEntityType" : entity_type, 
        "RelatedEntityIdentifier" : entity_identifier 
    }
    try:
        # Perform an API call
        response = partner_central_client.disassociate_opportunity(**disassociate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    #entity_type = Solutions | AWSProducts | AWSMarketplaceOffers 
    entity_type = "Solutions"
    entity_identifier = "S-0049999"
    opportunityIdentifier = "O4397574"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get updated Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(disassociate_opportunity(entity_type, entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [DisassociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.