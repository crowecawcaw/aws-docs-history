

# `pcluster update-cluster`
<a name="pcluster.update-cluster-v3"></a>

Updates an existing cluster to match the settings of a specified configuration file.

**Note**  
 The cluster update succeeds only if all cluster nodes have successfully applied the update. If the update fails, refer to the [`clusterStatus` is `UPDATE_FAILED`](troubleshooting-fc-v3-update-cluster.md#update-cluster-failure-v3) section for troubleshooting guidance. 

```
pcluster update-cluster [-h] 
                 --cluster-configuration {{CLUSTER_CONFIGURATION}}
                 --cluster-name {{CLUSTER_NAME}}
                [--debug]
                [--dryrun {{DRYRUN}}]
                [--force-update {{FORCE_UPDATE}}]
                [--query {{QUERY}}]
                [--region {{REGION}}]
                [--suppress-validators {{SUPPRESS_VALIDATORS}} [{{SUPPRESS_VALIDATORS}} ...]]
                [--validation-failure-level {INFO,WARNING,ERROR}]
```

## Named arguments
<a name="pcluster-v3.update-cluster.namedargs"></a>

**-h, --help**  
Shows the help text for `pcluster update-cluster`.

**--cluster-configuration, -c {{CLUSTER\_CONFIGURATION}}**  
Specifies the YAML cluster configuration file.

**--cluster-name, -n {{CLUSTER\_NAME}}**  
Specifies the name of the cluster.

**--debug**  
Enables debug logging.

**--dryrun {{DRYRUN}}**  
When `true`, performs the validation without updating the cluster and creating any resources. It can be used to validate the image configuration and update requirements. (Defaults to `false`.)

**--force-update {{FORCE\_UPDATE}}**  
When `true`, forces the update by ignoring the update validation errors. (Defaults to `false`.)

**--query {{QUERY}}**  
Specifies the JMESPath query to perform on the output.

**--region, -r {{REGION}}**  
Specifies the AWS Region to use. The AWS Region must be specified, using the [`Region`](cluster-configuration-file-v3.md#yaml-Region) setting in the cluster configuration file, the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

**--suppress-validators {{ SUPPRESS\_VALIDATORS}} [{{SUPPRESS\_VALIDATORS ...}}]**  
Identifies one or more config validators to suppress.  
Format: (`ALL`\|`type:[A-Za-z0-9]+`)

**--validation-failure-level {{{INFO,WARNING,ERROR}}}**  
Specifies the level of validation failures reported for update.

**Example using AWS ParallelCluster version 3.1.4:**

```
$ pcluster update-cluster -c {{cluster-config.yaml}} -n {{cluster-v3}} -r {{us-east-1}}
{
  "cluster": {
    "clusterName": "cluster-v3",
    "cloudformationStackStatus": "UPDATE_IN_PROGRESS",
    "cloudformationStackArn": "arn:aws:cloudformation:us-east-1:123456789012:stack/cluster-v3/1234abcd-56ef-78gh-90ij-abcd1234efgh",
    "region": "us-east-1",
    "version": "3.1.4",
    "clusterStatus": "UPDATE_IN_PROGRESS"
  },
  "changeSet": [
    {
      "parameter": "HeadNode.Iam.S3Access",
      "requestedValue": {
        "BucketName": "amzn-s3-demo-bucket1",
        "KeyName": "output",
        "EnableWriteAccess": false
      }
    },
    {
      "parameter": "HeadNode.Iam.S3Access",
      "currentValue": {
        "BucketName": "amzn-s3-demo-bucket2",
        "KeyName": "logs",
        "EnableWriteAccess": true
      }
    }
  ]
}
```