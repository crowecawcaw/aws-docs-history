# Get started with the Trusted Advisor API

The AWS Trusted Advisor API Reference is intended for programmers that need detailed information about
the Trusted Advisor
API operations and data types. This API provides access to Trusted Advisor recommendations for your account or all the
accounts
within your AWS Organization. The Trusted Advisor API uses HTTP methods that returns results in JSON format.

###### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Trusted Advisor API
- If you call the AWS Trusted Advisor API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, then you receive
  an Access Denied exception. For more information about changing your support plan,
  [see AWS Support.](aws-support-plans.md "aws-support-plans.md")

You can use the AWS Trusted Advisor API to get a list of checks and their descriptions, recommendations, and
resources for recommendations. You can also update the lifecycle of recommendations. To manage recommendations, use the
following API operations:

- Use the
  [ListChecks](../../../trustedadvisor/latest/APIReference/API_ListChecks.md "../../../trustedadvisor/latest/APIReference/API_ListChecks.md"),
  [ListRecommendations](../../../trustedadvisor/latest/APIReference/API_ListRecommendations.md "../../../trustedadvisor/latest/APIReference/API_ListRecommendations.md"),
  [GetRecommendation](../../../trustedadvisor/latest/APIReference/API_GetRecommendation.md "../../../trustedadvisor/latest/APIReference/API_GetRecommendation.md"),
  and
  [ListRecommendationResources](../../../trustedadvisor/latest/APIReference/API_ListRecommendationResources.md "../../../trustedadvisor/latest/APIReference/API_ListRecommendationResources.md")
  API operations to view recommendations and corresponding accounts and resources.
- Use The
  [UpdateRecommendationLifecycle](../../../trustedadvisor/latest/APIReference/API_UpdateRecommendationLifecycle.md "../../../trustedadvisor/latest/APIReference/API_UpdateRecommendationLifecycle.md")
  API operation to update the lifecycle of a recommendation that's managed by Trusted Advisor Priority.
- Use The
  [BatchUpdateRecommendationResourceExclusion](../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md "../../../trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.md")
  API operation to include or exclude one or more resources from your Trusted Advisor results.
- The
  [ListOrganizationRecommendations](../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendations.md "../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendations.md"),
  [GetOrganizationRecommendation](../../../trustedadvisor/latest/APIReference/API_GetOrganizationRecommendation.md "../../../trustedadvisor/latest/APIReference/API_GetOrganizationRecommendation.md"),
  [ListOrganizationRecommendationResources](../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationResources.md "../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationResources.md"),
  [ListOrganizationRecommendationAccounts](../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationAccounts.md "../../../trustedadvisor/latest/APIReference/API_ListOrganizationRecommendationAccounts.md"),
  and
  [UpdateOrganizationRecommendationLifecycle](../../../trustedadvisor/latest/APIReference/API_UpdateOrganizationRecommendationLifecycle.md "../../../trustedadvisor/latest/APIReference/API_UpdateOrganizationRecommendationLifecycle.md")
  API calls support only recommendations that are managed by Trusted Advisor Priority. These recommendations are also referred to as prioritized recommendations.
  You can view and manage your prioritized recommendations from a management or delegated admin account if you have activated Trusted Advisor
  Priority. If Priority isn't activated, then you receive an Access Denied exception when you make requests.

For more information,
[see AWS Trusted Advisor in the AWS Support User Guide.](aws-support-plans.md "aws-support-plans.md")

For authentication of requests, [see the Signature Version 4 Signing Process.](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md")
