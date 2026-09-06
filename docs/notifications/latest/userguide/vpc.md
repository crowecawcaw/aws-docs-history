

# Connecting to AWS User Notifications with interface VPC endpoints
<a name="vpc"></a>

You can use AWS PrivateLink to create a private connection between your virtual private cloud (VPC) and User Notifications so that you can access the service as if it were in your own VPC. This doesn't require the use of an internet gateway, network address translation (NAT) device, virtual private network (VPN) connection, or Direct Connect connection. You establish this private connection by creating an interface endpoint that is powered by AWS PrivateLink. An interface endpoint is an elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported AWS service. Instances in your VPC don't need public IP addresses to access User Notifications. For more information, see [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) and [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint).

**Topics**
+ [Creating an interface VPC endpoints for User Notifications](#creating-vpc-endpoint)
+ [Creating a VPC endpoint policy for User Notifications](#creating-vpc-endpoint-policy)

## Creating an interface VPC endpoints for User Notifications
<a name="creating-vpc-endpoint"></a>

You can create a VPC endpoint for User Notifications using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for User Notifications using the following service name:
+ `com.amazonaws.{{region}}.notifications`

Create a VPC endpoint for User Notifications Contacts using the following service name:
+ `com.amazonaws.{{region}}.notifications-contacts`
**Note**  
 The User Notifications Contacts service VPC endpoint is only supported in the us-east-1 (N. Virginia) Region. 

If you enable private domain name system (DNS) for the endpoint, you can make API requests to User Notifications using its default DNS name. For example, `notifications.us-east-1.api.aws`. For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for User Notifications
<a name="creating-vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to User Notifications. The policy specifies the following information:
+ The principal that can perform actions
+ The actions that can be performed
+ The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

### Example: VPC endpoint policy for User Notifications get and list actions
<a name="example-vpc-endpoint-policy"></a>

The following endpoint policy grants access to get and list actions.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "notifications:Get*",
        "notifications:List*",
        "notifications-contacts:Get*",
        "notifications-contacts:List*"
        
      ],
      "Resource": "*"
    }
  ]
}
```

------