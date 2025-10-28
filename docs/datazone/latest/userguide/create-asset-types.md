# Create custom asset types in Amazon DataZone

In Amazon DataZone, assets represent specific types of data resources such as database
tables, dashboards, or machine learning models. To provide consistency and
standardization when describing catalog assets, an Amazon DataZone domain must have a set of
asset types that define how assets are represented in the catalog. An asset type defines
the schema for a specific type of asset. An asset type has a set of required and
optional nameable metadata form types (for example, govForm or GovernanceFormType).
Asset type in Amazon DataZone are versioned. When assets are created, they are validated
against the schema defined by their asset type (typically latest version), and if an
invalid structure is specified, asset creation fails.

**System asset types** - Amazon DataZone provisions
service-owned system asset types (including GlueTableAssetType, GlueViewAssetType,
RedshiftTableAssetType, RedshiftViewAssetType, and S3ObjectCollectionAssetType) and
system form types (including DataSourceReferenceFormType, AssetCommonDetailsFormType,
and SubscriptionTermsFormType). System asset types cannot be edited.

**Custom asset types** - for creating custom asset types,
you start by creating the required metadata form types and glossaries to use in the form
types. You can then create custom asset types by specifying name, description, and
associated metadata forms which can be required or optional.

For asset types with structured data, to represent the column schema in the data
portal, you can use the `RelationalTableFormType` to add the technical
metadata to your columns, including column names, descriptions, and data types) and the
`ColumnBusinessMetadataForm` to add the business descriptions of the
columns, including business names, glossary terms, and custom key value pairs.

To create a custom asset type via the Data portal, complete the following
steps:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project where you want to create a custom asset type.
3. Navigate to the **Data** tab for the project.
4. Choose **Asset types** from the left navigation pane, then
   choose **Create asset type**.
5. Specify the following and then choose **Create**.
   - **Name** - the name of the custom asset type
   - **Description** - the description of the custom asset
     type.
   - **Choose Add metadata forms** to add metadata forms
     to this custom asset type.

6. Once the custom asset type is created, you can use it to create assets.
   To create a custom asset type via the APIs, complete the following steps:

7. Create a metadata form type by invoking the `CreateFormType` API
   action.

The following is an Amazon SageMaker example:

```

m_model = "

structure SageMakerModelFormType {
   @required
   @amazon.datazone#searchable
   modelName: String

   @required
   modelArn: String

   @required
   creationTime: String
}
"

CreateFormType(
    domainIdentifier="my-dz-domain",
    owningProjectIdentifier="d4bywm0cja1dbb",
    name="SageMakerModelFormType",
    model=m_model
    status="ENABLED"
    )

```

2. Next, you can create an asset type by invoking the
   `CreateAssetType` API action. You can create asset types only via
   Amazon DataZone APIs using the available system form types
   (`SubscriptionTermsFormType` in the below example) or your custom
   form types. For system form types, the type name must begin with
   `amazon.datazone`.

```

CreateAssetType(
    domainIdentifier="my-dz-domain",
    owningProjectIdentifier="d4bywm0cja1dbb",
    name="SageMakerModelAssetType",
    formsInput={
        "SageMakerModelForm": {
            "typeIdentifier": "SageMakerModelFormType",
            "typeRevision": 7,
            "required": True,
        },
        "SubscriptionTerms": {
            "typeIdentifier": "amazon.datazone.SubscriptionTermsFormType",
            "typeRevision": 1,
            "required": False,
        },
    },
)

```

The following is an example for creating an asset type for structured
data:

```

CreateAssetType(
    domainIdentifier="my-dz-domain",
    owningProjectIdentifier="d4bywm0cja1dbb",
    name="OnPremMySQLAssetType",
    formsInput={
        "OnpremMySQLForm": {
            "typeIdentifier": "OnpremMySQLFormType",
            "typeRevision": 5,
            "required": True,
        },
        "RelationalTableForm": {
            "typeIdentifier": "amazon.datazone.RelationalTableFormType",
            "typeRevision": 1,
            "required": True,
        },
        "ColumnBusinessMetadataForm": {
            "typeIdentifier": "amazon.datazone.ColumnBusinessMetadataFormType",
            "typeRevision": 1,
            "required": False,
        },
        "SubscriptionTerms": {
            "typeIdentifier": "amazon.datazone.SubscriptionTermsFormType",
            "typeRevision": 1,
            "required": False,
        },
    },
)

```

3. And now, you can create an asset using the custom asset types you created in
   the steps above.

```

CreateAsset(
   domainIdentifier="my-dz-domain",
   owningProjectIdentifier="d4bywm0cja1dbb",
   typeIdentifier="SageMakerModelAssetType",
   name="MyModelAsset",
   glossaryTerms="xxx",
   formsInput=[{
        "formName": "SageMakerModelForm",
        "typeIdentifier": "SageMakerModelFormType",
        "content": "{\n \"ModelName\" : \"sample-ModelName\",\n \"ModelArn\" : \"999999911111\",\n \"CreationTime\" : \"2025-01-01 18:00:00.000\"}"
        }
        ]
)

```

And in this example you're creating a structured data asset:

```

CreateAsset(
   domainIdentifier="my-dz-domain",
   owningProjectIdentifier="d4bywm0cja1dbb",
   typeIdentifier="OnPremMySQLAssetType",
   name="MyModelAsset",
   glossaryTerms="xxx",
   formsInput=[{
        "formName": "RelationalTableForm",
        "typeIdentifier": "amazon.datazone.RelationalTableFormType",
        "content": ".."
        },
        {
        "formName": "OnpremMySQLForm",
        "typeIdentifier": "OnpremMySQLFormType",
        "content": ".."
        },
        {
        "formName": "mySQLTableForm",
        "typeIdentifier": "MySQLTableFormType",
        "typeRevision": "1",
        "content": ".."
        },
        {
        "formName": "AssetCommonDetailsForm",
        "typeIdentifier": "amazon.datazone.AssetCommonDetailsFormType",
        "content": "..."
        },
        .....
        ]
)

```
