

# Moving your data to a new gateway instance
<a name="migrate-data"></a>

**Note**  
If you are performing a Storage Gateway AL2 to AL2023 migration, before you begin, ensure you have completed all items in the **Pre-migration Checklist** in [Storage Gateway AL2 to AL2023 Migration Campaign](https://docs.aws.amazon.com/storagegateway/latest/vgw/al2-to-al2023-migration.html) .

You can move data between gateways as your data and performance needs grow, or if you receive an AWS notification to migrate your gateway. The following are some reasons for doing this:
+ Move your data to better host platforms or newer Amazon EC2 instances.
+ Refresh the underlying hardware for your server.

**Important**  
Data can only be moved between the same gateway types.  
The following migration instructions can only be used for gateway appliances running version 2.x. You can't use them to migrate gateway appliances running lower versions.

The migration process differs depending on whether you use stored volumes or cached volumes. These two gateway types require different migration steps. Choose the procedure that matches your gateway type:

**Topics**
+ [Moving stored volumes to a new stored Volume Gateway](migrate-data-volume-stored.md)
+ [Moving cached volumes to a new gateway virtual machine](migrate-data-volume-cached.md)