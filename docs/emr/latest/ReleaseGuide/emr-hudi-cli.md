# Use the Hudi CLI

You can use the Hudi CLI to administer Hudi datasets to view information about
commits, the filesystem, statistics, and more. You can also use the CLI to manually
perform compactions, schedule compactions, or cancel scheduled compactions. For more
information, see [Interacting
via CLI](https://hudi.apache.org/docs/cli/ "https://hudi.apache.org/docs/cli/") in the Apache Hudi documentation.

###### To start the Hudi CLI and connect to a dataset

1. Connect to the master node using SSH. For more information, see [Connect to
   the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the
   _Amazon EMR Management Guide_.
2. At the command line, type `/usr/lib/hudi/cli/bin/hudi-cli.sh`.

The command prompt changes to `hudi->`. 3. Use the following command to connect to a dataset. Replace
`s3://amzn-s3-demo-bucket/myhudidataset` with the
path to the dataset that you want to work with. The value we use is the same as
the value established in earlier examples.

```
connect --path `s3://amzn-s3-demo-bucket/myhudidataset`
```

The command prompt changes to include the dataset that you're connected to, as
shown in the following example.

```
hudi:`myhudidataset`->
```

By default, the `hudi-cli.sh` script in Amazon EMR release 7.3.0 to 7.8.0 uses `hudi-cli-bundle.jar`. If you run into issues,
you can switch back to the classic Hudi CLI with the following command:

```
/usr/lib/hudi/cli/bin/hudi-cli.sh --cliBundle false
```

This command runs the `hudi-cli.sh` script, sets the `--cliBundle` flag, and instructs the CLI to use the individual
JAR files instead of the bundled JAR. By default, the `--cliBundle` is set to true, which means the CLI uses the bundled JAR instead.

## Using Amazon EMR 7.9.0 and higher releases

###### Note

The **hudi-cli.sh** script has been deprecated in EMR release 7.9.0 and higher. Amazon EMR release 7.9.0 and higher uses **hudi-cli-bundle.jar**.

**To start the Hudi CLI and connect to a dataset:**

1. Connect to the master node using SSH. For more information,
   see [Connect to the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the _Amazon EMR Management Guide_.
2. At the command line, type **/usr/lib/hudi/cli-bundle/bin/hudi-cli-with-bundle.sh** or simply type **hudi-cli-with-bundle** or **>hudi-cli**.

The command prompt changes to **hudi- >**. 3. Use the following command to connect to a dataset. Replace **s3://amzn-s3-demo-bucket/myhudidataset** with the path to the dataset that
you want to work with. The value we use is the same as the value established in earlier examples.

```
connect --path s3://amzn-s3-demo-bucket/myhudidataset
```

4. The command prompt changes to include the dataset that you're connected to, as shown in the following example.

```
hudi:myhudidataset->
```
