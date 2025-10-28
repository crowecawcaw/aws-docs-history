# The open-source graph-explorer

[Graph-explorer](https://github.com/aws/graph-explorer "https://github.com/aws/graph-explorer") is an
open-source low-code visual exploration tool for graph data, available under the
Apache-2.0 license. It lets you browse either labeled property graphs (LPG)
or Resource Description Framework (RDF) data in a graph database without having
to write graph queries. Graph-explorer is intended to help data scientists,
business analysts, and other roles in an organization explore graph data
interactively without having to learn a graph query language.

Graph-explorer provides a React-based web application that can be deployed
as a container to visualize graph data. You can connect to Amazon Neptune or
to other graph databases that provide an Apache TinkerPop Gremlin or
SPARQL 1.1 endpoint.

- You can quickly see a summary of the data using the faceted
  filters, or search the data by typing text into the search bar.
- You can also interactively explore node and edge connections.
  You can view node neighbors to see how objects relate to each other, and then
  drill down to inspect edges and properties visually.
- You can also customize the graph layout, colors, icons, and
  which default properties to display for nodes and edges. For RDF graphs,
  you can customize namespaces for resource URIs too.
- For reports and presentations involving graph data, you
  can configure and save views you've created in a high-resolution PNG
  format. You can also download the associated data into a CSV or JSON
  file for further processing.

## Using graph-explorer in a Neptune graph notebook

The easiest way to use graph-explorer with Neptune is in a [Neptune graph notebook](graph-notebooks.md "graph-notebooks.md").

If you [use Neptune workbench to host a
Neptune notebook](graph-notebooks.md#graph-notebooks-workbench "graph-notebooks.md#graph-notebooks-workbench"), graph-explorer is automatically deployed with the notebook
and connected to Neptune.

After you have created a notebook, go to the Neptune console to start graph-explorer:

1. Go to **Neptune**.
2. Under **Notebooks**, select your notebook.
3. Under Actions choose **Open Graph Explorer**.

## How to run graph-explorer in Amazon ECS on

AWS Fargate and connect to Neptune

You can also build the graph-explorer Docker image and run it on a local
machine or a hosted service like [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
or [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/"), as
explained in the [Getting
Started](https://github.com/aws/graph-explorer#getting-started "https://github.com/aws/graph-explorer#getting-started") section of the read-me in the [graph-explorer GitHub project](https://github.com/aws/graph-explorer "https://github.com/aws/graph-explorer").

As an example, this section provides step-by-step instructions for running graph-explorer
in Amazon ECS on AWS Fargate:

1.  Create a new IAM role and attach these policies to it:

        * [AmazonECSTaskExecutionRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy")
        * [CloudWatchLogsFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLogsFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/CloudWatchLogsFullAccess")

    Keep the role name handy to use in a minute.

2.  [Create
    an Amazon ECS cluster](../../../AmazonECS/latest/developerguide/create-cluster-console-v2.md "../../../AmazonECS/latest/developerguide/create-cluster-console-v2.md") with the infrastructure set to FARGATE and the following networking options:
    - `VPC`: set to the VPC where your Neptune database is located.
    - `Subnets`: set to the public subnets of that VPC (remove all others).

3.  Create a new JSON task definition as follows:

```
{
  "family": "explorer-test",
  "containerDefinitions": [
    {
      "name": "graph-explorer",
      "image": "public.ecr.aws/neptune/graph-explorer:latest",
      "cpu": 0,
      "portMappings": [
        {
          "name": "graph-explorer-80-tcp",
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp",
          "appProtocol": "http"
        },
        {
          "name": "graph-explorer-443-tcp",
          "containerPort": 443,
          "hostPort": 443,
          "protocol": "tcp",
          "appProtocol": "http"
        }
      ],
      "essential": true,
      "environment": [
        {
          "name": "HOST",
          "value": "localhost"
        }
      ],
      "mountPoints": [],
      "volumesFrom": [],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-create-group": "true",
          "awslogs-group": "/ecs/graph-explorer",
          "awslogs-region": "{region}",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ],
  "taskRoleArn": "arn:aws:iam::{account_no}:role/{role_name_from_step_1}",
  "executionRoleArn": "arn:aws:iam::{account_no}:role/{role_name_from_step_1}",
  "networkMode": "awsvpc",
  "requiresCompatibilities": [
    "FARGATE"
  ],
  "cpu": "1024",
  "memory": "3072",
  "runtimePlatform": {
    "cpuArchitecture": "X86_64",
    "operatingSystemFamily": "LINUX"
  }
}
```

4. Start a new task using the default settings, except for the following fields:
   - **Environment**
     - Compute options => **Launch type**

   - **Deployment configuration**
     - Application Type => **Task**
     - Family => `(your new JSON task definition)`
     - Revision => `(latest)`

   - **Networking**
     - VPC => `(the Neptune VPC you want to connect to)`
     - Subnets => `(ONLY the public subnets of the VPC– remove all others)`
     - Security group => **Create a new security group**
     - Security group name => graph-explorer
     - Security group description = Security group for access to graph-explorer
     - Inbound rules for security groups =>
       1. 80 Anywhere
       2. 443 Anywhere

5. Select **Create**.
6. After the task starts, copy the public IP of the running task, and navigate to:
   `https://`(your public IP)`/explorer`.
7. Accept risk of using the unrecognized certificate that has been generated, or add it
   to your key chain.
8. Now you can add a connection to Neptune. Create a new connection, either for
   a property graph (LPG) or for RDF, and set the following fields:

```
Using proxy server => `true`
Public or Proxy Endpoint => https://`(your public IP address)`
Graph connection URL => https://`(your Neptune endpoint)`:8182
```

You should now be connected.

## Graph-explorer demonstration

This brief video gives you some idea of how you can easily visualize your
graph data using graph-explorer:

![Graph-explorer text-only demo video](/images/neptune/latest/userguide/images/graph-explorer.gif)
