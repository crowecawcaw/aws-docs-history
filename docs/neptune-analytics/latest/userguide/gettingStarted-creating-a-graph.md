# Create an empty Neptune graph

Neptune allows you to create and manage graph databases. This step-by-step guide
outlines the process of creating an empty Neptune graph using the AWS management console, the AWS CLI, and
AWS CloudFormation. The guide covers the necessary configurations, such as setting the graph name, size, replica
configuration, and network connectivity options.

AWS console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at
   [https://console.aws.amazon.com/neptune/](https://console.aws.amazon.com/neptune/ "https://console.aws.amazon.com/neptune/").
2. In the upper right corner of the console, choose the AWS region in which you want to create the graph.
3. In the navigation pane, choose **Graphs** in the **Analytics**
   section.
4. Choose the **Create graph** button.
5. In **settings**, input the **graph name**, size, and replica
   configuration.
6. In the **data source** section, choose the **empty graph**
   option.

###### Note

Additional charges equivalent to the m-NCUs selected for the graph apply for each replica.

![Image showing the AWS console, with the available options and settings configurations.](images/getting-started/gettingStartedStep6.png) 7. You can connect to a Neptune graph from a public endpoint or a private endpoint. Select your
network configuration accordingly.

###### Note

If you're creating a private graph endpoint, the following permissions are required:

    * ec2:CreateVpcEndpoint

    * ec2:DescribeAvailabilityZones

    * ec2:DescribeSecurityGroups

    * ec2:DescribeSubnets

    * ec2:DescribeVpcAttribute

    * ec2:DescribeVpcEndpoints

    * ec2:DescribeVpcs

    * ec2:ModifyVpcEndpoint

    * route53:AssociateVPCWithHostedZone

For more information about required permissions, see
[Actions defined by Neptune Analytics](../../../service-authorization/latest/reference/list_amazonneptuneanalytics.md#amazonneptuneanalytics-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonneptuneanalytics.md#amazonneptuneanalytics-actions-as-permissions").

![Image showing the AWS console, with the available options and settings configurations.](images/getting-started/gettingStartedStep7.png) 8. Additionally, you can select vector search configuration for the graph. For more information on
vector search configuration, see [Vector indexing](vector-index.md "vector-index.md"). 9. Choose **Create graph**.

AWS CLI

Create a Neptune graph using the AWS
[CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/create-graph.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/create-graph.html").

Create a public graph endpoint:

```
aws neptune-graph create-graph --graph-name 'test-neptune-graph' \
--region us-east-1 --provisioned-memory 128  --public-connectivity \
--replica-count 0 --vector-search '{"dimension": 384}'
```

Create a private graph endpoint:

```
aws neptune-graph create-private-graph-endpoint —vpc-id vpc-0a9b7a5b15 \
--subnet-ids subnet-06a4b41a6221b subnet-0840a4b327ab77 subnet-0353627ab123 \
--vpc-security-group-ids sg-0ab7abab56ab \
--graph-identifier g-146a51b7a151ba —region us-east-1
```

Check the status of graph creation:

```
aws neptune-graph get-graph --graph-identifier <graph-id>
```

List all graphs in the default region:

```
aws neptune-graph list-graphs
```

AWS CloudFormation

Instead of using the console to create your Neptune graph, you can use AWS CloudFormation to provision AWS resources
by treating infrastructure as code. To help you organize your AWS resources into smaller and more
manageable units, you can use the AWS CloudFormation nested stack functionality. For more information, see
[Creating a stack on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md") and [working with nested stacks](../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.md").

AWS CloudFormation is free, but the resources that CloudFormation creates are live. You incur the standard usage fees
for these resources until you terminate them. The total charges will be minimal. For information about
how you might minimize any charges, see [AWS free tier](http://aws.amazon.com/free/ "http://aws.amazon.com/free/").

To create your resources using the AWS CloudFormation console, complete the following steps:

1. Create the CloudFormation template.
2. Configure your resources using CloudFormation.

The following sample template will create a Neptune graph with a public endpoint.

```
AWSTemplateFormatVersion: 2010-09-09
Description: NeptuneGraph Graph Create Demo using CloudFormation
Resources:
  NeptuneGraph:
    Type: AWS::NeptuneGraph::Graph
    DeletionPolicy: Delete
    Properties:
      DeletionProtection: false
      GraphName: neptune-graph-demo
      ProvisionedMemory: 128
      ReplicaCount: 1
      PublicConnectivity: true
      Tags:
        - Key: stage
          Value: test
```

The following sample template will create a Neptune graph with a private endpoint.

```
AWSTemplateFormatVersion: 2010-09-09
Description: NeptuneGraph Graph Create Demo using CloudFormation
Resources:
  NeptuneGraph:
    Type: AWS::NeptuneGraph::Graph
    DeletionPolicy: Delete
    Properties:
      DeletionProtection: false
      GraphName: neptune-graph-demo
      ProvisionedMemory: 128
      ReplicaCount: 1
      PublicConnectivity: false
      Tags:
        - Key: stage
          Value: test
  NeptuneGraphPrivateEndpoint:
    Type: AWS::NeptuneGraph::PrivateGraphEndpoint
    DeletionPolicy: Delete
    Properties:
      GraphIdentifier: NeptuneGraph
      VpcId: myVpc
```

###### Important

You can't change the graph name, VPC, subnet ids and vector search configuration. After starting the
graph creation, the graph has a status of **Creating** until the graph
is ready to use. When the status of the graph changes to **Available**,
you can connect to the DB cluster at that time. Depending on the configuration, it can take up to
20 minutes before the new graph is available.
