# Task configuration

You can set configuration variables to tune the performance of your MapReduce
jobs. This section provides the default values for important settings. Default
values vary based on the EC2 instance type of the node used in the cluster. HBase is
available when using Amazon EMR release version 4.6.0 and later. Different defaults are
used when HBase is installed. Those values are provided along with the initial
defaults.

Hadoop 2 uses two parameters, `mapreduce.map.java.opts` and
`mapreduce.reduce.java.opts`, to configure memory for map and reduce
JVMs respectively. These replace the single `mapreduce.map.java.opts`
configuration option from earlier Hadoop versions.

Similarly, `mapred.job.jvm.num.tasks` replaces
`mapred.job.reuse.jvm.num.tasks` in Hadoop 2.7.2 and later. Amazon EMR
sets this value to 20 regardless of EC2 instance type. You can override this setting
using the `mapred-site` configuration classification. Setting a value of
`-1` indicates that a JVM can be re-used for an infinite number of
tasks within a single job, and a value of `1` indicates that a new JVM is
spawned for each task.

For example, to set the value of `mapred.job.jvm.num.tasks` to -1 you
can create a file with the following contents:

```
[
	{
		"Classification": "mapred-site",
		"Properties": {
			"mapred.job.jvm.num.tasks": "-1"
		}
	}
]

```

When you use the `create-cluster` command or
`modify-instance-groups` command from the AWS CLI, you can then
reference the JSON configuration file. In the following example, the configuration
file is saved as `myConfig.json` and stored in Amazon S3.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --release-label `emr-7.12.0` --instance-type m5.xlarge \
--instance-count 3 --applications Name=Hadoop --configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json \
--use-default-roles

```

You can change default values listed below using the `mapred-site`
configuration classification in the same way, and set multiple values and multiple
configuration classifications using a single JSON file. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

With Amazon EMR version 5.21.0 and later, you can override cluster configurations and specify additional configuration classifications for each instance group in a running cluster. You do this by using the Amazon EMR console, the AWS Command Line Interface (AWS CLI), or the AWS SDK. For more information, see [Supplying a Configuration for an Instance Group in a Running Cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

## Default values for task configuration

settings

###### Note

The values specified for each instance are in accordance with the latest EMR release. Previous releases can have different default settings.

###### Instance Types

- [c1 instances](#emr-hadoop-task-config-c1 "#emr-hadoop-task-config-c1")
- [c3 instances](#emr-hadoop-task-config-c3 "#emr-hadoop-task-config-c3")
- [c4 instances](#emr-hadoop-task-config-c4 "#emr-hadoop-task-config-c4")
- [c5 instances](#emr-hadoop-task-config-c5 "#emr-hadoop-task-config-c5")
- [c5a instances](#emr-hadoop-task-config-c5a "#emr-hadoop-task-config-c5a")
- [c5ad instances](#emr-hadoop-task-config-c5ad "#emr-hadoop-task-config-c5ad")
- [c5d instances](#emr-hadoop-task-config-c5d "#emr-hadoop-task-config-c5d")
- [c5n instances](#emr-hadoop-task-config-c5n "#emr-hadoop-task-config-c5n")
- [c6a instances](#emr-hadoop-task-config-c6a "#emr-hadoop-task-config-c6a")
- [c6g instances](#emr-hadoop-task-config-c6g "#emr-hadoop-task-config-c6g")
- [c6gd instances](#emr-hadoop-task-config-c6gd "#emr-hadoop-task-config-c6gd")
- [c6gn instances](#emr-hadoop-task-config-c6gn "#emr-hadoop-task-config-c6gn")
- [c6i instances](#emr-hadoop-task-config-c6i "#emr-hadoop-task-config-c6i")
- [c6id instances](#emr-hadoop-task-config-c6id "#emr-hadoop-task-config-c6id")
- [c6in instances](#emr-hadoop-task-config-c6in "#emr-hadoop-task-config-c6in")
- [c7a instances](#emr-hadoop-task-config-c7a "#emr-hadoop-task-config-c7a")
- [c7g instances](#emr-hadoop-task-config-c7g "#emr-hadoop-task-config-c7g")
- [c7gd instances](#emr-hadoop-task-config-c7gd "#emr-hadoop-task-config-c7gd")
- [c7gn instances](#emr-hadoop-task-config-c7gn "#emr-hadoop-task-config-c7gn")
- [c7i instances](#emr-hadoop-task-config-c7i "#emr-hadoop-task-config-c7i")
- [c7i-flex instances](#emr-hadoop-task-config-c7i-flex "#emr-hadoop-task-config-c7i-flex")
- [c8g instances](#emr-hadoop-task-config-c8g "#emr-hadoop-task-config-c8g")
- [c8gd instances](#emr-hadoop-task-config-c8gd "#emr-hadoop-task-config-c8gd")
- [d2 instances](#emr-hadoop-task-config-d2 "#emr-hadoop-task-config-d2")
- [d3 instances](#emr-hadoop-task-config-d3 "#emr-hadoop-task-config-d3")
- [d3en instances](#emr-hadoop-task-config-d3en "#emr-hadoop-task-config-d3en")
- [f2 instances](#emr-hadoop-task-config-f2 "#emr-hadoop-task-config-f2")
- [g3 instances](#emr-hadoop-task-config-g3 "#emr-hadoop-task-config-g3")
- [g3s instances](#emr-hadoop-task-config-g3s "#emr-hadoop-task-config-g3s")
- [g4dn instances](#emr-hadoop-task-config-g4dn "#emr-hadoop-task-config-g4dn")
- [g5 instances](#emr-hadoop-task-config-g5 "#emr-hadoop-task-config-g5")
- [g6 instances](#emr-hadoop-task-config-g6 "#emr-hadoop-task-config-g6")
- [g6e instances](#emr-hadoop-task-config-g6e "#emr-hadoop-task-config-g6e")
- [gr6 instances](#emr-hadoop-task-config-gr6 "#emr-hadoop-task-config-gr6")
- [h1 instances](#emr-hadoop-task-config-h1 "#emr-hadoop-task-config-h1")
- [i2 instances](#emr-hadoop-task-config-i2 "#emr-hadoop-task-config-i2")
- [i3 instances](#emr-hadoop-task-config-i3 "#emr-hadoop-task-config-i3")
- [i3en instances](#emr-hadoop-task-config-i3en "#emr-hadoop-task-config-i3en")
- [i4g instances](#emr-hadoop-task-config-i4g "#emr-hadoop-task-config-i4g")
- [i4i instances](#emr-hadoop-task-config-i4i "#emr-hadoop-task-config-i4i")
- [i7i instances](#emr-hadoop-task-config-i7i "#emr-hadoop-task-config-i7i")
- [i7ie instances](#emr-hadoop-task-config-i7ie "#emr-hadoop-task-config-i7ie")
- [i8g instances](#emr-hadoop-task-config-i8g "#emr-hadoop-task-config-i8g")
- [im4gn instances](#emr-hadoop-task-config-im4gn "#emr-hadoop-task-config-im4gn")
- [is4gen instances](#emr-hadoop-task-config-is4gen "#emr-hadoop-task-config-is4gen")
- [m1 instances](#emr-hadoop-task-config-m1 "#emr-hadoop-task-config-m1")
- [m2 instances](#emr-hadoop-task-config-m2 "#emr-hadoop-task-config-m2")
- [m3 instances](#emr-hadoop-task-config-m3 "#emr-hadoop-task-config-m3")
- [m4 instances](#emr-hadoop-task-config-m4 "#emr-hadoop-task-config-m4")
- [m5 instances](#emr-hadoop-task-config-m5 "#emr-hadoop-task-config-m5")
- [m5a instances](#emr-hadoop-task-config-m5a "#emr-hadoop-task-config-m5a")
- [m5ad instances](#emr-hadoop-task-config-m5ad "#emr-hadoop-task-config-m5ad")
- [m5d instances](#emr-hadoop-task-config-m5d "#emr-hadoop-task-config-m5d")
- [m5dn instances](#emr-hadoop-task-config-m5dn "#emr-hadoop-task-config-m5dn")
- [m5n instances](#emr-hadoop-task-config-m5n "#emr-hadoop-task-config-m5n")
- [m5zn instances](#emr-hadoop-task-config-m5zn "#emr-hadoop-task-config-m5zn")
- [m6a instances](#emr-hadoop-task-config-m6a "#emr-hadoop-task-config-m6a")
- [m6g instances](#emr-hadoop-task-config-m6g "#emr-hadoop-task-config-m6g")
- [m6gd instances](#emr-hadoop-task-config-m6gd "#emr-hadoop-task-config-m6gd")
- [m6i instances](#emr-hadoop-task-config-m6i "#emr-hadoop-task-config-m6i")
- [m6id instances](#emr-hadoop-task-config-m6id "#emr-hadoop-task-config-m6id")
- [m6idn instances](#emr-hadoop-task-config-m6idn "#emr-hadoop-task-config-m6idn")
- [m6in instances](#emr-hadoop-task-config-m6in "#emr-hadoop-task-config-m6in")
- [m7a instances](#emr-hadoop-task-config-m7a "#emr-hadoop-task-config-m7a")
- [m7g instances](#emr-hadoop-task-config-m7g "#emr-hadoop-task-config-m7g")
- [m7gd instances](#emr-hadoop-task-config-m7gd "#emr-hadoop-task-config-m7gd")
- [m7i instances](#emr-hadoop-task-config-m7i "#emr-hadoop-task-config-m7i")
- [m7i-flex instances](#emr-hadoop-task-config-m7i-flex "#emr-hadoop-task-config-m7i-flex")
- [m8g instances](#emr-hadoop-task-config-m8g "#emr-hadoop-task-config-m8g")
- [m8gd instances](#emr-hadoop-task-config-m8gd "#emr-hadoop-task-config-m8gd")
- [p2 instances](#emr-hadoop-task-config-p2 "#emr-hadoop-task-config-p2")
- [p3 instances](#emr-hadoop-task-config-p3 "#emr-hadoop-task-config-p3")
- [p4d instances](#emr-hadoop-task-config-p4d "#emr-hadoop-task-config-p4d")
- [p5 instances](#emr-hadoop-task-config-p5 "#emr-hadoop-task-config-p5")
- [r3 instances](#emr-hadoop-task-config-r3 "#emr-hadoop-task-config-r3")
- [r4 instances](#emr-hadoop-task-config-r4 "#emr-hadoop-task-config-r4")
- [r5 instances](#emr-hadoop-task-config-r5 "#emr-hadoop-task-config-r5")
- [r5a instances](#emr-hadoop-task-config-r5a "#emr-hadoop-task-config-r5a")
- [r5ad instances](#emr-hadoop-task-config-r5ad "#emr-hadoop-task-config-r5ad")
- [r5b instances](#emr-hadoop-task-config-r5b "#emr-hadoop-task-config-r5b")
- [r5d instances](#emr-hadoop-task-config-r5d "#emr-hadoop-task-config-r5d")
- [r5dn instances](#emr-hadoop-task-config-r5dn "#emr-hadoop-task-config-r5dn")
- [r5n instances](#emr-hadoop-task-config-r5n "#emr-hadoop-task-config-r5n")
- [r6a instances](#emr-hadoop-task-config-r6a "#emr-hadoop-task-config-r6a")
- [r6g instances](#emr-hadoop-task-config-r6g "#emr-hadoop-task-config-r6g")
- [r6gd instances](#emr-hadoop-task-config-r6gd "#emr-hadoop-task-config-r6gd")
- [r6i instances](#emr-hadoop-task-config-r6i "#emr-hadoop-task-config-r6i")
- [r6id instances](#emr-hadoop-task-config-r6id "#emr-hadoop-task-config-r6id")
- [r6idn instances](#emr-hadoop-task-config-r6idn "#emr-hadoop-task-config-r6idn")
- [r6in instances](#emr-hadoop-task-config-r6in "#emr-hadoop-task-config-r6in")
- [r7a instances](#emr-hadoop-task-config-r7a "#emr-hadoop-task-config-r7a")
- [r7g instances](#emr-hadoop-task-config-r7g "#emr-hadoop-task-config-r7g")
- [r7gd instances](#emr-hadoop-task-config-r7gd "#emr-hadoop-task-config-r7gd")
- [r7i instances](#emr-hadoop-task-config-r7i "#emr-hadoop-task-config-r7i")
- [r7iz instances](#emr-hadoop-task-config-r7iz "#emr-hadoop-task-config-r7iz")
- [r8g instances](#emr-hadoop-task-config-r8g "#emr-hadoop-task-config-r8g")
- [r8gd instances](#emr-hadoop-task-config-r8gd "#emr-hadoop-task-config-r8gd")
- [x1 instances](#emr-hadoop-task-config-x1 "#emr-hadoop-task-config-x1")
- [x1e instances](#emr-hadoop-task-config-x1e "#emr-hadoop-task-config-x1e")
- [x2gd instances](#emr-hadoop-task-config-x2gd "#emr-hadoop-task-config-x2gd")
- [x2idn instances](#emr-hadoop-task-config-x2idn "#emr-hadoop-task-config-x2idn")
- [x2iedn instances](#emr-hadoop-task-config-x2iedn "#emr-hadoop-task-config-x2iedn")
- [x8g instances](#emr-hadoop-task-config-x8g "#emr-hadoop-task-config-x8g")
- [z1d instances](#emr-hadoop-task-config-z1d "#emr-hadoop-task-config-z1d")

### c1 instances

| c1.medium                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx288m             | -Xmx288m      |
| `mapreduce.java.opts`                  | -Xmx288m             | -Xmx288m      |
| `mapreduce.map.memory.mb`              | 512                  | 512           |
| `mapreduce.reduce.memory.mb`           | 512                  | 512           |
| `yarn.app.mapreduce.am.resource.mb`    | 512                  | 512           |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 512                  | 512           |
| `yarn.nodemanager.resource.memory-mb`  | 1024                 | 512           |

| c1.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx864m             | -Xmx864m      |
| `mapreduce.java.opts`                  | -Xmx1536m            | -Xmx1536m     |
| `mapreduce.map.memory.mb`              | 1024                 | 1024          |
| `mapreduce.reduce.memory.mb`           | 2048                 | 2048          |
| `yarn.app.mapreduce.am.resource.mb`    | 2048                 | 2048          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 2048                 | 2560          |
| `yarn.nodemanager.resource.memory-mb`  | 5120                 | 2560          |

### c3 instances

| c3.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11520                | 5760          |
| `yarn.nodemanager.resource.memory-mb`  | 11520                | 5760          |

| c3.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23040                | 11520         |
| `yarn.nodemanager.resource.memory-mb`  | 23040                | 11520         |

| c3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1331m            | -Xmx1331m     |
| `mapreduce.java.opts`                  | -Xmx2662m            | -Xmx2662m     |
| `mapreduce.map.memory.mb`              | 1664                 | 1664          |
| `mapreduce.reduce.memory.mb`           | 3328                 | 3328          |
| `yarn.app.mapreduce.am.resource.mb`    | 3328                 | 3328          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 53248                | 26624         |
| `yarn.nodemanager.resource.memory-mb`  | 53248                | 26624         |

### c4 instances

| c4.large                               | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx717m             | -Xmx717m      |
| `mapreduce.java.opts`                  | -Xmx1434m            | -Xmx1434m     |
| `mapreduce.map.memory.mb`              | 896                  | 896           |
| `mapreduce.reduce.memory.mb`           | 1792                 | 1792          |
| `yarn.app.mapreduce.am.resource.mb`    | 1792                 | 1792          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1792                 | 896           |
| `yarn.nodemanager.resource.memory-mb`  | 1792                 | 896           |

| c4.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c4.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11520                | 5760          |
| `yarn.nodemanager.resource.memory-mb`  | 11520                | 5760          |

| c4.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23040                | 11520         |
| `yarn.nodemanager.resource.memory-mb`  | 23040                | 11520         |

| c4.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1183m            | -Xmx1183m     |
| `mapreduce.java.opts`                  | -Xmx2366m            | -Xmx2366m     |
| `mapreduce.map.memory.mb`              | 1479                 | 1479          |
| `mapreduce.reduce.memory.mb`           | 2958                 | 2958          |
| `yarn.app.mapreduce.am.resource.mb`    | 2958                 | 2958          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 53248                | 26624         |
| `yarn.nodemanager.resource.memory-mb`  | 53248                | 26624         |

### c5 instances

| c5.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 6144                 | 3072          |
| `yarn.nodemanager.resource.memory-mb`  | 6144                 | 3072          |

| c5.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| c5.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| c5.9xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1456m            | -Xmx1456m     |
| `mapreduce.java.opts`                  | -Xmx2912m            | -Xmx2912m     |
| `mapreduce.map.memory.mb`              | 1820                 | 1820          |
| `mapreduce.reduce.memory.mb`           | 3640                 | 3640          |
| `yarn.app.mapreduce.am.resource.mb`    | 3640                 | 3640          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 65536                | 32768         |
| `yarn.nodemanager.resource.memory-mb`  | 65536                | 32768         |

| c5.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1502m            | -Xmx1502m     |
| `mapreduce.java.opts`                  | -Xmx3004m            | -Xmx3004m     |
| `mapreduce.map.memory.mb`              | 1877                 | 1877          |
| `mapreduce.reduce.memory.mb`           | 3754                 | 3754          |
| `yarn.app.mapreduce.am.resource.mb`    | 3754                 | 3754          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30048         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30048         |

| c5.18xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1547m            | -Xmx1547m     |
| `mapreduce.java.opts`                  | -Xmx3094m            | -Xmx3094m     |
| `mapreduce.map.memory.mb`              | 1934                 | 1934          |
| `mapreduce.reduce.memory.mb`           | 3868                 | 3868          |
| `yarn.app.mapreduce.am.resource.mb`    | 3868                 | 3868          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 139264               | 30960         |
| `yarn.nodemanager.resource.memory-mb`  | 139264               | 30960         |

| c5.24xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1570m            | -Xmx1570m     |
| `mapreduce.java.opts`                  | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.map.memory.mb`              | 1963                 | 1963          |
| `mapreduce.reduce.memory.mb`           | 3926                 | 3926          |
| `yarn.app.mapreduce.am.resource.mb`    | 3926                 | 3926          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31376         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31376         |

