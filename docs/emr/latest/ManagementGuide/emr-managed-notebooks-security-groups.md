# Specifying EC2 security groups

for EMR Notebooks

When you create an EMR notebook, two security groups are used to control
network traffic between the EMR notebook and the Amazon EMR cluster when you use the
notebook editor. The default security groups have minimal rules that allow only network
traffic between the EMR Notebooks service and the clusters to which notebooks are
attached.

An EMR notebook uses [Apache Livy](https://livy.incubator.apache.org/ "https://livy.incubator.apache.org/") to communicate with the cluster via a
proxy through TCP Port 18888. When you create custom security groups with rules that you
tailor to your environment, you can limit network traffic so that only a subset of
notebooks can run code within the notebook editor on particular clusters. The cluster
uses your custom security in addition to the default security groups for the cluster.
For more information, see [Control
network traffic with security groups](emr-security-groups.md "emr-security-groups.md") in the
_Amazon EMR Management Guide_ and Specifying EC2 security groups
for EMR Notebooks.

## Default EC2 security group for the

primary instance

The default EC2 security group for the primary instance is associated with the
primary instance in addition to the cluster's security groups for the primary
instance.

Group Name: **ElasticMapReduceEditors-Livy**

**Rules**

- Inbound

Allow TCP Port 18888 from any resources in the default EC2 security group
for EMR Notebooks

- Outbound

None

## Default EC2

security group for EMR Notebooks

The default EC2 security group for the EMR notebook is associated with the
notebook editor for any EMR notebook to which it is assigned.

Group Name: **ElasticMapReduceEditors-Editor**

**Rules**

- Inbound

None

- Outbound

Allow TCP Port 18888 to any resources in the default EC2 security group
for EMR Notebooks.

## Custom EC2

security group for EMR Notebooks when associating Notebooks with Git
repositories

To link a Git repository to your notebook, the security group for the
EMR notebook must include an outbound rule so that the notebook can route
traffic to the internet. It is recommended that you create a new security group for
this purpose. Updating the default
**ElasticMapReduceEditors-Editor** security group may give the
same outbound rules to other notebooks that are attached to this security group.

**Rules**

- Inbound

None

- Outbound

Allow the notebook to route traffic to the internet via the cluster, as
the following example demonstrates. The value 0.0.0.0/0 is used for example
purposes. You can modify this rule to specify the IP address(es) for your
Git-based repositories.

| Type            | Protocol | Port range | Destination   |
| --------------- | -------- | ---------- | ------------- |
| Custom TCP rule | TCP      | 18888      | SG-           |
| **HTTPS**       | **TCP**  | **443**    | **0.0.0.0/0** |
