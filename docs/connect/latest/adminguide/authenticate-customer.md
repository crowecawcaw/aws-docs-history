

# Flow block in Connect Customer: Authenticate Customer
<a name="authenticate-customer"></a>

This topic defines the flow block to authenticate customers and route them to specific paths within a flow based on the authentication result. 

**Note**  
Before you can use this block:  
The customer authentication capability must be enabled for your Connect Customer instance. In addition, a new Amazon Cognito user pool must be created with your identity provider. For instructions, see [Set up customer authentication in Connect Customer for chat contacts](customer-auth.md). 
Customer Profiles must be [enabled](enable-customer-profiles.md) for your Connect Customer instance.

## Description
<a name="authenticate-customer-description"></a>
+ Enables your customers to authenticate during a chat. 
+ After a customer successfully signs in, and an ID token is retrieved from Amazon Cognito, Connect Customer either updates an existing customer profile or creates a new customer profile, depending on the identifier used to store the information into customer profiles.
+ If the First Name field is present in the customer profile, the customer's display name is updated to that name.

## Use cases for this block
<a name="scenarios-authenticate-customer"></a>

This flow block is designed to be used in the following scenarios:
+ You can prompt your customers to sign in and authenticate during a chat. For example, unauthenticated customers can be prompted to sign in:
  + When engaged with a chat bot, before to being routed to an agent.
  + To perform a transaction, such as making a payment.
  + To validate their identity before providing account status or allowing them to update their profile information.
+ You can also use this block to authenticate customers during chats over [Apple Messages for Business](enabling-authentication-for-apple-messages-for-business.md).

## Contact types
<a name="play-channels"></a>


| Contact type | Supported? | 
| --- | --- | 
| Voice | No - **Error** branch | 
| Chat | Yes  | 
| Task | No - **Error** branch | 
| Email | No - Error branch | 

## Flow types
<a name="authenticate-customer-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):


| Flow type | Supported? | 
| --- | --- | 
| Inbound flow | Yes | 
| Customer queue flow | No | 
| Customer hold flow | No | 
| Customer whisper flow | No | 
| Outbound whisper flow | No | 
| Agent hold flow | No | 
| Agent whisper flow | No | 
| Transfer to agent flow | No | 
| Transfer to queue flow | No | 

## How to configure this block
<a name="authenticate-customer-properties"></a>

You can configure the **Authenticate Customer** block by using the Connect Customer admin website or by using the [AuthenticateParticipant](https://docs.aws.amazon.com/connect/latest/APIReference/participant-actions-authenticateparticipant.html) action in the Connect Customer Flow language. 

The following image shows an example of the Properties page for the **Authenticate Customer** block. 

![The properties page of the Authenticate Customer block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/authenticate-customer-properties.png)


**Amazon Cognito**
+ **Select an Amazon Cognito User Pool**: After you associate the user pool on the console page, choose the name of the user pool from the drop-down list. 
+ **Select an Amazon Cognito App Client**: After you select the user pool, choose the name of the app client from the drop-down list. 

**Connect Customer Customer Profiles Configuration**
+ **Store by default template**: By choosing the default template, Amazon Connect Customer Profile ingests [Amazon Cognito standard attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#cognito-user-pools-standard-attributes) into a unified standard profile object based on the predefined Customer Profile object type. This template uses phone number and email to map the customer to a profile. 
+ **Enter a unique identifier**: You can customize how Customer Profiles ingests data by [creating an object type mapping](create-object-type-mapping.md). If you want to customize the data mapping or key, create your own object type mapping in advance, select **Enter a unique identifier** and enter the mapping name. 

**Timeout**: Enter how long until inactive customers who haven't signed in are routed down the Timeout branch. 
+ Minimum (default): 3 minutes
+ Maximum: 15 minutes

### Flow block branches
<a name="authenticate-customer-branches"></a>

This block supports the following output branches:

![A configured Authenticate Customer block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/authenticate-customer-configured.png)

+ **Success**: The customer was authenticated.
+ **Timeout**: The customer was inactive and did not sign in within the allocated amount of time.
+ **Opted out**: The customer chose not to sign in.
+ **Error**: One of the [error scenarios](#authenticate-customer-errorscenarios) occurred.

### Additional configuration tips
<a name="authenticate-customer-tips"></a>
+ We recommend that you enable flow logs in an Amazon CloudWatch log group provide you with real-time details about events in your flows as customers interact with them. You can also use flow logs to help debug your flows as you are creating them. For more information, see [Enable Connect Customer flow logs in an Amazon CloudWatch log group](contact-flow-logs.md).
+ For information about enabling customer authentication for Apple Messages for Business Chats, see [Enable authentication for Apple Messages for Business](enabling-authentication-for-apple-messages-for-business.md).

### Data generated by this block
<a name="authenticate-customer-data"></a>

This block does not generate any data.

## Error scenarios
<a name="authenticate-customer-errorscenarios"></a>

A contact is routed down the **Error** branch in the following situations:
+ Customer Profiles has not been enabled in your Connect Customer instance. The option to enable Customer Profiles is selected by default when you create an instance, but it's possible to unselect this option. For instructions about enabling Customer Profiles manually, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md). 
+ The chat subtype is not supported. 
+ The provided authentication code is incorrect. 
+ Error from Amazon Cognito token endpoint because the client or request is not configured correctly (`invalid_request`, `invalid_client`, `unauthorized_client`)
+ The Region is not supported. For a list of supported Regions, see [Customer authentication availability by Region](regions.md#customerauthentication_region).