### c5a instances

| c5a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c5a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c5a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c5a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c5a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1502m            | -Xmx1502m     |
| `mapreduce.java.opts`                  | -Xmx3004m            | -Xmx3004m     |
| `mapreduce.map.memory.mb`              | 1877                 | 1877          |
| `mapreduce.reduce.memory.mb`           | 3754                 | 3754          |
| `yarn.app.mapreduce.am.resource.mb`    | 3754                 | 3754          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30048         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30048         |

| c5a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c5a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

### c5ad instances

| c5ad.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c5ad.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c5ad.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c5ad.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c5ad.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c5ad.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c5ad.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

### c5d instances

| c5d.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 6144                 | 3072          |
| `yarn.nodemanager.resource.memory-mb`  | 6144                 | 3072          |

| c5d.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| c5d.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| c5d.9xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1456m            | -Xmx1456m     |
| `mapreduce.java.opts`                  | -Xmx2912m            | -Xmx2912m     |
| `mapreduce.map.memory.mb`              | 1820                 | 1820          |
| `mapreduce.reduce.memory.mb`           | 3640                 | 3640          |
| `yarn.app.mapreduce.am.resource.mb`    | 3640                 | 3640          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 65536                | 32768         |
| `yarn.nodemanager.resource.memory-mb`  | 65536                | 32768         |

| c5d.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1502m            | -Xmx1502m     |
| `mapreduce.java.opts`                  | -Xmx3004m            | -Xmx3004m     |
| `mapreduce.map.memory.mb`              | 1877                 | 1877          |
| `mapreduce.reduce.memory.mb`           | 3754                 | 3754          |
| `yarn.app.mapreduce.am.resource.mb`    | 3754                 | 3754          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30048         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30048         |

| c5d.18xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1547m            | -Xmx1547m     |
| `mapreduce.java.opts`                  | -Xmx3094m            | -Xmx3094m     |
| `mapreduce.map.memory.mb`              | 1934                 | 1934          |
| `mapreduce.reduce.memory.mb`           | 3868                 | 3868          |
| `yarn.app.mapreduce.am.resource.mb`    | 3868                 | 3868          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 139264               | 30960         |
| `yarn.nodemanager.resource.memory-mb`  | 139264               | 30960         |

