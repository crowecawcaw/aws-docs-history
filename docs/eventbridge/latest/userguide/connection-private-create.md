# Creating connections to private APIs

The following steps walk you through how to create a connection to a private API. For detailed instructions that include all configuration options for connections, including creating connections to public APIs, see
[Creating
connections](eb-target-connection-create.md "eb-target-connection-create.md").

## Define the connection

The following steps walk you through how to create a connection to a private API endpoint. For instructions on creating connections to public APIs, see [Creating
connections](eb-target-connection-create.md "eb-target-connection-create.md").

1. Open the [EventBridge
   console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the left navigation pane, under **Integration**, choose **Connections**.
3. Choose **Create connection**.
4. On the **Create connection** page, enter a
   **Connection name** and **Description**.

## Configure the invocation

endpoint

Next, use the **Configure invocation** section to specify the
HTTPS endpoint you want the connection to invoke.

1. For **API type**, choose
   **Private**.
2. Specify the Amazon VPC Lattice resource configuration to use to connect to it.

Under **Private API**:

    * To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
    * To create a new VPC Lattice resource configuration, choose **New resource
     configuration**.


    You are taken to the Amazon VPC Lattice; service console, where you can create a new configuration. for more information, see
     [Create a resource configuration](../../../vpc-lattice/latest/ug/create-resource-configuration.md "../../../vpc-lattice/latest/ug/create-resource-configuration.md") in the *Amazon VPC Lattice User Guide*.

## Configure the endpoint

authorization

Lastly, specify the authorization settings to use to access the endpoint.

EventBridge supports basic, OAuth client credentials, and API key authentication methods.

1.  Under **Configure authorization**, choose **Custom
    configuration**.
2.  For **Authorization type**, select the authorization method for the
    connection to use.
3.  Specify the authorization configuration details for the authorization method you chose:
    - **Basic**

    Enter the **Username**
    and **Password** to use to
    authorize with the HTTPS endpoint.
    - **OAuth Client Credentials**
      1. For **OAuth authorization endpoint**,
         choose whether the endpoint to use for connection authorization is
         a public or private (VPC) endpoint.

      If you choose **Private**,
      specify the **Private OAuth endpoint resource
      configuration**:

          + To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
          + To create a new VPC Lattice resource configuration, choose **New resource
           configuration**.


          You are taken to the Amazon VPC Lattice service console, where you can create a new configuration. for more information, see
           [Create a resource configuration](../../../vpc-lattice/latest/ug/create-resource-configuration.md "../../../vpc-lattice/latest/ug/create-resource-configuration.md") in the *Amazon VPC Lattice User Guide*.

      2. Specify the following authorization information:
         - Authorization endpoint
         - HTTPS method
         - Client ID
         - Client secret

      3. Under **OAuth HTTP parameters**, add any additional
         parameters to include for authorization with the authorization endpoint.

      To do so:

          + Select a **Parameter** from the drop-down list.
          + Enter
           a **Key** and **Value**.

      To include an
      additional parameter, choose **Add parameter**.

    - **API Key**

    Enter the **API key
    name** and associated **Value** to use for API
    Key authorization.

4.  Under **Invocation Http Parameters**, add any additional
    parameters to include in the authorization request.

To add a parameter:

    1. Select a **Parameter** from the drop-down list
    2. Enter a **Key** and **Value**

To include an
additional parameter, choose **Add parameter**. 5. Choose **Create Connection**.

###### Note

For connections for private endpoints, EventBridge creates the necessary resource association when it create the connection. This can take up to 90
seconds.
