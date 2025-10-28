End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Use the AWS CLI to work with snapshots

You can use the AWS CLI to call the SimSpace Weaver APIs from a command prompt.
You must have the AWS CLI installed and configured properly. For more information,
see [Installing
or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide for
Version 2_.

###### Topics

- [Create a snapshot](#working-with_snapshots_cli_create "#working-with_snapshots_cli_create")
- [Start a simulation from a snapshot](#working-with_snapshots_cli_start "#working-with_snapshots_cli_start")

## Use the AWS CLI to create a snapshot

###### To create a snapshot

- At a **command prompt**, call the
  `CreateSnapshot` API.

```
aws simspaceweaver create-snapshot --simulation `simulation-name` —destination `s3-destination`
```

**Parameters**

simulation
The name of a started simulation. You can use `aws simspaceweaver list-simulations`
to see the names and statuses of your simulations.

destination
A string that specifies the destination Amazon S3 bucket
and optional object key prefix for your snapshot file. Your object
key prefix is usually a folder in your bucket. SimSpace Weaver creates
your snapshot inside a `snapshot` folder at this destination.

###### Important

The Amazon S3 bucket must be in the same
AWS Region as the simulation.

**Example**

```
aws simspaceweaver create-snapshot —simulation MyProjectSimulation_23-04-29_12_00_00 —destination BucketName=weaver-myproject-111122223333-artifacts-us-west-2,ObjectKeyPrefix=myFolder
```

For more information about the `CreateSnapshot` API,
see [CreateSnapshot](../APIReference/API_CreateSnapshot.md "../APIReference/API_CreateSnapshot.md")
in the _AWS SimSpace Weaver API Reference_.

## Use the AWS CLI to start a simulation from a snapshot

###### To start a simulation from a snapshot

- At a **command prompt**, call the
  `StartSimulation` API.

```
aws simspaceweaver start-simulation --name `simulation-name` --role-arn `role-arn` --snapshot-s3-location `s3-location`
```

**Parameters**

name
The name of the new simulation. The simulation name must
be unique in your AWS account. You can use
`aws simspaceweaver list-simulations`
to see the names of your existing simulations.

role-arn
The Amazon Resource Name (ARN) of the app role
that your simulation will use.

snapshot-s3-location
A string that specifies the Amazon S3 bucket
and object key of your snapshot file.

###### Important

The Amazon S3 bucket must be in the same
AWS Region as the simulation.

**Example**

```
aws simspaceweaver start-simulation —name MySimulation —role-arn arn:aws:iam::111122223333:role/weaver-MyProject-app-role —snapshot-s3-location BucketName=weaver-myproject-111122223333-artifacts-us-west-2,ObjectKey=myFolder/snapshot/MyProjectSimulation_23-04-29_12_00_00-230429-1530-27.zip
```

For more information about the `StartSimulation` API, see
[StartSimulation](../APIReference/API_StartSimulation.md "../APIReference/API_StartSimulation.md")
in the _AWS SimSpace Weaver API Reference_.
