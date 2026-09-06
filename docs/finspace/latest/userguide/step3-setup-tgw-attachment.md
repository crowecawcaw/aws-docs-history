

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Step 3: Setting up a transit gateway VPC attachment from your VPC
<a name="step3-setup-tgw-attachment"></a>

**Note**  
It may take a few minutes for [Step 1](step1-config-ntw.md) and [Step 2](step2-dns-details.md) to complete. Wait till these steps are successful before proceeding.

In the previous step you created a network connectivity from FinSpace environment to your transit gateway but FinSpace cannot reach into your network unless you create a VPC attachment from your VPC to Transit Gateway and set up routing and rules for the traffic to flow into your network. 

In this step, you create a transit gateway attachment and validate that it is associated in the transit gateway associations.

**To create a transit gateway VPC attachment from your VPC**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Choose **Create transit gateway attachment**.

1. For **Transit gateway ID**, choose the transit gateway for the attachment that you created in [step 1](step1-config-ntw.md) of this tutorial.

1. For **Attachment type**, choose **VPC**.

1. For **VPC ID**, choose the [default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) to attach to the transit gateway. This VPC must have at least one subnet associated with it. 
**Note**  
There is a default VPC for every AWS account. The default VPC ID is the value of the VPC ID column of the VPC table. To view your default VPC:  
Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).
In the navigation pane, choose **Your VPCs**.
In the **Default VPC** column, look for a value of **Yes**. Take note of the ID of the default VPC.

1. For **Subnet IDs**, choose 3 subnets from the availability zones where the environment is created. 

   To check the availability zones ID mapping for your AWS account, go to the AWS Resource Access Manager in your account. Navigate to the product console, find the AZ ID at the bottom right of the page.

**To validate the TGW associations**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway ID** for transit gateway that you created earlier. 

1. Under **Details**, choose **Association route table ID**. The **Association** tab shows the two VPC attachments, one from FinSpace infrastructure VPC and the other from your VPC.