# Amazon DataZone quickstart with sample scripts

You can access Amazon DataZone via the management portal or the Amazon DataZone data portal, or
programmatically by using the Amazon DataZone HTTPS API, which lets you issue HTTPS requests
directly to the service. This section contains sample scripts that invoke Amazon DataZone APIs that
you can use to complete the following common tasks:

###### Sample scripts

- [Create an Amazon DataZone domain and data
  portal](#create-domain-gs-glue-api "#create-domain-gs-glue-api")
- [Create a publishing project](#create-publishing-project-gs-glue-api "#create-publishing-project-gs-glue-api")
- [Create an environment
  profile](#create-environment-profile-gs-glue-api "#create-environment-profile-gs-glue-api")
- [Create an environment](#create-environment-gs-glue-api "#create-environment-gs-glue-api")
- [Gather metadata from AWS
  Glue](#gather-metadata-from-glue-gs-glue-api "#gather-metadata-from-glue-gs-glue-api")
- [Curate and publish a data asset](#curate-data-asset-gs-glue-api "#curate-data-asset-gs-glue-api")
- [Search the data catalog and subscribe
  to data](#search-catalog-subscribe-gs-glue-api "#search-catalog-subscribe-gs-glue-api")
- [Search for assets in the data
  catalog](#search-catalog-subscribe-gs-glue-api "#search-catalog-subscribe-gs-glue-api")
- [Other useful sample scripts](#other-useful-scripts-api "#other-useful-scripts-api")

## Create an Amazon DataZone domain and data

portal

You can use the following sample script to create an Amazon DataZone domain. For more
information about Amazon DataZone domains, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

```

import sys
import boto3

// Initialize datazone client
region = 'us-east-1'
dzclient = boto3.client(service_name='datazone', region_name='us-east-1')

// Create DataZone domain
def create_domain(name):
    return dzclient.create_domain(
        name = name,
        description = "this is a description",
        domainExecutionRole = "arn:aws:iam::<account>:role/AmazonDataZoneDomainExecutionRole",
    )

```

## Create a publishing project

You can use the following sample script to create a publishing project in
Amazon DataZone.

```

// Create Project
def create_project(domainId):
    return dzclient.create_project(
        domainIdentifier = domainId,
        name = "sample-project"
    )

```

## Create an environment

profile

You can use the following sample scripts to create an environment profile in
Amazon DataZone.

This sample payload is used when the `CreateEnvironmentProfile` API is
invoked:

```

Sample Payload
{
    "Content":{
        "project_name": "Admin_project",
        "domain_name": "Drug-Research-and-Development",
        "blueprint_account_region": [
            {
                "blueprint_name": "DefaultDataLake",
                "account_id": ["066535990535",
                "413878397724",
                "676266385322",
                "747721550195",
                "755347404384"
                ],
                "region": ["us-west-2", "us-east-1"]
            },
            {
                "blueprint_name": "DefaultDataWarehouse",
                "account_id": ["066535990535",
                "413878397724",
                "676266385322",
                "747721550195",
                "755347404384"
                ],
                "region":["us-west-2", "us-east-1"]
            }
        ]
    }
}

```

This sample script invokes the `CreateEnvironmentProfile` API:

```

def create_environment_profile(domain_id, project_id, env_blueprints)
        try:
            response = dz.list_environment_blueprints(
                domainIdentifier=domain_id,
                managed=True
            )
            env_blueprints = response.get("items")
            env_blueprints_map = {}
            for i in env_blueprints:
                env_blueprints_map[i["name"]] = i['id']

            print("Environment Blueprint map", env_blueprints_map)
            for i in blueprint_account_region:
                print(i)
                for j in i["account_id"]:
                    for k in i["region"]:
                        print("The env blueprint name is", i['blueprint_name'])
                        dz.create_environment_profile(
                            description='This is a test environment profile created via lambda function',
                            domainIdentifier=domain_id,
                            awsAccountId=j,
                            awsAccountRegion=k,
                            environmentBlueprintIdentifier=env_blueprints_map.get(i["blueprint_name"]),
                            name=i["blueprint_name"] + j + k + "_profile",
                            projectIdentifier=project_id
                        )
        except Exception as e:
            print("Failed to created Environment Profile")
            raise e

```

This is the sample output payload once the `CreateEnvironmentProfile` API is
invoked:

```

{
    "Content":{
        "project_name": "Admin_project",
        "domain_name": "Drug-Research-and-Development",
        "blueprint_account_region": [
            {
                "blueprint_name": "DefaultDataWarehouse",
                "account_id": ["111111111111"],
                "region":["us-west-2"],
                "user_parameters":[
                    {
                        "name": "dataAccessSecretsArn",
                        "value": ""
                    }
                ]
            }
        ]
    }
}

```

## Create an environment

You can use the following sample script to create an environment in Amazon DataZone.

```

def create_environment(domain_id, project_id,blueprint_account_region ):
         try:
            #refer to get_domain_id and get_project_id for fetching ids using names.
            sts_client = boto3.client("sts")
            # Get the current account ID
            account_id = sts_client.get_caller_identity()["Account"]
            print("Fetching environment profile ids")
            env_profile_map = get_env_profile_map(domain_id, project_id)

            for i in blueprint_account_region:
                for j in i["account_id"]:
                    for k in i["region"]:
                        print(" env blueprint name", i['blueprint_name'])
                        profile_name = i["blueprint_name"] + j + k + "_profile"
                        env_name = i["blueprint_name"] + j + k + "_env"
                        description = f'This is environment is created for {profile_name}, Account {account_id} and region {i["region"]}'
                        try:
                            dz.create_environment(
                                description=description,
                                domainIdentifier=domain_id,
                                environmentProfileIdentifier=env_profile_map.get(profile_name),
                                name=env_name,
                                projectIdentifier=project_id
                            )
                            print(f"Environment created - {env_name}")
                        except:
                            dz.create_environment(
                                description=description,
                                domainIdentifier=domain_id,
                                environmentProfileIdentifier=env_profile_map.get(profile_name),
                                name=env_name,
                                projectIdentifier=project_id,
                                userParameters= i["user_parameters"]
                            )
                            print(f"Environment created - {env_name}")
        except Exception as e:
            print("Failed to created Environment")
            raise e

```

## Gather metadata from AWS

Glue

You can use this sample script to gather metadata from AWS Glue. This script runs on a
standard schedule. You can retrieve the parameters from the sample script and make them
global. Fetch the project, environment, and domain ID using standard functions. The AWS
Glue data source is created and ran at a standard time which can be updated in the cron
section of the script.

```

def crcreate_data_source(domain_id, project_id,data_source_name)
        print("Creating Data Source")
        data_source_creation = dz.create_data_source(
            # Define data source : Customize the data source to which you'd like to connect
            # define the name of the Data source to create, example: name ='TestGlueDataSource'
            name=data_source_name,
            # give a description for the datasource (optional), example: description='This is a dorra test for creation on DZ datasources'
            description=data_source_description,
            # insert the domain identifier corresponding to the domain to which the datasource will belong, example: domainIdentifier= 'dzd_6f3gst5jjmrrmv'
            domainIdentifier=domain_id,
            # give environment identifier , example: environmentIdentifier= '3weyt6hhn8qcvb'
            environmentIdentifier=environment_id,
            # give corresponding project identifier, example: projectIdentifier= '6tl4csoyrg16ef',
            projectIdentifier=project_id,
            enableSetting="ENABLED",
            # publishOnImport used to select whether assets are added to the inventory and/or discovery catalog .
            # publishOnImport = True : Assets will be added to project's inventory as well as published to the discovery catalog
            # publishOnImport = False : Assets will only be added to project's inventory.
            # You can later curate the metadata of the assets and choose subscription terms to publish them from the inventory to the discovery catalog.
            publishOnImport=False,
            # Automated business name generation : Use AI to automatically generate metadata for assets as they are published or updated by this data source run.
            # Automatically generated metadata can be be approved, rejected, or edited by data publishers.
            # Automatically generated metadata is badged with a small icon next to the corresponding metadata field.
            recommendation={"enableBusinessNameGeneration": True},
            type="GLUE",
            configuration={
                "glueRunConfiguration": {
                    "dataAccessRole": "arn:aws:iam::"
                    + account_id
                    + ":role/service-role/AmazonDataZoneGlueAccess-"
                    + current_region
                    + "-"
                    + domain_id
                    + "",
                    "relationalFilterConfigurations": [
                        {
                            #
                            "databaseName": glue_database_name,
                            "filterExpressions": [
                                {"expression": "*", "type": "INCLUDE"},
                            ],
                            #    "schemaName": "TestSchemaName",
                        },
                    ],
                },
            },
            # Add metadata forms to the data source (OPTIONAL).
            # Metadata forms will be automatically applied to any assets that are created by the data source.
            # assetFormsInput=[
            #     {
            #         "content": "string",
            #         "formName": "string",
            #         "typeIdentifier": "string",
            #         "typeRevision": "string",
            #     },
            # ],
            schedule={
                "schedule": "cron(5 20 * * ? *)",
                "timezone": "UTC",
            },
        )
        # This is a suggested syntax to return values
        #        return_values["data_source_creation"] = data_source_creation["items"]
        print("Data Source Created")


//This is the sample response payload after the CreateDataSource API is invoked:

{
    "Content":{
        "project_name": "Admin",
        "domain_name": "Drug-Research-and-Development",
        "env_name": "GlueEnvironment",
        "glue_database_name": "test",
        "data_source_name" : "test",
        "data_source_description" : "This is a test data source"
    }
}

```

## Curate and publish a data asset

You can use the following sample scripts to curate and publish data assets in
Amazon DataZone.

You can use the following script to create custom form types:

```

def create_form_type(domainId, projectId):
    return dzclient.create_form_type(
        domainIdentifier = domainId,
        name = "customForm",
        model = {
            "smithy": "structure customForm { simple: String }"
        },
        owningProjectIdentifier = projectId,
        status = "ENABLED"
    )

```

You can use the following sample script to create custom asset types:

```

def create_custom_asset_type(domainId, projectId):
    return dzclient.create_asset_type(
        domainIdentifier = domainId,
        name = "userCustomAssetType",
        formsInput = {
            "Model": {
                "typeIdentifier": "customForm",
                "typeRevision": "1",
                "required": False
            }
        },
        owningProjectIdentifier = projectId,
    )

```

You can use the following sample script to create custom assets:

```

def create_custom_asset(domainId, projectId):
    return dzclient.create_asset(
        domainIdentifier = domainId,
        name = 'custom asset',
        description = "custom asset",
        owningProjectIdentifier = projectId,
        typeIdentifier = "userCustomAssetType",
        formsInput = [
            {
                "formName": "UserCustomForm",
                "typeIdentifier": "customForm",
                "content": "{\"simple\":\"sample-catalogId\"}"
            }
        ]
    )

```

You can use the following sample script to create a glossary:

```

def create_glossary(domainId, projectId):
    return dzclient.create_glossary(
        domainIdentifier = domainId,
        name = "test7",
        description = "this is a test glossary",
        owningProjectIdentifier = projectId
    )

```

You can use the following sample script to create a glossary term:

```

def create_glossary_term(domainId, glossaryId):
    return dzclient.create_glossary_term(
        domainIdentifier = domainId,
        name = "soccer",
        shortDescription = "this is a test glossary",
        glossaryIdentifier = glossaryId,
    )

```

You can use the following sample script to create an asset using a system-defined asset
type:

```

def create_asset(domainId, projectId):
    return dzclient.create_asset(
        domainIdentifier = domainId,
        name = 'sample asset name',
        description = "this is a glue table asset",
        owningProjectIdentifier = projectId,
        typeIdentifier = "amazon.datazone.GlueTableAssetType",
        formsInput = [
            {
                "formName": "GlueTableForm",
                "content": "{\"catalogId\":\"sample-catalogId\",\"columns\":[{\"columnDescription\":\"sample-columnDescription\",\"columnName\":\"sample-columnName\",\"dataType\":\"sample-dataType\",\"lakeFormationTags\":{\"sample-key1\":\"sample-value1\",\"sample-key2\":\"sample-value2\"}}],\"compressionType\":\"sample-compressionType\",\"lakeFormationDetails\":{\"lakeFormationManagedTable\":false,\"lakeFormationTags\":{\"sample-key1\":\"sample-value1\",\"sample-key2\":\"sample-value2\"}},\"primaryKeys\":[\"sample-Key1\",\"sample-Key2\"],\"region\":\"us-east-1\",\"sortKeys\":[\"sample-sortKey1\"],\"sourceClassification\":\"sample-sourceClassification\",\"sourceLocation\":\"sample-sourceLocation\",\"tableArn\":\"sample-tableArn\",\"tableDescription\":\"sample-tableDescription\",\"tableName\":\"sample-tableName\"}"
            }
        ]
    )

```

You can use the following sample script to create an asset revision and attach a
glossary term:

```

def create_asset_revision(domainId, assetId):
    return dzclient.create_asset_revision(
        domainIdentifier = domainId,
        identifier = assetId,
        name = 'glue table asset 7',
        description = "glue table asset description update",
        formsInput = [
            {
                "formName": "GlueTableForm",
                "content": "{\"catalogId\":\"sample-catalogId\",\"columns\":[{\"columnDescription\":\"sample-columnDescription\",\"columnName\":\"sample-columnName\",\"dataType\":\"sample-dataType\",\"lakeFormationTags\":{\"sample-key1\":\"sample-value1\",\"sample-key2\":\"sample-value2\"}}],\"compressionType\":\"sample-compressionType\",\"lakeFormationDetails\":{\"lakeFormationManagedTable\":false,\"lakeFormationTags\":{\"sample-key1\":\"sample-value1\",\"sample-key2\":\"sample-value2\"}},\"primaryKeys\":[\"sample-Key1\",\"sample-Key2\"],\"region\":\"us-east-1\",\"sortKeys\":[\"sample-sortKey1\"],\"sourceClassification\":\"sample-sourceClassification\",\"sourceLocation\":\"sample-sourceLocation\",\"tableArn\":\"sample-tableArn\",\"tableDescription\":\"sample-tableDescription\",\"tableName\":\"sample-tableName\"}"
            }
        ],
        glossaryTerms = ["<glossaryTermId:>"]
    )

```

You can use the following sample script to publish an asset:

```

def publish_asset(domainId, assetId):
    return dzclient.create_listing_change_set(
        domainIdentifier = domainId,
        entityIdentifier = assetId,
        entityType = "ASSET",
        action = "PUBLISH",
    )

```

## Search the data catalog and subscribe

to data

You can use the following sample scripts to search the data catalog and subscribe to
data:

```

def search_asset(domainId, projectId, text):
    return dzclient.search(
        domainIdentifier = domainId,
        owningProjectIdentifier = projectId,
        searchScope = "ASSET",
        searchText = text,
    )

```

You can use the following sample script to get the listing ID for the asset:

```

def search_listings(domainId, assetName, assetId):
    listings = dzclient.search_listings(
        domainIdentifier=domainId,
        searchText=assetName,
        additionalAttributes=["FORMS"]
    )

    assetListing = None
    for listing in listings['items']:
        if listing['assetListing']['entityId'] == assetId:
            assetListing = listing

    return listing['assetListing']['listingId']

```

You can use the following sample scripts to create a subscription request using the
listing ID:

```

create_subscription_response = def create_subscription_request(domainId, projectId, listingId):
    return dzclient.create_subscription_request(
        subscribedPrincipals=[{
            "project": {
                "identifier": projectId
            }
        }],
        subscribedListings=[{
            "identifier": listingId
        }],
        requestReason="Give request reason here."
    )

```

Using the `create_subscription_response` above, get the `subscription_request_id`, and then accept/approve the subscription using the
following sample script:

```

subscription_request_id = create_subscription_response["id"]

def accept_subscription_request(domainId, subscriptionRequestId):
    return dzclient.accept_subscription_request(
        domainIdentifier=domainId,
        identifier=subscriptionRequestId
    )

```

## Search for assets in the data

catalog

You can use the following sample scripts that utilize free text search to look up your
published data assets (listings) in the Amazon DataZone catalog.

- The following example performs a free text keyword search in the domain and returns
  all the listings that match the provided keyword 'credit':

```
aws datazone search-listings \
  --domain-identifier dzd_c1s7uxe71prrtz \
  --search-text "credit"
```

- You can also combine multiple keywords to further narrow down the search scope. For
  example, if you are looking for all the published data assets (listings) that have data
  related to sales in Mexico, you can formulate your query with two keyword 'Mexico' and
  'sales'.

```

            aws datazone search-listings \
  --domain-identifier dzd_c1s7uxe71prrtz \
  --search-text "mexico sales"

```

You can also search for listing using filters. The `filters` parameter in the
SearchListings API allows you to retrieve filtered results from the domain. The API supports
multiple default filters and you can also combine two or more filters and perform AND/OR
operation on them. The filter clause takes in two parameters: attrbibute and value. The
default supported filter attributes are `typeName`, `owningProjectId`,
and `glossaryTerms`.

- The following example performs a search of all the listings in a given domain using
  the `assetType` filter where the listing is a type of Redshift Table.

```

            aws datazone search-listings \
--domain-identifier dzd_c1s7uxe71prrtz \
--filters '{"or":[{"filter":{"attribute":"typeName","value":"RedshiftTableAssetType"}} ]}'

```

- You can also combine multiple filters together using AND/OR operations. In the
  following example, you combine `typeName` and `project`
  filters.

```

            aws datazone search-listings \
--domain-identifier dzd_c1s7uxe71prrtz \
--filters '{"or":[{"filter":{"attribute":"typeName","value":"RedshiftTableAssetType"}},  {"filter":{"attribute":"owningProjectId","value":"cwrrjch7f5kppj"}} ]}'

```

- You can even combine free text search along with filters to find exact results and
  further sort them by creation/last updated time of the listing as shown in the following
  example:

```

            aws datazone search-listings \
--domain-identifier dzd_c1s7uxe71prrtz \
--search-text "finance sales" \
--filters '{"or":[{"filter":{"attribute":"typeName","value":"GlueTableViewType"}} ]}' \
--sort '{"attribute": "UPDATED_AT", "order":"ASCENDING"}'

```

## Other useful sample scripts

You can use the following sample scripts to complete various tasks as you work with your
data in Amazon DataZone.

Use the following sample script to list existing Amazon DataZone domains:

```

def list_domains():
    datazone = boto3.client('datazone')
    response = datazone.list_domains(status='AVAILABLE')
    [print("%12s | %16s | %12s | %52s" % (item['id'], item['name'], item['managedAccountId'], item['portalUrl'])) for item in response['items']]
    return

```

Use the following sample script to list existing Amazon DataZone projects:

```

def list_projects(domain_id):
    datazone = boto3.client('datazone')
    response = datazone.list_projects(domainIdentifier=domain_id)
    [print("%12s | %16s " % (item['id'], item['name'])) for item in response['items']]
    return

```

Use the following sample script to list existing Amazon DataZone metadata forms:

```

def list_metadata_forms(domain_id):
    datazone = boto3.client('datazone')
    response = datazone.search_types(domainIdentifier=domain_id,
        managed=False,
        searchScope='FORM_TYPE')
    [print("%16s | %16s | %3s | %8s" % (item['formTypeItem']['name'], item['formTypeItem']['owningProjectId'],item['formTypeItem']['revision'], item['formTypeItem']['status'])) for item in response['items']]
    return

```
