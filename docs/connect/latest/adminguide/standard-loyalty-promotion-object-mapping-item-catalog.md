# Object

type mapping for Item Catalog

| Field                 | Type                | Description                                      |
| --------------------- | ------------------- | ------------------------------------------------ |
| Id                    | String              | Unique Identifier for the Item in the Catalog.   |
| Name                  | String              | Name of the Item                                 |
| Code                  | String              | Catalog item's code                              |
| Type                  | String              | Catalog item's type                              |
| Category              | String              | Category of the item in the Catalog              |
| Description           | String              | Item description                                 |
| AdditionalInformation | String              | Any additional information relevant to the item. |
| ImageLink             | String              | Link to the image of the Item                    |
| Link                  | String              | Item URL                                         |
| Price                 | String              | Price of the Item                                |
| CreatedAt             | Long                | Epoch timestamp for which the Item was created   |
| UpdatedAt             | Long                | Epoch timestamp for which the Item was updated   |
| Attributes            | Map<String, String> | Additional Item Attributes                       |

###### Note

You can only delete domain object type via APIs. You can delete item
catalog integration after all recommenders have been deleted first. This
prevents data dependency issues.

**Steps to delete:**

1. Delete all existing recommenders in your domain

2. Navigate to the item catalog integration.

3. Select the delete option.
