# Additional Volume Mappings

As an additional configuration option, when dealing with volume mappings, it’s possible to configure extra mappings
when the nodegroup is created.

To do this, set the field `additionalVolumes` as follows:

```
 apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: dev-cluster
  region: eu-north-1

managedNodeGroups:
  - name: ng-1-workers
    labels: { role: workers }
    instanceType: m5.xlarge
    desiredCapacity: 10
    volumeSize: 80
    additionalVolumes:
      - volumeName: '/tmp/mount-1' # required
        volumeSize: 80
        volumeType: 'gp3'
        volumeEncrypted: true
        volumeKmsKeyID: 'id'
        volumeIOPS: 3000
        volumeThroughput: 125
      - volumeName: '/tmp/mount-2'  # required
        volumeSize: 80
        volumeType: 'gp2'
        snapshotID: 'snapshot-id'
```

For more details about selecting volumeNames, see the [device naming documentation](../../../AWSEC2/latest/UserGuide/device_naming.md "../../../AWSEC2/latest/UserGuide/device_naming.md").
To find out more about EBS volumes, Instance volume limits or Block device mappings visit [this page](../../../AWSEC2/latest/UserGuide/Storage.md "../../../AWSEC2/latest/UserGuide/Storage.md").
