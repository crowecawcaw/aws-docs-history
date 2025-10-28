# Optimistic locking for asset model writes

When updating an asset model, an user does the following:

1. Read the current asset model definition.
2. Edit the asset model definition with required changes.
3. Update asset model with the new definition.

In a scenario with two users updating a model, the following is possible:

- User A reads the asset model X definition.
- User B reads the asset model X definition and commits changes, modifying the definition of X.
- User A commits and overwrites the change made by user B for asset model X,
  without verifying or incorporating User B's changes.

Optimistic locking is a mechanism used by AWS IoT SiteWise to prevent accidental overwrites like the scenario above. Optimistic locking
is a strategy to ensure the current version of asset model being updated or deleted, is the same
as its current version in AWS IoT SiteWise. This protects asset model writes from being overwritten
by accidental updates.

Follow these steps to perform asset model writes with optimistic locking:

###### Topics

- [Performing asset model writes with optimistic lock (console)](#opt-locking-for-model-console "#opt-locking-for-model-console")
- [Performing asset model writes with optimistic lock (AWS CLI)](#opt-locking-for-model-cli "#opt-locking-for-model-cli")

## Performing asset model writes with optimistic lock (console)

The procedure below describes how to perform asset model writes with an optimistic lock
on the asset model's active version in the console.

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Models**.
3. Choose the asset model or component model to update.
4. Choose **Edit**.
5. Make changes on the **Edit model** page.
6. Choose **Save**.

###### Note

Sometimes, one or more successful model updates have happened between when the user
starts editing the model, and saves the made edits to the model.

To ensure the user does not accidentally overwrite over new successful updates, the user's
write is rejected. The console disables the **Save** button, and prompts
the user to refresh the **Edit model** page. The user must update the
new active version of the model again. The user must perform the following additional steps: 7. Choose **Refresh**. 8. Follow steps 5 and 6 again.

## Performing asset model writes with optimistic lock (AWS CLI)

The procedure below describes how to perform asset model writes with optimistic locking in the AWS CLI.

1. **Fetch the ETag associated with current model definition**

`ETag` is a unique token generated for each new representation of an asset model.
Call [DescribeAssetModel](../APIReference/API_DescribeAssetModel.md "../APIReference/API_DescribeAssetModel.md")
API to fetch the current asset model definition, and associated `ETag` from the response.

During concurrent updates, users perform either successful updates (model in `ACTIVE` state), or
unsuccessful updates (model in `FAILED` state). To ensure that an user does not accidentally overwrite
a successful update, you must retrieve the active version of the asset model from [Asset model versions](model-active-version.md "model-active-version.md"),
and get the `ETag` value.

Run the following command:

```

aws iotsitewise describe-asset-model --asset-model-id asset-model-id \
--asset-model-version ACTIVE

```

The response returns the following structure:

```
{
  "assetModelId": "`String`",
  "assetModelArn": "`String`",
  "assetModelName": "`String`",
  ...
  "eTag": "`String`"
}

```

###### Note

You must retrieve the latest version of the asset model and its `ETag` in order to not
overwrite any updates. 2. **Perform UPDATE and DELETE operations with write conditions**

The following asset model APIs support optimistic locking:

    * [UpdateAssetModel](../APIReference/API_UpdateAssetModel.md "../APIReference/API_UpdateAssetModel.md")
    * [DeleteAssetModel](../APIReference/API_DeleteAssetModel.md "../APIReference/API_DeleteAssetModel.md")
    * [CreateAssetModelCompositeModel](../APIReference/API_CreateAssetModelCompositeModel.md "../APIReference/API_CreateAssetModelCompositeModel.md")
    * [UpdateAssetModelCompositeModel](../APIReference/API_UpdateAssetModelCompositeModel.md "../APIReference/API_UpdateAssetModelCompositeModel.md")
    * [DeleteAssetModelCompositeModel](../APIReference/API_DeleteAssetModelCompositeModel.md "../APIReference/API_DeleteAssetModelCompositeModel.md")

###### Note

The below scenarios use `UpdateAssetModel` API as a reference. The conditions apply to all the operations listed above.

The below scenarios describe the different write conditions depending on concurrency control requirements:

    * Run the following command in order not to overwrite any successful updates. A new active version must not exist, since the last read
     active version. Replace `e-tag` with the `ETag` returned in the API operation
     used in the read of the active version.




    ```

    aws iotsitewise update-asset-model \
      --asset-model-id asset-model-id \
      --if-match e-tag \
      --match-for-version-type ACTIVE \
      --cli-input-json file://model-payload.json

    ```
    * When a model creation fails, an active version does not exist for it yet, because it's in a `FAILED` state. It is
     still possible to overwrite a new active version that is present, before your changes are committed.
     Run the following command to not overwrite a new active version, when an active version does not exist during your
     last read.



    ```

    aws iotsitewise update-asset-model \
      --asset-model-id asset-model-id \
      --if-none-match "*" \
      --match-for-version-type ACTIVE \
      --cli-input-json file://model-payload.json

    ```
    * Run the following command to avoid overwriting any successful or unsuccessful updates. This command defines a write
     condition which ensures that a latest version is not created since your last read latest version.
     Replace `e-tag` with the `ETag` returned in the API operation
     used in the read of the active version.



    ```

    aws iotsitewise update-asset-model \
      --asset-model-id asset-model-id \
      --if-match eTag \
      --match-for-version-type LATEST \
      --cli-input-json file://model-payload.json

    ```

    If the write condition evaluates to `FALSE`, the write request fails with the `PreconditionFailedException`.
