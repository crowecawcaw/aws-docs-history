AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Cross-account resource sharing in AWS HealthOmics

Use cross-account sharing to share resources with collaborators without creating copies or modifying IAM
resource policies. The following resources support cross-account sharing:

- HealthOmics variant stores
- HealthOmics annotation stores
- Private workflows
  Sharing a resource includes the following steps:

1. The resource owner creates a share, and specifies the ARN of the resource and the AWS account of the
   intended subscriber. The resource share remains in pending state until the subscriber accepts the
   share.
2. The subscriber accepts the resource share to get access to the resource. The resource share transitions
   to activating state.
3. The HealthOmics service provides subscriber account with access to the resource.
4. The resource owner can delete the share, or the subscriber can revoke their access to the share. The
   subscriber can't delete the share or the associated resource.

###### Topics

- [Creating a share](#create-share "#create-share")
- [Retrieve information about a share](#get-share "#get-share")
- [View the shares that you own](#view-shares "#view-shares")
- [View accepted shares from other accounts](#view-accepted-shares "#view-accepted-shares")
- [Delete a share](#delete-share "#delete-share")

## Creating a share

You can use the **create-share** API operation to create a share. The principal
subscriber is the AWS account of the user who will subscribe to the shared resource. The following example creates
a share for a variant store.

```
aws omics create-share \
    --resource-arn "arn:aws:omics:us-west-2:555555555555:variantStore/omics_dev_var_store" \
    --principal-subscriber "123456789012"  \
    --name "my_Share-123"

```

If the create is successful, you receive a response with the share ID and status.

```
{
"shareId": "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a",
     "name": "my_Share-123",
     "status": "PENDING"
}
```

The share remains in **pending** state until the subscriber accepts it using the
**accept-share** API operation.

```

 aws omics accept-share \
    --share-id "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"

```

After the subscriber accepts the share, the share transitions to active state.

```
{
"status": "ACTIVATING"
}
```

## Retrieve information about a share

Use the **get-share** API operation to retrieve information about the
share.

```
aws omics get-share --share-id "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"
```

The API response includes metadata information about the share.

```
{
  "share":
    {
      "shareId": "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a",
      "name": "my_Share-123",
      "resourceArn": "arn:aws:omics:us-west-2:555555555555:variantStore/omics_dev_var_store",
      "principalSubscriber": "123456789012",
      "ownerId": "555555555555",
      "status": "PENDING"
    }
}
```

## View the shares that you own

Use the **list-shares** API to retrieve information about each of the shares that
you own.

```
aws omics list-shares  --resource-owner SELF
```

The API response includes the metadata for each share that you own.

## View accepted shares from other accounts

Use the **list-shares** API to view all shares that you accepted from other
accounts.

```
aws omics list-shares  --resource-owner OTHER
```

The API response includes the metadata for each share that you accepted.

## Delete a share

Use the **delete-share** API to delete a share after you no longer need it.

```
aws omics delete-share \
    --share-id "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"
```