| c5d.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1570m            | -Xmx1570m     |
| `mapreduce.java.opts`                  | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.map.memory.mb`              | 1963                 | 1963          |
| `mapreduce.reduce.memory.mb`           | 3926                 | 3926          |
| `yarn.app.mapreduce.am.resource.mb`    | 3926                 | 3926          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31376         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31376         |

### c5n instances

| c5n.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1613m            | -Xmx1613m     |
| `mapreduce.java.opts`                  | -Xmx3226m            | -Xmx3226m     |
| `mapreduce.map.memory.mb`              | 2016                 | 2016          |
| `mapreduce.reduce.memory.mb`           | 4032                 | 4032          |
| `yarn.app.mapreduce.am.resource.mb`    | 4032                 | 4032          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 8064                 | 4032          |
| `yarn.nodemanager.resource.memory-mb`  | 8064                 | 4032          |

| c5n.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1613m            | -Xmx1613m     |
| `mapreduce.java.opts`                  | -Xmx3226m            | -Xmx3226m     |
| `mapreduce.map.memory.mb`              | 2016                 | 2016          |
| `mapreduce.reduce.memory.mb`           | 4032                 | 4032          |
| `yarn.app.mapreduce.am.resource.mb`    | 4032                 | 4032          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 16128                | 8064          |
| `yarn.nodemanager.resource.memory-mb`  | 16128                | 8064          |

| c5n.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1741m            | -Xmx1741m     |
| `mapreduce.java.opts`                  | -Xmx3482m            | -Xmx3482m     |
| `mapreduce.map.memory.mb`              | 2176                 | 2176          |
| `mapreduce.reduce.memory.mb`           | 4352                 | 4352          |
| `yarn.app.mapreduce.am.resource.mb`    | 4352                 | 4352          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 34816                | 17408         |
| `yarn.nodemanager.resource.memory-mb`  | 34816                | 17408         |

| c5n.9xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2002m            | -Xmx2002m     |
| `mapreduce.java.opts`                  | -Xmx4004m            | -Xmx4004m     |
| `mapreduce.map.memory.mb`              | 2503                 | 2503          |
| `mapreduce.reduce.memory.mb`           | 5006                 | 5006          |
| `yarn.app.mapreduce.am.resource.mb`    | 5006                 | 5006          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30040         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30040         |

| c5n.18xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2094m            | -Xmx2094m     |
| `mapreduce.java.opts`                  | -Xmx4188m            | -Xmx4188m     |
| `mapreduce.map.memory.mb`              | 2617                 | 2617          |
| `mapreduce.reduce.memory.mb`           | 5234                 | 5234          |
| `yarn.app.mapreduce.am.resource.mb`    | 5234                 | 5234          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31396         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31396         |

### c6a instances

| c6a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c6a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c6a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1510m            | -Xmx1510m     |
| `mapreduce.java.opts`                  | -Xmx3020m            | -Xmx3020m     |
| `mapreduce.map.memory.mb`              | 1888                 | 1888          |
| `mapreduce.reduce.memory.mb`           | 3776                 | 3776          |
| `yarn.app.mapreduce.am.resource.mb`    | 3776                 | 3776          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| c6a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1527m            | -Xmx1527m     |
| `mapreduce.java.opts`                  | -Xmx3054m            | -Xmx3054m     |
| `mapreduce.map.memory.mb`              | 1909                 | 1909          |
| `mapreduce.reduce.memory.mb`           | 3818                 | 3818          |
| `yarn.app.mapreduce.am.resource.mb`    | 3818                 | 3818          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30608         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30608         |

### c6g instances

| c6g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c6gd instances

| c6gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c6gn instances

| c6gn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6gn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6gn.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6gn.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6gn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6gn.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c6i instances

| c6i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c6i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c6i.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1510m            | -Xmx1510m     |
| `mapreduce.java.opts`                  | -Xmx3020m            | -Xmx3020m     |
| `mapreduce.map.memory.mb`              | 1888                 | 1888          |
| `mapreduce.reduce.memory.mb`           | 3776                 | 3776          |
| `yarn.app.mapreduce.am.resource.mb`    | 3776                 | 3776          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### c6id instances

| c6id.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6id.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6id.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6id.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6id.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6id.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c6id.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c6id.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1510m            | -Xmx1510m     |
| `mapreduce.java.opts`                  | -Xmx3020m            | -Xmx3020m     |
| `mapreduce.map.memory.mb`              | 1888                 | 1888          |
| `mapreduce.reduce.memory.mb`           | 3776                 | 3776          |
| `yarn.app.mapreduce.am.resource.mb`    | 3776                 | 3776          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### c6in instances

| c6in.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c6in.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c6in.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c6in.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c6in.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c6in.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c6in.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c6in.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1510m            | -Xmx1510m     |
| `mapreduce.java.opts`                  | -Xmx3020m            | -Xmx3020m     |
| `mapreduce.map.memory.mb`              | 1888                 | 1888          |
| `mapreduce.reduce.memory.mb`           | 3776                 | 3776          |
| `yarn.app.mapreduce.am.resource.mb`    | 3776                 | 3776          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### c7a instances

| c7a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c7a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c7a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1510m            | -Xmx1510m     |
| `mapreduce.java.opts`                  | -Xmx3020m            | -Xmx3020m     |
| `mapreduce.map.memory.mb`              | 1888                 | 1888          |
| `mapreduce.reduce.memory.mb`           | 3776                 | 3776          |
| `yarn.app.mapreduce.am.resource.mb`    | 3776                 | 3776          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| c7a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1527m            | -Xmx1527m     |
| `mapreduce.java.opts`                  | -Xmx3054m            | -Xmx3054m     |
| `mapreduce.map.memory.mb`              | 1909                 | 1909          |
| `mapreduce.reduce.memory.mb`           | 3818                 | 3818          |
| `yarn.app.mapreduce.am.resource.mb`    | 3818                 | 3818          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30608         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30608         |

### c7g instances

| c7g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c7gd instances

| c7gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c7gn instances

| c7gn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7gn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7gn.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7gn.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7gn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7gn.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c7i instances

| c7i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c7i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c7i.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1527m            | -Xmx1527m     |
| `mapreduce.java.opts`                  | -Xmx3054m            | -Xmx3054m     |
| `mapreduce.map.memory.mb`              | 1909                 | 1909          |
| `mapreduce.reduce.memory.mb`           | 3818                 | 3818          |
| `yarn.app.mapreduce.am.resource.mb`    | 3818                 | 3818          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30608         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30608         |

### c7i-flex instances

| c7i-flex.xlarge                        | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c7i-flex.2xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c7i-flex.4xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c7i-flex.8xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c7i-flex.12xlarge                      | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c7i-flex.16xlarge                      | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

### c8g instances

| c8g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c8g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c8g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c8g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c8g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c8g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c8g.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c8g.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1527m            | -Xmx1527m     |
| `mapreduce.java.opts`                  | -Xmx3054m            | -Xmx3054m     |
| `mapreduce.map.memory.mb`              | 1909                 | 1909          |
| `mapreduce.reduce.memory.mb`           | 3818                 | 3818          |
| `yarn.app.mapreduce.am.resource.mb`    | 3818                 | 3818          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30608         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30608         |

### c8gd instances

| c8gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1126m            | -Xmx1126m     |
| `mapreduce.java.opts`                  | -Xmx2252m            | -Xmx2252m     |
| `mapreduce.map.memory.mb`              | 1408                 | 1408          |
| `mapreduce.reduce.memory.mb`           | 2816                 | 2816          |
| `yarn.app.mapreduce.am.resource.mb`    | 2816                 | 2816          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 5632                 | 2816          |
| `yarn.nodemanager.resource.memory-mb`  | 5632                 | 2816          |

| c8gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| c8gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1171m            | -Xmx1171m     |
| `mapreduce.java.opts`                  | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.map.memory.mb`              | 1464                 | 1464          |
| `mapreduce.reduce.memory.mb`           | 2928                 | 2928          |
| `yarn.app.mapreduce.am.resource.mb`    | 2928                 | 2928          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| c8gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1357m            | -Xmx1357m     |
| `mapreduce.java.opts`                  | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.map.memory.mb`              | 1696                 | 1696          |
| `mapreduce.reduce.memory.mb`           | 3392                 | 3392          |
| `yarn.app.mapreduce.am.resource.mb`    | 3392                 | 3392          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| c8gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1425m            | -Xmx1425m     |
| `mapreduce.java.opts`                  | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.map.memory.mb`              | 1781                 | 1781          |
| `mapreduce.reduce.memory.mb`           | 3562                 | 3562          |
| `yarn.app.mapreduce.am.resource.mb`    | 3562                 | 3562          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32074         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32074         |

| c8gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1459m            | -Xmx1459m     |
| `mapreduce.java.opts`                  | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.map.memory.mb`              | 1824                 | 1824          |
| `mapreduce.reduce.memory.mb`           | 3648                 | 3648          |
| `yarn.app.mapreduce.am.resource.mb`    | 3648                 | 3648          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| c8gd.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1494m            | -Xmx1494m     |
| `mapreduce.java.opts`                  | -Xmx2988m            | -Xmx2988m     |
| `mapreduce.map.memory.mb`              | 1867                 | 1867          |
| `mapreduce.reduce.memory.mb`           | 3734                 | 3734          |
| `yarn.app.mapreduce.am.resource.mb`    | 3734                 | 3734          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29840         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29840         |

| c8gd.48xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1527m            | -Xmx1527m     |
| `mapreduce.java.opts`                  | -Xmx3054m            | -Xmx3054m     |
| `mapreduce.map.memory.mb`              | 1909                 | 1909          |
| `mapreduce.reduce.memory.mb`           | 3818                 | 3818          |
| `yarn.app.mapreduce.am.resource.mb`    | 3818                 | 3818          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30608         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30608         |

### d2 instances

| d2.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| d2.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| d2.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| d2.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2417m            | -Xmx2417m     |
| `mapreduce.java.opts`                  | -Xmx4834m            | -Xmx4834m     |
| `mapreduce.map.memory.mb`              | 3021                 | 3021          |
| `mapreduce.reduce.memory.mb`           | 6042                 | 6042          |
| `yarn.app.mapreduce.am.resource.mb`    | 6042                 | 6042          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30194         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30194         |

### d3 instances

| d3.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| d3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| d3.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| d3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### d3en instances

| d3en.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| d3en.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| d3en.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| d3en.6xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.java.opts`                  | -Xmx5700m            | -Xmx5700m     |
| `mapreduce.map.memory.mb`              | 3563                 | 3563          |
| `mapreduce.reduce.memory.mb`           | 7126                 | 7126          |
| `yarn.app.mapreduce.am.resource.mb`    | 7126                 | 7126          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 28496         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 28496         |

| d3en.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| d3en.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

### f2 instances

| f2.6xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx8055m            | -Xmx8055m     |
| `mapreduce.java.opts`                  | -Xmx16110m           | -Xmx16110m    |
| `mapreduce.map.memory.mb`              | 10069                | 10069         |
| `mapreduce.reduce.memory.mb`           | 20138                | 20138         |
| `yarn.app.mapreduce.am.resource.mb`    | 20138                | 20138         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 20146         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 20146         |

| f2.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx8192m            | -Xmx8192m     |
| `mapreduce.java.opts`                  | -Xmx16384m           | -Xmx16384m    |
| `mapreduce.map.memory.mb`              | 10240                | 10240         |
| `mapreduce.reduce.memory.mb`           | 20480                | 20480         |
| `yarn.app.mapreduce.am.resource.mb`    | 20480                | 20480         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 20480         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 20480         |

| f2.48xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx8294m            | -Xmx8294m     |
| `mapreduce.java.opts`                  | -Xmx16588m           | -Xmx16588m    |
| `mapreduce.map.memory.mb`              | 10368                | 10368         |
| `mapreduce.reduce.memory.mb`           | 20736                | 20736         |
| `yarn.app.mapreduce.am.resource.mb`    | 20736                | 20736         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1990656              | 20736         |
| `yarn.nodemanager.resource.memory-mb`  | 1990656              | 20736         |

### g3 instances

| g3.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| g3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| g3.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### g3s instances

| g3s.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

### g4dn instances

| g4dn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| g4dn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| g4dn.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2867m            | -Xmx2867m     |
| `mapreduce.java.opts`                  | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.map.memory.mb`              | 3584                 | 3584          |
| `mapreduce.reduce.memory.mb`           | 7168                 | 7168          |
| `yarn.app.mapreduce.am.resource.mb`    | 7168                 | 7168          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| g4dn.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| g4dn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.java.opts`                  | -Xmx6280m            | -Xmx6280m     |
| `mapreduce.map.memory.mb`              | 3925                 | 3925          |
| `mapreduce.reduce.memory.mb`           | 7850                 | 7850          |
| `yarn.app.mapreduce.am.resource.mb`    | 7850                 | 7850          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31416         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31416         |

| g4dn.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.java.opts`                  | -Xmx6348m            | -Xmx6348m     |
| `mapreduce.map.memory.mb`              | 3968                 | 3968          |
| `mapreduce.reduce.memory.mb`           | 7936                 | 7936          |
| `yarn.app.mapreduce.am.resource.mb`    | 7936                 | 7936          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

### g5 instances

| g5.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| g5.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| g5.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| g5.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| g5.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| g5.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| g5.24xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| g5.48xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### g6 instances

| g6.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.java.opts`                  | -Xmx4608m            | -Xmx4608m     |
| `mapreduce.map.memory.mb`              | 2880                 | 2880          |
| `mapreduce.reduce.memory.mb`           | 5760                 | 5760          |
| `yarn.app.mapreduce.am.resource.mb`    | 5760                 | 5760          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11520                | 5760          |
| `yarn.nodemanager.resource.memory-mb`  | 11520                | 5760          |

