

# Node lifecycle action examples for AWS PCS
<a name="cng-node-lifecycle-actions-examples"></a>

The following examples use the AWS CLI to configure node lifecycle actions. You can define lifecycle actions when you create a compute node group with `create-compute-node-group`, or add or change them on an existing compute node group with `update-compute-node-group`. The `--node-lifecycle-actions` value is the same for both commands.

## Multiple scripts across stages
<a name="cng-node-lifecycle-actions-examples-multiple"></a>

This example combines scripts across both lifecycle stages with different execution policies and error behaviors.

```
aws pcs create-compute-node-group --region {{region}} \
  --cluster-identifier {{my-cluster}} \
  --compute-node-group-identifier {{my-cng}} \
  --subnet-ids {{subnet-ExampleID1}} \
  --custom-launch-template id={{lt-ExampleID1}},version='{{1}}' \
  --iam-instance-profile-arn={{arn:InstanceProfile}} \
  --scaling-config minInstanceCount={{0}},maxInstanceCount={{10}} \
  --instance-configs instanceType={{t3.large}} \
  --node-lifecycle-actions '{
    "stages": {
      "nodeBootstrapped": [
        { "name": "Mount FSx Lustre", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/mount-fsx.sh" }, "arguments": ["fs-{{0abc123}}", "/scratch"], "executionPolicy": "EVERY_BOOT" },
        { "name": "Join Active Directory", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/configure-ad.sh" }, "arguments": ["ad.example.com", "EXAMPLE"], "executionPolicy": "FIRST_BOOT_ONLY" }
      ],
      "nodeReady": [
        { "name": "Configure CloudWatch logging", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/setup-cloudwatch.sh" }, "arguments": ["/aws/pcs/{{my-cluster}}"], "onError": "CONTINUE" }
      ]
    }
  }'
```

## Mixed error behavior
<a name="cng-node-lifecycle-actions-examples-mixed-error"></a>

This example uses critical and optional scripts in the same stage. The first terminates the node on failure; the second continues.

```
aws pcs create-compute-node-group --region {{region}} \
  --cluster-identifier {{my-cluster}} \
  --compute-node-group-identifier {{my-cng}} \
  --subnet-ids {{subnet-ExampleID1}} \
  --custom-launch-template id={{lt-ExampleID1}},version='{{1}}' \
  --iam-instance-profile-arn={{arn:InstanceProfile}} \
  --scaling-config minInstanceCount={{0}},maxInstanceCount={{10}} \
  --instance-configs instanceType={{t3.large}} \
  --node-lifecycle-actions '{
    "stages": {
      "nodeBootstrapped": [
        { "name": "Install required packages", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/install-packages.sh" }, "onError": "TERMINATE" },
        { "name": "Install optional tools", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/install-optional.sh" }, "onError": "CONTINUE" }
      ]
    }
  }'
```

## Integrity validation with a checksum
<a name="cng-node-lifecycle-actions-examples-checksum"></a>

Adds a SHA-256 checksum so the agent rejects a script if its content does not match.

```
aws pcs update-compute-node-group \
  --cluster-identifier {{my-cluster}} \
  --compute-node-group-identifier {{my-cng}} \
  --node-lifecycle-actions '{
    "stages": {
      "nodeBootstrapped": [
        {
          "name": "Mount EFS",
          "scriptSource": {
            "scriptLocation": "s3://{{my-bucket}}/mount-efs.sh",
            "checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
          },
          "arguments": ["fs-{{12345678}}", "/shared"]
        }
      ]
    }
  }'
```

## Enable script refresh on reboot
<a name="cng-node-lifecycle-actions-examples-refresh"></a>

Sets `scriptCachingPolicy` to `REFRESH_ON_REBOOT`. This `UpdateComputeNodeGroup` call is a configuration change, so it drains and replaces existing instances. After the replacement completes, instances re-download scripts on each reboot. You can then update script content in Amazon S3 and instances pick up the change on their next reboot with no further API call.

```
aws pcs update-compute-node-group \
  --cluster-identifier {{my-cluster}} \
  --compute-node-group-identifier {{my-cng}} \
  --node-lifecycle-actions '{
    "stages": { "nodeBootstrapped": [ { "name": "Mount EFS", "scriptSource": { "scriptLocation": "s3://{{my-bucket}}/mount-efs.sh" }, "arguments": ["fs-{{12345678}}", "/shared"], "executionPolicy": "EVERY_BOOT" } ] },
    "scriptCachingPolicy": "REFRESH_ON_REBOOT"
  }'
```

## Migrating from AWS ParallelCluster bootstrap actions
<a name="cng-node-lifecycle-actions-examples-migrate"></a>

Many existing AWS ParallelCluster bootstrap scripts work as-is with AWS PCS lifecycle actions. AWS PCS provides per-script error handling (`TERMINATE`, `STOP_SEQUENCE`, or `CONTINUE`) and reboot control (`FIRST_BOOT_ONLY` or `EVERY_BOOT`). The AWS PCS default is `FIRST_BOOT_ONLY`. To match ParallelCluster behavior (run on every boot), set `executionPolicy` to `EVERY_BOOT`.


| **AWS ParallelCluster** | **AWS PCS** | 
| --- | --- | 
| `OnNodeStart` | `nodeBootstrapped` (runs after the AWS PCS configuration phase, before `slurmd`) | 
| `OnNodeConfigured` | `nodeReady` (runs after the node registers with the Slurm controller) | 
| `OnNodeUpdated` | No AWS PCS equivalent | 