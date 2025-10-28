# Deploy the AWS CloudFormation template for CDN and MediaTailor integrations

AWS Elemental MediaTailor deployment using the AWS CloudFormation template is straightforward once you understand what the template will create. This
process takes about 15-30 minutes, with most of the time spent waiting for the CloudFront
distribution to deploy.

To deploy the AWS CloudFormation template and set up your automated ad insertion workflow:

###### To deploy the MediaTailor AWS CloudFormation template

1. Download the AWS CloudFormation template from the AWS Elemental MediaTailor GitHub repository or copy it
   from the [AWS CloudFormation template reference for
   AWS Elemental MediaTailor and Amazon CloudFront integration](cloudformation-template-reference.md "cloudformation-template-reference.md").
2. Open the [AWS CloudFormation
   console](https://console.aws.amazon.com/cloudformation/home "https://console.aws.amazon.com/cloudformation/home").
3. Choose **Create stack** > **With new resources
   (standard)**.
4. Under **Specify template**, choose **Upload a
   template file** and upload the template.
5. Enter a stack name and provide values for the required parameters:
   - **AdServerUrl**: URL of your VAST ad server (e.g.,
     https://`your-ad-server.com`/vast)
   - **ContentOriginDomainName**: Domain name of your
     content origin without protocol (e.g.,
     `mediapackage-domain.mediapackagev2.us-west-2.amazonaws.com`)
   - **ContentOriginType**: Select the type of content
     origin:
     - _mediapackagev2_: For AWS Elemental MediaPackage
       origins
     - _s3_: For Amazon S3 bucket origins
     - _custom_: For any other origin type

6. Review the configuration and choose **Create stack**.
7. Wait for the stack creation to complete, which typically takes 5-10 minutes.
   You can monitor progress in the **Events** tab.
8. Once complete, navigate to the **Outputs** tab to find the
   URLs for your HLS and DASH manifests.

###### Note

If you're using AWS Elemental MediaPackage as your content origin, make sure your MediaPackage endpoints
are properly configured and accessible. For more information, see [MediaPackage CDN integration](mediapackage-integration.md "mediapackage-integration.md").
