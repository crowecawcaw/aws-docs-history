AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating HealthOmics annotation stores

An annotation store is a data store representing an annotation database, such as one from
a TSV, VCF, or GFF file. If the same reference genome is specified, annotation stores are
mapped to the same coordinate system as variant stores during an import. The following
topics show how to use the HealthOmics console and AWS CLI to create and manage annotation stores.

###### Topics

- [Creating an annotation
  store using the console](#gs-console-create-annotation-store "#gs-console-create-annotation-store")
- [Creating an annotation store using the API](#create-manage-annotation-store-api "#create-manage-annotation-store-api")

## Creating an annotation

store using the console

Use the following procedure to create annotation stores with the HealthOmics console.

###### To create an annotation store

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Annotation stores**.
3. On the **Annotation stores** page, choose
   **Create annotation store**.
4. On the **Create annotation store** page, provide the
   following information
   - **Annotation store name** - A unique name for
     this store.
   - **Description** (optional) - A description of
     this reference genome.
   - **Data format and schema details** - Select
     data file format and upload the schema definition for this
     store.
   - **Reference genome** - The reference genome
     for this annotation.
   - **Data Encryption** - Choose whether you want
     data encryption to be owned and managed by AWS or by yourself.
   - **Tags** (optional) - Provide up to 50 tags
     for this annotation store.

5. Choose **Create annotation store**.

## Creating an annotation store using the API

The following example shows how to create an annotation store using the AWS CLI. For all AWS CLI
and API operations, you must specify the format of your data.

```
aws omics create-annotation-store --name my_annotation_store \
           --store-format GFF \
           --reference referenceArn="arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/5987565360"
           --version-name new_version
```

You receive the following response to confirm the creation of your annotation store.

```
{
           "creationTime": "2022-08-24T20:34:19.229500Z",
           "id": "3b93cdef69d2",
           "name": "my_annotation_store",
           "reference": {
               "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/5987565360"
           },
           "status": "CREATING"
           "versionName": "my_version"
       }
```

To learn more about an annotation store, use the **get-annotation-store**
API.

```
aws omics get-annotation-store --name my_annotation_store
```

You receive the following response.

```
{
          "id": "eeb019ac79c2",
          "reference": {
              "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/5638433913/reference/5871590330“
          },
          "status": "ACTIVE",
          "storeArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/gffstore",
          "name": "my_annotation_store",
          "creationTime": "2022-11-05T00:05:19.136131+00:00",
          "updateTime": "2022-11-05T00:10:36.944839+00:00",
          "tags": {},
          "storeFormat": "GFF",
          "statusMessage": "",
          "storeSizeBytes": 0,
          "numVersions": 1
      }
```

To view all annotation stores associated with an account, use the
**list-annotation-stores** API operation.

```
aws omics list-annotation-stores
```

You receive a response that lists all annotation stores, along with their IDs,
statuses, and other details, as shown in the following example response.

```
{
           "annotationStores": [
               {
                  "id": "4d8f3eada259",
                   "reference":
                       "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/5638433913/reference/5871590330"
                   },
                   "status": "CREATING",
                   "name": "gffstore",
                   "creationTime": "2022-09-27T17:30:52.182990+00:00",
                   "updateTime": "2022-09-27T17:30:53.025362+00:00"
               }
           ]
       }
```

You can also filter responses based on status or other criteria.
