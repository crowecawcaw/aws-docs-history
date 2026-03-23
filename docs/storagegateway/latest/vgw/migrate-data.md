# Moving your data to a new gateway instance

You can move data between gateways as your data and performance needs grow, or if you
receive an AWS notification to migrate your gateway. The following are some reasons for
doing this:

- Move your data to better host platforms or newer Amazon EC2 instances.
- Refresh the underlying hardware for your server.

###### Important

Data can only be moved between the same gateway types.

The following migration instructions can only be used for gateway appliances running version 2.x. You can't use them
to migrate gateway appliances running lower versions.

The migration process differs depending on whether you use stored
volumes or cached volumes. These two gateway types require different migration
steps. Choose the procedure that matches your gateway type:

###### Topics

- [Moving stored volumes to a new stored Volume Gateway](migrate-data-volume-stored.md "migrate-data-volume-stored.md")
- [Moving cached volumes to a new gateway virtual machine](migrate-data-volume-cached.md "migrate-data-volume-cached.md")
