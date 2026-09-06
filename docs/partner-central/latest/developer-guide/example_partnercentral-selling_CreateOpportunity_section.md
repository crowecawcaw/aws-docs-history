

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Use `CreateOpportunity` with an AWS SDK
<a name="example_partnercentral-selling_CreateOpportunity_section"></a>

The following code examples show how to use `CreateOpportunity`.

------
#### [ .NET ]

**SDK for .NET**  
Create an opportunity.  

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
        static async Task Main(string[] args)
        {
            // Initialize credentials from .aws/credentials file
            var credentials = new Amazon.Runtime.CredentialManagement.SharedCredentialsFile();
            if (credentials.TryGetProfile("default", out var profile))
            {
                AWSCredentials awsCredentials = profile.GetAWSCredentials(credentials);

                var client = new AmazonPartnerCentralSellingClient(awsCredentials);

                var request = new CreateOpportunityRequest
                {
                    Catalog = catalogToUse,
                    Origin = "Partner Referral",
                    Customer = new Customer
                    {
                        Account = new Account
                        {
                            Address = new Address
                            {
                                CountryCode = "US",
                                PostalCode = "99502",
                                StateOrRegion = "Alaska"
                            },
                            CompanyName = "TestCompanyName",
                            Duns = "123456789",
                            WebsiteUrl = "www.test.io",
                            Industry = "Automotive"
                        },
                        Contacts = new List<Contact>
                        {
                            new Contact
                            {
                                Email = "test@test.io",
                                FirstName = "John  ",
                                LastName = "Doe",
                                Phone = "+14444444444",
                                BusinessTitle = "test title"
                            }
                        }
                    },
                    LifeCycle = new LifeCycle
                    {
                        ReviewStatus = "Submitted",
                        TargetCloseDate = "2024-12-30"
                    },
                    Marketing = new Marketing
                    {
                        Source = "None"
                    },
                    OpportunityType = "Net New Business",
                    PrimaryNeedsFromAws = new List<string> { "Co-Sell - Architectural Validation" },
                    Project = new Project
                    {
                        Title = "Moin Test UUID",
                        CustomerBusinessProblem = "Sandbox is not working as expected",
                        CustomerUseCase = "AI Machine Learning and Analytics",
                        DeliveryModels = new List<string> { "SaaS or PaaS" },
                        ExpectedCustomerSpend = new List<ExpectedCustomerSpend>
                        {
                            new ExpectedCustomerSpend
                            {
                                Amount = "2000.0",
                                CurrencyCode = "USD",
                                Frequency = "Monthly",
                                TargetCompany = "Ibexlabs"
                            }
                        },
                        SalesActivities = new List<string> { "Initialized discussions with customer" }
                    }
                };

                try
                {
                    var response = await client.CreateOpportunityAsync(request);
                    Console.WriteLine(response.HttpStatusCode);
                    string formattedJson = JsonConvert.SerializeObject(response, Formatting.Indented);
                    Console.WriteLine(formattedJson);
                }
                catch (ValidationException ex)
                {
                    Console.WriteLine("Validation error: " + ex.Message);
                }
                catch (AmazonPartnerCentralSellingException e)
                {
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
+  For API details, see [CreateOpportunity](https://docs.aws.amazon.com/goto/DotNetSDKV3/partnercentral-selling-2022-07-26/CreateOpportunity) in *AWS SDK for .NET API Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
Create an opportunity.  

```
package org.example;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

import static org.example.utils.Constants.*;

import org.example.entity.Root;
import org.example.utils.ReferenceCodesUtils;
import org.example.utils.StringSerializer;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.Account;
import software.amazon.awssdk.services.partnercentralselling.model.Address;
import software.amazon.awssdk.services.partnercentralselling.model.Contact;
import software.amazon.awssdk.services.partnercentralselling.model.CreateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.CreateOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.Customer;
import software.amazon.awssdk.services.partnercentralselling.model.ExpectedCustomerSpend;
import software.amazon.awssdk.services.partnercentralselling.model.LifeCycle;
import software.amazon.awssdk.services.partnercentralselling.model.Marketing;
import software.amazon.awssdk.services.partnercentralselling.model.MonetaryValue;
import software.amazon.awssdk.services.partnercentralselling.model.NextStepsHistory;
import software.amazon.awssdk.services.partnercentralselling.model.Project;
import software.amazon.awssdk.services.partnercentralselling.model.SoftwareRevenue;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.ToNumberPolicy;

public class CreateOpportunity {
	
	static final Gson GSON = new GsonBuilder()
			.setObjectToNumberStrategy(ToNumberPolicy.LAZILY_PARSED_NUMBER)
			.registerTypeAdapter(String.class, new StringSerializer())
			.create();
	
	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

	public static void main(String[] args) {

		String inputFile = "CreateOpportunity2.json";
		
		if (args.length > 0)
			inputFile = args[0];
		
		CreateOpportunityResponse response = createOpportunity(inputFile);
		
		client.close();
	}
	
	static CreateOpportunityResponse createOpportunity(String inputFile) {
		
		String inputString = ReferenceCodesUtils.readInputFileToString(inputFile);
		
		Root root = GSON.fromJson(inputString, Root.class);
				
		List<NextStepsHistory> nextStepsHistories = new ArrayList<NextStepsHistory>();
		if ( root.lifeCycle != null && root.lifeCycle.nextStepsHistories != null) {		
			for (org.example.entity.NextStepsHistory nextStepsHistoryJson : root.lifeCycle.nextStepsHistories) {
				NextStepsHistory nextStepsHistory = NextStepsHistory.builder()
						.time(Instant.parse(nextStepsHistoryJson.time))
						.value(nextStepsHistoryJson.value)
		                .build();
				nextStepsHistories.add(nextStepsHistory);
			}
		}
		
		LifeCycle lifeCycle = null;
		if ( root.lifeCycle != null ) {
			lifeCycle = LifeCycle.builder()
				.closedLostReason(root.lifeCycle.closedLostReason)
				.nextSteps(root.lifeCycle.nextSteps)
				.nextStepsHistory(nextStepsHistories)
				.reviewComments(root.lifeCycle.reviewComments)
				.reviewStatus(root.lifeCycle.reviewStatus)
				.reviewStatusReason(root.lifeCycle.reviewStatusReason)
				.stage(root.lifeCycle.stage)
				.targetCloseDate(root.lifeCycle.targetCloseDate)
				.build();
		}
		
		Marketing marketing = null;
		if ( root.marketing != null ) {
			marketing = Marketing.builder()
					.awsFundingUsed(root.marketing.awsFundingUsed)
					.campaignName(root.marketing.campaignName)
					.channels(root.marketing.channels)
					.source(root.marketing.source)
					.useCases(root.marketing.useCases)
					.build();
					
		}
		
		Address address = null;
		if ( root.customer != null && root.customer.account != null && root.customer.account.address != null ) {
			address = Address.builder()
				.city(root.customer.account.address.city)
                .postalCode(root.customer.account.address.postalCode)
                .stateOrRegion(root.customer.account.address.stateOrRegion)
                .countryCode(root.customer.account.address.countryCode)
                .streetAddress(root.customer.account.address.streetAddress)
                .build();
		}
		
		Account account = null;
		if ( root.customer != null && root.customer.account!= null) {
			account = Account.builder()
	            .address(address)
	            .awsAccountId(root.customer.account.awsAccountId)
                .duns(root.customer.account.duns)
                .industry(root.customer.account.industry)
                .otherIndustry(root.customer.account.otherIndustry)
                .companyName(root.customer.account.companyName)
                .websiteUrl(root.customer.account.websiteUrl)
                .build();
		}
		
		List<Contact> contacts = new ArrayList<Contact>();
		if ( root.customer != null && root.customer.contacts != null) {		
			for (org.example.entity.Contact jsonContact : root.customer.contacts) {
				Contact contact = Contact.builder()
		                .email(jsonContact.email)
		                .firstName(jsonContact.firstName)
		                .lastName(jsonContact.lastName)
		                .phone(jsonContact.phone)
		                .businessTitle(jsonContact.businessTitle)
		                .build();
				contacts.add(contact);
			}
		}

		Customer customer = Customer.builder()
				.account(account)
				.contacts(contacts)
				.build();
		
		Contact oportunityTeamContact = null;
		if (root.opportunityTeam != null && root.opportunityTeam.get(0) != null ) {
			oportunityTeamContact = Contact.builder()
                .firstName(root.opportunityTeam.get(0).firstName)
                .lastName(root.opportunityTeam.get(0).lastName)
                .email(root.opportunityTeam.get(0).email)
                .phone(root.opportunityTeam.get(0).phone)
                .businessTitle(root.opportunityTeam.get(0).businessTitle)
                .build();
		}
		
		List<ExpectedCustomerSpend> expectedCustomerSpends = new ArrayList<ExpectedCustomerSpend>();
		if ( root.project != null && root.project.expectedCustomerSpend != null) {
			for (org.example.entity.ExpectedCustomerSpend expectedCustomerSpendJson : root.project.expectedCustomerSpend) {
				ExpectedCustomerSpend expectedCustomerSpend = null;
				expectedCustomerSpend = ExpectedCustomerSpend.builder()
						.amount(expectedCustomerSpendJson.amount)
						.currencyCode(expectedCustomerSpendJson.currencyCode)
						.frequency(expectedCustomerSpendJson.frequency)
						.targetCompany(expectedCustomerSpendJson.targetCompany)
						.build();
				expectedCustomerSpends.add(expectedCustomerSpend);
			}
        }
        
        Project project = null;
        if ( root.project != null) {
        	project = Project.builder()
                .title(root.project.title)
                .customerBusinessProblem(root.project.customerBusinessProblem)
                .customerUseCase(root.project.customerUseCase)
                .deliveryModels(root.project.deliveryModels)
                .expectedCustomerSpend(expectedCustomerSpends)
                .salesActivities(root.project.salesActivities)
                .competitorName(root.project.competitorName)
                .otherSolutionDescription(root.project.otherSolutionDescription)
                .build();
        }
        
        SoftwareRevenue softwareRevenue = null;
        if ( root.softwareRevenue != null) {
        	MonetaryValue monetaryValue = null;
        	if ( root.softwareRevenue.value != null) {
        		monetaryValue = MonetaryValue.builder()
        				.amount(root.softwareRevenue.value.amount)
        				.currencyCode(root.softwareRevenue.value.currencyCode)
        				.build();
        	}
        	softwareRevenue = SoftwareRevenue.builder()
        			.deliveryModel(root.softwareRevenue.deliveryModel)
        			.effectiveDate(root.softwareRevenue.effectiveDate)
        			.expirationDate(root.softwareRevenue.expirationDate)
        			.value(monetaryValue)
        			.build();
        }
		
		// Building the Actual CreateOpportunity Request
		CreateOpportunityRequest createOpportunityRequest = CreateOpportunityRequest.builder()
				.catalog(CATALOG_TO_USE)
				.clientToken(root.clientToken)
				.primaryNeedsFromAwsWithStrings(root.primaryNeedsFromAws)
				.opportunityType(root.opportunityType)
				.lifeCycle(lifeCycle)
				.marketing(marketing)
				.nationalSecurity(root.nationalSecurity)
				.origin(root.origin)
				.customer(customer)
				.project(project)
				.partnerOpportunityIdentifier(root.partnerOpportunityIdentifier)
				.opportunityTeam(oportunityTeamContact)
				.softwareRevenue(softwareRevenue)
				.build();
		
		CreateOpportunityResponse response = client.createOpportunity(createOpportunityRequest);
		System.out.println("Successfully created: " + response);

		return response;
    }

}
```
+  For API details, see [CreateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateOpportunity) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Create an opportunity.  

```
#!/usr/bin/env python
import boto3
import logging
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.helpers as helper
import utils.stringify_details as sd
from botocore.client import ClientError
from utils.constants import CATALOG_TO_USE

serviceName = "partnercentral-selling"

def create_opportunity(partner_central_client):
    create_opportunity_request = helper.remove_nulls(sd.stringify_json("src/create_opportunity/createOpportunity.json"))
    try:
        # Perform an API call
        response = partner_central_client.create_opportunity(**create_opportunity_request)
        
        helper.pretty_print_datetime(response)

        # Retrieve the opportunity details
        get_response = partner_central_client.get_opportunity(
            Identifier=response["Id"],
            Catalog=CATALOG_TO_USE
        )
        helper.pretty_print_datetime(get_response)
        return response
    except ClientError as err:
        # Catch all client exceptions
        print(err.response)

def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Create Opportunity.")
    print("-" * 88)

    partner_central_client = boto3.client(
        service_name=serviceName,
        region_name='us-east-1'
    )

    create_opportunity(partner_central_client)

if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [CreateOpportunity](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateOpportunity) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Partner Central API with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.