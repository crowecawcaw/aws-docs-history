

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Create VPC endpoints
<a name="vpc-endpoints"></a>

You can create a VPC endpoint for AWS Wickr Admin, Messaging, and Calling.

**Complete the following procedure to create a VPC endpoint using AWS Console.**

**Step 1: Navigate to VPC Console**

1. Sign in to the [Amazon VPC Console](https://us-east-2.signin.aws.amazon.com).

1. In the left navigation pane, choose **Endpoints**.

1. Choose **Create Endpoint**.

**Step 2: Configure Endpoint Settings**

1. Under **Service Category**, select **AWS services.**

1. Under **Service Name**, search for `wickr` and select the appropriate service:
   + **For Admin**: `com.amazonaws.{{your-region}}.wickr-admin`
   + **For Messaging**: `com.amazonaws.{{your-region}}.wickr-messaging`
   + **For Calling**: `com.amazonaws.{{your-region}}.wickr-calling`

**Step 3: Network Configuration**

1. Under **VPC**, select your target VPC.

1. Under **Subnets**, choose subnets in multiple Availability Zones for high availability.

1. Under **Enable private DNS name**, select the checkbox. This enables support to private DNS names.

1. Under **Security Groups**, select or create security groups you want to associate with the endpoint network interfaces.

**Step 4: Create Endpoint**

1. Review your configuration.

1. Optionally, you can add or remove tags. Tags are name-value pairs that you use to associate with your endpoint.

1. Choose **Create Endpoint**.

**Complete the following procedure to create a VPC endpoint using AWS CLI.**

1. Check service availability in your region:

   **Check Wickr Admin availability**

   ```
   aws ec2 describe-vpc-endpoint-services --service-names com.amazonaws.{{your-region}}.wickr-admin
   ```

   **Check Wickr Messaging availability**

   ```
   aws ec2 describe-vpc-endpoint-services --service-names com.amazonaws.{{your-region}}.wickr-messaging
   ```

   **Check Wickr Calling availability**

   ```
   aws ec2 describe-vpc-endpoint-services --service-names com.amazonaws.{{your-region}}.wickr-calling
   ```

1. Create VPC endpoints.

   **Wickr Admin Endpoint**:

   ```
   aws ec2 create-vpc-endpoint \
     --vpc-endpoint-type Interface \
     --service-name com.amazonaws.{{your-region}}.wickr-admin \
     --subnet-ids {{subnet-12345678 subnet-87654321 subnet-11223344}} \
     --vpc-id {{vpc-12345678}} \
     --security-group-ids {{sg-12345678}} \
     --private-dns-enabled \
   ```

   **Wickr Messaging Endpoint**

   ```
   aws ec2 create-vpc-endpoint \
     --vpc-endpoint-type Interface \
     --service-name com.amazonaws.{{your-region}}.wickr-messaging \
     --subnet-ids {{subnet-12345678 subnet-87654321 subnet-11223344}} \
     --vpc-id {{vpc-12345678}} \
     --security-group-ids {{sg-12345678}} \
     --private-dns-enabled \
   ```

   **Wickr Calling Endpoint**

   ```
   aws ec2 create-vpc-endpoint \
     --vpc-endpoint-type Interface \
     --service-name com.amazonaws.{{your-region}}.wickr-calling \
     --subnet-ids {{subnet-12345678 subnet-87654321 subnet-11223344}} \
     --vpc-id {{vpc-12345678}} \
     --security-group-ids {{sg-12345678}} \
     --private-dns-enabled \
   ```