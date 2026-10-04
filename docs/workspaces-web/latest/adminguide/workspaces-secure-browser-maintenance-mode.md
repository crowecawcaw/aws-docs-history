

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Amazon WorkSpaces Secure Browser availability change
<a name="workspaces-secure-browser-maintenance-mode"></a>

After careful consideration, we decided to close Amazon WorkSpaces Secure Browser to new customers starting October 29, 2026. If you want to use WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal.

This section providesw information about the migration options for Amazon WorkSpaces Secure Browser customers.

## Alternative solutions
<a name="maintenance-mode-alternatives"></a>

You can continue to use the service. If you want to migrate to an alternative solution, we recommend one of the following.

### Amazon WorkSpaces Applications with a self-managed Chrome image
<a name="maintenance-mode-alt-workspaces-applications"></a>

Amazon WorkSpaces Applications with a self-managed Chrome image provides the same pixel-streaming isolation as WorkSpaces Secure Browser. With pixel streaming, browser content renders remotely, and only images stream to the device. It runs within your existing AWS account. It uses AWS Identity and Access Management (IAM), Amazon Virtual Private Cloud (VPC), and AWS CloudTrail, and it follows your data-residency posture. WorkSpaces Applications uses an instance-hour model. It supports the most important WorkSpaces Secure Browser features, including clipboard and download controls.

The following WorkSpaces Secure Browser features are not built in to WorkSpaces Applications. They need extra setup:

SSO passthrough to downstream applications  
WorkSpaces Secure Browser provides automatic single sign-on to applications that users access within the browser session. In WorkSpaces Applications, you configure this yourself. Force-install your identity provider's browser extension into the Chrome image by using the `ExtensionSettings` Chrome policy, and point the extension to your IdP tenant. Examples include the Okta Browser Plugin, Microsoft Single Sign-On, and Ping Identity. After you configure the extension, it recognizes the user's authenticated session and passes the user through to downstream applications without additional login prompts. Refer to your identity provider's documentation for the specific extension configuration parameters.

Browser policy updates  
WorkSpaces Secure Browser pushes policy changes from the console to active sessions in real time. In WorkSpaces Applications, policy changes require you to update the Chrome image and redeploy it.

Unified session audit  
In WorkSpaces Secure Browser, a single audit stream captures all session and browser activity. In WorkSpaces Applications, session events such as connections and disconnections go to Amazon CloudWatch. You can report browser events such as visited URLs, downloads, and installed extensions separately through the Google Admin console. Browser-level reporting requires a Chrome Enterprise subscription. It also requires you to enroll the Chrome browser in Chrome Browser Cloud Management by setting the `CloudManagementEnrollmentToken` policy in the Chrome image (`/etc/opt/chrome/policies/managed/`).

Content category filtering  
This requires you to filter outbound requests through Amazon Route 53 DNS Firewall, or through a third-party data loss prevention (DLP) browser extension or proxy.

Inline data redaction  
This requires a third-party data loss prevention (DLP) browser extension.

### An enterprise secure browser
<a name="maintenance-mode-alt-enterprise-browser"></a>

Enterprise secure browser solutions offer the same capabilities as WorkSpaces Secure Browser. These capabilities include data loss prevention, user-based management, auditing, and URL filtering. One example is the AWS Partner Island Enterprise Browser. Unlike the cloud-rendered approach of WorkSpaces Secure Browser, these browsers install and run natively on the endpoint. They apply enterprise security policies, such as DLP, URL filtering, and session controls, locally.

## Migration plan
<a name="maintenance-mode-migrate"></a>

The following recommendations can help you migrate to an alternative solution.

### Start by exporting your WorkSpaces Secure Browser configuration
<a name="maintenance-mode-export-config"></a>

If you migrate to a Chromium-based solution, start by exporting your browser policies. Examples of Chromium-based solutions include a Chrome image managed in WorkSpaces Applications and Island Enterprise Browser. Export the browser policies as JSON for each WorkSpaces Secure Browser portal from the WorkSpaces Secure Browser console. You can then upload the file in the new solution to replicate the browser policies.

