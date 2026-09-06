

# Planning ahead for bulk changes
<a name="profile-channel-params-plan-ahead"></a>

When you create a channel parameter that you might use in another profile, note its name carefully so you can enter the exact same name in the other profile. 

This careful planning will help if you ever want to make a bulk change to switch several channels to a different profile ([Changing the profile used by multiple channels](changing-the-profile-used-by-multiple-channels.md)). 

**Example of good planning**

You create profile\_A that has one channel parameter called {{input\_network\_location}}. You create profile\_B that has one channel parameter called {{input\_network\_location}}. You assign each profile to one channel: channel\_1 and channel\_2. You later want to use the [task feature](changing-the-profile-used-by-multiple-channels.md) to change the profile of channel\_1 and channel\_2 to use profile\_C. 

The two profiles have use the same channel parameter name for the same field. You will be able to switch both channels to profile C without a problem. 

**Example of bad planning**

This example is the same as the previous example except that you name the channel parameters differently:
+ Profile\_A uses the name {{input\_network\_location}}. 
+ Profile\_B uses the name {{input\_nw\_location}} for the channel parameter for the same field.

You won't be able to change the profiles without making adjustments.