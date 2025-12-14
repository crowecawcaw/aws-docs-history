# Step 4: Configure permissions for

the VPC endpoint connection

The procedures in this step demonstrate how to configure rules and permissions for
using the VPC endpoint with Amazon Keyspaces.

###### To configure an inbound rule for the new endpoint to allow TCP inbound

traffic

1. In the Amazon VPC console, on the left-side panel, choose
   **Endpoints** and choose the endpoint you created in the
   earlier step.
2. Choose **Manage security groups** and then choose the security group
   associated with this endpoint.
3. Choose **Inbound rules** and then choose **Edit
   inbound rules**.
4. Add an inbound rule with **Type** as **CQLSH / CASSANDRA**. This sets the
   **Port range**, automatically to **9142**.
5. To save the new inbound rule, choose **Save rules**.

###### To configure IAM user permissions

1. Confirm that the IAM user used to connect to Amazon Keyspaces has the appropriate
   permissions. In AWS Identity and Access Management (IAM), you can use the AWS managed policy
   `AmazonKeyspacesReadOnlyAccess` to grant the IAM user read
   access to Amazon Keyspaces.
   1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. On the IAM console dashboard, choose **Users**, and
      then choose your IAM user from the list.
   3. On the **Summary** page, choose **Add
      permissions**.
   4. Choose **Attach existing policies directly**.
   5. From the list of policies, choose
      **AmazonKeyspacesReadOnlyAccess**, and then choose
      **Next: Review**.
   6. Choose **Add permissions**.

2. Verify that you can access Amazon Keyspaces through the VPC endpoint.

```
`aws keyspaces list-tables --keyspace-name '`my_Keyspace`'`
```

If you want, you can try some other AWS CLI commands for Amazon Keyspaces. For more
information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

###### Note

The minimum permissions required for an IAM user or role to access Amazon Keyspaces
are read permissions to the system table, as shown in the following policy.
For more information about policy-based permissions, see [Amazon Keyspaces identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:Select"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

3. Grant the IAM user read access to the Amazon EC2 instance with the VPC.

When you use Amazon Keyspaces with VPC endpoints, you need to grant the IAM user or
role that accesses Amazon Keyspaces _read-only permissions to your
Amazon EC2 instance and the VPC to gather endpoint and network interface data_. Amazon Keyspaces stores
this information in the `system.peers` table and uses it to manage
connections.

###### Note

The managed policies `AmazonKeyspacesReadOnlyAccess_v2` and
`AmazonKeyspacesFullAccess` include the required permissions to let Amazon Keyspaces
access the Amazon EC2 instance to read information about available interface VPC endpoints.

    1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
    2. On the IAM console dashboard, choose
     **Policies**.
    3. Choose **Create policy**, and then choose the
     **JSON** tab.
    4. Copy the following policy and choose **Next:
     Tags**.



    ```
    {
       "Version":"2012-10-17",
       "Statement":[
          {
             "Sid":"ListVPCEndpoints",
             "Effect":"Allow",
             "Action":[
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVpcEndpoints"
             ],
             "Resource": "*"
          }
       ]
    }
    ```
    5. Choose **Next: Review**, enter the name
     `keyspacesVPCendpoint` for the policy, and choose
     **Create policy**.
    6. On the IAM console dashboard, choose **Users**, and
     then choose your IAM user from the list.
    7. On the **Summary** page, choose **Add
     permissions**.
    8. Choose **Attach existing policies directly**.
    9. From the list of policies, choose
     **keyspacesVPCendpoint**, and then choose
     **Next: Review**.
    10. Choose **Add permissions**.

4. To verify that the Amazon Keyspaces `system.peers` table is getting updated
   with VPC information, run the following query from your Amazon EC2 instance using
   `cqlsh`. If you haven't already installed `cqlsh`on
   your Amazon EC2 instance in step 2, follow the instructions in [Using the cqlsh-expansion to connect
   to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh").

```
SELECT * FROM system.peers;
```

The output returns nodes with private IPv6 IP addresses, depending on your VPC and
subnet setup in your AWS Region.

```
`peer | data_center | host_id | preferred_ip | rack | release_version | rpc_address | schema_version | tokens
-----------------------------------------+-------------+--------------------------------------+-----------------------------------------+-----------+-----------------+-----------------------------------------+--------------------------------------+---------------------------------------------
 2600:1111:2222:3333:283b:8e6:d04f | us-east-1 | dddddddd-7a22-3582-a73d-49338a686a53 | 2600:1111:2222:3333:283b:8e6:d04f | us-east-1 | 3.11.2 | 2600:1111:2222:3333:283b:8e6:d04f | 05deae2d-6405-494d-a965-c0e5836bcb3c | {'85070591730234615865843651857942052863'}
 2600:1111:2222:4444:7d26:5a09:1b44 | us-east-1 | 66666666-035d-37ef-a247-19a6a867ab09 | 2600:1111:2222:4444:7d26:5a09:1b44 | us-east-1 | 3.11.2 | 2600:1111:2222:4444:7d26:5a09:1b44 | 05deae2d-6405-494d-a965-c0e5836bcb3c | {'170141183460469231731687303715884105726'}`
```

###### Note

You have to use a `cqlsh`connection to Amazon Keyspaces to confirm that your VPC endpoint
has been configured correctly. If you use your local environment or the Amazon Keyspaces CQL editor in the
AWS Management Console, the connection automatically goes through the public endpoint
instead of your VPC endpoint. If you see nine IP addresses, these are the entries Amazon Keyspaces
automatically writes to the `system.peers` table for public endpoint connections.
