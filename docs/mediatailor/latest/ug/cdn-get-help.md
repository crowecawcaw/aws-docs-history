# Get support and troubleshooting

help for CDN and MediaTailor integrations

AWS Elemental MediaTailor CDN integration issues can be complex to diagnose and resolve. Use this guide
when you need additional help with CDN and MediaTailor integration issues that you can't resolve
through self-service troubleshooting.

**Before escalating, try these self-service options:**

- Follow the troubleshooting steps in [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md")
- Analyze your logs and error codes using [CDN integration log analysis
  reference](cdn-log-error-reference.md "cdn-log-error-reference.md")
- Review your monitoring setup with [Set up monitoring tools](cdn-monitoring.md#cdn-monitor-tools-setup "cdn-monitoring.md#cdn-monitor-tools-setup")
- Check the [MediaTailor troubleshooting guide](troubleshooting.md "troubleshooting.md") for service-specific issues
- Search [AWS re:Post](https://repost.aws/ "https://repost.aws/") for similar issues and
  community solutions
- Review [AWS Knowledge
  Center](https://aws.amazon.com/https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/https://aws.amazon.com/premiumsupport/knowledge-center/") for common integration patterns

###### Topics

- [When to escalate to Support](#when-to-escalate "#when-to-escalate")
- [Gather information for
  support](#information-to-gather "#information-to-gather")
- [Support resources](#support-resources "#support-resources")
- [Support case best
  practices](#support-case-best-practices "#support-case-best-practices")

## When to escalate MediaTailor CDN issues to AWS

Support

AWS Elemental MediaTailor CDN integration issues should be escalated to AWS Support when
self-service troubleshooting doesn't resolve the problem. Consider escalating to AWS
Support when:

**Note:** Technical support requires a paid AWS Support
plan. For support plan details and response times, see [AWS Support plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

- Issues affect production traffic or revenue
- You've followed all troubleshooting steps without resolution
- Error patterns suggest service-level issues
- You need assistance with complex configuration scenarios
- Performance issues persist despite optimization efforts

## Gather MediaTailor CDN information before contacting

support

AWS Elemental MediaTailor CDN integration support cases require specific configuration and diagnostic
information for effective troubleshooting. Before contacting AWS Support, gather this
information to help expedite resolution:

**Tip:** Having this information ready before creating
your support case will significantly reduce resolution time and help support engineers
understand your specific configuration.

- **MediaTailor configuration details:**
  - Configuration name and AWS Region
  - Playback configuration ARN
  - ADS URL and integration type

- **CDN configuration details:**
  - CDN distribution ID or configuration name
  - Cache behavior configurations for manifests and segments
  - Origin configuration and routing rules

- **Error information:**
  - Specific error messages and HTTP status codes
  - Timestamps when issues occur
  - Sample URLs that demonstrate the problem
  - CDN and MediaTailor log entries related to the issue

- **Testing information:**
  - Steps you've already taken to troubleshoot
  - Devices and players where the issue occurs
  - Whether the issue affects all content or specific streams
  - Frequency and pattern of the issue (intermittent, consistent,
    time-based)

## MediaTailor CDN integration support resources and

channels

AWS Elemental MediaTailor CDN integration support is available through multiple channels to help you
resolve issues and optimize your implementation:

- **AWS Support:** Create a support case through
  the AWS Management Console for technical assistance

Access: [AWS Support
Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home")

- **AWS re:Post:** Community-driven Q&A
  platform for AWS-related questions and community support

Access: [AWS re:Post](https://repost.aws/ "https://repost.aws/")

- **AWS Documentation:** Comprehensive guides for
  MediaTailor and CDN services

Access: [MediaTailor
Documentation](../../../mediatailor.md "../../../mediatailor.md") and [CloudFront
Documentation](cloudfront.md "cloudfront.md")

- **AWS Training:** Courses and certifications
  for media services and CDN optimization

Access: [AWS Training and
Certification](https://aws.amazon.com/training/ "https://aws.amazon.com/training/")

- **AWS Knowledge Center:** Curated articles for
  common AWS issues and best practices

Access: [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/")

- **AWS Trusted Advisor:** Automated
  recommendations for optimization and best practices

Access: [AWS Trusted
Advisor](https://console.aws.amazon.com/trustedadvisor/home "https://console.aws.amazon.com/trustedadvisor/home")

- **AWS Personal Health Dashboard:** Service
  health and maintenance notifications

Access: [AWS Personal Health
Dashboard](https://console.aws.amazon.com/phd/home "https://console.aws.amazon.com/phd/home")

## MediaTailor CDN integration support case best

practices

AWS Elemental MediaTailor CDN integration support cases are resolved more efficiently when you follow
these best practices. To get the fastest resolution:

- Choose the appropriate severity level based on business impact
- Provide all relevant information in your initial case submission
- Include specific examples and reproduction steps
- Attach relevant log files and configuration screenshots
- Respond promptly to support engineer requests for additional
  information

**Additional support resources:**

- [AWS Support case management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") - Guide to creating and managing
  support cases
- [AWS Support
  plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/") - Compare support plan features and response times
- [Prepare to support workloads](../../../wellarchitected/latest/operational-excellence-pillar/prepare-to-support-workloads.md "../../../wellarchitected/latest/operational-excellence-pillar/prepare-to-support-workloads.md") - Well-Architected guidance for
  operational readiness
- [AWS
  Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/") - Best practices for building and
  operating workloads on AWS
