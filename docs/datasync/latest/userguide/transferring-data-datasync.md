# Transferring your data with

AWS DataSync

With AWS DataSync, you can transfer data to or from storage that's on-premises, in AWS, or in
other clouds.

Setting up a DataSync transfer generally involves the following steps:

1. Determine if DataSync [supports your
   transfer](working-with-locations.md "working-with-locations.md").
2. If [you need a DataSync agent](do-i-need-datasync-agent.md "do-i-need-datasync-agent.md") for your
   transfer, deploy and activate an agent as close as possible to one of your storage
   systems.

For example, if you're transferring from an on-premises Network File System (NFS)
file server, deploy the agent as close as you can to that file server. 3. Provide DataSync access to your storage system.

DataSync needs permission to read from or write to your storage (depending on whether
your storage is a source or destination location). For example, learn how to [provide DataSync access to NFS file servers](create-nfs-location.md#accessing-nfs "create-nfs-location.md#accessing-nfs"). 4. [Connect your network](networking-datasync.md "networking-datasync.md") for traffic
between your storage system and DataSync. 5. Create a location for your source storage system by using the DataSync console,
AWS CLI, or DataSync API.

For example, learn how to [create an NFS
location](create-nfs-location.md#create-nfs-location-how-to "create-nfs-location.md#create-nfs-location-how-to") or [Amazon S3
location](create-s3-location.md#create-s3-location-how-to "create-s3-location.md#create-s3-location-how-to"). 6. Repeat steps 3-5 to create your transfer's destination location. 7. [Create and start a DataSync transfer task](create-task-how-to.md "create-task-how-to.md")
that includes your source and destination locations.

###### Topics

- [Where can I transfer my data with
  AWS DataSync?](working-with-locations.md "working-with-locations.md")
- [Transferring to or from on-premises
  storage with AWS DataSync](transferring-on-premises-storage.md "transferring-on-premises-storage.md")
- [Transferring to or from AWS storage with
  AWS DataSync](transferring-aws-storage.md "transferring-aws-storage.md")
- [Transferring to or from other cloud
  storage with AWS DataSync](transferring-other-cloud-storage.md "transferring-other-cloud-storage.md")
- [Creating a task for transferring your data](create-task-how-to.md "create-task-how-to.md")
- [Starting a task to transfer your data](run-task.md "run-task.md")
