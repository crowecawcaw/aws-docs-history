

# Prerequisites for connecting from Amazon EKS to Amazon Keyspaces
<a name="EKS-tutorial-prerequisites"></a>

**Create the following AWS resources before you can begin with the tutorial**

1. Before you start this tutorial, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md). These steps include signing up for AWS and creating an AWS Identity and Access Management (IAM) principal with access to Amazon Keyspaces. 

1. Create an Amazon Keyspaces keyspace with the name `aws` and a table with the name `user` that you can write to from the containerized application running in Amazon EKS later in this tutorial. You can do this either with the AWS CLI or using `cqlsh`.

------
#### [ AWS CLI ]

   ```
   aws keyspaces create-keyspace --keyspace-name '{{aws}}'
   ```

   To confirm that the keyspace was created, you can use the following command.

   ```
   aws keyspaces list-keyspaces
   ```

   To create the table, you can use the following command.

   ```
   aws keyspaces create-table --keyspace-name '{{aws}}' --table-name '{{user}}' --schema-definition 'allColumns=[
               {name=username,type=text}, {name=fname,type=text},{name=last_update_date,type=timestamp},{name=lname,type=text}],
               partitionKeys=[{name=username}]'
   ```

   To confirm that your table was created, you can use the following command.

   ```
   aws keyspaces list-tables --keyspace-name '{{aws}}'
   ```

   For more information, see [create keyspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/create-keyspace.html) and [create table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/create-table.html) in the *AWS CLI Command Reference*.

------
#### [ cqlsh ]

   ```
   CREATE KEYSPACE {{aws}} WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}  AND durable_writes = true;
   CREATE TABLE {{aws.user}} (
       username text PRIMARY KEY,
       fname text,
       last_update_date timestamp,
       lname text
   );
   ```

   To verify that your table was created, you can use the following statement.

   ```
   SELECT * FROM system_schema.tables WHERE keyspace_name = "{{aws}}";
   ```

   Your table should be listed in the output of this statement. Note that there can be a delay until the table is created. For more information, see [CREATE TABLE](cql.ddl.table.md#cql.ddl.table.create).

------

1. Create an Amazon EKS cluster with a **Fargate - Linux ** node type. Fargate is a serverless compute engine that lets you deploy Kubernetes Pods without managing Amazon Amazon EC2 instances. To follow this tutorial without having to update the cluster name in all the example commands, create a cluster with the name `my-eks-cluster` following the instructions at [Getting started with Amazon EKS – `eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) in the *Amazon EKS User Guide*. When your cluster is created, verify that your nodes and the two default Pods are running and healthy. You can do so with the following command.

   ```
   kubectl get pods -A -o wide
   ```

   You should see something similar to this output.

   ```
   NAMESPACE     NAME                       READY   STATUS    RESTARTS   AGE   IP          NODE                                                NOMINATED NODE   READINESS GATES
   kube-system   coredns-1234567890-abcde   1/1     Running   0          18m   192.0.2.0   fargate-ip-192-0-2-0.region-code.compute.internal   <none>           <none>
   kube-system   coredns-1234567890-12345   1/1     Running   0          18m   192.0.2.1   fargate-ip-192-0-2-1.region-code.compute.internal   <none>           <none>
   ```

1. Install Docker. For instructions on how to install Docker on an Amazon EC2 instance, see [Install Docker](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html#getting-started-cli-prereqs) in the Amazon Elastic Container Registry User Guide. 

   Docker is available for many different operating systems, including most modern Linux distributions, like Ubuntu, and even macOS and Windows. For more information about how to install Docker on your particular operating system, go to the [Docker installation guide](https://docs.docker.com/engine/install/#installation). 

1. Create an Amazon ECR repository. Amazon ECR is an AWS managed container image registry service that you can use with your preferred CLI to push, pull, and manage Docker images. For more information about Amazon ECR repositories, see the [Amazon Elastic Container Registry User Guide](https://docs.aws.amazon.com/AmazonECR/latest/userguide/). You can use the following command to create a repository with the name `my-ecr-repository`.

   ```
   aws ecr create-repository --repository-name {{my-ecr-repository}}
   ```

After completing the prerequisite steps, proceed to [Step 1: Configure the Amazon EKS cluster and setup IAM permissions](EKS-tutorial-step1.md).