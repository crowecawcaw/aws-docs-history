# Setting up Systems Manager

Inventory

Before you use AWS Systems Manager Inventory to collect metadata about the applications,
services, AWS components and more running on your managed nodes, we recommend that you
configure resource data sync to centralize the storage of your inventory data in a
single Amazon Simple Storage Service (Amazon S3) bucket. We also recommend that you configure Amazon EventBridge monitoring
of inventory events. These processes make it easier to view and manage inventory data
and collection.

###### Topics

- [Creating a resource data sync
  for Inventory](inventory-create-resource-data-sync.md "inventory-create-resource-data-sync.md")
- [Using EventBridge to
  monitor Inventory events](systems-manager-inventory-setting-up-eventbridge.md "systems-manager-inventory-setting-up-eventbridge.md")
