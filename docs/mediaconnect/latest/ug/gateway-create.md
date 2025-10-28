# Setting up a MediaConnect Gateway

Setup begins with creating the gateway. This can be done in the MediaConnect
console, programmatically using the MediaConnect API, or by using AWS
CloudFormation.

###### Contents

- [Prerequisites](gateway-create.md#gateway-create-prerequisites "gateway-create.md#gateway-create-prerequisites")
- [Procedure](gateway-create.md#gateway-create-procedure "gateway-create.md#gateway-create-procedure")
- [Next steps](gateway-create.md#gateway-create-next-steps "gateway-create.md#gateway-create-next-steps")

## Prerequisites

- Make sure that you’ve reviewed the [Supported operating systems and system
  architectures for using MediaConnect Gateway](gateway-prerequisites.md "gateway-prerequisites.md").
- Before creating a gateway, you will need the name, egress CIDR IP
  information, and network information of the gateway you want to
  create.

## Procedure

You can create a gateway using the console or the AWS CLI.

Console

###### To create a gateway using the console

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. From the navigation pane, select
   **Gateways**. In the
   **Gateways** section, choose
   **Create gateway**.
3. On the **Create gateway** page, enter a
   **Name** for your gateway. This name
   can't be modified later.
4. For the **Egress CIDR blocks**: Enter a
   CIDR block for the egress of your gateway. These IP
   addresses should be in the form of a Classless Inter-Domain
   Routing (CIDR) block; for example, 10.0.0.0/16. This CIDR
   block represents a range of IP addresses that are allowed to
   contribute content or initiate output requests for flows
   communicating with this gateway.

###### Important

Don't use 0.0.0.0/0 for the **Egress CIDR
blocks**. This will open the gateway to the
public. 5. In the **Networks** section, enter a name
for your first network. A gateway may contain a maximum of
two networks. Each network name must be unique for this
gateway. 6. Enter a **CIDR block** for this network.
To complete the creation of the gateway, choose the
**Create Gateway** button.

AWS CLI

###### To create a gateway using the AWS CLI

1. Find the name, egress CIDR IP information, and network
   information of the gateway you want to create. Store this
   information in a JSON file on the computer that runs the
   AWS CLI. The JSON file should be named
   `gateway.json`. The following example shows
   the correct sections and formatting for the JSON
   file.

```
{
    "Name": "`gateway`",
    "EgressCidrBlocks": [
        "`10.20.30.0/24`"
    ],
    "Networks": [
        {
            "Name": "`blue`",
            "CidrBlock": "`172.31.48.0/20`",
        }
    ]
}
```

2. Enter the following command into the AWS CLI interface. Replace
   the `<yourprofile>` and `<region>`
   values with your desired profile and AWS Region.

```
 aws --profile `<yourprofile>` --region `<region>` mediaconnect create-gateway
      --cli-input-json file://gateway.json
```

3. The AWS CLI will return a response like the following
   example.

```
    "Gateway": {
        "EgressCidrBlocks": [
            "10.20.30.0/24"
        ],
        "GatewayArn": "arn:aws:mediaconnect:us-west-2:111122223333:gateway:1-23aBC45dEF67hiJ8-12AbC34DE5fG:gateway",
        "GatewayState": "CREATING",
        "Name": "gateway",
        "Networks": [
            {
                "CidrBlock": "172.31.48.0/20",
                "Name": "blue"
            }
        ]
    }
}
```

## Next steps

After a MediaConnect Gateway and its networks are created, you can begin registering
instances to that MediaConnect Gateway. For instructions, see [Registering a MediaConnect Gateway
instance](gateway-components-instances-create.md "gateway-components-instances-create.md").
