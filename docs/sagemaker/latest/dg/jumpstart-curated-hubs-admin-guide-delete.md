# Delete a private hub

You can delete a private hub from your admin account. Before deleting a private
hub, you must first remove any content in that hub. Delete hub contents and hubs
with the following commands:

```
# List the model references in the private hub
response = hub.list_models()
models = response["hub_content_summaries"]
while response["next_token"]:
    response = hub.list_models(next_token=response["next_token"])
    models.extend(response["hub_content_summaries"])

# Delete all model references in the hub
for model in models:
    hub.delete_model_reference(model_name=model.get('HubContentName'))

# Delete the private hub
hub.delete()
```
