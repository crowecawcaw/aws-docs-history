# Step

1: Set up permissions

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
`GenerateEmbedUrlForAnonymousUser` and
`GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
`GetSessionEmbedUrl` APIs to embed dashboards and the
Amazon Quick Sight console, but they do not contain the latest embedding
capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your
applications](../../../quicksight/latest/user/embedding-overview.md "../../../quicksight/latest/user/embedding-overview.md").

|                                                   |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Applies to:** Enterprise Edition                |
|                                                   |
| ---                                               |
| Intended audience: Amazon Quick Suite developers  | In the following section, you can find out how to set up permissions for the backend application or web server. This task requires administrative access to IAM. Each user who accesses a dashboard assumes a role that gives them Amazon Quick Sight access and permissions to the dashboard. To make this possible, create an IAM role in your AWS account. Associate an IAM policy with the role to provide permissions to any user who assumes it. The following sample policy provides these permissions for use with `IdentityType=ANONYMOUS`. For this approach to work, you also need a session pack, or session capacity pricing, on your AWS account. Otherwise, when a user tries to access the dashboard, the error `UnsupportedPricingPlanException` is returned. JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:GetDashboardEmbedUrl", "quickSight:GetAnonymousUserEmbedUrl" ], "Resource": "*" } ] }` `` Your application's IAM identity must have a trust policy associated with it to allow access to the role that you just created. This means that when a user accesses your application, your application can assume the role on the user's behalf to open the dashboard. The following example shows a role called `QuickSightEmbeddingAnonymousPolicy`, which has the sample policy preceding as its resource. For more information regarding trust policies, see [Temporary security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the _IAM User Guide_. |
