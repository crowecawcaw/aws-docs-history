

# Embedding with the AWS Quick Sight APIs


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  AWS Quick developers  | 

There are only a few steps involved in the actual process of embedding analytics using the AWS Quick Sight APIs. 

Before you begin, make sure to have the following items in place:
+ Set up the required IAM permissions for the caller identity used by your application that will use the AWS SDK to make API calls. For example, grant permission to allow the `quicksight:GenerateEmbedUrlForAnonymousUser` or `quicksight:GenerateEmbedUrlForRegisteredUser` action.
+ To embed for registered users, share AWS Quick Sight assets with them beforehand. For new authenticating users, know how to grant access to the assets. One way to do this is by adding all the assets to a AWS Quick Sight folder. If you prefer to use the AWS Quick Sight API, use the `DescribeDashboardPermissions` and `UpdateDashboardPermissions` API operations. For more information, see [DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardPermissions.html) or [UpdateDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPermissions.html) in the *AWS Quick API Reference*. If you want to share the dashboard with all users in a namespace or group, you can share the dashboard with `namespace` or `group`.
+ If you're embedding dashboards, make sure to have the ID of the dashboards you want to embed. The dashboard ID is the code in the URL of the dashboard. You can also get it from the dashboard URL.
+ A AWS Quick Sight administrator must explicitly enable domains where you plan to embed your AWS Quick Sight analytics. You can do this by using the **Manage AWS Quick Sight**, **Domains and Embedding** from the profile menu, or you can use the `AllowedDomains` parameter of a `GenerateEmbedUrlForAnonymousUser` or `GenerateEmbedUrlForRegisteredUser` API call.

  This option is only visible to AWS Quick Sight administrators. You can also add subdomains as part of a domain. For more information, see [Allow listing domains at runtime with the AWS Quick API](manage-domains.md#embedding-run-time).

  All domains in your static allow list (such as development, staging, and production) must be explicitly allowed, and they must use HTTPS. You can add up to 100 domains to the allow list. You can add domains at runtime with AWS Quick Sight API operations.

After all the prerequisites are complete, embedding AWS Quick Sight involves the following steps, which are explained in greater detail later: 

1. For authentication, use your application server to authenticate the user. After authentication in your server, generate the embedded dashboard URL using the AWS SDK that you need.

1. In your web portal or application, embed AWS Quick Sight using the generated URL. To simplify this process, you can use the AWS Quick Sight Embedding SDK, available on [NPMJS](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) and [GitHub](https://github.com/awslabs/amazon-quicksight-embedding-sdk). This customized JavaScript SDK is designed to help you efficiently integrate AWS Quick Sight into your application pages, set defaults, connect controls, get callbacks, and handle errors. 

You can use AWS CloudTrail auditing logs to get information about the number of embedded dashboards, users of an embedded experience, and access rates.

**Topics**
+ [Embedding AWS Quick Sight dashboards with the AWS Quick Sight API](embedding-dashboards.md)
+ [Embedding AWS Quick Sight visuals with the AWS Quick Sight APIs](embedding-visuals.md)
+ [Embedding the full functionality of the AWS Quick Sight console for registered users](embedded-analytics-full-console-for-authenticated-users.md)
+ [Embedding the Amazon Q in AWS Quick Sight Generative Q&A experience](embedding-gen-bi.md)
+ [Embedding the AWS Quick Sight Q search bar (Classic)](embedding-quicksight-q.md)
+ [Embedding analytics using the GetDashboardEmbedURL and GetSessionEmbedURL API operations](embedded-analytics-deprecated.md)