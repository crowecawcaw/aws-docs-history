# Delete models from a private hub

You can delete models from a private hub used by your organization by specifying
the model ARN in the `hub.delete_model_reference()` method. This removes
access to the model from the private hub.

```
hub.delete_model_reference(`model-name`)
```
