# AWS CloudFormation template reference for

AWS Elemental MediaTailor and Amazon CloudFront integration

AWS Elemental MediaTailor integration with Amazon CloudFront can be automated using the following complete AWS CloudFormation template:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: |
  CloudFormation template that sets up AWS Elemental MediaTailor integration with CloudFront Distribution
  for server-side ad insertion. This template supports various content origins including MediaPackage, Amazon S3,
  and custom origins, making it versatile for different streaming architectures.

Parameters:
  AdServerUrl:
    Type: String
    Default: 'https://d1kbmkziz9rksx.CloudFront.net/VASTEndpoint.xml'
    Description: URL of the VAST ad server for dynamic ad insertion. Static VAST endpoint provided for testing.

  ContentOriginDomainName:
    Type: String
    Description: |
      Domain name of your content origin without protocol (e.g., `mediapackage-domain.mediapackagev2.us-west-2.amazonaws.com`,
      `mybucket.s3.amazonaws.com`, or `custom-origin.example.com`).
      Do not include http:// or https:// prefixes or any paths.
    AllowedPattern: "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$"
    ConstraintDescription: Must be a valid domain name (e.g., `example.com`) without protocol or path components. IP addresses are not allowed.

  ContentOriginType:
    Type: String
    AllowedValues:
      - mediapackagev2
      - s3
      - custom
    Default: mediapackagev2
    Description: |
      The type of content origin:
      - mediapackagev2: AWS Elemental MediaPackage V2
      - s3: Amazon S3 bucket
      - custom: Any other custom origin

