

# Embedding dashboards for everyone using GetDashboardEmbedURL (old API)

**Important**  
AWS Quick Sight has new APIs for embedding analytics: `GenerateEmbedUrlForAnonymousUser` and `GenerateEmbedUrlForRegisteredUser`.  
You can still use the `GetDashboardEmbedUrl` and `GetSessionEmbedUrl` APIs to embed dashboards and the AWS Quick Sight console, but they do not contain the latest embedding capabilities. For the latest up-to-date embedding experience, see [Embedding AWS Quick Sight analytics into your applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html).


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  AWS Quick developers  | 

In the following sections, you can find detailed information on how to set up embedded AWS Quick Sight dashboards for everyone (nonauthenticated users) using GetDashboardEmbedURL.

**Topics**
+ [Step 1: Set up permissions](embedded-analytics-dashboards-with-anonymous-users-get-step-1.md)
+ [Step 2: Get the URL with the authentication code attached](embedded-analytics-dashboards-with-anonymous-users-get-step-2.md)
+ [Step 3: Embed the dashboard URL](embedded-analytics-dashboards-with-anonymous-users-get-step-3.md)