# Example cluster with custom

bootstrap actions

The following steps create a simple script to be executed after the node is configured,
that installs the `R,` `curl` and `wget` packages in the
nodes of the cluster.

1. Create a script.

```
#!/bin/bash
  echo "The script has $# arguments"
  for arg in "$@"
  do
      echo "arg: ${arg}"
  done
  yum -y install "${@:1}"
```

2. Upload the script with the correct permissions to Amazon S3. If
   public read permissions aren't appropriate for you,
   use [HeadNode](HeadNode-v3.md "HeadNode-v3.md") /
   [Iam](HeadNode-v3.md#HeadNode-v3-Iam "HeadNode-v3.md#HeadNode-v3-Iam") /
   [S3Access](HeadNode-v3.md#yaml-HeadNode-Iam-S3Access "HeadNode-v3.md#yaml-HeadNode-Iam-S3Access") and
   [Scheduling](Scheduling-v3.md "Scheduling-v3.md") /
   [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues")
   configuration sections. For more information, see [Working with Amazon S3](s3_resources-v3.md "s3_resources-v3.md").

```
`$` `aws s3 cp --acl public-read `/path/to/myscript.sh` s3://`amzn-s3-demo-bucket`/`myscript.sh``
```

###### Important

If the script was edited on Windows, line endings must be changed from CRLF to
LF before the script is uploaded to Amazon S3. 3. Update the AWS ParallelCluster configuration to include the new `OnNodeConfigured`
action.

```
CustomActions:
  OnNodeConfigured:
    Script: https://`<amzn-s3-demo-bucket>`.s3.`<region>`.amazonaws.com/`myscript.sh`
    Args:
      - "R"
      - "curl"
      - "wget"
```

If the bucket doesn't have public-read permission, use `s3` as the URL protocol.

```
CustomActions:
  OnNodeConfigured:
    Script: s3://`amzn-s3-demo-bucket`/`myscript.sh`
    Args:
      - "R"
      - "curl"
      - "wget"
```

4. Launch the cluster.

```
`$` `pcluster create-cluster --cluster-name `mycluster` \
 --region `<region>` --cluster-configuration `config-file.yaml``
```

5.  Verify the output.

        * If you added custom actions to the `HeadNode` configuration, log
         in to the head node and check the `cfn-init.log` file located
         at `/var/log/cfn-init.log` by running the following command:



        ```
        $ less /var/log/cfn-init.log
          2021-09-03 10:43:54,588 [DEBUG] Command run
          postinstall output: The script has 3 arguments
          arg: R
          arg: curl
          arg: wget
          Loaded plugins: dkms-build-requires, priorities, update-motd, upgrade-helper
          Package R-3.4.1-1.52.amzn1.x86_64 already installed and latest version
          Package curl-7.61.1-7.91.amzn1.x86_64 already installed and latest version
          Package wget-1.18-4.29.amzn1.x86_64 already installed and latest version
          Nothing to do
        ```
        * If you added custom actions to the `SlurmQueues` setting, check the
         `cloud-init.log` located at `/var/log/cloud-init.log`
         in a compute node. Use CloudWatch to view these logs.

    You can view both of these logs in the Amazon CloudWatch console. For more information, see
    [Integration with Amazon CloudWatch Logs](cloudwatch-logs-v3.md "cloudwatch-logs-v3.md").