To export your browser policies for a portal, complete the following steps.

1. Open the WorkSpaces Secure Browser console in your AWS account.

1. In the navigation pane, choose **Portals**.

1. Select your web portal, and then choose **Edit**.

1. Scroll down to **Policy settings**, and then select **JSON editor**.

1. Copy the JSON content, and then save it as a `.json` file on your computer.

We also recommend that you document any additional configuration settings for replication in the target solution. These settings include SSO integration, DLP rules, and session and control policies.

### Migrating to Amazon WorkSpaces Applications
<a name="maintenance-mode-migrate-workspaces-applications"></a>

WorkSpaces Applications offers three fleet types. The right choice depends on your startup time requirements, your operational preferences, and whether your use case involves multi-session instances or Active Directory integration.

The session launch times that follow are approximate. They vary based on factors such as instance type, network configuration, and installed browser extensions. We recommend that you test your configuration to validate performance before you deploy at scale.

Always-On  
Always-On instances run continuously and provide near-instant session launch. You manage the fleet's auto scaling policies to match capacity to user demand. The fleet uses a full image that includes the operating system and applications, which gives you full control over the OS configuration. Always-On fleets support Active Directory domain join for environments that require it, such as Kerberos authentication to downstream resources or Group Policy application. They also support multi-session instances (Windows only), where multiple users share the same instance.

On-Demand  
On-Demand is similar to Always-On in capabilities, including Active Directory join, multiple applications, multi-session, and a full OS image. It is optimized for cost. WorkSpaces Applications provisions instances but keeps them stopped until a user requests a session, which results in a one-to-two-minute startup. You pay a lower stopped-instance rate when instances are idle, and the running rate only during active sessions. Auto scaling policies are still required.

Elastic  
WorkSpaces Applications assigns Elastic instances from an AWS-managed pool when a user starts a session, with an approximately one-minute startup. Elastic fleets need no capacity planning or auto scaling policies, which simplifies operations. You pay only for the duration of each streaming session. WorkSpaces Applications delivers the application through an app block, which is a VHD stored in Amazon S3 that contains only the Chrome application. This makes image management simpler, because you maintain only the application VHD rather than a full OS image. Elastic fleets do not support Active Directory domain join or multi-session instances.

For a browser-only use case where no user state persists between sessions and Active Directory domain join is not required, we recommend Elastic. It provides a session-based, non-persistent model with no scaling management overhead and a simpler image lifecycle.

If your environment requires Active Directory domain join or multi-session instances, choose Always-On or On-Demand. Also choose one of these if your users need Chrome alongside other applications in a single desktop session. Choose Always-On if near-instant session launch is a priority. Choose On-Demand if you prefer to optimize for cost.

For instructions on setting up an Always-On or On-Demand fleet, refer to the Amazon WorkSpaces Applications documentation. Complete the following tasks:

1. Create a custom image. Launch an image builder, install Chrome, configure your security hardening and browser policies, and then create your image.

1. Create a fleet. Provision your Always-On or On-Demand fleet by using the image you created.

1. Create a stack. Associate your fleet with a stack, and then configure user access with SAML or OIDC.

1. Configure fleet auto scaling. Set scaling policies to match fleet capacity to user demand.

For instructions on setting up an Elastic fleet, refer to the Amazon WorkSpaces Applications documentation. Complete the following tasks:

1. Create an app block. Build a VHD that contains your Chrome application, browser policies, and extensions, and then upload it to Amazon S3.

1. Create an application. Define the application resource that points to the Chrome executable in your app block.

1. Create a fleet. Create an Elastic fleet, and then associate your application with it.

1. Create a stack. Associate your fleet with a stack, and then configure user access with SAML or OIDC.

### Migrating to a third-party enterprise secure browser
<a name="maintenance-mode-migrate-third-party"></a>

We recommend that you consult your target solution's documentation for detailed migration steps.