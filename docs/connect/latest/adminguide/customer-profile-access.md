

# Access Customer Profiles in the agent workspace
<a name="customer-profile-access"></a>

After you enable Customer Profiles, agents can begin using customer information to provide personalized service. This topic explains how to access Customer Profiles in the agent workspace.

**Tip**  
Make sure your agents have **Customer profiles** permissions in their security profile so they can access Customer Profiles. For more information, see [Security profile permissions for Connect Customer Customer Profiles](assign-security-profile-customer-profile.md).

## Use Customer Profiles in the agent workspace
<a name="customer-profile-access-out-of-the-box"></a>

Customer Profiles is a native application in the agent workspace. Your agents can access contact controls, Customer Profiles, and Cases all in a single browser window.

**Note**  
You can access the agent workspace by using the following URL:  
`https://{{instance-name}}.my.connect.aws/agent/`
If you access your instance using the **awsapps.com** domain, use the following URL:   
`https://{{instance-name}}.awsapps.com/connect/agent/`
For help finding your instance name, see [Find your Connect Customer instance name](find-instance-name.md).

## Embed Customer Profiles into a custom agent application
<a name="customer-profile-access-embed"></a>

You can embed Customer Profiles alongside the Contact Control Panel (CCP) in a custom agent application. You use the [Connect Customer Streams](https://github.com/aws/amazon-connect-streams) library to embed the CCP and Customer Profiles into a custom agent application.

For information about embedding Customer Profiles, see the [Streams documentation](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md).

To build your own user interface for Customer Profiles information, see the documentation for the CustomerProfilesJS library on [GitHub](https://github.com/amazon-connect/amazon-connect-customer-profiles).

**Tip**  
When you build a custom agent application, you determine the URL agents use to access it. That URL might be very different from the one provided by Connect Customer. For example, your URL could be https://example-corp.com/agent-support-app. 