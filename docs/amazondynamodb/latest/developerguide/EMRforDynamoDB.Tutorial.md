# Step 1: Create an Amazon EC2 key

pair

In this step, you will create the Amazon EC2 key pair you need to connect to an Amazon EMR
leader node and run Hive commands.

1. Sign in to the AWS Management Console and open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose a region (for example, `US West (Oregon)`). This should
   be the same region in which your DynamoDB table is located.
3. In the navigation pane, choose **Key Pairs**.
4. Choose **Create Key Pair**.
5. In **Key pair name**, type a name for your key pair (for
   example, `mykeypair`), and then choose
   **Create**.
6. Download the private key file. The file name will end with
   `.pem` (such as `mykeypair.pem`). Keep this
   private key file in a safe place. You will need it to access any Amazon EMR
   cluster that you launch with this key pair.

###### Important

If you lose the key pair, you cannot connect to the leader node
of your Amazon EMR cluster.

For more information about key pairs, see [Amazon EC2 Key Pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide_.

###### Next step

[Step 2: Launch an Amazon EMR
cluster](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
