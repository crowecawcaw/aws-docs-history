# Create an AWS Direct Connect dedicated connection using the Connection wizard

This section describes creating a connection using the Connection wizard. If you prefer to
create a Classic connection, see the steps at [Step 2: Request an AWS Direct Connect dedicated connection](toolkit-classic.md#ConnectionRequest "toolkit-classic.md#ConnectionRequest").

###### To create a Connection wizard connection

1.  Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose
    **Connections**, and then choose
    **Create connection**.
3.  On the **Create Connection** page, under
    **Connection ordering type**, choose
    **Connection wizard**.
4.  Choose a **Resiliency Level** for your
    network connections. A resiliency level can be one of the
    following:

        * **Maximum Resiliency**
        * **High Resiliency**
        * **Development and Test**

    For descriptions and more detailed information about these
    resiliency levels, see [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md").

5.  Choose **Next**.
6.  On the **Configure connections** page,
    provide the following details.
    1. From the **Bandwidth** drop-down list, choose the bandwidth
       required for the connection. This can be anywhere from
       **1Gbps** to **400
       Gbps**.
    2. For **Location**, choose the
       appropriate AWS Direct Connect location, and then choose the
       **First location service
       provider**, select the service provider
       providing connectivity for the connection at this
       location.
    3. For **Second location**, choose the
       appropriate AWS Direct Connect at the second location, and then
       choose the **Second location service
       provider**, select the service provider
       providing connectivity for the connection at this second
       location.
    4. (Optional) Configure MAC security (MACsec) for the
       connection. Under **Additional
       Settings**, select **Request a
       MACsec capable port**.

    MACsec is only available on dedicated
    connections. 5. (Optional) Choose **Add tag** to add
    key/value pairs to further help identify this
    connection.

        * For **Key**, enter the key
         name.
        * For **Value**, enter the key
         value.

    To remove an existing tag, choose the tag and then choose **Remove
    tag**. You can't have empty tags.

7.  Choose **Next**.
8.  On the **Review and create page**, verify the
    connection. This page also displays estimated costs for port
    usage and additional data transfer charges.
9.  Choose **Create**.
10. Download your Letter of Authorization and Connecting Facility
    Assignment (LOA-CFA), For more information, see [Letter of Authorization and Connecting Facility
    Assignment (LOA-CFA)](dedicated_connection.md#create-connection-loa-cfa "dedicated_connection.md#create-connection-loa-cfa").
    Use one of the following commands.

- [create-connection](../../../cli/latest/reference/directconnect/create-connection.md "../../../cli/latest/reference/directconnect/create-connection.md") (AWS CLI)
- [CreateConnection](../APIReference/API_CreateConnection.md "../APIReference/API_CreateConnection.md") (AWS Direct Connect API)
