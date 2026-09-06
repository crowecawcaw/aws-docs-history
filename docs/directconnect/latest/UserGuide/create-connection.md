

# Create a Direct Connect dedicated connection using the Connection wizard
<a name="create-connection"></a>

This section describes creating a connection using the Connection wizard. If you prefer to create a Classic connection, see the steps at [Step 2: Request a Direct Connect dedicated connection](toolkit-classic.md#ConnectionRequest).

**To create a Connection wizard connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**, and then choose **Create connection**.

1. On the **Create Connection** page, under **Connection ordering type**, choose **Connection wizard**.

1. Choose a **Resiliency Level** for your network connections. A resiliency level can be one of the following:
   + **Maximum Resiliency**
   + **High Resiliency**
   + **Development and Test**

   For descriptions and more detailed information about these resiliency levels, see [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md).

1. Choose **Next**.

1. On the **Configure connections** page, provide the following details.

   1. From the **Bandwidth** drop-down list, choose the bandwidth required for the connection. This can be anywhere from **1Gbps** to **400 Gbps**.

   1. For **Location**, choose the appropriate Direct Connect location, and then choose the **First location service provider**, select the service provider providing connectivity for the connection at this location.

   1. For **Second location**, choose the appropriate Direct Connect at the second location, and then choose the **Second location service provider**, select the service provider providing connectivity for the connection at this second location.

   1. (Optional) Configure MAC security (MACsec) for the connection. Under **Additional Settings**, select **Request a MACsec capable port**.

      MACsec is only available on dedicated connections.

   1. (Optional) Choose **Add tag** to add key/value pairs to further help identify this connection.
      + For **Key**, enter the key name.
      + For **Value**, enter the key value.

      To remove an existing tag, choose the tag and then choose **Remove tag**. You can't have empty tags.

1. Choose **Next**.

1. On the **Review and create page**, verify the connection. This page also displays estimated costs for port usage and additional data transfer charges. 

1. Choose **Create**.

1. Download your Letter of Authorization and Connecting Facility Assignment (LOA-CFA), For more information, see [Letter of Authorization and Connecting Facility Assignment (LOA-CFA)](dedicated_connection.md#create-connection-loa-cfa).

Use one of the following commands.
+ [create-connection](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-connection.html) (AWS CLI)
+ [CreateConnection](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateConnection.html) (Direct Connect API)