Resources:
  #---------------------------------------------------------------------------
  # Origin Access Control (for securing MediaPackage V2 and Amazon S3 origins)
  #---------------------------------------------------------------------------
  CloudFrontOriginAccessControl:
    Type: AWS::CloudFront::OriginAccessControl
    Condition: IsNotCustomOrigin
    Properties:
      OriginAccessControlConfig:
        Name: !Sub '${AWS::StackName}-OAC'
        OriginAccessControlOriginType: !Ref ContentOriginType
        SigningBehavior: always
        SigningProtocol: sigv4
        Description: Origin Access Control for content origin

  #---------------------------------------------------------------------------
  # MediaTailor Playback Configuration
  #---------------------------------------------------------------------------
  MediaTailorPlaybackConfig:
    Type: AWS::MediaTailor::PlaybackConfiguration
    Properties:
      Name: !Sub '${AWS::StackName}-PlaybackConfig'
      # The video content source should point to your CloudFront distribution
      VideoContentSourceUrl: !Sub 'https://${CloudFrontDistribution.DomainName}/'
      # The Ad Decision Server URL is where MediaTailor will request ads
      AdDecisionServerUrl: !Ref AdServerUrl
      # Configuration for pre-roll ads during live streams
      LivePreRollConfiguration:
        AdDecisionServerUrl: !Ref AdServerUrl
        MaxDurationSeconds: 30
      # CDN configuration for integrating with CloudFront
      CdnConfiguration:
        AdSegmentUrlPrefix: '/'
        ContentSegmentUrlPrefix: '/'
      # Set a reasonable manifest segment timeout
      ManifestProcessingRules:
        AdMarkerPassthrough:
          Enabled: false

  #---------------------------------------------------------------------------
  # CloudFront Distribution
  #---------------------------------------------------------------------------
  CloudFrontDistribution:
    Type: AWS::CloudFront::Distribution
    Properties:
      DistributionConfig:
        Enabled: true
        HttpVersion: http2and3
        IPV6Enabled: true
        Comment: !Sub 'Distribution for MediaTailor ad insertion with ${ContentOriginType} origin'

        # Default cache behavior points to the content origin
        DefaultCacheBehavior:
          TargetOriginId: ContentOrigin
          ViewerProtocolPolicy: 'https-only'
          # Using managed policies for optimal performance and simplicity
          CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  # Managed-CachingOptimized
          OriginRequestPolicyId: 88a5eaf4-2fd4-4709-b370-b4c650ea3fcf # Managed-HostHeaderOnly
          ResponseHeadersPolicyId: eaab4381-ed33-4a86-88ca-d9558dc6cd63  # Managed-CORS-with-preflight-and-SecurityHeadersPolicy
          Compress: true

        # Define all the origins needed for the workflow
        Origins:
          # Main content origin (MediaPackage, Amazon S3, or Custom)
          - Id: ContentOrigin
            DomainName: !Ref ContentOriginDomainName
            # Apply Origin Access Control for secure origins
            OriginAccessControlId: !If [IsNotCustomOrigin, !GetAtt CloudFrontOriginAccessControl.Id, !Ref "AWS::NoValue"]
            # For custom origins, we need a CustomOriginConfig
            CustomOriginConfig:
              OriginProtocolPolicy: 'https-only'
              OriginSSLProtocols:
                - TLSv1.2
              OriginKeepaliveTimeout: 5
              OriginReadTimeout: 30
              HTTPPort: 80
              HTTPSPort: 443

          # MediaTailor Manifests Origin - handles manifest manipulation for ad insertion
          - Id: MediaTailorManifests
            DomainName: !Sub 'manifests.mediatailor.${AWS::Region}.amazonaws.com'
            CustomOriginConfig:
              OriginProtocolPolicy: 'https-only'
              OriginSSLProtocols:
                - TLSv1.2
              OriginKeepaliveTimeout: 5
              OriginReadTimeout: 30
            # Origin Shield improves caching efficiency
            OriginShield:
              Enabled: true
              OriginShieldRegion: !Ref AWS::Region

          # MediaTailor Segments Origin - handles personalized ads
          - Id: MediaTailorSegments
            DomainName: !Sub 'segments.mediatailor.${AWS::Region}.amazonaws.com'
            CustomOriginConfig:
              OriginProtocolPolicy: 'https-only'
              OriginSSLProtocols:
                - TLSv1.2
              OriginKeepaliveTimeout: 5
              OriginReadTimeout: 30

        # Cache behaviors to route specific request patterns to the right origin
        CacheBehaviors:
          # Handle MediaTailor segment requests for ad content which are cache-able
          - PathPattern: '/tm/*'
            TargetOriginId: MediaTailorSegments
            ViewerProtocolPolicy: 'https-only'
            CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  # Managed-CachingOptimized
            OriginRequestPolicyId: 88a5eaf4-2fd4-4709-b370-b4c650ea3fcf  # Managed-HostHeaderOnly
            ResponseHeadersPolicyId: eaab4381-ed33-4a86-88ca-d9558dc6cd63  # Managed-CORS-with-preflight-and-SecurityHeadersPolicy
            Compress: true

          # Handle MediaTailor interstitial (SGAI) media requests which are cache-able
          - PathPattern: '/v1/i-media/*'
            TargetOriginId: MediaTailorManifests
            ViewerProtocolPolicy: 'https-only'
            CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  # Managed-CachingOptimized
            OriginRequestPolicyId: 88a5eaf4-2fd4-4709-b370-b4c650ea3fcf  # Managed-HostHeaderOnly
            ResponseHeadersPolicyId: eaab4381-ed33-4a86-88ca-d9558dc6cd63  # Managed-CORS-with-preflight-and-SecurityHeadersPolicy
            Compress: true

          # Handle MediaTailor Personalized manifests which are not cache-able
          - PathPattern: '/v1/*'
            TargetOriginId: MediaTailorManifests
            ViewerProtocolPolicy: 'https-only'
            CachePolicyId: 4135ea2d-6df8-44a3-9df3-4b5a84be39ad # Managed-CachingDisabled
            OriginRequestPolicyId: 59781a5b-3903-41f3-afcb-af62929ccde1 # Managed-AllViewer
            ResponseHeadersPolicyId: eaab4381-ed33-4a86-88ca-d9558dc6cd63  # Managed-CORS-with-preflight-and-SecurityHeadersPolicy
            Compress: true

          # Handle MediaTailor segment *redirect* requests which are not cache-able (used for server side reporting)
          - PathPattern: '/segment/*'
            TargetOriginId: MediaTailorManifests
            ViewerProtocolPolicy: 'https-only'
            CachePolicyId: 4135ea2d-6df8-44a3-9df3-4b5a84be39ad # Managed-CachingDisabled
            OriginRequestPolicyId: 59781a5b-3903-41f3-afcb-af62929ccde1 # Managed-AllViewer
            ResponseHeadersPolicyId: eaab4381-ed33-4a86-88ca-d9558dc6cd63  # Managed-CORS-with-preflight-and-SecurityHeadersPolicy
            Compress: true

Conditions:
  IsNotCustomOrigin: !Not [!Equals [!Ref ContentOriginType, 'custom']]

Outputs:
  CloudFrontDomainName:
    Description: Domain name of the CloudFront distribution
    Value: !GetAtt CloudFrontDistribution.DomainName

  HlsManifestUrl:
    Description: URL for HLS manifest with ads inserted (append your manifest path)
    Value: !Sub 'https://${CloudFrontDistribution.DomainName}${MediaTailorPlaybackConfig.HlsConfiguration.ManifestEndpointPrefix}'

  DashManifestUrl:
    Description: URL for DASH manifest with ads inserted (append your manifest path)
    Value: !Sub 'https://${CloudFrontDistribution.DomainName}${MediaTailorPlaybackConfig.DashConfiguration.ManifestEndpointPrefix}'

  MediaTailorPlaybackConfigName:
    Description: Name of the MediaTailor playback configuration
    Value: !Ref MediaTailorPlaybackConfig
```
