# Configuring AWS DMS secrets

manager VPC Endpoint

You must create a VPC endpoint to access the AWS Secrets Manager from a
replication instance in a private subnet. This allows the replication instance
access the Secrets Manager directly through the private network without sending
traffic over the public internet.

To configure, you must follow the following steps:

###### Create a security group for the VPC endpoint.

1. Navigate to the [Amazon
   VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane on the left, select **Security
   groups**, and choose **Create security
   group**.
3. Configure security group details:
   - **Security group name**: Example:
     `SecretsManagerEndpointSG`
   - **Description**: Enter an appropriate
     description. (Example: Security group for secrets manager VPC
     endpoint).
   - **VPC**: Select the VPC where your
     replication instance and endpoints reside.

4. Click **Add Rule** to set inbound rules and configure the
   following:
   - Type: HTTPS (As the secrets manager uses HTTPS on port
     443).
   - Source: Choose **Custom**, and enter the securty
     group ID of your replication instance. This ensures that any
     instance associated with that security group can access the VPC
     endpoint.

5. Review the changes and click **Create security
   group**.

###### Create a VPC endpoint for secrets manager

###### Note

Create an interface VPC endpoint as outline in the [Creating an Interface Endpoint documentation](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") topic in the
_Amazon Virtual Private Cloud user
guide_. When following this procedure, ensure the
following:

- For **Service Category**, you should select
  **AWS services.**
- For **Service name**, search
  `seretsmanager` and select the secretes manager
  service.

1. Select **VPC and Subnets** and configure the
   following:
   - **VPC**: Ensure it is the same VPC as
     your replication instance.
   - **Subnets**: Select the subnets where
     your replication instance resides.

2. In **Additional Settings**, ensure that the
   **Enable DNS name** is enabled by default for the
   interface endpoints
3. Under **Security group**, select the appropriate security
   group name. Example: `SecretsManagerEndpointSG` as created
   earlier).
4. Review all the settings and Click **Create
   endpoint**.

###### Retrieve the VPC endpoint DNS name

1. Access the VPC endpoint details:
   1. Navigate to the [Amazon VPC console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") and choose
      **Endpoints**.
   2. Select the appropriate endpoint you created.

2. Copy the DNS name:
   1. Under the **Details** tab, navigate to the
      **DNS Names** section.
   2. Copy the first DNS name listed. (Example:
      `vpce-0abc123def456789g-secretsmanager.us-east-1.vpce.amazonaws.com`).
      This is the regional DNS name.

###### Update your DMS endpoint

1. Navigate to the [AWS DMS](https://console.aws.amazon.com/dms/v2 "https://console.aws.amazon.com/dms/v2") console.
2. Modify the DMS endpoint:
   1. In the navigation pane on the left, select
      **Endpoints**.
   2. Choose the appropriate endpoint you want to configure.
   3. Click **Actions** and select
      **Modify**.

3. Configure endpoint settings:
   1. Navigate to **Endpoint settings** and select
      **Use endpoint connection attributes**
      checkbox.
   2. In the **Connection attributes** field, add:
      `secretsManagerEndpointOverride=<copied DNS
name>`.

   ###### Note

   If you have multiple connection attributes, you can separate
   them with a semicolon ";". For example:
   `datePartitionEnabled=false;secretsManagerEndpointOverride=vpce-0abc123def456789g-secretsmanager.us-east-1.vpce.amazonaws.com`

4. Click **Modify endpoint** to save your changes.
