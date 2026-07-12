The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Update associated entity of an opportunity

The following code examples show how to:

- Disassociate an old entity.
- Associate a new entity.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[Scenarios](https://github.com/aws-samples/partner-crm-integration-samples/tree/main/partner-central-api-sample-codes/java_preview "https://github.com/aws-samples/partner-crm-integration-samples/tree/main/partner-central-api-sample-codes/java_preview")
repository.

Update associated entity of an opportunity

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
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityResponse;

/*
Purpose
PC-API -17 Replacing a solution
*/

public class ReplaceSolution {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String entityType = "Solutions";
    	String originalEntityIdentifier = "S-0000000";
    	String newEntityIdentifier = "S-0011111";

    	disassociateOppornitityResponse(opportunityId, entityType, originalEntityIdentifier );
    	AssociateOpportunityResponse associateOpportunityResponse = associateOpportunityResponse(opportunityId, entityType, newEntityIdentifier );

    	ReferenceCodesUtils.formatOutput(associateOpportunityResponse);
    }

	private static AssociateOpportunityResponse associateOpportunityResponse(String opportunityId, String entityType, String entityIdentifier) {

        AssociateOpportunityRequest associateOpportunityRequest = AssociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();

        AssociateOpportunityResponse response = client.associateOpportunity(associateOpportunityRequest);

        return response;
	}

	private static DisassociateOpportunityResponse disassociateOppornitityResponse(String opportunityId, String entityType, String entityIdentifier) {
		PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

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

- For API details, see the following topics in _AWS SDK for Java 2.x API Reference_.

  - [AssociateOpportunity](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity.md")
  - [DisassociateOpportunity](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity.md")

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/partner-central-api-sample-codes/python_preview/#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/partner-central-api-sample-codes/python_preview/#code-examples").

Update Associated Entity of an opportunity

```

#!/usr/bin/env python

"""
Purpose
PC-API -17 Replacing a solution
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

def replace_solution(original_entity_identifier, new_entity_identifier, opportunityIdentifier):
    disassociate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : "Solutions",
        "RelatedEntityIdentifier" : original_entity_identifier
    }

    associate_opportunity_request ={
        "Catalog": CATALOG_TO_USE,
	    "OpportunityIdentifier" : opportunityIdentifier,
        "RelatedEntityType" : "Solutions",
        "RelatedEntityIdentifier" : new_entity_identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.disassociate_opportunity(**disassociate_opportunity_request)
        response = partner_central_client.associate_opportunity(**associate_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    original_entity_identifier = "S-0049999"
    new_entity_identifier = "S-0050014"
    opportunityIdentifier = "O4397574"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Replacing a solution.")
    print("-" * 88)

    helper.pretty_print_datetime(replace_solution(original_entity_identifier, new_entity_identifier, opportunityIdentifier))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see the following topics in _AWS SDK for Python (Boto3) API Reference_.

  - [AssociateOpportunity](../../../goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity.md "../../../goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity.md")
  - [DisassociateOpportunity](../../../goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity.md "../../../goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity.md")

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
