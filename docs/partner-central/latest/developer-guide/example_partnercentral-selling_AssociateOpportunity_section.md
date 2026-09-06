

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Use `AssociateOpportunity` with an AWS SDK
<a name="example_partnercentral-selling_AssociateOpportunity_section"></a>

The following code examples show how to use `AssociateOpportunity`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Update associated entity of an opportunity](example_partnercentral-selling__UpdateAssociatedEntity_section.md) 

------
#### [ Java ]

**SDK for Java 2.x**  
Create a formal association between an Opportunity and various related entities.  

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityResponse;

/*
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
entity_type = Solutions | AWSProducts | AWSMarketplaceOffers 
*/

public class AssociateOpportunity {
	
	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {
    	
    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;
    	    	
    	String entityType = "Solutions";
    	
    	String entityIdentifier = "S-0000000";
    	
    	AssociateOpportunityResponse response = getResponse(opportunityId, entityType, entityIdentifier );
    	
    	ReferenceCodesUtils.formatOutput(response);
    }

static AssociateOpportunityResponse getResponse(String opportunityId, String entityType, String entityIdentifier) {
		
        AssociateOpportunityRequest associateOpportunityRequest = AssociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();
        
        AssociateOpportunityResponse response = client.associateOpportunity(associateOpportunityRequest);
        
        return response;
	}
}
```
+  For API details, see [AssociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Create a formal association between an Opportunity and various related entities.  

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

def associate_opportunity(entity_type, entity_identifier, opportunityIdentifier):
    associate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier, 
        "RelatedEntityType" : entity_type, 
        "RelatedEntityIdentifier" : entity_identifier 
    }
    try:
        # Perform an API call
        response = partner_central_client.associate_opportunity(**associate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    #entity_type = Solutions | AWSProducts | AWSMarketplaceOffers 
    entity_type = "Solutions"
    entity_identifier = "S-0059717"
    opportunityIdentifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Associate Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(associate_opportunity(entity_type, entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [AssociateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.