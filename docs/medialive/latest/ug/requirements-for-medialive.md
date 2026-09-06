

# Requirements for AWS Elemental MediaLive features
<a name="requirements-for-medialive"></a>

You must give your users access to AWS Elemental MediaLive features. The permissions for MediaLive can be divided into three categories:
+ Permissions to create
+ Permissions to view
+ Permissions to run

You might choose to give different access to different kinds of users. For example, you might decide that "basic operators" should not have create permissions. 

In particular, you must decide whether to restrict the ability to work with reservations; you might decide to give this access only to administrators or advanced users. For more information about reservations, see [Working with reservations in MediaLive](reservations.md).

The following table shows the operations in IAM that relate to access for MediaLive.



- **Create, modify, and delete channels, devices, inputs, and input security groups**
  - **Service name in IAM:** MediaLive
  - **Actions:** CreateChannel`CreateInput`<br />`CreateInputSecurityGroup`<br />`DeleteChannel`<br />`DeleteInput`<br />`DeleteInputSecurityGroup`<br />`UpdateChannel`<br />`UpdateInput`<br />`UpdateInputDevice`<br />`UpdateInputSecurityGroup`

- **View channels, devices, inputs, and input security groups**
  - **Service name in IAM:** MediaLive
  - **Actions:** `ListChannels`<br />`ListInputDevices`<br />`ListInputs`<br />`ListInputSecurityGroups`<br />`DescribeChannel`<br />`DescribeInput`<br />`DescribeInputDevice`<br />`DescribeInputDeviceThumbnail`<br />`DescribeInputSecurityGroup`

- **View alerts for channels and multiplexes, when they are running, and for AWS Elemental MediaLive Anywhere clusters.**
  - **Service name in IAM:** MediaLive
  - **Actions:** ListAlerts`ListClusterAlerts`<br />`ListMultiplexAlerts`

- **Perform a batch operation on several channels or inputs or multiplexes or input security groups**
  - **Service name in IAM:** MediaLive
  - **Actions:** `BatchDelete`<br />`BatchStart`<br />`BatchStop`

- **Create or cancel an outgoing device transfer, or accept or reject an incoming device transfer, and view pending device transfers**
  - **Service name in IAM:** MediaLive
  - **Actions:** `AcceptInputDeviceTransfer`<br />`CancelInputDeviceTransfer`<br />`ListInputDeviceTransfers`<br />`RejectInputDeviceTransfer`<br />`TransferInputDevice`

- **Work with schedules**
  - **Service name in IAM:** MediaLive
  - **Actions:** DescribeSchedule`BatchUpdateSchedule`

- **Create or modify multiplexes**
  - **Service name in IAM:** MediaLive / **Actions:** CreateMultiplex`DescribeMultiplex`<br />`ListMultiplexes`<br />`UpdateMultiplex`
  - **Service name in IAM:** EC2  / **Actions:** DescribeAvailabilityZonesYou need this operation to view the list of Availability Zones on the MediaLive console, so that you can choose two for the multiplex.

- **Delete multiplexes**
  - **Service name in IAM:** MediaLive
  - **Actions:** `DeleteMultiplex`<br />`DescribeMultiplex`<br />`ListMultiplexes`

- **View multiplexes**
  - **Service name in IAM:** MediaLive
  - **Actions:** `DescribeMultiplex`<br />`ListMultiplexes`

- **Change the class for a channel**
  - **Service name in IAM:** MediaLive
  - **Actions:** UpdateChannelClass

- **Run channels**
  - **Service name in IAM:** MediaLive
  - **Actions:** StartChannel`StopChannel`

- **Pause channels**
  - **Service name in IAM:** MediaLive
  - **Actions:** Pause is part of the schedule feature, above.

- **Run multiplexes**
  - **Service name in IAM:** MediaLive
  - **Actions:** StartMultiplex`StopMultiplex`

- **Attach tags to channels, inputs, and input security groups when creating those resources**
  - **Service name in IAM:** MediaLive
  - **Actions:** CreateTag`DeleteTags`<br />`ListTagsForResources`

- **Create, modify, delete, and view reservations and offerings**
  - **Service name in IAM:** MediaLive
  - **Actions:** `DeleteReservation`<br />`DescribeOffering`<br />`DescribeReservation`<br />`ListOfferings`<br />`ListReservations`<br />`PurchaseOffering`

