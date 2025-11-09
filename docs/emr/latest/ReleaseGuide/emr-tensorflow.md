# TensorFlow

TensorFlow is an open-source symbolic math library for machine intelligence and deep learning applications. For more information, see the [TensorFlow website](https://www.tensorflow.org/ "https://www.tensorflow.org/"). TensorFlow is available with Amazon EMR release version 5.17.0 and later.

The following table lists the version of TensorFlow included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with TensorFlow.

For the version of components installed with TensorFlow in this release, see [Release 7.10.0 Component Versions](emr-7100-release.md "emr-7100-release.md").

| TensorFlow version information for emr-7.10.0 | Amazon EMR Release Label | TensorFlow Version                                                                                                                                                                                                                         | Components Installed With TensorFlow |
| --------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| emr-7.10.0                                    | TensorFlow 2.18.0        | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tensorflow |

The following table lists the version of TensorFlow included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with TensorFlow.

For the version of components installed with TensorFlow in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| TensorFlow version information for emr-6.15.0 | Amazon EMR Release Label | TensorFlow Version                                                                                                                                                                                                                         | Components Installed With TensorFlow |
| --------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| emr-6.15.0                                    | TensorFlow 2.11.0        | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tensorflow |

The following table lists the version of TensorFlow included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with TensorFlow.

For the version of components installed with TensorFlow in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| TensorFlow version information for emr-5.36.2 | Amazon EMR Release Label | TensorFlow Version                                                                                                                                                                                                                         | Components Installed With TensorFlow |
| --------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| emr-5.36.2                                    | TensorFlow 2.4.1         | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tensorflow |

## TensorFlow builds by Amazon EC2 instance type

Amazon EMR uses different builds of the TensorFlow library depending on the instance types that you choose for your cluster. Amazon EMR also supports TensorFlow for clusters with aarch64 instance
types (Graviton instances) from EMR-7.5.0 and above.

The following table lists builds by instance type for EMR-7.10.0:

| EC2 instance types                | TensorFlow build                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P2, P4D, P5, G4DN, G5, G6 and GR6 | Tensorflow 2.18.0 with CUDA 12.5, cuDNN 9.3.0.75                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| P3, P3DN, G3 and G3S              | Tensorflow 2.18.0 with CUDA 12.5, cuDNN 9.3.0.75, NCCL 2.22.3<br>[Nvidia NCCL](https://developer.nvidia.com/nccl "https://developer.nvidia.com/nccl") is available only on P3, P3DN, G3 and G3s instances with<br>version 2.22.3. **End User License Agreement (EULA)**: By using Nvidia components on Amazon EMR, you agree to the terms and conditions outlined in<br>the [product EULA](https://d7umqicpi7263.cloudfront.net/eula/product/d0199cf7-a04a-4204-be4d-dc3e2af678af/5b36dd71-7d6e-4d97-a8f7-013d3eccec70.txt "https://d7umqicpi7263.cloudfront.net/eula/product/d0199cf7-a04a-4204-be4d-dc3e2af678af/5b36dd71-7d6e-4d97-a8f7-013d3eccec70.txt"). |
| Graviton instances                | Tensorflow 2.18.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| All others                        | Tensorflow CPU 2.18.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Security

In addition to following the guidance in [Using TensorFlow securely](https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md "https://github.com/tensorflow/tensorflow/blob/master/SECURITY.md") we recommend that you launch your cluster in a private subnet to help you limit access to trusted sources. For more information, see [Amazon VPC options](../ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-private-subnet "../ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-private-subnet") in the _Amazon EMR Management Guide_.

## Using TensorBoard

TensorBoard is a suite of visualization tools for TensorFlow programs. For more information, see [TensorBoard: Visualized learning](https://www.tensorflow.org/get_started/summaries_and_tensorboard "https://www.tensorflow.org/get_started/summaries_and_tensorboard") on the Tensorflow website.

To use TensorBoard with Amazon EMR, you must start TensorBoard on the cluster master node.

###### To use tensorboard with Tensorflow on Amazon EMR

1. Connect to the master node of the cluster using SSH. For more information, see [Connect to the master node using SSH](../ManagementGuide/emr-connect-master-node-ssh.md "../ManagementGuide/emr-connect-master-node-ssh.md") in the _Amazon EMR Management Guide_.
2. Type the following command to start Tensorboard on the master node. Replace `/my/log/directory` with a directory on the master node where you have generated and stored summary data using a summary writer.

Amazon EMR 5.19.0 and later

```
python3 -m tensorboard.main --logdir=/home/hadoop/tensor --bind_all
```

Amazon EMR 5.18.1 and earlier

```
python3 -m tensorboard.main --logdir=/my/log/dir
```

By default, the master node hosts TensorBoard using port 6006 and the master public DNS name. After you start TensorBoard, the command line output presents the URL that can be used to connect to TensorBoard, as shown in the following example:

```
TensorBoard 2.18.0 at http://`master-public-dns-name`:6006 (Press CTRL+C to quit)
```

3. Set up access to web interfaces on the master node from trusted clients. For more information, see [View web interfaces hosted on Amazon EMR clusters](../ManagementGuide/emr-web-interfaces.md "../ManagementGuide/emr-web-interfaces.md") in the _Amazon EMR Management Guide_.
4. Open TensorBoard at `http://`master-public-dns-name`:6006`.
