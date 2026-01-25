**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create self-managed Windows Server 2022 nodes with `eksctl`

You can use the following `test-windows-2022.yaml` as reference for creating self-managed Windows Server 2022 nodes. Replace every `example value` with your own values.

###### Note

You must use `eksctl` version [0.116.0](https://github.com/weaveworks/eksctl/releases/tag/v0.116.0 "https://github.com/weaveworks/eksctl/releases/tag/v0.116.0") or later to run self-managed Windows Server 2022 nodes.

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: windows-2022-cluster
  region: region-code
  version: '1.33'

nodeGroups:
  - name: windows-ng
    instanceType: m5.2xlarge
    amiFamily: WindowsServer2022FullContainer
    volumeSize: 100
    minSize: 2
    maxSize: 3
  - name: linux-ng
    amiFamily: AmazonLinux2
    minSize: 2
    maxSize: 3
```

The node groups can then be created using the following command.

```
eksctl create cluster -f test-windows-2022.yaml
```
