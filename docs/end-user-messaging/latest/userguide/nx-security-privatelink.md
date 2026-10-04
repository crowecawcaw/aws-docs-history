

# AWS PrivateLink
<a name="nx-security-privatelink"></a>

You can use AWS PrivateLink to create a private connection between your virtual private cloud (VPC) and AWS End User Messaging by creating an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), which lets you privately access AWS End User Messaging APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not need public IP addresses to communicate with the AWS End User Messaging APIs. For more information, see the [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html).

AWS End User Messaging is made up of separate APIs, and each one has its own interface endpoint service name. Create an interface endpoint for the API that matches the channel you send on. When you turn on private DNS for the interface endpoint, you can make API requests using the default Regional DNS name for the API.


**AWS End User Messaging interface endpoint service names**  

| API | Service name | Channels | 
| --- | --- | --- | 
| End User Messaging | `com.amazonaws.{{region}}.end-user-messaging` | All channels | 
| SMS and Voice v2 | `com.amazonaws.{{region}}.pinpoint-sms-voice-v2` | SMS, MMS, voice, and RCS | 
| Social messaging | `com.amazonaws.{{region}}.social-messaging` | WhatsApp | 
| Push | `com.amazonaws.{{region}}.pinpoint` | Push notifications | 

Each service name also has a Federal Information Processing Standard (FIPS) compliant variant, formed by appending `-fips` to the service name, for example `com.amazonaws.{{region}}.end-user-messaging-fips`.