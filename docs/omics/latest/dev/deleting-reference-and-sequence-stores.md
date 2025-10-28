AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Deleting HealthOmics reference and

sequence stores

Both reference and sequence stores can be deleted. Sequence stores can only be deleted if they don't
contain read sets, and reference stores can only be deleted if they don't contain references. Deleting a
sequence or reference store also deletes any tags associated with that store.

The following example shows how to delete a reference store by using the AWS CLI. If
the action is successful, you won't receive a response. In the following example,
replace `reference store ID` with your reference store
ID.

```
aws omics delete-reference-store --id ``reference store ID``
```

The following example shows you how to delete a sequence store. You don't receive a response if the
action succeeds. In the following example, replace `sequence store ID`
with your sequence store ID.

```
aws omics delete-sequence-store --id ``sequence store ID``
```

You can also delete a reference in a reference store as shown in the following
example. References can only be deleted if they aren't being used in a read set,
variant store, or annotation store. In the following example, replace
`reference store ID` with your reference store ID, and
replace `reference ID` with the ID for the reference you
want to delete.

```
aws omics delete-reference  --id ``reference ID`` --reference-store-id ``reference store ID``
```
