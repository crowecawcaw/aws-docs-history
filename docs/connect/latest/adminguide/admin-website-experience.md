

# Admin website experience
<a name="admin-website-experience"></a>

**Important**  
To use this feature, ensure that users, including admins and supervisors, who access the Connect Customer admin website are associated with a traffic distribution group.

With Connect Customer Global Resiliency (ACGR), you are redirected to a Region's admin website based on your traffic distribution group (TDG) configuration. For example, if your TDG is configured 100-0 to US East (N. Virginia), you are presented with the US East (N. Virginia) instance admin website when you sign in.

To access the linked ACGR instance in the alternate Region, choose **Sign in to alternate environment** in the banner. This banner is available on all pages.

![Admin website banner reading "Amazon Connect Global Resiliency is enabled on this instance. Select 'Sign in to alternate environment' to access the other instance," with a Sign in to alternate environment button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/admin-website-acgr-signin-banner.png)


**Note**  
You are always redirected to the Region that your TDG configuration points to. For example, if your TDG is configured 100-0 to US East (N. Virginia) and you try to access the US West (Oregon) admin website, you are redirected to US East (N. Virginia). To reach the US West (Oregon) website, use **Sign in to alternate environment** in the banner.

## Admin website experience during a Region switch
<a name="admin-website-experience-region-switch"></a>

When you call [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) to move users to the alternate Region, a banner notifies you that a Region switch has started. This appears while you are working in the admin website, for example, when you are monitoring real-time metrics or making configuration updates. A 60-second timer gives you time to finish before the switch. When the timer expires, you are redirected to the alternate Region. This differs from the agent workspace, which adopts graceful Region switch and waits for active contacts to close before switching.

If you need more time, choose **Delay switch** in the banner to add another 60 seconds.

![Admin website banner reading "Your organization is switching to an alternate environment. You will be switched automatically in 42 seconds. If you have unsaved changes, delay the switch," with a Delay switch button.](https://docs.aws.amazon.com/connect/latest/adminguide/images/admin-website-region-switch-banner.png)


**Note**  
You can choose **Delay switch** as many times as you need. If you browse to a different page in the admin website after the UpdateTrafficDistribution call is made, the admin website redirects to the alternate Region automatically.