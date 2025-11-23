# Pull-time update exclusions

Amazon ECR updates the `LastRecordedPullTime` timestamp on every pull except for pulls by AWS Inspector. Pull-time update exclusions allow you to specify IAM role ARNs that should not update image pull times when they pull images, such as pulls by third-party scanners (such as Crowdstrike, Snyk, and Trivy). This is useful for images that are used for testing or CI/CD purposes where you don't want the pull time to affect lifecycle policy decisions.

When a role in the exclusion list pulls an image, the pull time remains unchanged. Any other role continues to update pull time (current behavior). You can configure up to 100 exclusions per account.
