

# Security profile permissions for outbound communications in Connect Customer
<a name="security-profile-outbound-communication"></a>

To enable agents to make outbound calls, assign **Make outbound calls** permissions to the agent's security profile as shown in the following image:

![The CCP security profile permissions page, the make outbound calls permission.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_outbound_calls.png)


To enable call center managers to create outbound campaigns, assign the following permissions to their security profile:
+ **Routing**, **Queues**, **View** permission
+ **Outbound campaigns**, **Campaigns**, **View** permission
+ **Channels and Flows**, **Flows**, **View** permission

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).

By default, the **Admin** security profile already has permissions to perform all activities.