| g6.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.java.opts`                  | -Xmx4608m            | -Xmx4608m     |
| `mapreduce.map.memory.mb`              | 2880                 | 2880          |
| `mapreduce.reduce.memory.mb`           | 5760                 | 5760          |
| `yarn.app.mapreduce.am.resource.mb`    | 5760                 | 5760          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23040                | 11520         |
| `yarn.nodemanager.resource.memory-mb`  | 23040                | 11520         |

| g6.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2662m            | -Xmx2662m     |
| `mapreduce.java.opts`                  | -Xmx5324m            | -Xmx5324m     |
| `mapreduce.map.memory.mb`              | 3328                 | 3328          |
| `mapreduce.reduce.memory.mb`           | 6656                 | 6656          |
| `yarn.app.mapreduce.am.resource.mb`    | 6656                 | 6656          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 53248                | 26624         |
| `yarn.nodemanager.resource.memory-mb`  | 53248                | 26624         |

| g6.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2893m            | -Xmx2893m     |
| `mapreduce.java.opts`                  | -Xmx5786m            | -Xmx5786m     |
| `mapreduce.map.memory.mb`              | 3616                 | 3616          |
| `mapreduce.reduce.memory.mb`           | 7232                 | 7232          |
| `yarn.app.mapreduce.am.resource.mb`    | 7232                 | 7232          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 115712               | 28928         |
| `yarn.nodemanager.resource.memory-mb`  | 115712               | 28928         |

| g6.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2953m            | -Xmx2953m     |
| `mapreduce.java.opts`                  | -Xmx5906m            | -Xmx5906m     |
| `mapreduce.map.memory.mb`              | 3691                 | 3691          |
| `mapreduce.reduce.memory.mb`           | 7382                 | 7382          |
| `yarn.app.mapreduce.am.resource.mb`    | 7382                 | 7382          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 177152               | 29512         |
| `yarn.nodemanager.resource.memory-mb`  | 177152               | 29512         |

| g6.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2995m            | -Xmx2995m     |
| `mapreduce.java.opts`                  | -Xmx5990m            | -Xmx5990m     |
| `mapreduce.map.memory.mb`              | 3744                 | 3744          |
| `mapreduce.reduce.memory.mb`           | 7488                 | 7488          |
| `yarn.app.mapreduce.am.resource.mb`    | 7488                 | 7488          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 239616               | 29952         |
| `yarn.nodemanager.resource.memory-mb`  | 239616               | 29952         |

| g6.24xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3038m            | -Xmx3038m     |
| `mapreduce.java.opts`                  | -Xmx6076m            | -Xmx6076m     |
| `mapreduce.map.memory.mb`              | 3797                 | 3797          |
| `mapreduce.reduce.memory.mb`           | 7594                 | 7594          |
| `yarn.app.mapreduce.am.resource.mb`    | 7594                 | 7594          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 364544               | 30408         |
| `yarn.nodemanager.resource.memory-mb`  | 364544               | 30408         |

| g6.48xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 737280               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 737280               | 30720         |

### g6e instances

| g6e.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| g6e.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| g6e.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| g6e.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| g6e.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| g6e.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| g6e.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| g6e.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### gr6 instances

| gr6.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5786m            | -Xmx5786m     |
| `mapreduce.java.opts`                  | -Xmx11572m           | -Xmx11572m    |
| `mapreduce.map.memory.mb`              | 7232                 | 7232          |
| `mapreduce.reduce.memory.mb`           | 14464                | 14464         |
| `yarn.app.mapreduce.am.resource.mb`    | 14464                | 14464         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 115712               | 28928         |
| `yarn.nodemanager.resource.memory-mb`  | 115712               | 28928         |

| gr6.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5990m            | -Xmx5990m     |
| `mapreduce.java.opts`                  | -Xmx11980m           | -Xmx11980m    |
| `mapreduce.map.memory.mb`              | 7488                 | 7488          |
| `mapreduce.reduce.memory.mb`           | 14976                | 14976         |
| `yarn.app.mapreduce.am.resource.mb`    | 14976                | 14976         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 239616               | 29952         |
| `yarn.nodemanager.resource.memory-mb`  | 239616               | 29952         |

### h1 instances

| h1.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| h1.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2867m            | -Xmx2867m     |
| `mapreduce.java.opts`                  | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.map.memory.mb`              | 3584                 | 3584          |
| `mapreduce.reduce.memory.mb`           | 7168                 | 7168          |
| `yarn.app.mapreduce.am.resource.mb`    | 7168                 | 7168          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| h1.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| h1.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.java.opts`                  | -Xmx6348m            | -Xmx6348m     |
| `mapreduce.map.memory.mb`              | 3968                 | 3968          |
| `mapreduce.reduce.memory.mb`           | 7936                 | 7936          |
| `yarn.app.mapreduce.am.resource.mb`    | 7936                 | 7936          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

### i2 instances

| i2.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i2.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i2.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i2.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### i3 instances

| i3.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i3.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| i3.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### i3en instances

| i3en.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4915m            | -Xmx4915m     |
| `mapreduce.java.opts`                  | -Xmx9830m            | -Xmx9830m     |
| `mapreduce.map.memory.mb`              | 6144                 | 6144          |
| `mapreduce.reduce.memory.mb`           | 12288                | 12288         |
| `yarn.app.mapreduce.am.resource.mb`    | 12288                | 12288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| i3en.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.java.opts`                  | -Xmx11468m           | -Xmx11468m    |
| `mapreduce.map.memory.mb`              | 7168                 | 7168          |
| `mapreduce.reduce.memory.mb`           | 14336                | 14336         |
| `yarn.app.mapreduce.am.resource.mb`    | 14336                | 14336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| i3en.3xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6007m            | -Xmx6007m     |
| `mapreduce.java.opts`                  | -Xmx12014m           | -Xmx12014m    |
| `mapreduce.map.memory.mb`              | 7509                 | 7509          |
| `mapreduce.reduce.memory.mb`           | 15018                | 15018         |
| `yarn.app.mapreduce.am.resource.mb`    | 15018                | 15018         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30040         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30040         |

| i3en.6xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6281m            | -Xmx6281m     |
| `mapreduce.java.opts`                  | -Xmx12562m           | -Xmx12562m    |
| `mapreduce.map.memory.mb`              | 7851                 | 7851          |
| `mapreduce.reduce.memory.mb`           | 15702                | 15702         |
| `yarn.app.mapreduce.am.resource.mb`    | 15702                | 15702         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31396         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31396         |

| i3en.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6417m            | -Xmx6417m     |
| `mapreduce.java.opts`                  | -Xmx12834m           | -Xmx12834m    |
| `mapreduce.map.memory.mb`              | 8021                 | 8021          |
| `mapreduce.reduce.memory.mb`           | 16042                | 16042         |
| `yarn.app.mapreduce.am.resource.mb`    | 16042                | 16042         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32100         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32100         |

| i3en.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6486m            | -Xmx6486m     |
| `mapreduce.java.opts`                  | -Xmx12972m           | -Xmx12972m    |
| `mapreduce.map.memory.mb`              | 8107                 | 8107          |
| `mapreduce.reduce.memory.mb`           | 16214                | 16214         |
| `yarn.app.mapreduce.am.resource.mb`    | 16214                | 16214         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 778240               | 32396         |
| `yarn.nodemanager.resource.memory-mb`  | 778240               | 32396         |

### i4g instances

| i4g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i4g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i4g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i4g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| i4g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### i4i instances

| i4i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i4i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i4i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i4i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| i4i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| i4i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| i4i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| i4i.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

### i7i instances

| i7i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i7i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i7i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i7i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| i7i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| i7i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| i7i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| i7i.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### i7ie instances

| i7ie.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i7ie.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i7ie.3xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5700m            | -Xmx5700m     |
| `mapreduce.java.opts`                  | -Xmx11400m           | -Xmx11400m    |
| `mapreduce.map.memory.mb`              | 7125                 | 7125          |
| `mapreduce.reduce.memory.mb`           | 14250                | 14250         |
| `yarn.app.mapreduce.am.resource.mb`    | 14250                | 14250         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 28504         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 28504         |

| i7ie.6xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5974m            | -Xmx5974m     |
| `mapreduce.java.opts`                  | -Xmx11948m           | -Xmx11948m    |
| `mapreduce.map.memory.mb`              | 7467                 | 7467          |
| `mapreduce.reduce.memory.mb`           | 14934                | 14934         |
| `yarn.app.mapreduce.am.resource.mb`    | 14934                | 14934         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29860         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29860         |

| i7ie.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| i7ie.18xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6155m            | -Xmx6155m     |
| `mapreduce.java.opts`                  | -Xmx12310m           | -Xmx12310m    |
| `mapreduce.map.memory.mb`              | 7694                 | 7694          |
| `mapreduce.reduce.memory.mb`           | 15388                | 15388         |
| `yarn.app.mapreduce.am.resource.mb`    | 15388                | 15388         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 553984               | 30792         |
| `yarn.nodemanager.resource.memory-mb`  | 553984               | 30792         |

| i7ie.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| i7ie.48xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### i8g instances

| i8g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| i8g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| i8g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| i8g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| i8g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| i8g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| i8g.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| i8g.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### im4gn instances

| im4gn.xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| im4gn.2xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| im4gn.4xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| im4gn.8xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| im4gn.16xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### is4gen instances

| is4gen.xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3514m            | -Xmx3514m     |
| `mapreduce.java.opts`                  | -Xmx7028m            | -Xmx7028m     |
| `mapreduce.map.memory.mb`              | 4393                 | 4393          |
| `mapreduce.reduce.memory.mb`           | 8786                 | 8786          |
| `yarn.app.mapreduce.am.resource.mb`    | 8786                 | 8786          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 17572.12             | 8786.06       |
| `yarn.nodemanager.resource.memory-mb`  | 17572.12             | 8786.06       |

| is4gen.2xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3866m            | -Xmx3866m     |
| `mapreduce.java.opts`                  | -Xmx7732m            | -Xmx7732m     |
| `mapreduce.map.memory.mb`              | 4832                 | 4832          |
| `mapreduce.reduce.memory.mb`           | 9664                 | 9664          |
| `yarn.app.mapreduce.am.resource.mb`    | 9664                 | 9664          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 38656                | 19328         |
| `yarn.nodemanager.resource.memory-mb`  | 38656                | 19328         |

| is4gen.4xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4275m            | -Xmx4275m     |
| `mapreduce.java.opts`                  | -Xmx8550m            | -Xmx8550m     |
| `mapreduce.map.memory.mb`              | 5344                 | 5344          |
| `mapreduce.reduce.memory.mb`           | 10688                | 10688         |
| `yarn.app.mapreduce.am.resource.mb`    | 10688                | 10688         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 32064         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 32064         |

| is4gen.8xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4480m            | -Xmx4480m     |
| `mapreduce.java.opts`                  | -Xmx8960m            | -Xmx8960m     |
| `mapreduce.map.memory.mb`              | 5600                 | 5600          |
| `mapreduce.reduce.memory.mb`           | 11200                | 11200         |
| `yarn.app.mapreduce.am.resource.mb`    | 11200                | 11200         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 22400         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 22400         |

### m1 instances

| m1.small                               | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx288m             | -Xmx288m      |
| `mapreduce.java.opts`                  | -Xmx288m             | -Xmx288m      |
| `mapreduce.map.memory.mb`              | 512                  | 512           |
| `mapreduce.reduce.memory.mb`           | 512                  | 512           |
| `yarn.app.mapreduce.am.resource.mb`    | 512                  | 512           |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 512                  | 512           |
| `yarn.nodemanager.resource.memory-mb`  | 1024                 | 512           |

| m1.medium                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx512m             | -Xmx512m      |
| `mapreduce.java.opts`                  | -Xmx768m             | -Xmx768m      |
| `mapreduce.map.memory.mb`              | 768                  | 768           |
| `mapreduce.reduce.memory.mb`           | 1024                 | 1024          |
| `yarn.app.mapreduce.am.resource.mb`    | 1024                 | 1024          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 2048                 | 1024          |
| `yarn.nodemanager.resource.memory-mb`  | 2048                 | 1024          |

| m1.large                               | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx512m             | -Xmx512m      |
| `mapreduce.java.opts`                  | -Xmx1024m            | -Xmx1024m     |
| `mapreduce.map.memory.mb`              | 768                  | 768           |
| `mapreduce.reduce.memory.mb`           | 1536                 | 1536          |
| `yarn.app.mapreduce.am.resource.mb`    | 1536                 | 1536          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 3072                 | 2560          |
| `yarn.nodemanager.resource.memory-mb`  | 5120                 | 2560          |

| m1.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx512m             | -Xmx512m      |
| `mapreduce.java.opts`                  | -Xmx1536m            | -Xmx1536m     |
| `mapreduce.map.memory.mb`              | 768                  | 768           |
| `mapreduce.reduce.memory.mb`           | 2048                 | 2048          |
| `yarn.app.mapreduce.am.resource.mb`    | 2048                 | 2048          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 8192                 | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

### m2 instances

