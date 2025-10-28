# Stop or terminate your Amazon EC2 Mac instance

When you stop a Mac instance, the instance remains in the `stopping` state
for about 15 minutes before it enters the `stopped` state.

When you stop or terminate a Mac instance, Amazon EC2 performs a scrubbing workflow on
the underlying Dedicated Host to erase the internal SSD, to clear the persistent NVRAM variables,
and to update to the latest device firmware. This ensures that Mac instances provide the
same security and data privacy as other EC2 Nitro instances. It also allows you to run
the latest macOS AMIs. During the scrubbing workflow, the Dedicated Host temporarily
enters the pending state. On x86 Mac instances, the scrubbing workflow might take up to
50 minutes to complete. On Apple silicon Mac instances, the scrubbing workflow might
take up to 110 minutes to complete. Additionally, on x86 Mac instances, if the device
firmware needs to be updated, the scrubbing workflow might take up to 3 hours to
complete.

You can't start the stopped Mac instance or launch a new Mac instance until after the
scrubbing workflow completes, at which point the Dedicated Host enters the `available`
state.

Metering and billing is paused when the Dedicated Host enters the `pending`
state. You are not charged for the duration of the scrubbing workflow.

## Release the Dedicated Host for your Mac instance

When you are finished with your Mac instance, you can release the Dedicated Host. Before
you can release the Dedicated Host, you must stop or terminate the Mac instance. You cannot
release the host until the allocation period exceeds the 24-hour minimum.

###### To release the Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance and choose **Instance state**, then
   choose either **Stop instance** or **Terminate
   instance**.
4. In the navigation pane, choose **Dedicated Hosts**.
5. Select the Dedicated Host and choose **Actions**, **Release host**.
6. When prompted for confirmation, choose **Release**.
