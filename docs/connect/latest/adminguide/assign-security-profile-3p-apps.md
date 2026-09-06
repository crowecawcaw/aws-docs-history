

# Assign permissions to use third-party applications
<a name="assign-security-profile-3p-apps"></a>

Agents need specific security profile permissions to access third-party applications that you have added and associated with your instance. For a list of third-party application permissions and their API names, see [List of security profile permissions in Connect Customer](security-profile-list.md).

**Note**  
After you associate an application with an instance, the application can take up to 10 minutes to appear in the **Agent Applications** section of the **Security profiles** page.

Applications that you have onboarded to AWS and associated with your Connect Customer instance appear in the **Agent Applications** section of the **Security profiles** page. The following image shows an example.

![The Agent applications section of the Security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_agent_apps.png)


You also need to enable the **Access Contact Control Panel** permission for third-party apps to appear.

![Access Contact Control Panel (CCP) permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/assign-security-profile-3p-apps-ccp-permissions.png)


After you assign permissions, see [Access third-party applications in the agent workspace](3p-apps-agent-workspace.md).