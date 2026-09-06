

# Access Connect Customer Customer Profiles in the agent workspace
<a name="customer-profile-access"></a>

After you enable Connect Customer Customer Profiles, agents can begin interacting with customers and access [customer information](https://docs.aws.amazon.com/connect/latest/adminguide/customer-profiles.html) to provide personalized service. This topic explains how to access the Connect Customer agent workspace.

**Tip**  
Make sure your agents have **Customer profiles** permissions in their security profile so they can access Customer Profiles. For more information, see [Security profile permissions for Connect Customer Customer Profiles](assign-security-profile-customer-profile.md).

## Option 1: Use Customer Profiles with the CCP out-of-the-box
<a name="customer-profile-access-out-of-the-box"></a>

Customer Profiles is already embedded alongside the Contact Control Panel (CCP). Your agents can access the CCP, Customer Profiles, and Connect Customer's Case management all in the same browser window by logging into their Connect Customer instance and choosing the **Agent Workspace** button located at the top right corner as shown in the following image.

![The Customer Profiles page and the button highlighted that opens the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-agent-workspace-open.png)


**Note**  
You can also access the agent workspace by using the following URL:  
**https://{{instance name}}.my.connect.aws/agent-app-v2/**
If you access your instance using the **awsapps.com** domain, use the following URL:   
**https://{{instance name}}.awsapps.com/connect/agent-app-v2/**
For help finding your instance name, see [Find your Connect Customer instance name](find-instance-name.md).

Following is an example of what Customer Profiles looks like in the agent workspace.

![The Customer Profiles tab and the CCP in the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-profiles-agent-app.png)


## Option 2: Embed Customer Profiles into a custom agent workspace
<a name="customer-profile-access-embed"></a>

When you embed your Contact Control Panel (CCP), you have the option of showing or hiding the pre-built CCP user interface. For example, you might want to develop a custom agent workspace that has a user interface you design, with customized buttons to accept and reject calls. Or, you might want to embed the pre-built CCP that's included with Connect Customer into another custom app.

Regardless of whether you display the pre-built CCP user interface, or hide it and build your own, you use the [Connect Customer Streams](https://github.com/aws/amazon-connect-streams) library to embed the CCP and Customer Profiles into the agent's workspace. This way, Connect Customer Streams is initialized, and the agent can connect and authenticate to Connect Customer, and Customer Profiles. 

For information about embedding Customer Profiles, see [Initialization for CCP, Customer Profiles, and Wisdom](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#initialization-for-ccp-customer-profiles-and-wisdom).

To build your own widget while using raw data from Customer Profiles, see the [Github](https://github.com/amazon-connect/amazon-connect-customer-profiles) documentation about how to use the CustomerProfilesJS open source library.

**Tip**  
When you customize the agent's workspace, you determine the URL agents will use to access their agent workspace, and it might very different from the one provided by Connect Customer. For example, your URL could be https://example-corp.com/agent-support-app. 