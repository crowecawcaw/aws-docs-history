# Tutorial: Get started with Verified Access

Use this tutorial to get started with AWS Verified Access. You'll learn how to create and configure
Verified Access resources.

As a part of this tutorial, you'll add an application to Verified Access. At the end of the tutorial,
specific users can access that application over the internet, without using VPN. Instead, you'll
use AWS IAM Identity Center as an identity trust provider. Note that this tutorial doesn't also use a device
trust provider.

###### Tasks

- [Verified Access tutorial prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Create a Verified Access trust provider](#getting-started-configure-trust-provider "#getting-started-configure-trust-provider")
- [Step 2: Create a Verified Access instance](#getting-started-create-instance "#getting-started-create-instance")
- [Step 3: Create a Verified Access group](#getting-started-create-group "#getting-started-create-group")
- [Step 4: Create a Verified Access endpoint](#getting-started-create-endpoint "#getting-started-create-endpoint")
- [Step 5: Configure DNS for the Verified Access endpoint](#getting-started-configure-dns "#getting-started-configure-dns")
- [Step 6: Test connectivity to the application](#getting-started-test "#getting-started-test")
- [Step 7: Add a Verified Access group-level access policy](#getting-started-create-policy "#getting-started-create-policy")
- [Clean up your Verified Access resources](#getting-started-cleanup "#getting-started-cleanup")

## Verified Access tutorial prerequisites

The following are the prerequisites for completing this tutorial:

- AWS IAM Identity Center enabled in the AWS Region that you're working in. You can then use IAM Identity Center as a
  trust provider with Verified Access. For more information, see [Enable AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md")
  in the _AWS IAM Identity Center User Guide_.
- A security group to control access to the application. Allow all inbound traffic from
  the VPC CIDR and all outbound traffic.
- An application running behind an internal load balancer from Elastic Load Balancing. Associate your
  security group with the load balancer.
- A self-signed or public TLS certificate in AWS Certificate Manager. Use an RSA certificate with a key length of
  1,024 or 2,048.
- A public hosted domain and the permissions required to update DNS records for the domain.
- An IAM policy with the permissions required to create an AWS Verified Access instance. For
  more information, see [Policy for
  creating Verified Access instances](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance").

## Step 1: Create a Verified Access trust provider

Use the following procedure to set up AWS IAM Identity Center as your trust provider.

###### To create an IAM Identity Center trust provider

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access trust providers**.
3. Choose **Create Verified Access trust provider**.
4. (Optional) For **Name tag** and **Description**, enter a
   name and description for the Verified Access trust provider.
5. Enter a custom identifier to use later when working with policy rules for **Policy
   reference name**. For example, you can enter `idc`.
6. For **Trust provider type**, choose **User trust provider**.
7. For **User trust provider type**, choose **IAM Identity Center**.
8. Choose **Create Verified Access trust provider**.

## Step 2: Create a Verified Access instance

Use the following procedure to create a Verified Access instance.

###### To create a Verified Access instance

1. In the navigation pane, choose **Verified Access instances**.
2. Choose **Create Verified Access instance**.
3. (Optional) For **Name** and **Description**, enter a
   name and description for the Verified Access instance.
4. For **Verified Access trust provider**, choose your trust provider.
5. Choose **Create Verified Access instance**.

## Step 3: Create a Verified Access group

Use the following procedure to create a Verified Access group.

###### To create a Verified Access group

1. In the navigation pane, choose **Verified Access groups**.
2. Choose **Create Verified Access group**.
3. (Optional) For **Name tag** and **Description**, enter a
   name and description for the group.
4. For **Verified Access instance**, choose your Verified Access instance.
5. Keep **Policy definition** blank. You will add a group-level policy in a
   later step.
6. Choose **Create Verified Access group**.

## Step 4: Create a Verified Access endpoint

Use the following procedure to create a Verified Access endpoint. This step assumes that you have an
application running behind an internal load balancer from Elastic Load Balancing and a public domain certificate
in AWS Certificate Manager.

###### To create a Verified Access endpoint

1. In the navigation pane, choose **Verified Access endpoints**.
2. Choose **Create Verified Access endpoint**.
3. (Optional) For **Name tag** and **Description**, enter a
   name and description for the endpoint.
4. For **Verified Access group**, choose your Verified Access group.
5. For **Endpoint details**, do the following:
   1. For **Protocol**, select **HTTPS** or
      **HTTP**, depending on the configuration of your load balancer.
   2. For **Attachment type**, choose **VPC**.
   3. For **Endpoint type**, choose **Load
      balancer**.
   4. For **Port**, enter the port number used by your load balancer
      listener. For example, 443 for HTTPS or 80 for HTTP.
   5. For **Load balancer ARN**, choose your load balancer.
   6. For **Subnets**, select the subnets associated with your load
      balancer.
   7. For **Security groups**, select your security group. Using the same
      security group for your load balancer and endpoint allows traffic between them. If you
      prefer not to use the same security group, be sure to reference the endpoint security
      group from your load balancer so that it accepts traffic from the endpoint.
   8. For **Endpoint domain prefix**, enter a custom identifier. For example,
      `my-ava-app`. This prefix is prepended to the DNS name that Verified Access
      generates.

6. For **Application details**, do the following:
   1. For **Application domain**, enter the DNS name for your
      application. This domain must match the one in your domain certificate.
   2. For **Domain certificate ARN**, select the Amazon Resource Name (ARN)
      of your domain certificate in AWS Certificate Manager.

7. Keep **Policy details** blank. You will add a group-level access policy
   in a later step.
8. Choose **Create Verified Access endpoint**.

## Step 5: Configure DNS for the Verified Access endpoint

For this step, you map your application's domain name (for example, www.myapp.example.com)
to the domain name of your Verified Access endpoint. To complete the DNS mapping, create a Canonical Name
Record (CNAME) with your DNS provider. After you create the CNAME record, all requests from users
to your application will be sent to Verified Access.

###### To get the domain name of your endpoint

1. In the navigation pane, choose **Verified Access endpoints**.
2. Select your endpoint.
3. Choose the **Details** tab.
4. Copy the domain from **Endpoint domain**. The following is an example
   endpoint domain name: `my-ava-app.edge-1a2b3c4d5e6f7g.vai-1a2b3c4d5e6f7g.prod.verified-access.us-west-2.amazonaws.com`.

Follow the directions provided by your DNS provider to create a CNAME record. Use the domain
name of your application as the record name and the domain name of the Verified Access endpoint as the
record value.

## Step 6: Test connectivity to the application

You can now test connectivity to your application. Enter your application's domain name into
your web browser. The default behavior of Verified Access is to deny all requests. Because we did not add
a Verified Access policy to the group or the endpoint, all requests are denied.

## Step 7: Add a Verified Access group-level access policy

Use the following procedure to modify the Verified Access group and configure an access policy that
allows connectivity to your application. The details of the policy will depend on the users and
groups that are configured in IAM Identity Center. For information, see [Verified Access policies](auth-policies.md "auth-policies.md").

###### To modify a Verified Access group

1. In the navigation pane, choose **Verified Access groups**.
2. Select your group.
3. Choose **Actions**, **Modify Verified Access group policy**.
4. Turn on **Enable policy**.
5. Enter a policy that allows users from your IAM Identity Center to access your application.
   For examples, see [Verified Access example policies](trust-data-iam-add-pol.md "trust-data-iam-add-pol.md").
6. Choose **Modify Verified Access group policy**.
7. Now that your group policy is in place, repeat the test from the previous step to verify that
   the request is allowed. If the request is allowed, you are prompted to sign in through the
   IAM Identity Center sign-in page. After you provide the user name and password, you can access your
   application.

## Clean up your Verified Access resources

After you are finished with this tutorial, use the following procedure to delete your Verified Access resources.

###### To delete your Verified Access resources

1. In the navigation pane, choose **Verified Access endpoints**. Select the
   endpoint and choose **Actions**, **Delete Verified Access endpoint**.
2. In the navigation pane, choose **Verified Access groups**. Select the group and choose
   **Actions**, **Delete Verified Access group**. You might need to wait
   until the endpoint deletion process is complete.
3. In the navigation pane, choose **Verified Access instances**. Select your instance
   and choose **Actions**, **Detach Verified Access trust provider**.
   Select the trust provider and choose **Detach Verified Access trust provider**.
4. In the navigation pane, choose **Verified Access trust providers**. Select your
   trust provider and choose **Actions**, **Delete Verified Access trust provider**.
5. In the navigation pane, choose **Verified Access instances**. Select your
   instance and choose **Actions**, **Delete Verified Access instance**.
