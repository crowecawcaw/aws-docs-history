# Customize the AWS CloudFormation template for CDN and MediaTailor integrations

AWS Elemental MediaTailor template customization allows broadcast professionals to adapt the AWS CloudFormation template to fit specific workflow requirements. Although the basic template works for many scenarios,
these customizations can help you address more complex needs.

The examples below show YAML code snippets that you can add to the template. If you're
not familiar with YAML or AWS CloudFormation syntax, consider working with a developer or AWS
solutions architect to make these changes.

You can customize the AWS CloudFormation template to meet your specific workflow
requirements.

## Add or modify origins

For broadcast workflows that use multiple content sources (like primary and backup
sources, or different content libraries), you can add additional origins to your
CloudFront distribution:

```
Origins:
  # Add a new origin for additional content
  - Id: SecondaryContentOrigin
    DomainName: `secondary-content.example.com`
    CustomOriginConfig:
      OriginProtocolPolicy: 'https-only'
      OriginSSLProtocols:
        - TLSv1.2
```

Then add a corresponding cache behavior to route specific patterns to this
origin:

```
CacheBehaviors:
  - PathPattern: '/secondary-content/*'
    TargetOriginId: SecondaryContentOrigin
    ViewerProtocolPolicy: 'https-only'
    CachePolicyId: 658327ea-f89d-4fab-a63d-7e88639e58f6  # Managed-CachingOptimized
```

## Create custom cache policies

For broadcast workflows with specific caching requirements (like quality selection
parameters or viewer authentication), you can create custom cache policies instead
of using the managed ones. For detailed guidance on TTL values and caching strategies, see [Caching optimization for CDN and MediaTailor
integrations](cdn-optimize-caching.md "cdn-optimize-caching.md").

```
# Define a custom cache policy
CustomCachePolicy:
  Type: AWS::CloudFront::CachePolicy
  Properties:
    CachePolicyConfig:
      Name: !Sub '${AWS::StackName}-CustomCachePolicy'
      DefaultTTL: 86400  # 24 hours
      MaxTTL: 31536000   # 1 year
      MinTTL: 1          # 1 second
      ParametersInCacheKeyAndForwardedToOrigin:
        CookiesConfig:
          CookieBehavior: none
        HeadersConfig:
          HeaderBehavior: none
        QueryStringsConfig:
          QueryStringBehavior: whitelist
          QueryStrings:
            - quality
            - format

# Reference the custom policy in a cache behavior
CacheBehaviors:
  - PathPattern: '/custom-path/*'
    TargetOriginId: ContentOrigin
    ViewerProtocolPolicy: 'https-only'
    CachePolicyId: !Ref CustomCachePolicy
```

## Enhance MediaTailor

configuration

For broadcast workflows that need advanced ad insertion features, you can enhance
the MediaTailor configuration with options like ad prefetching (to reduce latency),
personalization thresholds, and bumper ads.

```
MediaTailorPlaybackConfig:
  Type: AWS::MediaTailor::PlaybackConfiguration
  Properties:
    # Add ad prefetching for improved performance
    AvailSuppression:
      Mode: BEHIND_LIVE_EDGE
      Value: 00:00:00
    # Add personalization parameters
    PersonalizationThresholdSeconds: 2
    # Add bumper ads
    Bumper:
      StartUrl: https://`example.com/bumper-start.mp4`
      EndUrl: https://`example.com/bumper-end.mp4`
    # Other existing properties...
```

For more information about MediaTailor configuration options, see [Using AWS Elemental MediaTailor to insert ads](configurations.md "configurations.md").

## Add security features

For broadcast workflows with specific security requirements (like geo-restrictions
or protection against DDoS attacks), you can add AWS WAF integration and
geo-restrictions:

```
# Create a AWS WAF Web ACL
WebACL:
  Type: AWS::WAFv2::WebACL
  Properties:
    Name: !Sub '${AWS::StackName}-WebACL'
    Scope: CloudFront
    DefaultAction:
      Allow: {}
    VisibilityConfig:
      SampledRequestsEnabled: true
      CloudWatchMetricsEnabled: true
      MetricName: !Sub '${AWS::StackName}-WebACL'
    Rules:
      - Name: RateLimitRule
        Priority: 0
        Action:
          Block: {}
        VisibilityConfig:
          SampledRequestsEnabled: true
          CloudWatchMetricsEnabled: true
          MetricName: RateLimitRule
        Statement:
          RateBasedStatement:
            Limit: 1000
            AggregateKeyType: IP

# Reference the AWS WAF Web ACL in the CloudFront distribution
CloudFrontDistribution:
  Type: AWS::CloudFront::Distribution
  Properties:
    DistributionConfig:
      WebACLId: !GetAtt WebACL.Arn
      # Add geo-restriction
      Restrictions:
        GeoRestriction:
          RestrictionType: whitelist
          Locations:
            - US
            - CA
            - GB
      # Other existing properties...
```

For more information about AWS CloudFormation templates, see the [AWS CloudFormation User
Guide](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md").

For broadcast-specific AWS CloudFormation templates and examples, see the [AWS Media Services
Tools GitHub repository](https://github.com/aws-samples/aws-media-services-tools "https://github.com/aws-samples/aws-media-services-tools").
