# Deleting HealthOmics analytics stores

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

When you delete a variant or annotation store, the system
also deletes all imported data in that store and any associated tags.

The following example shows how to delete a variant store using the AWS CLI. If the
action is successful, the variant store status transitions to `DELETING`.

```
aws omics delete-variant-store --id <variant-store-id>
```

The following example shows how to delete an annotation store. If the action is successful, the
annotation store status transitions to `DELETING`. Annotation stores can't be
deleted if more than one version exists.

```
aws omics delete-annotation-store --id <annotation-store-id>
```
