

# Apply branding to managed login pages
<a name="managed-login-branding"></a>

You might want to provide a consistent user experience between your authentication service and your application. You can accomplish this goal either with custom forms and back-end API operations in an AWS SDK, or with managed login. Managed login and the classic hosted UI are web front ends for the component of your application that serves authentication with user pools. To synchronize your managed authentication services with your application UX, you have two customization options: the branding editor and hosted UI branding. You can choose your preferred experience in the Amazon Cognito console and with user pool API operations.

**The branding editor**  
The [branding editor](managed-login-brandingeditor.md) is the newest customization option for the newest user pools UI experience, [managed login](cognito-user-pools-managed-login.md). The branding editor is a no-code visual editor for managed login assets and style, and a set of API operations for programmatic configuration of a large number of configuration options. User pools that you configure with a [domain](cognito-user-pools-assign-domain.md) and managed login automatically render the branding-designer version of your login pages.

**Hosted UI (classic) branding**  
The [hosted UI (classic) branding experience](hosted-ui-classic-branding.md) has two options: to modify a cascading stylesheets (CSS) file with a fixed set of style options, and to add a custom logo image. You can set these options in the Amazon Cognito console or with the [SetUICustomization](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUICustomization.html) API operation. At the time that the service launched, Amazon Cognito had only this option. User pools that you configure with a [domain](cognito-user-pools-assign-domain.md) and the hosted UI branding version automatically render the classic version of your login pages. Your [feature plan](cognito-sign-in-feature-plans.md) might also support only the hosted UI.

**Note**  
The branding editor and the classic branding experience modify the visual properties of your hosted authentication service. Currently, you can't modify the text that's displayed on your managed login pages, except to apply localization into one of several languages. For more information about localization, see [Managed login localization](cognito-user-pools-managed-login.md#managed-login-localization).

## Choose a branding experience and assign styles
<a name="managed-login-branding-choose"></a>

In the Amazon Cognito console, new user pools default to the **Managed login** branding experience. User pools that you set up before managed login was available will have **Hosted UI (classic)** branding. You can switch between managed login and hosted UI branding. When you change your **Branding version**, Amazon Cognito immediately applies the change to the user-interactive pages of your user pool domain. With managed login and the hosted UI, your user pool can have a style for each app client.

Each app client can have a distinct branding *style*, but a user pool domain serves either managed login or the hosted UI. A style is the set of customization settings applied to an app client. You can set up one [custom domain](cognito-user-pools-add-custom-domain.md) and one [prefix domain](cognito-user-pools-assign-domain-prefix.md) per user pool. You can assign different branding versions to your custom and prefix domains. However, a prefix domain isn't fully functional when you also have a custom domain—the `.well-known` OIDC discovery endpoints *only* present custom-domain paths. You can only use the prefix domain for operations that don't require endpoint discovery (`openid-configuration`) in a user pool with this configuration. Because of these properties of user pools, you can effectively choose one branding version per user pool.

You can assign styles to the app clients in a user pool where a domain is set to the managed login branding version. Styles are a set of visual settings made up of image files, display options, CSS values. When you assign a style to an app client, Amazon Cognito immediately pushes your updates to your user-interactive login pages. Amazon Cognito renders your user-interactive pages with your chosen branding version and the customization that you have applied to it.

### Update and delete styles
<a name="managed-login-branding-update"></a>

When you create a style, you link it to an app client. To change a style assignment for an app client, you must first delete the original style. Currently, you can't copy settings between styles. You must do this programmatically. To replicate settings between styles and app clients, get the settings for a style with the [DescribeManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeManagedLoginBranding.html) API operation and apply them with [CreateManagedLoginBranding](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.html) or [UpdateManagedLoginBranding](https://docs.aws.amazon.com/). You can't change the assigned styles of an app client—you can only delete the original and set a new one. For more information about managing styles with API and SDK operations, see [API and SDK operations for managed login branding](managed-login-brandingeditor.md#branding-designer-api).

**Note**  
Programmatic requests that create or update branding style must have a request size of no more than 2 MB. If your request is larger than this limit, break your request up into multiple `UpdateManagedLoginBranding` requests for groups of parameters that don't exceed the maximum request size. These requests don't result in unspecified parameters being set to default, so you can send partial requests without any effect on existing settings.

You delete a style in the Amazon Cognito console from the **Managed login** menu. Under **Styles**, choose the style that you want to delete and choose **Delete style**.

At a high level, the process of assigning branding to a domain consists of the following steps.

1. [Create a domain and set the branding version](cognito-user-pools-assign-domain.md).

1. Create a branding style and assign it to an app client.

**To assign a style to an app client**

1. In the **Domain** menu of your user pool, create a domain and set the **Branding version** to **Managed login**.

1. Navigate to the **Managed login** menu. Under **Styles**, choose **Create a style**.

1. Choose the app client that you want to assign your style to, or create a new [app client](user-pool-settings-client-apps.md).

1. To start configuring your branding settings, choose **Launch branding editor**.

**Topics**
+ [Choose a branding experience and assign styles](#managed-login-branding-choose)
+ [The branding editor and customizing managed login](managed-login-brandingeditor.md)
+ [Customizing hosted UI (classic) branding](hosted-ui-classic-branding.md)