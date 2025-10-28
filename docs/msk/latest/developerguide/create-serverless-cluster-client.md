# Create a client machine to access MSK

Serverless cluster

In the step, you perform two tasks. The first task is to create an Amazon EC2 instance to
use as an Apache Kafka client machine. The second task is to install Java and Apache
Kafka tools on the machine.

###### To create a client machine

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch instance**.
3. Enter a descriptive **Name** for your client machine, such as
   `msk-serverless-tutorial-client`.
4. Leave the **Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume
   Type** selected for **Amazon Machine Image (AMI)
   type**.
5. Leave the **t2.micro** instance type selected.
6. Under **Key pair (login)**, choose **Create a new key
   pair**. Enter `MSKServerlessKeyPair` for
   **Key pair name**. Then choose **Download Key
   Pair**. Alternatively, you can use an existing key pair.
7. For **Network settings**, choose
   **Edit**.
8. Under **VPC**, enter the ID of the virtual private cloud
   (VPC) for your serverless cluster . This is the VPC based on the Amazon VPC service
   whose ID you saved after you created the cluster.
9. For **Subnet**, choose the subnet whose ID you saved after you created the cluster.
10. For **Firewall (security groups)**, select the security group
    associated with the cluster. This value works if that security group has an
    inbound rule that allows traffic from the security group to itself. With such a
    rule, members of the same security group can communicate with each other. For
    more information, see [Security group rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the Amazon VPC Developer Guide.
11. Expand the **Advanced details** section and choose the IAM
    role that you created in [Create an IAM role for topics on MSK Serverless
    cluster](create-iam-role.md "create-iam-role.md").
12. Choose **Launch**.
13. In the left navigation pane, choose **Instances**. Then
    choose the check box in the row that represents your newly created Amazon EC2
    instance. From this point forward, we call this instance the _client
    machine_.
14. Choose **Connect** and follow the instructions to connect
    to the client machine.

###### To set up Apache Kafka client tools on the client machine

1. To install Java, run the following command on the client machine:

```
sudo yum -y install java-11
```

2. To get the Apache Kafka tools that we need to create topics and send data, run the following
   commands:

```
wget https://archive.apache.org/dist/kafka/2.8.1/kafka_2.12-2.8.1.tgz
```

```
tar -xzf kafka_2.12-2.8.1.tgz
```

###### Note

After extracting the Kafka archive, make sure that the scripts in the `bin` directory have proper execute permissions. To do this, run the following command.

```
chmod +x kafka_2.12-2.8.1/bin/*.sh
```

3. Go to the `kafka_2.12-2.8.1/libs` directory, then run the following command
   to download the Amazon MSK IAM JAR file. The Amazon MSK IAM JAR makes it possible for
   the client machine to access the cluster.

```
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v2.3.0/aws-msk-iam-auth-2.3.0-all.jar
```

Using this command, you can also [download other or newer versions](https://github.com/aws/aws-msk-iam-auth/releases "https://github.com/aws/aws-msk-iam-auth/releases") of Amazon MSK IAM JAR file. 4. Go to the `kafka_2.12-2.8.1/bin` directory. Copy the
following property settings and paste them into a new file. Name the file
`client.properties` and save it.

```
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

**Next Step**

[Create an Apache Kafka topic](msk-serverless-create-topic.md "msk-serverless-create-topic.md")