| m2.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx864m             | -Xmx864m      |
| `mapreduce.java.opts`                  | -Xmx1536m            | -Xmx1536m     |
| `mapreduce.map.memory.mb`              | 1024                 | 1024          |
| `mapreduce.reduce.memory.mb`           | 2048                 | 2048          |
| `yarn.app.mapreduce.am.resource.mb`    | 2048                 | 2048          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 7168                 | 7168          |
| `yarn.nodemanager.resource.memory-mb`  | 14336                | 7168          |

| m2.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1280m            | -Xmx1280m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 2560                 | 2560          |
| `yarn.app.mapreduce.am.resource.mb`    | 2560                 | 2560          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 8192                 | 15360         |
| `yarn.nodemanager.resource.memory-mb`  | 30720                | 15360         |

| m2.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1280m            | -Xmx1280m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 2560                 | 2560          |
| `yarn.app.mapreduce.am.resource.mb`    | 2560                 | 2560          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 8192                 | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 61440                | 30720         |

### m3 instances

| m3.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11520                | 5760          |
| `yarn.nodemanager.resource.memory-mb`  | 11520                | 5760          |

| m3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1152m            | -Xmx1152m     |
| `mapreduce.java.opts`                  | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.map.memory.mb`              | 1440                 | 1440          |
| `mapreduce.reduce.memory.mb`           | 2880                 | 2880          |
| `yarn.app.mapreduce.am.resource.mb`    | 2880                 | 2880          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23040                | 11520         |
| `yarn.nodemanager.resource.memory-mb`  | 23040                | 11520         |

### m4 instances

| m4.large                               | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 6144                 | 3072          |
| `yarn.nodemanager.resource.memory-mb`  | 6144                 | 3072          |

| m4.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| m4.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1229m            | -Xmx1229m     |
| `mapreduce.java.opts`                  | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.map.memory.mb`              | 1536                 | 1536          |
| `mapreduce.reduce.memory.mb`           | 3072                 | 3072          |
| `yarn.app.mapreduce.am.resource.mb`    | 3072                 | 3072          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| m4.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1434m            | -Xmx1434m     |
| `mapreduce.java.opts`                  | -Xmx2868m            | -Xmx2868m     |
| `mapreduce.map.memory.mb`              | 1792                 | 1792          |
| `mapreduce.reduce.memory.mb`           | 3584                 | 3584          |
| `yarn.app.mapreduce.am.resource.mb`    | 3584                 | 3584          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| m4.10xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1557m            | -Xmx1557m     |
| `mapreduce.java.opts`                  | -Xmx3114m            | -Xmx3114m     |
| `mapreduce.map.memory.mb`              | 1946                 | 1946          |
| `mapreduce.reduce.memory.mb`           | 3892                 | 3892          |
| `yarn.app.mapreduce.am.resource.mb`    | 3892                 | 3892          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 155648               | 31104         |
| `yarn.nodemanager.resource.memory-mb`  | 155648               | 31104         |

| m4.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx1587m            | -Xmx1587m     |
| `mapreduce.java.opts`                  | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.map.memory.mb`              | 1984                 | 1984          |
| `mapreduce.reduce.memory.mb`           | 3968                 | 3968          |
| `yarn.app.mapreduce.am.resource.mb`    | 3968                 | 3968          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

### m5 instances

| m5.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| m5.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| m5.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2867m            | -Xmx2867m     |
| `mapreduce.java.opts`                  | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.map.memory.mb`              | 3584                 | 3584          |
| `mapreduce.reduce.memory.mb`           | 7168                 | 7168          |
| `yarn.app.mapreduce.am.resource.mb`    | 7168                 | 7168          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| m5.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| m5.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.java.opts`                  | -Xmx6280m            | -Xmx6280m     |
| `mapreduce.map.memory.mb`              | 3925                 | 3925          |
| `mapreduce.reduce.memory.mb`           | 7850                 | 7850          |
| `yarn.app.mapreduce.am.resource.mb`    | 7850                 | 7850          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31416         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31416         |

| m5.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.java.opts`                  | -Xmx6348m            | -Xmx6348m     |
| `mapreduce.map.memory.mb`              | 3968                 | 3968          |
| `mapreduce.reduce.memory.mb`           | 7936                 | 7936          |
| `yarn.app.mapreduce.am.resource.mb`    | 7936                 | 7936          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| m5.24xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3209m            | -Xmx3209m     |
| `mapreduce.java.opts`                  | -Xmx6418m            | -Xmx6418m     |
| `mapreduce.map.memory.mb`              | 4011                 | 4011          |
| `mapreduce.reduce.memory.mb`           | 8022                 | 8022          |
| `yarn.app.mapreduce.am.resource.mb`    | 8022                 | 8022          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32056         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32056         |

### m5a instances

| m5a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| m5a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| m5a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2867m            | -Xmx2867m     |
| `mapreduce.java.opts`                  | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.map.memory.mb`              | 3584                 | 3584          |
| `mapreduce.reduce.memory.mb`           | 7168                 | 7168          |
| `yarn.app.mapreduce.am.resource.mb`    | 7168                 | 7168          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| m5a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| m5a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.java.opts`                  | -Xmx6280m            | -Xmx6280m     |
| `mapreduce.map.memory.mb`              | 3925                 | 3925          |
| `mapreduce.reduce.memory.mb`           | 7850                 | 7850          |
| `yarn.app.mapreduce.am.resource.mb`    | 7850                 | 7850          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31416         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31416         |

| m5a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.java.opts`                  | -Xmx6348m            | -Xmx6348m     |
| `mapreduce.map.memory.mb`              | 3968                 | 3968          |
| `mapreduce.reduce.memory.mb`           | 7936                 | 7936          |
| `yarn.app.mapreduce.am.resource.mb`    | 7936                 | 7936          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| m5a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3209m            | -Xmx3209m     |
| `mapreduce.java.opts`                  | -Xmx6418m            | -Xmx6418m     |
| `mapreduce.map.memory.mb`              | 4011                 | 4011          |
| `mapreduce.reduce.memory.mb`           | 8022                 | 8022          |
| `yarn.app.mapreduce.am.resource.mb`    | 8022                 | 8022          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32056         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32056         |

### m5ad instances

| m5ad.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m5ad.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m5ad.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m5ad.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m5ad.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m5ad.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m5ad.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

### m5d instances

| m5d.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 12288                | 6144          |
| `yarn.nodemanager.resource.memory-mb`  | 12288                | 6144          |

| m5d.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2458m            | -Xmx2458m     |
| `mapreduce.java.opts`                  | -Xmx4916m            | -Xmx4916m     |
| `mapreduce.map.memory.mb`              | 3072                 | 3072          |
| `mapreduce.reduce.memory.mb`           | 6144                 | 6144          |
| `yarn.app.mapreduce.am.resource.mb`    | 6144                 | 6144          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| m5d.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2867m            | -Xmx2867m     |
| `mapreduce.java.opts`                  | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.map.memory.mb`              | 3584                 | 3584          |
| `mapreduce.reduce.memory.mb`           | 7168                 | 7168          |
| `yarn.app.mapreduce.am.resource.mb`    | 7168                 | 7168          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| m5d.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| m5d.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3140m            | -Xmx3140m     |
| `mapreduce.java.opts`                  | -Xmx6280m            | -Xmx6280m     |
| `mapreduce.map.memory.mb`              | 3925                 | 3925          |
| `mapreduce.reduce.memory.mb`           | 7850                 | 7850          |
| `yarn.app.mapreduce.am.resource.mb`    | 7850                 | 7850          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31416         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31416         |

| m5d.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3174m            | -Xmx3174m     |
| `mapreduce.java.opts`                  | -Xmx6348m            | -Xmx6348m     |
| `mapreduce.map.memory.mb`              | 3968                 | 3968          |
| `mapreduce.reduce.memory.mb`           | 7936                 | 7936          |
| `yarn.app.mapreduce.am.resource.mb`    | 7936                 | 7936          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| m5d.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3209m            | -Xmx3209m     |
| `mapreduce.java.opts`                  | -Xmx6418m            | -Xmx6418m     |
| `mapreduce.map.memory.mb`              | 4011                 | 4011          |
| `mapreduce.reduce.memory.mb`           | 8022                 | 8022          |
| `yarn.app.mapreduce.am.resource.mb`    | 8022                 | 8022          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32056         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32056         |

### m5dn instances

| m5dn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m5dn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m5dn.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m5dn.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m5dn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m5dn.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m5dn.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

### m5n instances

| m5n.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m5n.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m5n.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m5n.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m5n.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m5n.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m5n.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

### m5zn instances

| m5zn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2304m            | -Xmx2304m     |
| `mapreduce.java.opts`                  | -Xmx4608m            | -Xmx4608m     |
| `mapreduce.map.memory.mb`              | 2880                 | 2880          |
| `mapreduce.reduce.memory.mb`           | 5760                 | 5760          |
| `yarn.app.mapreduce.am.resource.mb`    | 5760                 | 5760          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11520                | 5760          |
| `yarn.nodemanager.resource.memory-mb`  | 11520                | 5760          |

| m5zn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m5zn.3xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2577m            | -Xmx2577m     |
| `mapreduce.java.opts`                  | -Xmx5154m            | -Xmx5154m     |
| `mapreduce.map.memory.mb`              | 3221                 | 3221          |
| `mapreduce.reduce.memory.mb`           | 6442                 | 6442          |
| `yarn.app.mapreduce.am.resource.mb`    | 6442                 | 6442          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 38656                | 19328         |
| `yarn.nodemanager.resource.memory-mb`  | 38656                | 19328         |

| m5zn.6xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2850m            | -Xmx2850m     |
| `mapreduce.java.opts`                  | -Xmx5700m            | -Xmx5700m     |
| `mapreduce.map.memory.mb`              | 3563                 | 3563          |
| `mapreduce.reduce.memory.mb`           | 7126                 | 7126          |
| `yarn.app.mapreduce.am.resource.mb`    | 7126                 | 7126          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 85504                | 28496         |
| `yarn.nodemanager.resource.memory-mb`  | 85504                | 28496         |

| m5zn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

### m6a instances

| m6a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m6a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m6a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m6a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| m6a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### m6g instances

| m6g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m6g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### m6gd instances

| m6gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m6gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### m6i instances

| m6i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m6i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m6i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m6i.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### m6id instances

| m6id.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6id.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6id.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6id.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6id.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m6id.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m6id.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m6id.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### m6idn instances

| m6idn.xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6idn.2xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6idn.4xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6idn.8xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6idn.12xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m6idn.16xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m6idn.24xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m6idn.32xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### m6in instances

| m6in.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m6in.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m6in.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m6in.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m6in.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m6in.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m6in.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m6in.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### m7a instances

| m7a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m7a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m7a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m7a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m7a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m7a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m7a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m7a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3072m            | -Xmx3072m     |
| `mapreduce.java.opts`                  | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.map.memory.mb`              | 3840                 | 3840          |
| `mapreduce.reduce.memory.mb`           | 7680                 | 7680          |
| `yarn.app.mapreduce.am.resource.mb`    | 7680                 | 7680          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| m7a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### m7g instances

| m7g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m7g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m7g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m7g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m7g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m7g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### m7gd instances

| m7gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m7gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m7gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m7gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m7gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m7gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### m7i instances

| m7i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m7i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m7i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m7i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m7i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m7i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m7i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m7i.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### m7i-flex instances

| m7i-flex.xlarge                        | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m7i-flex.2xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m7i-flex.4xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m7i-flex.8xlarge                       | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m7i-flex.12xlarge                      | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m7i-flex.16xlarge                      | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### m8g instances

| m8g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m8g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m8g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m8g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m8g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 181248               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 181248               | 30208         |

| m8g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m8g.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m8g.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### m8gd instances

| m8gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 11712                | 5856          |
| `yarn.nodemanager.resource.memory-mb`  | 11712                | 5856          |

| m8gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| m8gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| m8gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| m8gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2986m            | -Xmx2986m     |
| `mapreduce.java.opts`                  | -Xmx5972m            | -Xmx5972m     |
| `mapreduce.map.memory.mb`              | 3733                 | 3733          |
| `mapreduce.reduce.memory.mb`           | 7466                 | 7466          |
| `yarn.app.mapreduce.am.resource.mb`    | 7466                 | 7466          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 179200               | 29880         |
| `yarn.nodemanager.resource.memory-mb`  | 179200               | 29880         |

| m8gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| m8gd.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3055m            | -Xmx3055m     |
| `mapreduce.java.opts`                  | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.map.memory.mb`              | 3819                 | 3819          |
| `mapreduce.reduce.memory.mb`           | 7638                 | 7638          |
| `yarn.app.mapreduce.am.resource.mb`    | 7638                 | 7638          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30520         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30520         |

