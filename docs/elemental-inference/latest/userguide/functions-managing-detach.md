

# Stopping and deleting a function
<a name="functions-managing-detach"></a>

To stop a function without deleting it, either set the function output's `status` to `DISABLED`, or remove the output from the feed with `update-feed`. Both stop the runs and the model charges. Metadata that has already been written stays readable until it ages out.

To delete the function itself, first remove its function output from every feed that references it, then call `delete-function`. A disabled function output still references the function.

```
aws elemental-inference delete-function \
  --region {{us-west-2}} \
  --id {{function-id}}
```

A delete request for a function that a feed still references fails with `ConflictException`, and the message reports how many feeds hold it.

In the console, **Rename** and **Delete** are unavailable while a function is referenced, and the tooltip explains why.