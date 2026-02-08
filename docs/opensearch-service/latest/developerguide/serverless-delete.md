# Deleting collections

Deleting a collection deletes all data and indexes in the collection. You can't
recover collections after you delete them.

###### To delete a collection using the console

1. From the **Collections** panel of the Amazon OpenSearch Service console,
   select the collection you want to delete.
2. Choose **Delete** and confirm deletion.
   To delete a collection using the AWS CLI, send a [DeleteCollection](../ServerlessAPIReference/API_DeleteCollection.md "../ServerlessAPIReference/API_DeleteCollection.md") request:

```
&aws opensearchserverless delete-collection --id `07tjusf2h91cunochc`
```

**Sample response**

```
{
   "deleteCollectionDetail":{
      "id":"07tjusf2h91cunochc",
      "name":"my-collection",
      "status":"DELETING"
   }
}
```