| m8gd.48xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3089m            | -Xmx3089m     |
| `mapreduce.java.opts`                  | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.map.memory.mb`              | 3861                 | 3861          |
| `mapreduce.reduce.memory.mb`           | 7722                 | 7722          |
| `yarn.app.mapreduce.am.resource.mb`    | 7722                 | 7722          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30952         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30952         |

### p2 instances

| p2.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.java.opts`                  | -Xmx21708m           | -Xmx21708m    |
| `mapreduce.map.memory.mb`              | 13568                | 13568         |
| `mapreduce.reduce.memory.mb`           | 27136                | 27136         |
| `yarn.app.mapreduce.am.resource.mb`    | 27136                | 27136         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| p2.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.java.opts`                  | -Xmx24576m           | -Xmx24576m    |
| `mapreduce.map.memory.mb`              | 15360                | 15360         |
| `mapreduce.reduce.memory.mb`           | 30720                | 30720         |
| `yarn.app.mapreduce.am.resource.mb`    | 30720                | 30720         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| p2.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx9267m            | -Xmx9267m     |
| `mapreduce.java.opts`                  | -Xmx18534m           | -Xmx18534m    |
| `mapreduce.map.memory.mb`              | 11584                | 11584         |
| `mapreduce.reduce.memory.mb`           | 23168                | 23168         |
| `yarn.app.mapreduce.am.resource.mb`    | 23168                | 23168         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 23168         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 23168         |

### p3 instances

| p3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| p3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| p3.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### p4d instances

| p4d.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx9302m            | -Xmx9302m     |
| `mapreduce.java.opts`                  | -Xmx18604m           | -Xmx18604m    |
| `mapreduce.map.memory.mb`              | 11627                | 11627         |
| `mapreduce.reduce.memory.mb`           | 23254                | 23254         |
| `yarn.app.mapreduce.am.resource.mb`    | 23254                | 23254         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1116160              | 23222         |
| `yarn.nodemanager.resource.memory-mb`  | 1116160              | 23222         |

### p5 instances

| p5.48xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx8294m            | -Xmx8294m     |
| `mapreduce.java.opts`                  | -Xmx16588m           | -Xmx16588m    |
| `mapreduce.map.memory.mb`              | 10368                | 10368         |
| `mapreduce.reduce.memory.mb`           | 20736                | 20736         |
| `yarn.app.mapreduce.am.resource.mb`    | 20736                | 20736         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1990656              | 20736         |
| `yarn.nodemanager.resource.memory-mb`  | 1990656              | 20736         |

### r3 instances

| r3.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2342m            | -Xmx2342m     |
| `mapreduce.java.opts`                  | -Xmx4684m            | -Xmx4684m     |
| `mapreduce.map.memory.mb`              | 2928                 | 2928          |
| `mapreduce.reduce.memory.mb`           | 5856                 | 5856          |
| `yarn.app.mapreduce.am.resource.mb`    | 5856                 | 5856          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r3.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2714m            | -Xmx2714m     |
| `mapreduce.java.opts`                  | -Xmx5428m            | -Xmx5428m     |
| `mapreduce.map.memory.mb`              | 3392                 | 3392          |
| `mapreduce.reduce.memory.mb`           | 6784                 | 6784          |
| `yarn.app.mapreduce.am.resource.mb`    | 6784                 | 6784          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r3.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx2918m            | -Xmx2918m     |
| `mapreduce.java.opts`                  | -Xmx5836m            | -Xmx5836m     |
| `mapreduce.map.memory.mb`              | 3648                 | 3648          |
| `mapreduce.reduce.memory.mb`           | 7296                 | 7296          |
| `yarn.app.mapreduce.am.resource.mb`    | 7296                 | 7296          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r3.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx3021m            | -Xmx3021m     |
| `mapreduce.java.opts`                  | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.map.memory.mb`              | 3776                 | 3776          |
| `mapreduce.reduce.memory.mb`           | 7552                 | 7552          |
| `yarn.app.mapreduce.am.resource.mb`    | 7552                 | 7552          |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

### r4 instances

| r4.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r4.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r4.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r4.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r4.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### r5 instances

| r5.xlarge                              | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4915m            | -Xmx4915m     |
| `mapreduce.java.opts`                  | -Xmx9830m            | -Xmx9830m     |
| `mapreduce.map.memory.mb`              | 6144                 | 6144          |
| `mapreduce.reduce.memory.mb`           | 12288                | 12288         |
| `yarn.app.mapreduce.am.resource.mb`    | 12288                | 12288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| r5.2xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.java.opts`                  | -Xmx11468m           | -Xmx11468m    |
| `mapreduce.map.memory.mb`              | 7168                 | 7168          |
| `mapreduce.reduce.memory.mb`           | 14336                | 14336         |
| `yarn.app.mapreduce.am.resource.mb`    | 14336                | 14336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| r5.4xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| r5.8xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6349m            | -Xmx6349m     |
| `mapreduce.java.opts`                  | -Xmx12698m           | -Xmx12698m    |
| `mapreduce.map.memory.mb`              | 7936                 | 7936          |
| `mapreduce.reduce.memory.mb`           | 15872                | 15872         |
| `yarn.app.mapreduce.am.resource.mb`    | 15872                | 15872         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| r5.12xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6417m            | -Xmx6417m     |
| `mapreduce.java.opts`                  | -Xmx12834m           | -Xmx12834m    |
| `mapreduce.map.memory.mb`              | 8021                 | 8021          |
| `mapreduce.reduce.memory.mb`           | 16042                | 16042         |
| `yarn.app.mapreduce.am.resource.mb`    | 16042                | 16042         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32100         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32100         |

| r5.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6451m            | -Xmx6451m     |
| `mapreduce.java.opts`                  | -Xmx12902m           | -Xmx12902m    |
| `mapreduce.map.memory.mb`              | 8064                 | 8064          |
| `mapreduce.reduce.memory.mb`           | 16128                | 16128         |
| `yarn.app.mapreduce.am.resource.mb`    | 16128                | 16128         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 516096               | 32256         |
| `yarn.nodemanager.resource.memory-mb`  | 516096               | 32256         |

| r5.24xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6486m            | -Xmx6486m     |
| `mapreduce.java.opts`                  | -Xmx12972m           | -Xmx12972m    |
| `mapreduce.map.memory.mb`              | 8107                 | 8107          |
| `mapreduce.reduce.memory.mb`           | 16214                | 16214         |
| `yarn.app.mapreduce.am.resource.mb`    | 16214                | 16214         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 778240               | 32396         |
| `yarn.nodemanager.resource.memory-mb`  | 778240               | 32396         |

### r5a instances

| r5a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4915m            | -Xmx4915m     |
| `mapreduce.java.opts`                  | -Xmx9830m            | -Xmx9830m     |
| `mapreduce.map.memory.mb`              | 6144                 | 6144          |
| `mapreduce.reduce.memory.mb`           | 12288                | 12288         |
| `yarn.app.mapreduce.am.resource.mb`    | 12288                | 12288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| r5a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.java.opts`                  | -Xmx11468m           | -Xmx11468m    |
| `mapreduce.map.memory.mb`              | 7168                 | 7168          |
| `mapreduce.reduce.memory.mb`           | 14336                | 14336         |
| `yarn.app.mapreduce.am.resource.mb`    | 14336                | 14336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| r5a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| r5a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6349m            | -Xmx6349m     |
| `mapreduce.java.opts`                  | -Xmx12698m           | -Xmx12698m    |
| `mapreduce.map.memory.mb`              | 7936                 | 7936          |
| `mapreduce.reduce.memory.mb`           | 15872                | 15872         |
| `yarn.app.mapreduce.am.resource.mb`    | 15872                | 15872         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| r5a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6417m            | -Xmx6417m     |
| `mapreduce.java.opts`                  | -Xmx12834m           | -Xmx12834m    |
| `mapreduce.map.memory.mb`              | 8021                 | 8021          |
| `mapreduce.reduce.memory.mb`           | 16042                | 16042         |
| `yarn.app.mapreduce.am.resource.mb`    | 16042                | 16042         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32100         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32100         |

| r5a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6451m            | -Xmx6451m     |
| `mapreduce.java.opts`                  | -Xmx12902m           | -Xmx12902m    |
| `mapreduce.map.memory.mb`              | 8064                 | 8064          |
| `mapreduce.reduce.memory.mb`           | 16128                | 16128         |
| `yarn.app.mapreduce.am.resource.mb`    | 16128                | 16128         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 516096               | 32256         |
| `yarn.nodemanager.resource.memory-mb`  | 516096               | 32256         |

| r5a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6486m            | -Xmx6486m     |
| `mapreduce.java.opts`                  | -Xmx12972m           | -Xmx12972m    |
| `mapreduce.map.memory.mb`              | 8107                 | 8107          |
| `mapreduce.reduce.memory.mb`           | 16214                | 16214         |
| `yarn.app.mapreduce.am.resource.mb`    | 16214                | 16214         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 778240               | 32396         |
| `yarn.nodemanager.resource.memory-mb`  | 778240               | 32396         |

### r5ad instances

| r5ad.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r5ad.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r5ad.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r5ad.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r5ad.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r5ad.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6246m            | -Xmx6246m     |
| `mapreduce.java.opts`                  | -Xmx12492m           | -Xmx12492m    |
| `mapreduce.map.memory.mb`              | 7808                 | 7808          |
| `mapreduce.reduce.memory.mb`           | 15616                | 15616         |
| `yarn.app.mapreduce.am.resource.mb`    | 15616                | 15616         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 499712               | 31232         |
| `yarn.nodemanager.resource.memory-mb`  | 499712               | 31232         |

| r5ad.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

### r5b instances

| r5b.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r5b.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r5b.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r5b.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r5b.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r5b.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r5b.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

### r5d instances

