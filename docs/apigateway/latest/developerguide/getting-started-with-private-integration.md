# Tutorial: Create a REST API with a private integration

You can create an API Gateway API with private integration to provide your customers access to
HTTP/HTTPS resources within your Amazon Virtual Private Cloud (Amazon VPC). Such VPC resources are HTTP/HTTPS
endpoints on an EC2 instance behind a Network Load Balancer in the VPC. The Network Load Balancer encapsulates the VPC
resource and routes incoming requests to the targeted resource.

When a client calls the API, API Gateway connects to the Network Load Balancer through the
pre-configured VPC link. A VPC link is encapsulated by an API Gateway resource of [VpcLink](../api/API_VpcLink.md "../api/API_VpcLink.md"). It is responsible for forwarding
API method requests to the VPC resources and returns backend responses to the caller. For an
API developer, a `VpcLink` is functionally equivalent to an integration endpoint.

To create an API with private integration, you must create a new
`VpcLink`, or choose an existing one, that is connected to a Network Load Balancer that targets the desired VPC
resources. You must have [appropriate
permissions](grant-permissions-to-create-vpclink.md "grant-permissions-to-create-vpclink.md") to create and manage a `VpcLink`. You then set up an API
[method](../api/API_Method.md "../api/API_Method.md") and integrate it with the
`VpcLink` by setting either `HTTP` or `HTTP_PROXY` as
the [integration type](../api/API_Integration.md#type "../api/API_Integration.md#type"), setting
`VPC_LINK` as the integration [connection type](../api/API_Integration.md#connectionType "../api/API_Integration.md#connectionType"), and
setting the `VpcLink` identifier on the integration [`connectionId`](../api/API_Integration.md#connectionId "../api/API_Integration.md#connectionId").

###### Note

The Network Load Balancer and API must be owned by the same AWS account.

To quickly get started creating an API to access VPC resources, we walk through the
essential steps for building an API with the private integration, using the API Gateway console.
Before creating the API, do the following:

1. Create a VPC resource, create or choose a Network Load Balancer under your
   account in the same region, and add the EC2 instance hosting the resource as a
   target of the Network Load Balancer. For more information, see [Set up a Network Load Balancer
   for API Gateway private integrations](set-up-nlb-for-vpclink-using-console.md "set-up-nlb-for-vpclink-using-console.md").
2. Grant permissions to create the VPC links for private integrations. For more
   information, see [Grant permissions for API Gateway to create a VPC
   link](grant-permissions-to-create-vpclink.md "grant-permissions-to-create-vpclink.md").
   After creating your VPC resource and your Network Load Balancer with your VPC resource
   configured in its target groups, follow the instructions below to create an API and
   integrate it with the VPC resource via a `VpcLink` in a private integration.

###### To create an API with a private integration

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. If this is your first time using API Gateway, you see a page that introduces you to
   the features of the service. Under **REST API**, choose **Build**. When the
   **Create Example API** popup appears, choose
   **OK**.

If this is not your first time using API Gateway, choose **Create
API**. Under **REST API**, choose **Build**. 3. Create an edge-optimized or Regional REST API. For **IP address type**, use
**IPv4**. 4. Select your API. 5. Choose **Create method**, and then do the following:

    1. For **Method type**, select `GET`.
    2. For **Integration type**, select **VPC link**.
    3. Turn on **VPC proxy integration**.
    4. For **HTTP method**, select `GET`.
    5. For **VPC link**, select **[Use stage variable]** and enter `${stageVariables.vpcLinkId}` in the text box below.


    You define the `vpcLinkId` stage variable after
     deploying the API to a stage and set its value to the ID of the
     `VpcLink`.
    6. For **Endpoint URL**, enter a URL, for example, `http://myApi.example.com`.


    The URL must be a valid top-level domain and the host name (for example, `myApi.example.com`)
     is used to set the `Host` header of the integration request.
    7. Choose **Create method**.


    With the proxy integration, the API is ready for deployment. Otherwise, you need to proceed to set up appropriate method responses and integration responses.

6. Choose **Deploy API**, and then do the following:
   1. For **Stage**, select **New stage**.
   2. For **Stage name**, enter a stage name.
   3. (Optional) For **Description**, enter a description.
   4. Choose **Deploy**.

7. Under the **Stage details** section, note the resulting **Invoke URL**. You need it to invoke
   the API. Before doing that, you must set up the `vpcLinkId` stage
   variable.
8. In the **Stages** pane, choose the
   **Stage variables** tab, and then do the following:
   1. Choose **Manage variables**, and then choose **Add stage variable**.
   2. For **Name**, enter
      `vpcLinkId`.
   3. For **Value**, enter the ID
      of `VPC_LINK`, for example,
      `gix6s7`.
   4. Choose **Save**.

   Using the stage variable, you can easily switch to different VPC
   links for the API by changing the stage variable value.
