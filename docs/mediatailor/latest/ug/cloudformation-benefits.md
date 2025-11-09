# Why use AWS CloudFormation for MediaTailor and CDN

integration

AWS Elemental MediaTailor automation with AWS CloudFormation provides significant advantages for broadcast professionals managing streaming workflows. Manually configuring
MediaTailor with a content delivery network (CDN) can be time-consuming and error-prone. Using AWS CloudFormation automation
offers the following advantages.

- **Consistency**: Ensures the same configuration
  is deployed every time, reducing human error.
- **Version control**: Store your infrastructure as
  code in a version control system for tracking changes.
- **Rapid deployment**: Deploy complex
  configurations in minutes instead of hours of manual configuration.
- **Environment replication**: Easily replicate
  configurations across development, testing, and production environments.
- **Documentation**: The template itself serves as
  documentation of your infrastructure.
  Here's how the automated workflow compares to manual configuration:

| Manual setup (multiple steps)             | Automated setup (single template)                      |
| ----------------------------------------- | ------------------------------------------------------ |
| Create MediaTailor playback configuration | Deploy one AWS CloudFormation template with parameters |
| Create CloudFront distribution            |
| Configure cache behaviors                 |
| Set up security configurations            |

The automated workflow for setting up MediaTailor with CloudFront follows these steps:

1. Deploy the AWS CloudFormation template with your content origin and ad server
   parameters
2. AWS CloudFormation creates and configures all necessary resources:
   - MediaTailor playback configuration for ad insertion
   - CloudFront distribution with appropriate cache behaviors
   - Security configurations for content protection

3. Use the AWS CloudFormation outputs to access your ad-enabled stream URLs
4. Stream your content with dynamically inserted ads
