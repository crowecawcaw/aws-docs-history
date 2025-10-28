# Creating connections for API targets in

EventBridge

The following steps walk you through how to create a connection to an HTTPS endpoint.

###### Steps

- [Define the connection](#eb-target-connection-create-define "#eb-target-connection-create-define")
- [Configure the invocation
  endpoint](#eb-target-connection-create-invocation "#eb-target-connection-create-invocation")
- [Configure the endpoint
  authorization](#eb-target-connection-create-auth "#eb-target-connection-create-auth")
- [Configure encryption](#eb-target-connection-create-cmkms "#eb-target-connection-create-cmkms")

## Define the connection

1. Open the [EventBridge
   console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events").
2. In the left navigation pane, under **Integration**, choose **Connections**.
3. Choose **Create connection**.
4. On the **Create connection** page, enter a
   **Connection name** and **Description**.

## Configure the invocation

endpoint

Next, use the **Configure invocation** section to specify the API
type you want the connection to invoke. EventBridge connections support public and private
APIs.

- For **API type**, choose whether the endpoint is a public
  or private API.

If you choose a private API, specify the VPC Lattice resource configuration to use to
connect to it.

Under **Private API**:

    + To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
    + To create a new VPC Lattice resource configuration, choose **New Resource configuration**.


    You are taken to the Amazon VPC Lattice service console, where you can create a new configuration. for more information, see
     [Create a resource configuration](../../../vpc-lattice/latest/ug/create-resource-configuration.md "../../../vpc-lattice/latest/ug/create-resource-configuration.md") in the *Amazon VPC Lattice User Guide*.

## Configure the endpoint

authorization

Next, specify the authorization settings to use to access the endpoint.

EventBridge supports basic, OAuth client credentials, and API key authentication methods.

1. For **Configure authorization**, choose the type of endpoint to which you
   want to connect.

Custom endpoint
If the connection is to an endpoint other than a partner endpoint, choose **Custom
configuration**.

    1. For **Authorization type**, select the authorization method for the
     connection to use.
    2. Specify the authorization configuration details for the authorization method you chose:


    	* **Basic**


    	Enter the **Username**
    	 and **Password** to use to
    	 authorize with the HTTPS endpoint.
    	* **OAuth Client Credentials**


    		1. For **OAuth authorization
    		 endpoint**, choose whether the endpoint
    		 to use for connection authorization is a public or
    		 private endpoint.


    		If you choose
    		 **Private**, specify the
    		 **Private OAuth endpoint resource
    		 configuration**:




    			+ To use an existing resource configuration, choose a resource configuration from the drop-down menu.
    			+ To create a new resource configuration, choose **New resource
    			 configuration**.


    			You are taken to the Amazon VPC Lattice; service console, where you can create a new configuration. for more information, see
    			 [Create a resource configuration](../../../vpc-lattice/latest/ug/create-resource-configuration.md "../../../vpc-lattice/latest/ug/create-resource-configuration.md") in the *Amazon VPC Lattice User Guide*.
    		2. Specify the following authorization information:




    			+ Authorization endpoint
    			+ HTTP method
    			+ Client ID
    			+ Client secret
    		3. Under **OAuth HTTP parameters**, add any additional
    		 parameters to include for authorization with the authorization endpoint.


    		To do so:




    			+ Select a **Parameter** from the drop-down list.
    			+ Enter
    			 a **Key** and **Value**.
    		To include an
    		 additional parameter, choose **Add parameter**.
    	* **API Key**


    	Enter the **API key
    	 name** and associated **Value** to use for API
    	 Key authorization.

Partner endpoint
If the connection is to a partner endpoint, choose
**Use partner template**. For a list of
available partner endpoints, see [API destination partners](eb-api-destination-partners.md "eb-api-destination-partners.md").

    1. From **Partner destination**, select the partner to which to connect.


    Under **Authorization type**,
     EventBridge enables the authorization methods available for the
     partner.
    2. For **Authorization type**, select the authorization method for the
     connection to use.
    3. Specify the authorization configuration details for the authorization method you chose:


    	* **Basic**


    	Enter the
    	 **Username** and **Password** to use
    	 to authorize with the HTTP endpoint.
    	* **OAuth Client Credentials**


    		1. For **OAuth authorization endpoint**,
    		 choose whether the endpoint to use for connection authorization is
    		 a public or private (VPC) endpoint.


    		If you choose
    		 **Private**, specify the
    		 **Private OAuth endpoint resource
    		 configuration**:




    			+ To use an existing VPC Lattice resource configuration, choose a resource configuration from the drop-down menu.
    			+ To create a new VPC Lattice resource configuration, choose **New resource
    			 configuration**.


    			You are taken to the Amazon VPC Lattice service console, where you can create a new configuration. for more information, see
    			 [Create a resource configuration](../../../vpc-lattice/latest/ug/create-resource-configuration.md "../../../vpc-lattice/latest/ug/create-resource-configuration.md") in the *Amazon VPC Lattice User Guide*.
    		2. Specify the following authorization information:




    			+ Authorization endpoint
    			+ HTTPS method
    			+ Client ID
    			+ Client secret
    		3. Under **OAuth HTTP parameters**, add any additional
    		 parameters to include for authorization with the authorization endpoint.


    		To do so:




    			+ Select a **Parameter** from the drop-down list.
    			+ Enter
    			 a **Key** and **Value**.
    		To include an
    		 additional parameter, choose **Add parameter**.
    	* **API Key**


    	Enter the **API key
    	 name** and associated **Value** to use for API
    	 Key authorization.

2. Under **Invocation Http Parameters**, add any additional
   parameters to include in the authorization request.

To add a parameter:

    1. Select a **Parameter** from the drop-down list
    2. Enter a **Key** and **Value**

To include an
additional parameter, choose **Add parameter**.

## Configure encryption

Lastly, specify the type of KMS key you want EventBridge to use when encrypting and decrypting the authorization parameters that it stores as a secret in AWS Secrets Manager..
By default, EventBridge uses an AWS owned key.

For more information, see [Encrypting
connections](encryption-connections.md "encryption-connections.md").

1.  Choose the KMS key for EventBridge to use when encrypting
    the connection secret.
    - Choose **Use AWS owned key** for EventBridge to encrypt the secret using an AWS owned key.

    This AWS owned key is a KMS key that EventBridge owns and manages for use in multiple AWS
    accounts. In general, unless you are required to audit or control the
    encryption key that protects your resources, an AWS owned key
    is a good choice.

    This is the default.
    - Choose **Use customer managed key** for EventBridge to encrypt the secret using the customer managed key that you
      specify or create.

    Customer managed keys are KMS keys in your AWS account that you create, own, and manage. You have full
    control over these KMS keys.

        1. Specify an existing customer managed key, or choose
         **Create a new KMS key**.


        EventBridge displays the key status and any key aliases that
         have been associated with the specified customer managed key.

2.  Choose **Create Connection**.

###### Note

For connections for private endpoints, EventBridge creates the necessary resource association when it create the connection. This can take up to 90
seconds.
