AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Sharing HealthOmics analytics stores

As the owner of a variant store or an annotation store, you can share the store with other AWS accounts. The
owner can revoke access to the shared resource by deleting the share.

As the subscriber to a shared store, you first accept the share. You can then define workflows that use the
shared store. The data shows up as a table in both AWS Glue and Lake Formation.

When you no longer need access to the store, you delete the share.

See [Cross-account resource sharing in AWS HealthOmics](resource-sharing.md "resource-sharing.md") for additional information
about resource sharing.

## Creating a store share

To create a store share, use the **create-share** API operation.
The principal subscriber is the AWS account of the user who will subscribe to the share.
The following example creates a share for a variant store.
To share a store with more than one account, you create multiple shares of the same store.

```
aws omics create-share  \
        --resource-arn "arn:aws:omics:us-west-2:555555555555:variantStore/omics_dev_var_store" \
        --principal-subscriber "123456789012" \
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

The share remains in pending state until the subscriber accepts it using the accept-share API operation.
