

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Utilities to start a changeset using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ChangeSetUtilities_section"></a>

The following code examples show how to define utilities to start a changeset.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code) repository. 
Utility to load a changeset from a JSON file and start processing it.  

```
package com.example.awsmarketplace.catalogapi;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.apache.commons.lang3.StringUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.core.document.Document;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.protocols.json.internal.unmarshall.document.DocumentUnmarshaller;
import software.amazon.awssdk.protocols.jsoncore.JsonNodeParser;
import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.Change;
import software.amazon.awssdk.services.marketplacecatalog.model.Entity;
import software.amazon.awssdk.services.marketplacecatalog.model.StartChangeSetRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.StartChangeSetResponse;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.ToNumberPolicy;
import com.example.awsmarketplace.catalogapi.Entity.ChangeSet;
import com.example.awsmarketplace.catalogapi.Entity.ChangeSetEntity;
import com.example.awsmarketplace.catalogapi.Entity.Root;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;
import com.example.awsmarketplace.utils.StringSerializer;

/**
 * Before running this Java V2 code example, convert all Details attribute to DetailsDocument if any
 */

public class RunChangesets {
	
	private static final Gson GSON = new GsonBuilder()
			.setObjectToNumberStrategy(ToNumberPolicy.LAZILY_PARSED_NUMBER)
			.registerTypeAdapter(String.class, new StringSerializer())
			.create();

	public static void main(String[] args) {

		// input json can be specified here or passed from input parameter
		String inputChangeSetFile = "changeSets/offers/CreateReplacementOfferFromAGWithContractPricingDetailDocument.json";
		
		if (args.length > 0)
			inputChangeSetFile = args[0];
		
		// parse the input changeset file to string for process
		String changeSetsInput = readChangeSetToString(inputChangeSetFile);

		// process the changeset request
		try {
			StartChangeSetResponse result = getChangeSetRequestResult(changeSetsInput);
			ReferenceCodesUtils.formatOutput(result);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static StartChangeSetResponse getChangeSetRequestResult(String changeSetsInput) throws IOException {
		
		//set up AWS credentials
		MarketplaceCatalogClient marketplaceCatalogClient = 
				MarketplaceCatalogClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();
		
		//changeset list to save all the changesets in the changesets file
		List<Change> changeSetLists = new ArrayList<Change>();

		// read all changesets into object
		Root root = GSON.fromJson(changeSetsInput, Root.class);
		
		// process each changeset and add each changeset request to changesets list
		for (ChangeSet cs : root.changeSet) {
			
			ChangeSetEntity entity = cs.Entity;
			String entityType = entity.Type;
			String entityIdentifier = StringUtils.defaultIfBlank(entity.Identifier, null);
			Document detailsDocument = getDocumentFromObject(cs.DetailsDocument);
			
			Entity awsEntity = 
					Entity.builder()
					.type(entityType)
					.identifier(entityIdentifier)
					.build();

			Change inputChangeRequest = 
					Change.builder()
					.changeType(cs.ChangeType)
					.changeName(cs.ChangeName)
					.entity(awsEntity)
					.detailsDocument(detailsDocument)
					.build();
			
			changeSetLists.add(inputChangeRequest);
		}
		
		// process all changeset requests
		StartChangeSetRequest startChangeSetRequest = 
				StartChangeSetRequest.builder()
				.catalog(root.catalog)
				.changeSet(changeSetLists)
				.build();

		StartChangeSetResponse result = marketplaceCatalogClient.startChangeSet(startChangeSetRequest);

		return result;
	}

	public static Document getDocumentFromObject(Object detailsObject) {
		
		String detailsString = "{}";
		try {
			detailsString = IOUtils.toString(new ByteArrayInputStream(GSON.toJson(detailsObject).getBytes()), "UTF-8");
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		JsonNodeParser jsonNodeParser = JsonNodeParser.create();
		Document doc = jsonNodeParser.parse(detailsString).visit(new DocumentUnmarshaller());
		return doc;
	}
	
	
	public static String readChangeSetToString (String inputChangeSetFile) {
		
		InputStream changesetInputStream = RunChangesets.class.getClassLoader().getResourceAsStream(inputChangeSetFile);

		String changeSetsInput = null;
		
		try {
			changeSetsInput = IOUtils.toString(changesetInputStream, "UTF-8");
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return changeSetsInput;
		
	}
}
```
+  For API details, see [StartChangeSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python##catalog-api-reference-code) repository. 
Utility to start a changeset.  

```
"""
Purpose:

Generic function to start a changeset
"""

import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def generate_changeset(mp_client, change_set, change_set_name):
    """
    Start changeset
    """
    try:
        response = mp_client.start_change_set(
            Catalog="AWSMarketplace",
            ChangeSet=change_set,
            ChangeSetName=change_set_name,
        )
        logger.info("Changeset created!")
        logger.info("ChangeSet ID: %s", response["ChangeSetId"])
        logger.info("ChangeSet ARN: %s", response["ChangeSetArn"])

        return response

    except ClientError as e:
        logger.exception("Unexpected error: %s", e)
        raise


def usage_demo(change_set, change_set_name):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Executing changeset: " + change_set_name)
    print("-" * 88)

    mp_client = boto3.client("marketplace-catalog")

    response = generate_changeset(mp_client, change_set, change_set_name)

    return response

    print("-" * 88)
```
Utility to load a changeset from a JSON file.  

```
"""
Purpose:

This module will stringify the details sections of a changeset file.
"""

import json


def pretty_print(response):
    json_object = json.dumps(response, indent=4)
    print(json_object)


# open json file from path
def open_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f)


def stringify_details_sections(json_object):
    """
    Loops through every change type in the changeset to look for non-empty
    details section and stringifies them
    """
    for change_type in json_object["ChangeSet"]:
        # Only stringify details section if it is not empty
        if "Details" in change_type and change_type["Details"] != "{}":
            string_details = json.dumps(change_type["Details"])
            change_type["Details"] = string_details
        else:
            pass

    return json_object["ChangeSet"]


def stringify_changeset(file_path):
    changeset_file = open_json_file(file_path)
    changeset_stringified = stringify_details_sections(changeset_file)

    return changeset_stringified
```
+  For API details, see [StartChangeSet](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/StartChangeSet) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.