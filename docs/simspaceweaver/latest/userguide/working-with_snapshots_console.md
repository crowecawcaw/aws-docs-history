End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Use the SimSpace Weaver console to work with snapshots

You can use the SimSpace Weaver console to create a snapshot of your simulation.

###### Topics

- [Create a snapshot](#working-with_snapshots_console_create "#working-with_snapshots_console_create")
- [Start a simulation from a snapshot](#working-with_snapshots_console_start "#working-with_snapshots_console_start")

## Use the console to create a snapshot

###### To create a snapshot

1. Sign to the AWS Management Console and connect to the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver").
2. Choose **Simulations** from the navigation pane.
3. Select the radio button next to simulation name.
   Your simulation's **Status** must be **Started**.
4. At the top of the page, choose **Create snapshot**.
5. Under **Snapshot settings**, for
   **Snapshot destination**, enter the Amazon S3 URI of a bucket or a
   bucket and folder where you want SimSpace Weaver to create your snapshot. You can
   choose **Browse S3** if you prefer to browse your available
   buckets and select a location.

###### Important

The Amazon S3 bucket must be in the same
AWS Region as the simulation.

###### Note

SimSpace Weaver creates a `snapshot` folder inside your selected
snapshot destination. SimSpace Weaver creates the snapshot .zip file in that
`snapshot` folder. 6. Choose **Create snapshot**.

## Use the console to start a simulation from a snapshot

To start a simulation from a snapshot, your snapshot .zip file must exist
in an Amazon S3 bucket that your simulation can access. Your simulation uses
permissions defined in the app role that you select when you start the
simulation. All of the app .zip files from the original simulation must
exist at their same locations as when the snapshot was created.

###### To start a simulation from a snapshot

1. Sign to the AWS Management Console and connect to the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver").
2. Choose **Simulations** from the navigation pane.
3. At the top of the page, choose **Start simulation**.
4. Under **Simulation settings**, enter a name and optional
   description for your simulation. Your simulation name must be unique in your AWS account.
5. For **Simulation start method**, choose
   **Use a snapshot in Amazon S3**.
6. For **Amazon S3 URI for snapshot**, enter the Amazon S3 URI of your
   snapshot file, or choose **Browse S3** to browse and select the file.

###### Important

The Amazon S3 bucket must be in the same
AWS Region as the simulation. 7. For **IAM role**, select the app role that your simulation
will use. 8. For **Maximum duration**, enter the maximum amount of time
that your simulation resource should run for. The maximum value is
`14D`. For more information about
the maximum duration, see [.](../APIReference/API_StartSimulation.md "../APIReference/API_StartSimulation.md") 9. Under **Tags - _optional_**, choose
**Add new tag** if you want to add a tag. 10. Choose **Start simulation**.
