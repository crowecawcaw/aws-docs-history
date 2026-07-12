The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Use `ListOpportunities` with an AWS SDK

The following code examples show how to use `ListOpportunities`.

.NET

**SDK for .NET**

List opportunities.

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
        static readonly string catalogToUse = "Sandbox";
        static async Task Main(string[] args)
        {
            // Initialize credentials from .aws/credentials file
            var credentials = new Amazon.Runtime.CredentialManagement.SharedCredentialsFile();
            if (credentials.TryGetProfile("default", out var profile))
            {
                AWSCredentials awsCredentials = profile.GetAWSCredentials(credentials);

                //var config = new AmazonPartnerCentralSellingConfig()
                //{
                //    ServiceURL = "https://partnercentral-selling.us-east-1.api.aws",
                //};
                //var client = new AmazonPartnerCentralSellingClient(awsCredentials, config);
                var client = new AmazonPartnerCentralSellingClient(awsCredentials);
                var request = new ListOpportunitiesRequest
                {
                    Catalog = catalogToUse,
                    MaxResults = 2
                };

                try {
                    var response = await client.ListOpportunitiesAsync(request);
                    Console.WriteLine(response.HttpStatusCode);
                    foreach (var opportunity in response.OpportunitySummaries)
                    {
                        Console.WriteLine("Opportunity id: " + opportunity.Id);
                    }
                    string formattedJson = JsonConvert.SerializeObject(response.OpportunitySummaries, Formatting.Indented);
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
  [ListOpportunities](../../../goto/DotNetSDKV3/partnercentral-selling-2022-07-26/ListOpportunities.md "../../../goto/DotNetSDKV3/partnercentral-selling-2022-07-26/ListOpportunities.md")
  in _AWS SDK for .NET API Reference_.

Go

**SDK for Go V2**

List opportunities.

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

	output, err := client.ListOpportunities(context.TODO(), &partnercentralselling.ListOpportunitiesInput{
		MaxResults: aws.Int32(2),
		Catalog:    aws.String("AWS"),
	})

	if err != nil {
		log.Fatal(err)
	}

	jsonOutput, err := json.MarshalIndent(output, "", "    ")
	fmt.Println(string(jsonOutput))
}


```

- For API details, see
  [ListOpportunities](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.ListOpportunities "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.ListOpportunities")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

List opportunities.

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
import software.amazon.awssdk.services.partnercentralselling.model.ListOpportunitiesRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListOpportunitiesResponse;
import software.amazon.awssdk.services.partnercentralselling.model.OpportunitySummary;

/*
 * Purpose
 * PC-API-18 Getting list of Opportunities
 */

public class ListOpportunititesPaging {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {
    	List<OpportunitySummary> opportunitySummaries = getResponse();
        ReferenceCodesUtils.formatOutput(opportunitySummaries);
    }

    private static List<OpportunitySummary> getResponse() {
    	List<OpportunitySummary> opportunitySummaries = new ArrayList<OpportunitySummary>();

		ListOpportunitiesRequest listOpportunityRequest = ListOpportunitiesRequest.builder()
                .catalog(CATALOG_TO_USE)
        		.maxResults(5)
        		.build();

    	ListOpportunitiesResponse response = client.listOpportunities(listOpportunityRequest);

    	opportunitySummaries.addAll(response.opportunitySummaries());

    	while (response.nextToken() != null && response.nextToken().length() > 0) {
    		listOpportunityRequest = ListOpportunitiesRequest.builder()
                    .catalog(CATALOG_TO_USE)
            		.maxResults(5)
            		.nextToken(response.nextToken())
            		.build();
    		response = client.listOpportunities(listOpportunityRequest);
    		opportunitySummaries.addAll(response.opportunitySummaries());
    	}

    	client.close();

        return opportunitySummaries;
	}
}


```

- For API details, see
  [ListOpportunities](../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunities.md "../../../goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunities.md")
  in _AWS SDK for Java 2.x API Reference_.

Python

**SDK for Python (Boto3)**

List opportunities.

```

#!/usr/bin/env python

"""
Purpose
PC-API -18 Getting list of Opportunities
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

def get_list_of_opportunities():

    opportunity_list = []

    list_opportunities_request ={
        "Catalog": CATALOG_TO_USE,
	    "MaxResults": 20
    }
    try:
        # Perform an API call
        response = partner_central_client.list_opportunities(**list_opportunities_request)
        opportunity_list.extend(response["OpportunitySummaries"])

        while "NextToken" in response and response["NextToken"] is not None:
            list_opportunities_request["NextToken"] = response["NextToken"]
            response = partner_central_client.list_opportunities(**list_opportunities_request)
            opportunity_list.extend(response["OpportunitySummaries"])

        return opportunity_list

    except Exception as err:
        # Catch all client exceptions
        print(json.dumps(err.response))

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Getting list of Opportunities.")
    print("-" * 88)

    helper.pretty_print_datetime(get_list_of_opportunities())

if __name__ == "__main__":
    usage_demo()


```

- For API details, see
  [ListOpportunities](../../../goto/boto3/partnercentral-selling-2022-07-26/ListOpportunities.md "../../../goto/boto3/partnercentral-selling-2022-07-26/ListOpportunities.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
