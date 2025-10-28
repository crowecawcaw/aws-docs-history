After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Step 6: Validating network connectivity

After you’ve successfully created an outbound network connectivity between FinSpace VPC and
your VPC using transit gateway, you can validate the network configuration. To do this, run a
test to connect to a customer EC2 instance q process from an RDB cluster in the FinSpace
environment.

The following procedure shows how to connect to an RDB cluster and then connect to a q/kdb
process running on EC2 instance in the your VPC account. In this step, you will create two EC2
instances:

- **customerEc2Instance** – This is a q process to
  which the RDB would connect to.
- **clientEc2Instance** – This is a q client to
  connect to the RDB cluster.

## Create an RDB Cluster

Create an RDB cluster with a single-AZ mode by following the steps in [this](create-kdb-clusters.md "create-kdb-clusters.md") tutorial.

## Create an EC2 instance

Use the following command to create an EC2 instance with a name _customerEc2Instance_ instance to which an RDB would connect to.

```
echo '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}' > policy.json
aws iam create-role --role-name ssmrole --assume-role-policy-document file://policy.json
aws iam attach-role-policy --role-name ssmrole --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
aws iam attach-role-policy --role-name ssmrole --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
aws iam attach-role-policy --role-name ssmrole --policy-arn arn:aws:iam::aws:policy/AmazonSSMPatchAssociation
aws iam create-instance-profile --instance-profile-name "SSMRole"
aws iam add-role-to-instance-profile --instance-profile-name SSMRole --role-name ssmrole

aws ec2 run-instances \
--count 1 \
--instance-type t2.micro \
--security-group-ids <SecurityGroup>\
--subnet-id <SUBNET> \
--iam-instance-profile Name=SSMRole \
--tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=CustomerEc2Instance}]" \
--image-id $(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-2 | jq ".Parameters[0].Value" -r) \
--metadata-options "HttpEndpoint=enabled,HttpTokens=required"

```

## Start a q process and listen on port 5005

1. Connect to the _CustomerEc2Instance_ instance. For more
   information, see [this](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md#session-manager "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md#session-manager") section.
2. Install the q client. For more information on installation, see [Installing kdb+](https://code.kx.com/q/learn/install/ "https://code.kx.com/q/learn/install/").
3. Launch a q process and run the following command to listen on port _5005_.

```
q) \p 5005
```

## Create another EC2 instance

Create another instance with a name _clientEc2Instance_, which you can use to connect to the RDB cluster. The EC2
instance should use the same security group and subnet that you chose for the cluster.

```
aws ec2 run-instances \
--count 1 \
--instance-type t2.micro \
--security-group-ids <security group> \
--subnet-id <SUBNET> \
--iam-instance-profile Name=SSMRole \
--tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=Bastion}]" \
--image-id $(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1 | jq ".Parameters[0].Value" -r) \
--metadata-options "HttpEndpoint=enabled,HttpTokens=required"

```

## Test the connection

Test the connection from q process on
EC2 instance to the RDB cluster.

Create an RDB cluster with a single-AZ mode by following the steps in [this](create-kdb-clusters.md "create-kdb-clusters.md") tutorial.

1. Connect to the _clientEc2Instance_ by
   following the steps in
   [this](../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md#session-manager "../../../AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.md#session-manager")
   section.
2. Install the q client. For more information on installation, see
   [Installing
   kdb+](https://code.kx.com/q/learn/install/ "https://code.kx.com/q/learn/install/").
3. Start a q process and connect to the RDB cluster on port _5005_ by using the following example command.

```
q)cs_rdb1: <RDB cluster connection string> 
            q)cs_rdb1: ssr[cs_rdb1;"\n";""] 
            q)conn: hopen cs_rdb1 
            q)conn hopen(":<Private IP DNS name
            of **customerEc2Instance**
            5005"; 10)
```

The following section explains the sample code:

    * *cs\_rdb1* has a cluster connection string. For more information
     on how to get a connection string, see the [Interacting with a kdb cluster](interacting-with-kdb-clusters.md "interacting-with-kdb-clusters.md") section.
    * *hopen* command opens a connection to the RDB cluster and gets
     a connection handle.
    * Use connection handle to run *hopen* connection test to
     the *customerEc2Instance* q process listening on port
     *5005* to test connectivity from RDB cluster
     to *customerEc2Instance*.

You should be able to successfully connect to port _5005_.

Repeat
the steps for [starting a q process](#step6c-start-q "#step6c-start-q") and [testing connection](#step6e-test-connection "#step6e-test-connection") with port
_5006_. You will fail to connect because only port _5005_ is allowed in the in-bound rules of the security groups.
