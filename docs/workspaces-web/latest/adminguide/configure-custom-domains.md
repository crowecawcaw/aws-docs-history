# Configuring custom domain for your portal

## How it works

When you configure a custom domain:

- You create and configure a reverse proxy with your custom domain to route traffic to the portal endpoint.
- Users access your portal through your custom domain instead of the default portal endpoint.
- SSL certificates ensure secure connections throughout the process.

## Prerequisites

Before setting up custom domains, ensure you have:

- A domain name that you manage through a DNS service provider such as Amazon Route53.
- A WorkSpaces Secure Browser portal. For more information about creating a portal, see [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md").
- Ensure you have the necessary permissions to manage AWS Certificate Manager, CloudFront, and DNS configurations.

###### Important

Users must enable third-party cookies for the custom domain in their browsers to ensure proper portal functionality.

Ensure that you own and properly manage the custom domain and its DNS records to maintain security and functionality of your portal.

###### Note

To enable single sign-on extension for custom domains, users must install the extension in their browser with a version later than 1.0.2505.6608.

Users are prompted to install the extension when they sign into a portal. For details about the user experience with the extension, see [Single sign-on extension for Amazon WorkSpaces Secure Browser](extension.md "extension.md").

## Getting started

You can configure your custom domain as a
portal settings attribute either when creating a new portal or when editing an existing portal.
This can be done using the AWS Console, SDK, CloudFormation or
AWS CLI commands.

We recommend setting up a Amazon CloudFront distribution as a reverse proxy that routes traffic from your custom
domain to the WorkSpaces Secure Browser portal endpoint.

###### Note

Although Amazon CloudFront is recommended as the reverse proxy solution, you can use alternative reverse proxy configurations. Ensure you meet the required origin and cache configuration settings as detailed in the Amazon CloudFront setup steps.

## Setting up CloudFront as reverse proxy

To complete setting up a reverse proxy, you need:

- An SSL Certificate through AWS Certificate Manager (ACM)
- An Amazon CloudFront Distribution
- DNS records
- Portal configured with your custom domain

**SSL Certificate**

If you don't have one already, follow these steps to
request one through ACM:

1. Navigate to the ACM console at [https://console.aws.amazon.com/acm](https://console.aws.amazon.com/acm "https://console.aws.amazon.com/acm").

###### Important

Use the US East (N. Virginia) Region, as CloudFront requires certificates to be stored there. 2. Request a certificate:

    * For new ACM users: Choose **Get started** under
     **Provision certificates**
    * For existing ACM users: Choose **Request a certificate**

3. Choose **Request a public certificate** and then choose
   **Request a certificate**.

###### Note

You can also import an existing certificate. For more information, see
[Importing
certificates into ACM](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the _ACM User Guide_. 4. Enter your primary domain name (for example, `myportal.example.com`). 5. Choose a validation method:

    * **DNS Validation** (Recommended for Route 53 users) –
     Allows automatic record set creation in your hosted zone. For more information, see
     [DNS
     validation](../../../acm/latest/userguide/gs-acm-validate-dns.md "../../../acm/latest/userguide/gs-acm-validate-dns.md") in the *ACM User Guide*.
    * **Email Validation** – For more information, see
     [Email
     validation](../../../acm/latest/userguide/gs-acm-validate-email.md "../../../acm/latest/userguide/gs-acm-validate-email.md") in the *ACM User Guide*.

6. Review your settings and choose **Confirm and request**.
   **CloudFront distribution**

Create a CloudFront distribution to proxy requests from your custom domain to the portal endpoint.

1. Navigate to the CloudFront console at [https://console.aws.amazon.com/cloudfront](https://console.aws.amazon.com/cloudfront "https://console.aws.amazon.com/cloudfront").
2. Choose **Create Distribution**.
   - **Distribution name**: Enter a name for the distribution
   - **Distribution type**: Single website or app

###### Note

If your custom domain is managed in Route 53 in the same AWS account, CloudFront can automatically manage your DNS for you.
Enter your custom domain and click "Check domain". If you have a domain from a different DNS provider, skip this step and configure your domain later. 3. Configure the origin settings:

    * **Origin Type**: Other
    * **Custom Origin**: Enter the portal endpoint
     `<portalId>`.workspaces-web.com
    * **Origin Path**: Leave empty (default)

4.  Customize origin settings:
    - Add custom header

    ###### Important

    Portal access through custom domain will only work if this header is present in proxied requests. Ensure the header name and value are specified exactly as mentioned.

        + **Header Name**: workspacessecurebrowser-custom-domain
        + **Value**: Your custom domain (for example, `myportal.example.com`)

    - **Protocol**: HTTPS only
    - **HTTPS port**: 443 (keep default)
    - **Minimum Original SSL protocol**: TLSv1.2 (default)
    - **Origin IP address type**: IPv4 only (Amazon WorkSpaces Secure Browser does not
      support IPv6 at the time of writing this administration guide.)

5.  Customize cache settings:
    - **Viewer protocol policy**: Redirect HTTP to HTTPS
    - **Allowed HTTP methods**: GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE
    - **Cache Policy**: CachingDisabled
    - **Origin request policy**: AllViewerExceptHostHeader

    ###### Important

    Portal access through custom domain will only work if origin request policy is set to AllViewerExceptHostHeader. As the name suggests, this policy filters out only the host header from the request headers and passes on all the remaining headers to the origin.

6.  You can configure WAF if you want but it is not necessary for the purpose of this setup.
7.  In Get TLS certificate, select the TLS Certificate created in Step 1.
8.  Review the settings and choose **Create Distribution**.
    **DNS records**

Cloudfront can update your DNS records in Route 53 to route traffic from the specified domains to the distribution created in Step 2, if your hosted zone is in the same AWS account.

1.  Navigate to CloudFront settings
2.  Click "Route domains to CloudFront"
3.  Click "Set up routing automatically"
    If you have configured DNS for the custom domain in another service provider or another AWS account, configure your DNS provider to route traffic for your
    domain to the distribution. The following steps describe how to do so using Route 53.

4.  Open the Amazon Route 53 console at [https://console.aws.amazon.com/route53](https://console.aws.amazon.com/route53 "https://console.aws.amazon.com/route53").
5.  Access DNS management:
    - If you are new to using Route 53 with this AWS account, the Amazon Route 53 overview
      page opens. Under DNS management, choose **Get started now**.
    - If you have used Route 53 before with this AWS account, proceed to the next step.

6.  In the navigation pane, choose **Hosted zones**.
7.  Create a hosted zone if you don't already have one:
    - To route internet traffic to your resources, see
      [Creating
      a Public Hosted Zone](../../../Route53/latest/DeveloperGuide/CreatingHostedZone.md "../../../Route53/latest/DeveloperGuide/CreatingHostedZone.md") in the _Amazon Route 53 Developer Guide_.
    - To route traffic in your VPC, see
      [Creating
      a Private Hosted Zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md") in the _Amazon Route 53 Developer Guide_.

8.  On the **Hosted Zones** page, choose the name of the hosted zone that
    you want to administer.
9.  Choose **Create Record Set**.
10. Create an entry for your domain (for example, `myportal.example.com`):

        * **Type**: A – IPv4 address
        * **Alias**: Yes
        * **Alias Target**: CloudFront Distribution URL

    Keep the default values for all other settings.

###### Note

If you are not using Route 53 to manage DNS for your domain, use your DNS service provider
and add DNS entries that point to your domain to the URL of your CloudFront distribution.

**Alternatively, you can use the following CloudFormation template to create your CloudFront distribution:**

This CloudFormation template automatically creates the CloudFront distribution, configures the reverse proxy settings, and optionally creates Route53 DNS records:

###### Example workspaces-web-custom-domain-template.yaml

```

AWSTemplateFormatVersion: '2010-09-09'
Description: 'CloudFront Distribution for custom domain configuration with existing AWS WorkSpaces Secure Browser Portal'

Parameters:
  PortalEndpoint:
    Type: String
    Description: 'The endpoint of your existing WorkSpaces Web Portal (e.g., abc123.workspaces-web.com)'
    AllowedPattern: '^[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)?\.workspaces-web\.com$'
    ConstraintDescription: 'Must be a valid WorkSpaces Web portal endpoint'

  CustomDomainName:
    Type: String
    Description: 'Custom domain name for the portal (e.g., myportal.example.com)'
    AllowedPattern: '^([a-zA-Z0-9]?((?!-)([A-Za-z0-9-]*[A-Za-z0-9])\.)+[a-zA-Z0-9]+)$'
    ConstraintDescription: 'Must be a valid domain name'

  CertificateArn:
    Type: String
    Description: 'ARN of the validated SSL certificate in ACM (must be in us-east-1 region for CloudFront)'
    AllowedPattern: 'arn:aws:acm:us-east-1:[0-9]{12}:certificate/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
    ConstraintDescription: 'Must be a valid ACM certificate ARN in us-east-1 region'

  CreateRoute53Record:
    Type: String
    Description: 'Create Route53 record for custom domain (requires existing hosted zone)'
    Default: 'No'
    AllowedValues:
      - 'Yes'
      - 'No'

  HostedZoneId:
    Type: String
    Description: 'Route53 Hosted Zone ID for the custom domain (required if creating Route53 record)'
    Default: ''

Conditions:
  ShouldCreateRoute53Record: !And
    - !Equals [!Ref CreateRoute53Record, 'Yes']
    - !Not [!Equals [!Ref HostedZoneId, '']]

Resources:
  # CloudFront Distribution
  CloudFrontDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Aliases:
          - !Ref CustomDomainName
        Comment: !Sub 'CloudFront distribution for WorkSpaces Web Portal - ${CustomDomainName}'
        Enabled: true
        HttpVersion: http2
        IPV6Enabled: false  # WorkSpaces Secure Browser does not support IPv6
        PriceClass: PriceClass_All

        # Origin Configuration
        Origins:
          - Id: WorkSpacesWebOrigin
            DomainName: !Ref PortalEndpoint
            CustomOriginConfig:
              HTTPSPort: 443
              OriginProtocolPolicy: https-only
              OriginSSLProtocols:
                - TLSv1.2
            OriginCustomHeaders:
              - HeaderName: workspacessecurebrowser-custom-domain
                HeaderValue: !Ref CustomDomainName

        # Default Cache Behavior
        DefaultCacheBehavior:
          TargetOriginId: WorkSpacesWebOrigin
          ViewerProtocolPolicy: https-only
          AllowedMethods:
            - GET
            - HEAD
            - OPTIONS
            - PUT
            - POST
            - PATCH
            - DELETE
          Compress: false
          # Cache Policy: CachingDisabled (using predefined managed policy)
          CachePolicyId: 4135ea2d-6df8-44a3-9df3-4b5a84be39ad
          # Origin Request Policy: AllViewerExceptHostHeader (using predefined managed policy)
          OriginRequestPolicyId: b689b0a8-53d0-40ab-baf2-68738e2966ac

        # SSL Configuration
        ViewerCertificate:
          AcmCertificateArn: !Ref CertificateArn
          SslSupportMethod: sni-only
          MinimumProtocolVersion: TLSv1.2_2021

      Tags:
        - Key: Name
          Value: !Sub '${AWS::StackName}-cloudfront'

  # Route 53 Record (optional - requires hosted zone to exist)
  Route53Record:
    Type: AWS::Route53::RecordSet
    Condition: ShouldCreateRoute53Record
    Properties:
      HostedZoneId: !Ref HostedZoneId
      Name: !Ref CustomDomainName
      Type: A
      AliasTarget:
        DNSName: !GetAtt CloudFrontDistribution.DomainName
        HostedZoneId: Z2FDTNDATAQYW2  # CloudFront Hosted Zone ID
        EvaluateTargetHealth: false

Outputs:
  PortalEndpoint:
    Description: 'WorkSpaces Web Portal endpoint used as origin'
    Value: !Ref PortalEndpoint
    Export:
      Name: !Sub '${AWS::StackName}-PortalEndpoint'

  CustomDomainEndpoint:
    Description: 'Custom domain endpoint for the portal'
    Value: !Sub 'https://${CustomDomainName}'
    Export:
      Name: !Sub '${AWS::StackName}-CustomDomainEndpoint'

  CloudFrontDistributionId:
    Description: 'CloudFront Distribution ID'
    Value: !Ref CloudFrontDistribution
    Export:
      Name: !Sub '${AWS::StackName}-CloudFrontDistributionId'

  CloudFrontDomainName:
    Description: 'CloudFront Distribution Domain Name'
    Value: !GetAtt CloudFrontDistribution.DomainName
    Export:
      Name: !Sub '${AWS::StackName}-CloudFrontDomainName'

  CertificateArn:
    Description: 'SSL Certificate ARN used by CloudFront'
    Value: !Ref CertificateArn
    Export:
      Name: !Sub '${AWS::StackName}-CertificateArn'

Metadata:
  AWS::CloudFormation::Interface:
    ParameterGroups:
      - Label:
          default: "Existing Portal Configuration"
        Parameters:
          - PortalEndpoint
      - Label:
          default: "Custom Domain Configuration"
        Parameters:
          - CustomDomainName
          - CertificateArn
          - CreateRoute53Record
          - HostedZoneId
    ParameterLabels:
      PortalEndpoint:
        default: "Portal Endpoint"
      CustomDomainName:
        default: "Custom Domain Name"
      CertificateArn:
        default: "SSL Certificate ARN"
      CreateRoute53Record:
        default: "Create Route53 Record"
      HostedZoneId:
        default: "Hosted Zone ID"

```

To use this template:

1. Save the template above as `workspaces-web-custom-domain-template.yaml`
2. Deploy using the AWS Console, AWS CLI, or AWS SDK with your specific parameter values
3. After deployment, configure your portal with the custom domain as described in Step 4 below
   **Portal configuration**

Register your custom domain as a portal settings attribute using the AWS Console,
UpdatePortal API, or the update-portal AWS CLI command.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home](https://console.aws.amazon.com/workspaces-web/home "https://console.aws.amazon.com/workspaces-web/home").
2. In the navigation pane, choose **Web portals**.
3. Select the web portal you want to configure and choose **Edit**.
4. In the portal settings, add your custom domain.
5. Save the portal configuration.
   **Test your configuration**

To test your configuration, follow these steps:

1. Open a web browser and navigate to the URL for your custom domain
   (for example, `https://myportal.example.com`).
2. If everything is set up correctly, you should see the sign-in page for your portal.
3. Next, enter the portal URL in your browser, you should be redirected to the custom domain after logging in to your IdP.
4. Finally, log in to your IdP and click on the application tile for your portal. You should be redirected to custom domain.
