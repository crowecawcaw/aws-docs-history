AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Listing tags for a resource

Follow these steps to use the AWS CLI to view a list of the AWS tags for an HealthOmics
resource. If no tags have been added, the returned list is empty.

At the terminal or command line, run the list-tags-for-resource command as shown in
the following example.

```
aws omics list-tags-for-resource --resource-arn arn:aws:omics:us-west-2:555555555555:sequenceStore/2275234794
```

You will receive a list of tags in response, in JSON format.

```
 {
    "tags": {
        "key1": "value1",
        "key2": "value2"
    }
}
```
