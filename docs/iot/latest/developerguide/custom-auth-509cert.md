

# Custom authentication with X.509 client certificates
<a name="custom-auth-509cert"></a>

When connecting devices to AWS IoT Core, you have multiple [authentication types](protocols.md#connection-protocol-auth-mode) available. You can use [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) that can be used to authenticate client and device connections, or define [custom authorizers](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html) to manage your own client authentication and authorization logic. This topic covers how to use custom authentication with X.509 client certificates.

Using custom authentication with X.509 certificates can be helpful if you've already authenticated your devices using X.509 certificates and want to perform additional validation and custom authorization. For example, if you store your devices' data such as their serial numbers in the X.509 client certificate, after AWS IoT Core authenticated the X.509 client certificate, you can use a custom authorizer to identify specific devices based on the information stored in the certificate's CommonName field. Using custom authentication with X.509 certificates can enhance your device security management when connecting devices to AWS IoT Core and provides more flexibility to manage the authentication and authorization logic. AWS IoT Core supports custom authentication with X.509 certificates using the X.509 certificate and custom authorizer authentication type, which works with both the [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) protocol and the [HTTPS](https://docs.aws.amazon.com/iot/latest/developerguide/http.html) protocol. For more information about the authentication types and application protocols that AWS IoT Core device endpoints support, see [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).

**Note**  
Custom authentication with X.509 client certificates is not supported in the AWS GovCloud (US) Regions.

**Important**  
You must use an endpoint created using [domain configurations](iot-custom-endpoints-configurable.md). In addition, clients must provide the [Server Name Indication (SNI)](https://www.rfc-editor.org/rfc/rfc3546#section-3.1) extension when connecting to AWS IoT Core.

**Topics**
+ [Step 1: Register your X.509 client certificates with AWS IoT Core](#custom-auth-509cert-client)
+ [Step 2: Create a Lambda function](#custom-auth-509cert-lambda)
+ [Step 3: Create a custom authorizer](#custom-auth-509cert-authorizer)
+ [Step 4: Set authentication type and application protocol in a domain configuration](#custom-auth-509cert-domainconfig)

## Step 1: Register your X.509 client certificates with AWS IoT Core
<a name="custom-auth-509cert-client"></a>

If you haven't done this already, register and activate your [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) with AWS IoT Core. Otherwise, skip to the next step.

To register and activate your client certificates with AWS IoT Core, follow the steps:

1. If you [create client certificates directly with AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-create.html). These client certificates will be automatically registered with AWS IoT Core.

1. If you [create your own client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html), follow [these instructions to register them with AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/register-device-cert.html).

1. To activate your client certificates, follow [these instructions](https://docs.aws.amazon.com/iot/latest/developerguide/activate-or-deactivate-device-cert.html).

## Step 2: Create a Lambda function
<a name="custom-auth-509cert-lambda"></a>

AWS IoT Core uses custom authorizers to implement custom authentication and authorization schemes. A custom authorizer is associated with a Lambda function that determines whether a device is authenticated and what operations the device is allowed to perform. When a device connects to AWS IoT Core, AWS IoT Core retrieves the authorizer details including authorizer name and associated Lambda function, and invokes the Lambda function. The Lambda function receives an event that contains a JSON object with the device's X.509 client certificate data. Your Lambda function uses this event JSON object to evaluate the authentication request, decide the actions to take, and send a response back.

### Lambda function event example
<a name="custom-auth-509cert-event"></a>

The following example JSON object contains all possible fields that can be included. The actual JSON object will only contain fields relevant to the specific connection request.

```
{
	"token": "aToken",
	"signatureVerified": true,
	"protocols": [
		"tls",
		"mqtt"
	],
	"protocolData": {
		"tls": {
			"serverName": "serverName",
			"x509CertificatePem": "x509CertificatePem",
			"principalId": "principalId"
		},
		"mqtt": {
			"clientId": "myClientId",
                     "username": "myUserName",
                     "password": "myPassword"
		}
	},
	"connectionMetadata": {
		"id": "UUID"
	}
}
```

`signatureVerified`  
A Boolean value that indicates whether the token signature configured in the authorizer is verified or not before invoking the authorizer's Lambda function. If the authorizer is configured to disable token signing, this field will be false. 

`protocols`  
An array that contains the protocols to expect for the request.

`protocolData`  
An object that contains information of the protocols used in the connection. It provides protocol-specific details that can be useful for authentication, authorization, and more.  
`tls` - This object holds information related to the TLS (Transport Layer Security) protocol.   
+ `serverName` - The [Server Name Indication (SNI)](https://www.rfc-editor.org/rfc/rfc3546#section-3.1) hostname string. AWS IoT Core requires devices to send the [SNI extension](https://www.rfc-editor.org/rfc/rfc3546#section-3.1) to the Transport Layer Security (TLS) protocol and provide the complete endpoint address in the `host_name` field.
+ `x509CertificatePem` - The X.509 certificate in PEM format, which is used for client authentication in the TLS connection.
+ `principalId` - The principal identifier associated with the client in the TLS connection.
`mqtt` - This object holds information related to the MQTT protocol.  
+ `clientId` - A string only needs to be included in the event that the device sends this value.
+ `username` - The user name provided in the MQTT Connect packet.
+ `password` - The password provided in the MQTT Connect packet.

`connectionMetadata`  
Metadata of the connection.  
`id` - The connection ID, which you can use for logging and troubleshooting.

**Note**  
In this event JSON object, `x509CertificatePem` and `principalId` are two new fields in the request. The value of `principalId` is the same as the value of `certificateId`. For more information, see [Certificate](https://docs.aws.amazon.com/iot/latest/apireference/API_Certificate.html).

### Lambda function response example
<a name="custom-auth-509cert-response"></a>

The Lambda function should use information from the event JSON object to authenticate the incoming connection and decide what actions are permitted in the connection.

The following JSON object contains an example response that your Lambda function can send.

```
{
	"isAuthenticated": true,
	"principalId": "xxxxxxxx",
	"disconnectAfterInSeconds": 86400,
	"refreshAfterInSeconds": 300,
	"policyDocuments": [
		{
			"Version": "2012-10-17",		 	 	 
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "iot:Publish",
					"Resource": "arn:aws:iot:us-east-1:123456789012:topic/customauthtesting"
				}
			]
		}
	]
}
```

In this example, this function should send a response that contains the following values.

`isAuthenticated`  
A Boolean value that indicates whether the request is authenticated.

`principalId`  
An alphanumeric string that acts as an identifier for the token sent by the custom authorization request. The value must be an alphanumeric string with at least one, and no more than 128, characters. It identifies the connection in logs. The value of `principalId` must be the same as the value of `principalId` in the event JSON object (i.e. certificateId of the X.509 certificate).

`policyDocuments`  
A list of JSON-formatted AWS IoT Core policy documents. The value is optional and supports [thing policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/thing-policy-variables.html) and [certificate policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/cert-policy-variables.html). The maximum number of policy documents is 10. Each policy document can contain a maximum of 2,048 characters. If you have multiple policies attached to your client certificate and the Lambda function, the permission is a collection of all policies. For more information about creating AWS IoT Core policies, see [Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html).

`disconnectAfterInSeconds`  
An integer that specifies the maximum duration (in seconds) of the connection to the AWS IoT Core gateway. The minimum value is 300 seconds, and the maximum value is 86,400 seconds. `disconnectAfterInSeconds` is for the lifetime of a connection and doesn't get refreshed on consecutive policy refreshes.

`refreshAfterInSeconds`  
An integer that specifies the interval between policy refreshes. When this interval passes, AWS IoT Core invokes the Lambda function to allow for policy refreshes. The minimum value is 300 seconds, and the maximum value is 86,400 seconds.

### Example Lambda function
<a name="custom-auth-509cert-js-example"></a>

The following is a sample Node.js Lambda function. The function examines the client's X.509 certificate and extracts relevant information such as the serial number, fingerprint, and subject name. If the extracted information matches the expected values, the client is granted access to connect. This mechanism ensures that only authorized clients with valid certificates can establish a connection.

```
const crypto = require('crypto');

exports.handler = async (event) => {
    
    // Extract the certificate PEM from the event
    const certPem = event.protocolData.tls.x509CertificatePem;
    
    // Parse the certificate using Node's crypto module
    const cert = new crypto.X509Certificate(certPem);
    
    var effect = "Deny";
    // Allow permissions only for a particular certificate serial, fingerprint, and subject
    if (cert.serialNumber === "7F8D2E4B9C1A5036DE8F7C4B2A91E5D80463BC9A1257" // This is a random serial
       && cert.fingerprint === "F2:9A:C4:1D:B5:E7:08:3F:6B:D0:4E:92:A7:C1:5B:8D:16:0F:E3:7A" // This is a random fingerprint
       && cert.subject === "allow.example.com") {
      effect = "Allow";
    }
    
    return generateAuthResponse(event.protocolData.tls.principalId, effect);
};


// Helper function to generate the authorization response.
function generateAuthResponse(principalId, effect) {
    const authResponse = {
        isAuthenticated: true,
        principalId,
        disconnectAfterInSeconds: 3600,
        refreshAfterInSeconds: 300,
        policyDocuments: [
          {
            Version: "2012-10-17",		 	 	 
            Statement: [
              {
                Action: ["iot:Connect"],
                Effect: effect,
                Resource: [
                  "arn:aws:iot:{{us-east-1}}:{{123456789012}}:client/{{myClientName}}"
                ]
              },
              {
                Action: ["iot:Publish"],
                Effect: effect,
                Resource: [
                  "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topic/{{telemetry/myClientName}}"
                ]
              },
              {
                Action: ["iot:Subscribe"],
                Effect: effect,
                Resource: [
                   "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topicfilter/{{telemetry/myClientName}}"
                ]
              },
              {
                Action: ["iot:Receive"],
                Effect: effect,
                Resource: [
                   "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topic/{{telemetry/myClientName}}"
                ]
              }
            ]
          }
        ]
      };

  return authResponse;
}
```

The preceding Lambda function returns the following JSON when it receives a certificate with the expected serial, fingerprint, and subject. The value of `x509CertificatePem` will be the client certificate provided in the TLS handshake. For more information, see [Defining your Lambda function](https://docs.aws.amazon.com/iot/latest/developerguide/config-custom-auth.html#custom-auth-lambda).

```
{
	"isAuthenticated": true,
	"principalId": "principalId in the event JSON object",
	"policyDocuments": [
		{
			"Version": "2012-10-17",		 	 	 
			"Statement": [
				{
					"Action": "iot:Connect",
					"Effect": "Allow",
					"Resource": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:client/{{myClientName}}"
				},
				{
					"Action": "iot:Publish",
					"Effect": "Allow",
					"Resource": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topic/{{telemetry/myClientName}}"
				},
				{
					"Action": "iot:Subscribe",
					"Effect": "Allow",
					"Resource": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topicfilter/{{telemetry/myClientName}}"
				},
				{
					"Action": "iot:Receive",
					"Effect": "Allow",
					"Resource": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:topic/{{telemetry/myClientName}}"
				}
			]
		}
	],
	"disconnectAfterInSeconds": 3600,
	"refreshAfterInSeconds": 300
}
```

## Step 3: Create a custom authorizer
<a name="custom-auth-509cert-authorizer"></a>

After [you define the Lambda function](#custom-auth-509cert-lambda), create a custom authorizer to manage your own client authentication and authorization logic. You can follow the detailed instructions in [Step 3: Create a customer authorizer resource and its authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-tutorial.html#custom-auth-tutorial-authorizer). For more information, see [Creating an authorizer](https://docs.aws.amazon.com/iot/latest/developerguide/config-custom-auth.html). 

In the process of creating the custom authorizer, you must grant AWS IoT permission to invoke the Lambda function after it's created. For detailed instructions, see [Authorizing AWS IoT to invoke your Lambda function](custom-auth-authorize.md).

## Step 4: Set authentication type and application protocol in a domain configuration
<a name="custom-auth-509cert-domainconfig"></a>

To authenticate devices using custom authentication with X.509 client certificates, you must set the authentication type and application protocol in a domain configuration, and you must send the SNI extension. The value of `authenticationType` must be `CUSTOM_AUTH_X509`, and the value of `applicationProtocol` can either be `SECURE_MQTT` or `HTTPS`.

### Set authentication type and application protocol in domain configuration (CLI)
<a name="custom-auth-509cert-cli"></a>

If you don't have a domain configuration, use the [**create-domain-configuration**](https://docs.aws.amazon.com/cli/latest/reference/iot/create-domain-configuration.html) command to create one. The value of `authenticationType` must be `CUSTOM_AUTH_X509`, and the value of `applicationProtocol` can either be `SECURE_MQTT` or `HTTPS`.

```
aws iot create-domain-configuration \
    --domain-configuration-name {{domainConfigurationName}} \
    --authentication-type {{CUSTOM_AUTH_X509}} \  
    --application-protocol {{SECURE_MQTT}} \ 
    --authorizer-config '{
        "defaultAuthorizerName": {{my-custom-authorizer}}
    }'
```

If you already have a domain configuration, use the [**update-domain-configuration**](https://docs.aws.amazon.com/cli/latest/reference/iot/update-domain-configuration.html) command update `authenticationType` and `applicationProtocol` if needed. Note that you can't change the authentication type or protocol on the default endpoint (`iot:Data-ATS`).

```
aws iot update-domain-configuration \
    --domain-configuration-name {{domainConfigurationName}} \
    --authentication-type {{CUSTOM_AUTH_X509}} \  
    --application-protocol {{SECURE_MQTT}} \
    --authorizer-config '{
        "defaultAuthorizerName": {{my-custom-authorizer}}
    }'
```

`domain-configuration-name`  
The name of the domain configuration.

`authentication-type`  
The authentication type of the domain configuration. For more information, see [choosing an authentication type](protocols.md#connection-protocol-auth-mode).

`application-protocol`  
The application protocol which devices use to communicate with AWS IoT Core. For more information, see [choosing an application protocol](protocols.md#protocol-selection).

`--authorizer-config`  
An object that specifies the authorizer configuration in a domain configuration.

`defaultAuthorizerName`  
The name of the authorizer for a domain configuration.

For more information, see [CreateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html) and [UpdateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html) from the *AWS IoT API Reference*. For more information about domain configuration, see [Domain configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html).