

# Get and store an agent's validated physical address in your Connect Customer instance
<a name="get-and-store-agent-address-e911"></a>

The first step in setting up E911 for your Connect Customer instance is to get and store the agent's validated physical address. The following illustration shows the process for storing addresses.

![Connect Customer E911 address storage process.](http://docs.aws.amazon.com/connect/latest/adminguide/images/e911-workflow.png)


1. Since agents might be working from different locations (for example, office building, home, or coffee shop), it's critical that the most recently validated address is passed along with the emergency outbound call. 

   1. Store a validated address when you first set up an agent on Connect Customer, based on the agent's usual location. 

   1. Prompt the agent to update their address at the start of their shift to help make sure that the emergency outbound call has their latest address.

   1. Check addresses against a database of valid street addresses (Master Street Address Guide).

1. Use the Amazon Chime API [ValidateE911Address](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html). This API validates and returns the validated physical address. 

1. Use the [CreateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html) or [UpdateProfile](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateProfile.html) APIs to store the validated address in Connect Customer Customer Profiles. 
**Note**  
We recommend using `CreateProfile` when it is required to add a validated address the first time. After that, use `UpdateProfile`. 