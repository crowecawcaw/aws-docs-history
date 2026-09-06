

# Creating connections to private APIs
<a name="connection-private-create"></a>

The following steps walk you through how to create a connection to a private API. For detailed instructions that include all configuration options for connections, including creating connections to public APIs, see [Creating connections](eb-target-connection-create.md).

## Define the connection
<a name="connection-private-create-define"></a>

The following steps walk you through how to create a connection to a private API endpoint. For instructions on creating connections to public APIs, see [Creating connections](eb-target-connection-create.md).

1. Open the [EventBridge console](https://console.aws.amazon.com/events).

1. In the left navigation pane, under **Integration**, choose **Connections**.

1. Choose **Create connection**.

1. On the **Create connection** page, enter a **Connection name** and **Description**.

## Configure the invocation endpoint
<a name="connection-private-create-invocation"></a>

Next, use the **Configure invocation** section to specify the HTTPS endpoint you want the connection to invoke.

1. For **API type**, choose **Private**.

1. Specify the Amazon VPC Lattice resource configuration to use to connect to it. 

   Under **Private API**: 
   + To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
   + To create a new VPC Lattice resource configuration, choose **New resource configuration**.

     You are taken to the Amazon VPC Lattice; service console, where you can create a new configuration. for more information, see [Create a resource configuration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-resource-configuration.html) in the *Amazon VPC Lattice User Guide*.

## Configure the endpoint authorization
<a name="connection-private-create-auth"></a>

Lastly, specify the authorization settings to use to access the endpoint. 

EventBridge supports basic, OAuth client credentials, and API key authentication methods.

1. Under **Configure authorization**, choose **Custom configuration**.

1. For **Authorization type**, select the authorization method for the connection to use.

1. Specify the authorization configuration details for the authorization method you chose:
   + **Basic**

     Enter the **Username** and **Password** to use to authorize with the HTTPS endpoint.
   + **OAuth Client Credentials**

     1. For **OAuth authorization endpoint**, choose whether the endpoint to use for connection authorization is a public or private (VPC) endpoint.

        If you choose **Private**, specify the **Private OAuth endpoint resource configuration**:
        + To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
        + To create a new VPC Lattice resource configuration, choose **New resource configuration**.

          You are taken to the Amazon VPC Lattice service console, where you can create a new configuration. for more information, see [Create a resource configuration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/create-resource-configuration.html) in the *Amazon VPC Lattice User Guide*.

     1. Specify the following authorization information:
        + Authorization endpoint
        + HTTPS method
        + Client ID
        + Client secret

     1. Under **OAuth HTTP parameters**, add any additional parameters to include for authorization with the authorization endpoint. 

        To do so:
        + Select a **Parameter** from the drop-down list.
        + Enter a **Key** and **Value**.

        To include an additional parameter, choose **Add parameter**.
   + **API Key**

     Enter the **API key name** and associated **Value** to use for API Key authorization.

1. Under **Invocation Http Parameters**, add any additional parameters to include in the authorization request. 

   To add a parameter:

   1. Select a **Parameter** from the drop-down list

   1. Enter a **Key** and **Value**

   To include an additional parameter, choose **Add parameter**.

1. Choose **Create Connection**.
**Note**  
For connections for private endpoints, EventBridge creates the necessary resource association when it create the connection. This can take up to 90 seconds.