| r5d.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4915m            | -Xmx4915m     |
| `mapreduce.java.opts`                  | -Xmx9830m            | -Xmx9830m     |
| `mapreduce.map.memory.mb`              | 6144                 | 6144          |
| `mapreduce.reduce.memory.mb`           | 12288                | 12288         |
| `yarn.app.mapreduce.am.resource.mb`    | 12288                | 12288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| r5d.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.java.opts`                  | -Xmx11468m           | -Xmx11468m    |
| `mapreduce.map.memory.mb`              | 7168                 | 7168          |
| `mapreduce.reduce.memory.mb`           | 14336                | 14336         |
| `yarn.app.mapreduce.am.resource.mb`    | 14336                | 14336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| r5d.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 122880               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 122880               | 30720         |

| r5d.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6349m            | -Xmx6349m     |
| `mapreduce.java.opts`                  | -Xmx12698m           | -Xmx12698m    |
| `mapreduce.map.memory.mb`              | 7936                 | 7936          |
| `mapreduce.reduce.memory.mb`           | 15872                | 15872         |
| `yarn.app.mapreduce.am.resource.mb`    | 15872                | 15872         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 253952               | 31744         |
| `yarn.nodemanager.resource.memory-mb`  | 253952               | 31744         |

| r5d.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6417m            | -Xmx6417m     |
| `mapreduce.java.opts`                  | -Xmx12834m           | -Xmx12834m    |
| `mapreduce.map.memory.mb`              | 8021                 | 8021          |
| `mapreduce.reduce.memory.mb`           | 16042                | 16042         |
| `yarn.app.mapreduce.am.resource.mb`    | 16042                | 16042         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32100         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32100         |

| r5d.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6451m            | -Xmx6451m     |
| `mapreduce.java.opts`                  | -Xmx12902m           | -Xmx12902m    |
| `mapreduce.map.memory.mb`              | 8064                 | 8064          |
| `mapreduce.reduce.memory.mb`           | 16128                | 16128         |
| `yarn.app.mapreduce.am.resource.mb`    | 16128                | 16128         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 516096               | 32256         |
| `yarn.nodemanager.resource.memory-mb`  | 516096               | 32256         |

| r5d.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6486m            | -Xmx6486m     |
| `mapreduce.java.opts`                  | -Xmx12972m           | -Xmx12972m    |
| `mapreduce.map.memory.mb`              | 8107                 | 8107          |
| `mapreduce.reduce.memory.mb`           | 16214                | 16214         |
| `yarn.app.mapreduce.am.resource.mb`    | 16214                | 16214         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 778240               | 32396         |
| `yarn.nodemanager.resource.memory-mb`  | 778240               | 32396         |

### r5dn instances

| r5dn.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r5dn.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r5dn.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r5dn.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r5dn.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r5dn.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r5dn.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

### r5n instances

| r5n.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r5n.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r5n.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r5n.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r5n.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r5n.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r5n.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

### r6a instances

| r6a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r6a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r6a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

| r6a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### r6g instances

| r6g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### r6gd instances

| r6gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### r6i instances

| r6i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r6i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r6i.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6029m            | -Xmx6029m     |
| `mapreduce.java.opts`                  | -Xmx12058m           | -Xmx12058m    |
| `mapreduce.map.memory.mb`              | 7536                 | 7536          |
| `mapreduce.reduce.memory.mb`           | 15072                | 15072         |
| `yarn.app.mapreduce.am.resource.mb`    | 15072                | 15072         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 964608               | 30144         |
| `yarn.nodemanager.resource.memory-mb`  | 964608               | 30144         |

### r6id instances

| r6id.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6id.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6id.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6id.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6id.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6id.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r6id.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r6id.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

### r6idn instances

| r6idn.xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6idn.2xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6idn.4xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6idn.8xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6idn.12xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6idn.16xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r6idn.24xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r6idn.32xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

### r6in instances

| r6in.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r6in.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r6in.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r6in.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r6in.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r6in.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r6in.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r6in.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

### r7a instances

| r7a.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r7a.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r7a.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r7a.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r7a.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r7a.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r7a.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r7a.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6195m            | -Xmx6195m     |
| `mapreduce.java.opts`                  | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.map.memory.mb`              | 7744                 | 7744          |
| `mapreduce.reduce.memory.mb`           | 15488                | 15488         |
| `yarn.app.mapreduce.am.resource.mb`    | 15488                | 15488         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

| r7a.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### r7g instances

| r7g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r7g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r7g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r7g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r7g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r7g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### r7gd instances

| r7gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r7gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r7gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r7gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r7gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r7gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

### r7i instances

| r7i.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r7i.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r7i.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r7i.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r7i.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r7i.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r7i.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r7i.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### r7iz instances

| r7iz.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r7iz.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r7iz.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r7iz.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r7iz.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r7iz.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r7iz.32xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6029m            | -Xmx6029m     |
| `mapreduce.java.opts`                  | -Xmx12058m           | -Xmx12058m    |
| `mapreduce.map.memory.mb`              | 7536                 | 7536          |
| `mapreduce.reduce.memory.mb`           | 15072                | 15072         |
| `yarn.app.mapreduce.am.resource.mb`    | 15072                | 15072         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 964608               | 30144         |
| `yarn.nodemanager.resource.memory-mb`  | 964608               | 30144         |

### r8g instances

| r8g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r8g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r8g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r8g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r8g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r8g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r8g.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r8g.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### r8gd instances

| r8gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4685m            | -Xmx4685m     |
| `mapreduce.java.opts`                  | -Xmx9370m            | -Xmx9370m     |
| `mapreduce.map.memory.mb`              | 5856                 | 5856          |
| `mapreduce.reduce.memory.mb`           | 11712                | 11712         |
| `yarn.app.mapreduce.am.resource.mb`    | 11712                | 11712         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 23424                | 11712         |
| `yarn.nodemanager.resource.memory-mb`  | 23424                | 11712         |

| r8gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5427m            | -Xmx5427m     |
| `mapreduce.java.opts`                  | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.map.memory.mb`              | 6784                 | 6784          |
| `mapreduce.reduce.memory.mb`           | 13568                | 13568         |
| `yarn.app.mapreduce.am.resource.mb`    | 13568                | 13568         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| r8gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5837m            | -Xmx5837m     |
| `mapreduce.java.opts`                  | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.map.memory.mb`              | 7296                 | 7296          |
| `mapreduce.reduce.memory.mb`           | 14592                | 14592         |
| `yarn.app.mapreduce.am.resource.mb`    | 14592                | 14592         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| r8gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6042m            | -Xmx6042m     |
| `mapreduce.java.opts`                  | -Xmx12084m           | -Xmx12084m    |
| `mapreduce.map.memory.mb`              | 7552                 | 7552          |
| `mapreduce.reduce.memory.mb`           | 15104                | 15104         |
| `yarn.app.mapreduce.am.resource.mb`    | 15104                | 15104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| r8gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6110m            | -Xmx6110m     |
| `mapreduce.java.opts`                  | -Xmx12220m           | -Xmx12220m    |
| `mapreduce.map.memory.mb`              | 7637                 | 7637          |
| `mapreduce.reduce.memory.mb`           | 15274                | 15274         |
| `yarn.app.mapreduce.am.resource.mb`    | 15274                | 15274         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 366592               | 30564         |
| `yarn.nodemanager.resource.memory-mb`  | 366592               | 30564         |

| r8gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6144m            | -Xmx6144m     |
| `mapreduce.java.opts`                  | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.map.memory.mb`              | 7680                 | 7680          |
| `mapreduce.reduce.memory.mb`           | 15360                | 15360         |
| `yarn.app.mapreduce.am.resource.mb`    | 15360                | 15360         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| r8gd.24xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6178m            | -Xmx6178m     |
| `mapreduce.java.opts`                  | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.map.memory.mb`              | 7723                 | 7723          |
| `mapreduce.reduce.memory.mb`           | 15446                | 15446         |
| `yarn.app.mapreduce.am.resource.mb`    | 15446                | 15446         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30860         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30860         |

| r8gd.48xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6212m            | -Xmx6212m     |
| `mapreduce.java.opts`                  | -Xmx12424m           | -Xmx12424m    |
| `mapreduce.map.memory.mb`              | 7765                 | 7765          |
| `mapreduce.reduce.memory.mb`           | 15530                | 15530         |
| `yarn.app.mapreduce.am.resource.mb`    | 15530                | 15530         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31124         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31124         |

### x1 instances

| x1.16xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12058m           | -Xmx12058m    |
| `mapreduce.java.opts`                  | -Xmx24116m           | -Xmx24116m    |
| `mapreduce.map.memory.mb`              | 15072                | 15072         |
| `mapreduce.reduce.memory.mb`           | 30144                | 30144         |
| `yarn.app.mapreduce.am.resource.mb`    | 30144                | 30144         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 964608               | 30144         |
| `yarn.nodemanager.resource.memory-mb`  | 964608               | 30144         |

| x1.32xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12109m           | -Xmx12109m    |
| `mapreduce.java.opts`                  | -Xmx24218m           | -Xmx24218m    |
| `mapreduce.map.memory.mb`              | 15136                | 15136         |
| `mapreduce.reduce.memory.mb`           | 30272                | 30272         |
| `yarn.app.mapreduce.am.resource.mb`    | 30272                | 30272         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1937408              | 30272         |
| `yarn.nodemanager.resource.memory-mb`  | 1937408              | 30272         |

### x1e instances

| x1e.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx22682m           | -Xmx22682m    |
| `mapreduce.java.opts`                  | -Xmx45364m           | -Xmx45364m    |
| `mapreduce.map.memory.mb`              | 28352                | 28352         |
| `mapreduce.reduce.memory.mb`           | 56704                | 56704         |
| `yarn.app.mapreduce.am.resource.mb`    | 56704                | 56704         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 113408               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 113408               | 0             |

| x1e.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx23501m           | -Xmx23501m    |
| `mapreduce.java.opts`                  | -Xmx47002m           | -Xmx47002m    |
| `mapreduce.map.memory.mb`              | 29376                | 29376         |
| `mapreduce.reduce.memory.mb`           | 58752                | 58752         |
| `yarn.app.mapreduce.am.resource.mb`    | 58752                | 58752         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 235008               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 235008               | 0             |

| x1e.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx23910m           | -Xmx23910m    |
| `mapreduce.java.opts`                  | -Xmx47820m           | -Xmx47820m    |
| `mapreduce.map.memory.mb`              | 29888                | 29888         |
| `mapreduce.reduce.memory.mb`           | 59776                | 59776         |
| `yarn.app.mapreduce.am.resource.mb`    | 59776                | 59776         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 478208               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 478208               | 0             |

| x1e.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24115m           | -Xmx24115m    |
| `mapreduce.java.opts`                  | -Xmx48230m           | -Xmx48230m    |
| `mapreduce.map.memory.mb`              | 30144                | 30144         |
| `mapreduce.reduce.memory.mb`           | 60288                | 60288         |
| `yarn.app.mapreduce.am.resource.mb`    | 60288                | 60288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 964608               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 964608               | 0             |

| x1e.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24218m           | -Xmx24218m    |
| `mapreduce.java.opts`                  | -Xmx48436m           | -Xmx48436m    |
| `mapreduce.map.memory.mb`              | 30272                | 30272         |
| `mapreduce.reduce.memory.mb`           | 60544                | 60544         |
| `yarn.app.mapreduce.am.resource.mb`    | 60544                | 60544         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1937408              | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 1937408              | 0             |

| x1e.32xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24269m           | -Xmx24269m    |
| `mapreduce.java.opts`                  | -Xmx48538m           | -Xmx48538m    |
| `mapreduce.map.memory.mb`              | 30336                | 30336         |
| `mapreduce.reduce.memory.mb`           | 60672                | 60672         |
| `yarn.app.mapreduce.am.resource.mb`    | 60672                | 60672         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 3883008              | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 3883008              | 0             |

### x2gd instances

| x2gd.xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.java.opts`                  | -Xmx21708m           | -Xmx21708m    |
| `mapreduce.map.memory.mb`              | 13568                | 13568         |
| `mapreduce.reduce.memory.mb`           | 27136                | 27136         |
| `yarn.app.mapreduce.am.resource.mb`    | 27136                | 27136         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| x2gd.2xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.java.opts`                  | -Xmx23348m           | -Xmx23348m    |
| `mapreduce.map.memory.mb`              | 14592                | 14592         |
| `mapreduce.reduce.memory.mb`           | 29184                | 29184         |
| `yarn.app.mapreduce.am.resource.mb`    | 29184                | 29184         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| x2gd.4xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12083m           | -Xmx12083m    |
| `mapreduce.java.opts`                  | -Xmx24166m           | -Xmx24166m    |
| `mapreduce.map.memory.mb`              | 15104                | 15104         |
| `mapreduce.reduce.memory.mb`           | 30208                | 30208         |
| `yarn.app.mapreduce.am.resource.mb`    | 30208                | 30208         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| x2gd.8xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.java.opts`                  | -Xmx24576m           | -Xmx24576m    |
| `mapreduce.map.memory.mb`              | 15360                | 15360         |
| `mapreduce.reduce.memory.mb`           | 30720                | 30720         |
| `yarn.app.mapreduce.am.resource.mb`    | 30720                | 30720         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| x2gd.12xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.java.opts`                  | -Xmx24712m           | -Xmx24712m    |
| `mapreduce.map.memory.mb`              | 15445                | 15445         |
| `mapreduce.reduce.memory.mb`           | 30890                | 30890         |
| `yarn.app.mapreduce.am.resource.mb`    | 30890                | 30890         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30906         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30906         |

