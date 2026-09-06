

# `pcluster describe-cluster`
<a name="pcluster.describe-cluster-v3"></a>

Get detailed information about a cluster.

```
pcluster describe-cluster [-h] 
                 --cluster-name {{CLUSTER_NAME}}
                [--debug]
                [--query {{QUERY}}]
                [--region {{REGION}}]
```

## Named arguments
<a name="pcluster-v3.describe-cluster.namedargs"></a>

**-h, --help**  
Shows the help text for `pcluster describe-cluster`.

**--cluster-name, -n {{CLUSTER\_NAME}}**  
Specifies the name of the cluster.

**--debug**  
Enables debug logging.

**--query {{QUERY}}**  
Specifies the JMESPath query to perform on the output.

**--region, -r {{REGION}}**  
Specifies the AWS Region to use. The AWS Region must be specified, using the `AWS_DEFAULT_REGION` environment variable, the `region` setting in the `[default]` section of the `~/.aws/config` file, or the `--region` parameter.

**Examples using AWS ParallelCluster version 3.1.4:**

Describe cluster details:

```
$ pcluster describe-cluster -n {{cluster-v3}}
{
  "creationTime": "2022-07-12T17:19:16.101Z",
  "headNode": {
    "launchTime": "2022-07-12T17:22:21.000Z",
    "instanceId": "i-1234567890abcdef0",
    "publicIpAddress": "198.51.100.44",
    "instanceType": "t2.micro",
    "state": "running",
    "privateIpAddress": "192.0.2.0.196"
  },
  "loginNodes": [
      {
          "status": "active",
          "poolName": "pool1",
          "address": "cluster-v3-eMr9BYRKZVDa-e5bb34f40b24f51d.elb.us-east-1.amazonaws.com",
          "scheme": "internet-facing",
          "healthyNodes": 1,
          "unhealthyNodes": 0
      },
      {
          "status": "active",
          "poolName": "pool2",
          "address": "cluster-v3-PaQ7GgC27sic-aba10c890247b36b.elb.us-east-1.amazonaws.com",
          "scheme": "internet-facing",
          "healthyNodes": 1,
          "unhealthyNodes": 0
      }
  ],
  "version": "3.1.4",
  "clusterConfiguration": {
    "url": "https://parallelcluster-e5ca74255d6c3886-v1-do-not-delete..."
  },
  "tags": [
    {
      "value": "3.11",
      "key": "parallelcluster:version"
    }
  ],
  "cloudFormationStackStatus": "CREATE_COMPLETE",
  "clusterName": "cluster-v3",
  "computeFleetStatus": "RUNNING",
  "cloudformationStackArn": "arn:aws:cloudformation:us-east-1:123456789012:stack/cluster-v3/1234abcd-56ef-78gh-90ij-abcd1234efgh",
  "lastUpdatedTime": "2022-07-12T17:19:16.101Z",
  "region": "us-east-1",
  "clusterStatus": "CREATE_COMPLETE"
}
```

Use `describe-cluster` to retrieve the cluster configuration:

```
$ curl -o - $(pcluster describe-cluster -n {{cluster-v3}} --query clusterConfiguration.url | xargs echo)
Region: us-east-1
Image:
  Os: alinux2023
HeadNode:
  InstanceType: t2.micro
  Networking:
    SubnetId: subnet-abcdef01234567890
  Ssh:
    KeyName: adpc
  Iam:
    S3Access:
      - BucketName: cluster-v3-bucket
        KeyName: logs
        EnableWriteAccess: true
Scheduling:
  Scheduler: slurm
  SlurmQueues:
  - Name: queue1
    ComputeResources:
    - Name: t2micro
      InstanceType: t2.micro
      MinCount: 0
      MaxCount: 10
    Networking:
      SubnetIds:
      - subnet-021345abcdef6789
```