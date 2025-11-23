# Create an App Block Builder

You can use app block builder instance to create your application package for WorkSpaces Applications
Elastic fleets.

###### To create an app block builder

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. Choose **Applications Manager** in the left navigation pane,
   then choose the **App block builders** tab and **Create
   app block builder**.
3. For **Step 1: Configure app block builder**, configure the
   app block builder by providing the following details:
   - **Name**: Type a unique name identifier for the app block builder.
   - **Display name (optional)**: Type a name to display for the app block builder
     (maximum of 100 characters).
   - **Operating system**: Select an operating system for
     your application. This must align with the operating system that you are
     going to select for you elastic fleet, which your end users will use to
     stream the application.
   - **IAM role (Optional)**: When you apply an IAM
     role from your account to an WorkSpaces Applications app block builder, you can make
     AWS API requests from the app block builder instance without manually
     managing AWS credentials. To apply an IAM role to the app block
     builder, do either of the following:
     - To use an existing IAM role in your Amazon Web Services account,
       choose the role that you want to use from the **IAM
       role** list. The role must must be accessible from
       the image builder. For more information, see [Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances](configuring-existing-iam-role-to-use-with-streaming-instances.md "configuring-existing-iam-role-to-use-with-streaming-instances.md").
     - To create a new IAM role, choose **Create new IAM
       role** and follow the steps in [How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances](how-to-create-iam-role-to-use-with-streaming-instances.md "how-to-create-iam-role-to-use-with-streaming-instances.md").

   - **Instance Type**: Select the instance type for the
     app block builder. Choose a type that matches the performance
     requirements of the applications that you plan to install.
   - **Tags (optional)**: Choose **Add Tag**, and type the key and value
     for the tag. To add more tags, repeat this step. For more
     information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").

4. Choose **Next**.
5. For **Step 2: Configure Network**, do the following:
   - To add internet access for the app block builder in a VPC with a public subnet, choose
     **Default Internet Access**. If you are providing
     internet access by using a NAT gateway, leave **Default Internet
     Access** unselected. For more information, see [Internet Access](internet-access.md "internet-access.md").
   - For **VPC** and **Subnet 1**, choose a VPC and at least two
     subnets. For increased fault tolerance, we recommend that you choose
     three subnets in different Availability Zones. For more information, see
     [Configure a VPC with Private Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md").

   If you don't have your own VPC and subnet, you can use the [default VPC](default-vpc-with-public-subnet.md "default-vpc-with-public-subnet.md") or create your own. To create your own, choose the **Create a new
   VPC** and **Create new subnet** links to
   create them. Choosing these links opens the Amazon VPC console. After you
   create your VPC and subnets, return to the WorkSpaces Applications console and choose the refresh icon to the left of the **Create a new
   VPC** and **Create new subnet** links to display them in the list. For more information, see [Configure a VPC for WorkSpaces Applications](appstream-vpc.md "appstream-vpc.md").
   - For **Security group(s)**, choose up to five security groups to associate
     with this image builder. If you don't have your own security group and
     you don't want to use the default security group, choose the
     **Create new security group** link to create one.
     After you create your subnets in the Amazon VPC console, return to the WorkSpaces Applications
     console and choose the refresh icon to the left of the **Create
     new security group** link to display them in the list. For
     more information, see [Security Groups in Amazon WorkSpaces Applications](managing-network-security-groups.md "managing-network-security-groups.md").
   - For **VPC Endpoints (Optional)**, you can create an
     interface VPC endpoint (interface endpoint) in your virtual private
     cloud (VPC). To create the interface endpoint, choose **Create
     VPC Endpoint**. Selecting this link opens the VPC console.
     To finish creating the endpoint, follow steps 3 through 6 in [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md"). After
     you create the interface endpoint, you can use it to keep streaming
     traffic within your VPC.

6. Choose **Next**.
7. Choose **Review** and confirm the details for the app block
   builder. To change the configuration for any section, choose
   **Edit** and make the needed changes.
8. After you finish reviewing the configuration details, choose **Create app block
   builder**.

###### Note

If an error message notifies you that you don't have sufficient limits (quotas) to create the image builder, submit a limit increase request through the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/"). For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.
