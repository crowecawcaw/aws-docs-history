AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating HealthOmics variant stores

The following topics describe how to create HealthOmics variant stores using the console and the API.

###### Topics

- [Creating a variant store using the console](#gs-console-analytics "#gs-console-analytics")
- [Creating a variant store using the API](#gs-api-analytics "#gs-api-analytics")

## Creating a variant store using the console

You can create a variant store using the HealthOmics console.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Variant stores**.
3. On the **Create variant store** page, provide the
   following information
   - **Variant store name** - A unique name for
     this store.
   - **Description** (optional) - A description of
     this variant store.
   - **Reference genome** - The reference genome
     for this variant store.
   - **Data Encryption** - Choose whether you want
     data encryption to be owned and managed by AWS or by yourself.
   - **Tags** (optional) - Provide up to 50 tags
     for this variant store.

4. Choose **Create variant store**.

## Creating a variant store using the API

Use HealthOmics `CreateVariantStore` API operation to create variant stores. You can also perform this
operation with the AWS CLI.

To create a variant store, you provide a name for the store and the ARN of a reference store. The variant
store is ready to ingest data when its status changes to READY.

The following example uses the AWS CLI to create a variant store.

```
aws omics create-variant-store --name myvariantstore \
    --reference referenceArn="arn:aws:omics:us-west-2:555555555555:referenceStore/123456789/reference/5987565360"
```

To confirm the creation of your variant store, you receive the following response.

```
{
    "creationTime": "2022-11-03T18:19:52.296368+00:00",
    "id": "45aeb91d5678",
    "name": "myvariantstore",
    "reference": {
        "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/123456789/reference/5987565360"
    },
    "status": "CREATING"
}
```

To learn more about a variant store, use the **get-variant-store**
API.

```
aws omics get-variant-store --name myvariantstore
```

You receive the following response.

```
{
    "id": "45aeb91d5678",
    "reference": {
        "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/123456789/reference/5987565360"
    },
    "status": "ACTIVE",
    "storeArn": "arn:aws:omics:us-west-2:555555555555:variantStore/myvariantstore",
    "name": "myvariantstore",
    "creationTime": "2022-11-03T18:19:52.296368+00:00",
    "updateTime": "2022-11-03T18:30:56.272792+00:00",
    "tags": {},
    "storeSizeBytes": 0
}
```

To view all variant stores associated with an account, use the
**list-variant-stores** API.

```
aws omics list-variant-stores
```

You receive a response that lists all variant stores, along with their IDs, statuses, and other details, as
shown in the following example response.

```
{
    "variantStores": [
        {
            "id": "45aeb91d5678",
            "reference": {
                "referenceArn": "arn:aws:omics:us-west-2:55555555555:referenceStore/5506874698"
            },
            "status": "ACTIVE",
            "storeArn": "arn:aws:omics:us-west-2:55555555555:variantStore/new_variant_store",
            "name": "variantstore",
            "creationTime": "2022-11-03T18:19:52.296368+00:00",
            "updateTime": "2022-11-03T18:30:56.272792+00:00",
            "statusMessage": "",
            "storeSizeBytes": 141526
        }
    ]
}
```

You can also filter the responses for the **list-variant-stores** API
based on statuses or other criteria.

VCF Files imported into analytic stores created on or after May 15, 2023 have defined schemas for Variant
Effect Predictor (VEP) annotations. This makes it easier to query and parse imported VCF data. The change doesn't
impact stores created before May 15, 2023, except if the `annotation fields` parameter is included in
the API or CLI call. For these stores, using the `annotation fields` parameter will cause the request
to fail.
