# Step 2: Create a key pair

To enable your end users to launch the product that is based on the sample template for this
tutorial, you must create an Amazon EC2 key pair. A key pair is a combination of a public key that is
used to encrypt data and a private key that is used to decrypt data. For more information about
key pairs, ensure you are signed into the AWS console and then review [Amazon EC2 Key Pairs](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") in the
_Amazon EC2 User Guide_.

The AWS CloudFormation template for this tutorial, `development-environment.template`,
includes the `KeyName` parameter:

```
. . .
  "Parameters" : {
    "KeyName": {
      "Description" : "Name of an existing EC2 key pair for SSH access to the EC2 instance.",
      "Type": "AWS::EC2::KeyPair::KeyName"
    },
. . .
```

End users must specify the name of a key pair when they use AWS Service Catalog to launch the product that
is based on the template.

If you already have a key pair in your account that you would prefer to use, you can skip
ahead to [Step 3: Create a portfolio](getstarted-portfolio.md "getstarted-portfolio.md"). Otherwise,
complete the following steps.

###### To create a key pair

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Network & Security**, choose
   **Key Pairs**.
3. On the **Key Pairs** page, choose **Create Key
   Pair**.
4. For **Key pair name**, type a name that is easy for you to remember,
   and then choose **Create**.
5. When the console prompts you to save the private key file, save it in a safe
   place.

###### Important

This is the only chance for you to save the private key file.
