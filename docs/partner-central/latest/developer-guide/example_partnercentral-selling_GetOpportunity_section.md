The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `GetOpportunity` with an AWS SDK

The following code examples show how to use `GetOpportunity`.

.NET

**SDK for .NET**

Get an opportunity.

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// PDX-License-Identifier: Apache-2.0

using System;
using Newtonsoft.Json;
using Amazon;
using Amazon.Runtime;
using Amazon.PartnerCentralSelling;
using Amazon.PartnerCentralSelling.Model;

namespace AWSExample
{
    class Program
    {
        static readonly string catalogToUse = "AWS";
        static readonly string identifier = "O1111111";
        static async Task Main(string[] args)
        {
            // Initialize credentials from .aws/credentials file
            var credentials = new Amazon.Runtime.CredentialManagement.SharedCredentialsFile();
            if (credentials.TryGetProfile("default", out var profile))
            {
                AWSCredentials awsCredentials = profile.GetAWSCredentials(credentials);

                var client = new AmazonPartnerCentralSellingClient(awsCredentials);

                var request = new GetOpportunityRequest
                {
                    Catalog = catalogToUse,
                    Identifier = identifier
                };

                try {
                    var response = await client.GetOpportunityAsync(request);
                    Console.WriteLine(response.HttpStatusCode);
                    string formattedJson = JsonConvert.SerializeObject(response, Formatting.Indented);
                    Console.WriteLine(formattedJson);
                } catch(ValidationException ex) {
                    Console.WriteLine("Validation error: " + ex.Message);
                } catch (AmazonPartnerCentralSellingException e) {
                    Console.WriteLine("Failed:");
                    Console.WriteLine(e.RequestId);
                    Console.WriteLine(e.ErrorCode);
                    Console.WriteLine(e.Message);
                }
            }
            else
            {
                Console.WriteLine("Profile not found.");
            }
        }
    }
}


```

- For API details, see
  [GetOpportunity](../../../goto/DotNetSDKV3/partnercentral-selling-2022-07-26/GetOpportunity.md "../../../goto/DotNetSDKV3/partnercentral-selling-2022-07-26/GetOpportunity.md")
  in _AWS SDK for .NET API Reference_.

Go

**SDK for Go V2**

Get an opportunity.

```

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/partnercentralselling"
)

func main() {
	config, err := config.LoadDefaultConfig(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	config.Region = "us-east-1"

	client := partnercentralselling.NewFromConfig(config)

	output, err := client.GetOpportunity(context.TODO(), &partnercentralselling.GetOpportunityInput{
		Identifier: aws.String("O1111111"),
		Catalog:    aws.String("AWS"),
	})

	if err != nil {
		log.Fatal(err)
	}
	log.Println("printing opportuniy...\n")

	jsonOutput, err := json.MarshalIndent(output, "", "    ")

	fmt.Println(string(jsonOutput))
}


```

- For API details, see
  [GetOpportunity](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.GetOpportunity "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.GetOpportunity")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

Get an opportunity.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityResponse;

/*
 * Purpose
 * PC-API-08 Get updated Opportunity
 */

public class GetOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	GetOpportunityResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	public static GetOpportunityResponse getResponse(String opportunityId) {

        GetOpportunityRequest getOpportunityRequest = GetOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.build();

        GetOpportunityResponse response = client.getOpportunity(getOpportunityRequest);

        return response;
	}
}


```

- For API details, see
  [GetOpportunity](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetOpportunity.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetOpportunity.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

Get an opportunity.

```

#!/usr/bin/env python

"""
Purpose
PC-API -08 Get updated Opportunity given opportunity id
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
	    "Identifier": identifier
    }
    try:
        # Perform an API call
        response = partner_central_client.get_opportunity(**get_opportunity_request)
        return response

    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    identifier = "O5465588"

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Get updated Opportunity.")
    print("-" * 88)

    helper.pretty_print_datetime(get_opportunity(identifier))

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [GetOpportunity](../../../goto/boto3/partnercentral-selling-2022-07-26/GetOpportunity.md "../../../goto/boto3/partnercentral-selling-2022-07-26/GetOpportunity.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