| x2gd.16xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.java.opts`                  | -Xmx24780m           | -Xmx24780m    |
| `mapreduce.map.memory.mb`              | 15488                | 15488         |
| `mapreduce.reduce.memory.mb`           | 30976                | 30976         |
| `yarn.app.mapreduce.am.resource.mb`    | 30976                | 30976         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

### x2idn instances

| x2idn.16xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.java.opts`                  | -Xmx24780m           | -Xmx24780m    |
| `mapreduce.map.memory.mb`              | 15488                | 15488         |
| `mapreduce.reduce.memory.mb`           | 30976                | 30976         |
| `yarn.app.mapreduce.am.resource.mb`    | 30976                | 30976         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

| x2idn.24xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12425m           | -Xmx12425m    |
| `mapreduce.java.opts`                  | -Xmx24850m           | -Xmx24850m    |
| `mapreduce.map.memory.mb`              | 15531                | 15531         |
| `mapreduce.reduce.memory.mb`           | 31062                | 31062         |
| `yarn.app.mapreduce.am.resource.mb`    | 31062                | 31062         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31030         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31030         |

| x2idn.32xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12442m           | -Xmx12442m    |
| `mapreduce.java.opts`                  | -Xmx24884m           | -Xmx24884m    |
| `mapreduce.map.memory.mb`              | 15552                | 15552         |
| `mapreduce.reduce.memory.mb`           | 31104                | 31104         |
| `yarn.app.mapreduce.am.resource.mb`    | 31104                | 31104         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1990656              | 31104         |
| `yarn.nodemanager.resource.memory-mb`  | 1990656              | 31104         |

### x2iedn instances

| x2iedn.xlarge                          | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx23347m           | -Xmx23347m    |
| `mapreduce.java.opts`                  | -Xmx46694m           | -Xmx46694m    |
| `mapreduce.map.memory.mb`              | 29184                | 29184         |
| `mapreduce.reduce.memory.mb`           | 58368                | 58368         |
| `yarn.app.mapreduce.am.resource.mb`    | 58368                | 58368         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 0             |

| x2iedn.2xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24166m           | -Xmx24166m    |
| `mapreduce.java.opts`                  | -Xmx48332m           | -Xmx48332m    |
| `mapreduce.map.memory.mb`              | 30208                | 30208         |
| `mapreduce.reduce.memory.mb`           | 60416                | 60416         |
| `yarn.app.mapreduce.am.resource.mb`    | 60416                | 60416         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 0             |

| x2iedn.4xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24576m           | -Xmx24576m    |
| `mapreduce.java.opts`                  | -Xmx49152m           | -Xmx49152m    |
| `mapreduce.map.memory.mb`              | 30720                | 30720         |
| `mapreduce.reduce.memory.mb`           | 61440                | 61440         |
| `yarn.app.mapreduce.am.resource.mb`    | 61440                | 61440         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 0             |

| x2iedn.8xlarge                         | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24781m           | -Xmx24781m    |
| `mapreduce.java.opts`                  | -Xmx49562m           | -Xmx49562m    |
| `mapreduce.map.memory.mb`              | 30976                | 30976         |
| `mapreduce.reduce.memory.mb`           | 61952                | 61952         |
| `yarn.app.mapreduce.am.resource.mb`    | 61952                | 61952         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 0             |

| x2iedn.16xlarge                        | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24883m           | -Xmx24883m    |
| `mapreduce.java.opts`                  | -Xmx49766m           | -Xmx49766m    |
| `mapreduce.map.memory.mb`              | 31104                | 31104         |
| `mapreduce.reduce.memory.mb`           | 62208                | 62208         |
| `yarn.app.mapreduce.am.resource.mb`    | 62208                | 62208         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1990656              | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 1990656              | 0             |

| x2iedn.24xlarge                        | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24918m           | -Xmx24918m    |
| `mapreduce.java.opts`                  | -Xmx49836m           | -Xmx49836m    |
| `mapreduce.map.memory.mb`              | 31147                | 31147         |
| `mapreduce.reduce.memory.mb`           | 62294                | 62294         |
| `yarn.app.mapreduce.am.resource.mb`    | 62294                | 62294         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 2990080              | -32           |
| `yarn.nodemanager.resource.memory-mb`  | 2990080              | -32           |

| x2iedn.32xlarge                        | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx24934m           | -Xmx24934m    |
| `mapreduce.java.opts`                  | -Xmx49868m           | -Xmx49868m    |
| `mapreduce.map.memory.mb`              | 31168                | 31168         |
| `mapreduce.reduce.memory.mb`           | 62336                | 62336         |
| `yarn.app.mapreduce.am.resource.mb`    | 62336                | 62336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 3989504              | 0             |
| `yarn.nodemanager.resource.memory-mb`  | 3989504              | 0             |

### x8g instances

| x8g.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx10854m           | -Xmx10854m    |
| `mapreduce.java.opts`                  | -Xmx21708m           | -Xmx21708m    |
| `mapreduce.map.memory.mb`              | 13568                | 13568         |
| `mapreduce.reduce.memory.mb`           | 27136                | 27136         |
| `yarn.app.mapreduce.am.resource.mb`    | 27136                | 27136         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 54272                | 27136         |
| `yarn.nodemanager.resource.memory-mb`  | 54272                | 27136         |

| x8g.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx11674m           | -Xmx11674m    |
| `mapreduce.java.opts`                  | -Xmx23348m           | -Xmx23348m    |
| `mapreduce.map.memory.mb`              | 14592                | 14592         |
| `mapreduce.reduce.memory.mb`           | 29184                | 29184         |
| `yarn.app.mapreduce.am.resource.mb`    | 29184                | 29184         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 116736               | 29184         |
| `yarn.nodemanager.resource.memory-mb`  | 116736               | 29184         |

| x8g.4xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12083m           | -Xmx12083m    |
| `mapreduce.java.opts`                  | -Xmx24166m           | -Xmx24166m    |
| `mapreduce.map.memory.mb`              | 15104                | 15104         |
| `mapreduce.reduce.memory.mb`           | 30208                | 30208         |
| `yarn.app.mapreduce.am.resource.mb`    | 30208                | 30208         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 241664               | 30208         |
| `yarn.nodemanager.resource.memory-mb`  | 241664               | 30208         |

| x8g.8xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12288m           | -Xmx12288m    |
| `mapreduce.java.opts`                  | -Xmx24576m           | -Xmx24576m    |
| `mapreduce.map.memory.mb`              | 15360                | 15360         |
| `mapreduce.reduce.memory.mb`           | 30720                | 30720         |
| `yarn.app.mapreduce.am.resource.mb`    | 30720                | 30720         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 491520               | 30720         |
| `yarn.nodemanager.resource.memory-mb`  | 491520               | 30720         |

| x8g.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12356m           | -Xmx12356m    |
| `mapreduce.java.opts`                  | -Xmx24712m           | -Xmx24712m    |
| `mapreduce.map.memory.mb`              | 15445                | 15445         |
| `mapreduce.reduce.memory.mb`           | 30890                | 30890         |
| `yarn.app.mapreduce.am.resource.mb`    | 30890                | 30890         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 741376               | 30906         |
| `yarn.nodemanager.resource.memory-mb`  | 741376               | 30906         |

| x8g.16xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12390m           | -Xmx12390m    |
| `mapreduce.java.opts`                  | -Xmx24780m           | -Xmx24780m    |
| `mapreduce.map.memory.mb`              | 15488                | 15488         |
| `mapreduce.reduce.memory.mb`           | 30976                | 30976         |
| `yarn.app.mapreduce.am.resource.mb`    | 30976                | 30976         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 991232               | 30976         |
| `yarn.nodemanager.resource.memory-mb`  | 991232               | 30976         |

| x8g.24xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12425m           | -Xmx12425m    |
| `mapreduce.java.opts`                  | -Xmx24850m           | -Xmx24850m    |
| `mapreduce.map.memory.mb`              | 15531                | 15531         |
| `mapreduce.reduce.memory.mb`           | 31062                | 31062         |
| `yarn.app.mapreduce.am.resource.mb`    | 31062                | 31062         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 1490944              | 31030         |
| `yarn.nodemanager.resource.memory-mb`  | 1490944              | 31030         |

| x8g.48xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx12458m           | -Xmx12458m    |
| `mapreduce.java.opts`                  | -Xmx24916m           | -Xmx24916m    |
| `mapreduce.map.memory.mb`              | 15573                | 15573         |
| `mapreduce.reduce.memory.mb`           | 31146                | 31146         |
| `yarn.app.mapreduce.am.resource.mb`    | 31146                | 31146         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 2990080              | 31210         |
| `yarn.nodemanager.resource.memory-mb`  | 2990080              | 31210         |

### z1d instances

| z1d.xlarge                             | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx4915m            | -Xmx4915m     |
| `mapreduce.java.opts`                  | -Xmx9830m            | -Xmx9830m     |
| `mapreduce.map.memory.mb`              | 6144                 | 6144          |
| `mapreduce.reduce.memory.mb`           | 12288                | 12288         |
| `yarn.app.mapreduce.am.resource.mb`    | 12288                | 12288         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 24576                | 12288         |
| `yarn.nodemanager.resource.memory-mb`  | 24576                | 12288         |

| z1d.2xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx5734m            | -Xmx5734m     |
| `mapreduce.java.opts`                  | -Xmx11468m           | -Xmx11468m    |
| `mapreduce.map.memory.mb`              | 7168                 | 7168          |
| `mapreduce.reduce.memory.mb`           | 14336                | 14336         |
| `yarn.app.mapreduce.am.resource.mb`    | 14336                | 14336         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 57344                | 28672         |
| `yarn.nodemanager.resource.memory-mb`  | 57344                | 28672         |

| z1d.3xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6007m            | -Xmx6007m     |
| `mapreduce.java.opts`                  | -Xmx12014m           | -Xmx12014m    |
| `mapreduce.map.memory.mb`              | 7509                 | 7509          |
| `mapreduce.reduce.memory.mb`           | 15018                | 15018         |
| `yarn.app.mapreduce.am.resource.mb`    | 15018                | 15018         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 90112                | 30040         |
| `yarn.nodemanager.resource.memory-mb`  | 90112                | 30040         |

| z1d.6xlarge                            | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6281m            | -Xmx6281m     |
| `mapreduce.java.opts`                  | -Xmx12562m           | -Xmx12562m    |
| `mapreduce.map.memory.mb`              | 7851                 | 7851          |
| `mapreduce.reduce.memory.mb`           | 15702                | 15702         |
| `yarn.app.mapreduce.am.resource.mb`    | 15702                | 15702         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 188416               | 31396         |
| `yarn.nodemanager.resource.memory-mb`  | 188416               | 31396         |

| z1d.12xlarge                           | Configuration option | Default value | With HBase installed |
| -------------------------------------- | -------------------- | ------------- | -------------------- |
| `mapreduce.map.java.opts`              | -Xmx6417m            | -Xmx6417m     |
| `mapreduce.java.opts`                  | -Xmx12834m           | -Xmx12834m    |
| `mapreduce.map.memory.mb`              | 8021                 | 8021          |
| `mapreduce.reduce.memory.mb`           | 16042                | 16042         |
| `yarn.app.mapreduce.am.resource.mb`    | 16042                | 16042         |
| `yarn.scheduler.minimum-allocation-mb` | 1                    | 1             |
| `yarn.scheduler.maximum-allocation-mb` | 385024               | 32100         |
| `yarn.nodemanager.resource.memory-mb`  | 385024               | 32100         |
