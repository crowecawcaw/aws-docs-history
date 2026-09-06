

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Use `ListSolutions` with an AWS SDK
<a name="example_partnercentral-selling_ListSolutions_section"></a>

The following code examples show how to use `ListSolutions`.

------
#### [ Java ]

**SDK for Java 2.x**  
Retrieves a list of Partner Solutions that the partner registered on Partner Central.  

```
package org.example;

import java.util.ArrayList;
import java.util.List;

import static org.example.utils.Constants.*;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.ListSolutionsRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListSolutionsResponse;
import software.amazon.awssdk.services.partnercentralselling.model.SolutionBase;

/*
 * Purpose
 * PC-API-10 Getting list of solutions
 */

public class ListSolutions {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();
	
    public static void main(String[] args) {
    	List<SolutionBase> solutionSummaries = getResponse();
        ReferenceCodesUtils.formatOutput(solutionSummaries);
    }
    
    static List<SolutionBase> getResponse() {
		List<SolutionBase> solutionSummaries = new ArrayList<SolutionBase>();

		ListSolutionsRequest listSolutionsRequest = ListSolutionsRequest.builder()
				.catalog(CATALOG_TO_USE)
        		.maxResults(5)
        		.build();
        
    	ListSolutionsResponse response = client.listSolutions(listSolutionsRequest);
        
    	solutionSummaries.addAll(response.solutionSummaries());
    	
        return solutionSummaries;
	}
}
```
+  For API details, see [ListSolutions](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListSolutions) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Retrieves a list of Partner Solutions that the partner registered on Partner Central.  

```
#!/usr/bin/env python

"""
Purpose
PC-API-10 Getting list of solutions
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

def get_list_of_solutions():
    list_solutions_request ={
        "Catalog": CATALOG_TO_USE,
	    "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_solutions(**list_solutions_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Getting list of solutions.")
    print("-" * 88)

    helper.pretty_print_datetime(get_list_of_solutions())

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [ListSolutions](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListSolutions) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.