# Configure Amazon EMR cluster hardware and networking

An important consideration when you create an Amazon EMR cluster is how you configure Amazon EC2
instances and network options. This chapter covers the following options, and then ties them
all together with [best practices and
guidelines](emr-plan-instances-guidelines.md "emr-plan-instances-guidelines.md").

- **Node types** – Amazon EC2 instances in an EMR
  cluster are organized into _node types_. There are three:
  _primary nodes_, _core
  nodes_, and _task nodes_. Each node
  type performs a set of roles defined by the distributed applications that you
  install on the cluster. During a Hadoop MapReduce or Spark job, for example,
  components on core and task nodes process data, transfer output to Amazon S3 or HDFS, and
  provide status metadata back to the primary node. With a single-node cluster, all
  components run on the primary node. For more information, see [Understand node types in Amazon EMR:
  primary, core, and task nodes](emr-master-core-task-nodes.md "emr-master-core-task-nodes.md").
- **EC2 instances** – When you create a cluster,
  you make choices about the Amazon EC2 instances that each type of node will run on. The
  EC2 instance type determines the processing and storage profile of the node. The
  choice of Amazon EC2 instance for your nodes is important because it determines the
  performance profile of individual node types in your cluster. For more information,
  see [Configure Amazon EC2 instance types for use with Amazon EMR](emr-plan-ec2-instances.md "emr-plan-ec2-instances.md").
- **Networking** – You can launch your Amazon EMR
  cluster into a VPC using a public subnet, private subnet, or a shared subnet. Your
  networking configuration determines how customers and services can connect to
  clusters to perform work, how clusters connect to data stores and other AWS
  resources, and the options you have for controlling traffic on those connections.
  For more information, see [Configure networking in a VPC for Amazon EMR](emr-plan-vpc-subnet.md "emr-plan-vpc-subnet.md").
- **Instance grouping** – The collection of EC2
  instances that host each node type is called either an _instance
  fleet_ or a _uniform instance group_. The instance
  grouping configuration is a choice you make when you create a cluster. This choice
  determines how you can add nodes to your cluster while it is running. The
  configuration applies to all node types. It can't be changed later. For more
  information, see [Create an Amazon EMR cluster with instance
  fleets or uniform instance groups](emr-instance-group-configuration.md "emr-instance-group-configuration.md").

###### Note

The instance fleets configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.0 and 5.0.3.
