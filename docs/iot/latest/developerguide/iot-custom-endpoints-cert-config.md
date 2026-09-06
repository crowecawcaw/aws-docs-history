

# Server certificate configuration for OCSP stapling
<a name="iot-custom-endpoints-cert-config"></a>

AWS IoT Core supports [Online Certificate Status Protocol (OCSP)](https://www.rfc-editor.org/rfc/rfc6960.html) stapling for server certificate, also known as server certificate OCSP stapling, or OCSP stapling. It is a security mechanism used to check the revocation status on the server certificate in a Transport Layer Security (TLS) handshake. OCSP stapling in AWS IoT Core lets you add an additional layer of verification to your custom domain's server certificate validity.

You can enable server certificate OCSP stapling in AWS IoT Core to check the validity of the certificate by querying the OCSP responder periodically. The OCSP stapling setting is part of the process to create or update a domain configuration with a custom domain. OCSP stapling checks for revocation status on the server certificate continuously. This helps verify that any certificates that have been revoked by the CA are no longer trusted by the clients connecting to your custom domains. For more information, see [Enabling server certificate OCSP in AWS IoT Core](#iot-custom-endpoints-cert-config-ocsp-manage).

Server certificate OCSP stapling provides real-time revocation status check, reduces the latency associated with checking the revocation status, and improves privacy and reliability of secure connections. For more information about the benefits of using OCSP stapling, see [Benefits of using OCSP stapling compared to client-side OCSP checks](#iot-custom-endpoints-ocsp-stapling-benefits).

**Note**  
This feature is not available in AWS GovCloud (US) Regions.

**Topics**
+ [What is OCSP?](#iot-custom-endpoints-cert-config-ocsp-what-is)
+ [How OCSP stapling works](#iot-custom-endpoints-cert-config-ocsp-stapling-what-is)
+ [Enabling server certificate OCSP in AWS IoT Core](#iot-custom-endpoints-cert-config-ocsp-manage)
+ [Configuring server certificate OCSP for private endpoints in AWS IoT Core](#iot-custom-endpoints-cert-config-ocsp-private-endpoint)
+ [Important notes for using server certificate OCSP stapling in AWS IoT Core](#iot-custom-endpoints-cert-config-ocsp-notes)
+ [Troubleshooting server certificate OCSP stapling in AWS IoT Core](#iot-custom-endpoints-cert-config-ocsp-troubleshooting)

## What is OCSP?
<a name="iot-custom-endpoints-cert-config-ocsp-what-is"></a>

The Online Certificate Status Protocol (OCSP) aids in providing a server certificate's revocation status for a Transport Layer Security (TLS) handshake.

### Key concepts
<a name="iot-custom-endpoints-cert-config-ocsp-concepts"></a>

The following key concepts provide details about the Online Certificate Status Protocol (OCSP).

**OCSP**

[OCSP](https://www.rfc-editor.org/rfc/rfc6960.html) is used to check the certificate revocation status during the Transport Layer Security (TLS) handshake. OCSP allows for real-time validation of certificates. This confirms that the certificate hasn't been revoked or expired since it was issued. OCSP is also more scalable compared with traditional Certificate Revocation Lists (CRLs). OCSP responses are smaller and can be efficiently generated, making them more suitable for large-scale Private Key Infrastructures (PKIs).

**OCSP responder**

An OCSP responder (also known as OCSP server) receives and responds to OCSP requests from clients that seek to verify the revocation status of certificates.

**Client-side OCSP**

 In client-side OCSP, the client uses OCSP to contact an OCSP responder to check the certificate's revocation status during the TLS handshake.

**Server-side OCSP**

In server-side OCSP (also known as OCSP stapling), the server is enabled (rather than the client) to make the request to the OCSP responder. The server staples the OCSP response to the certificate and returns it to the client during the TLS handshake.

### OCSP diagrams
<a name="iot-custom-endpoints-cert-config-ocsp-diagram"></a>

The following diagram illustrates how client-side OCSP and server-side OCSP work.

![Client-side OCSP and server-side OCSP diagrams](http://docs.aws.amazon.com/iot/latest/developerguide/images/custom-domain-ocsp-uml.png)


**Client-side OCSP**

1. The client sends a `ClientHello` message to initiate the TLS handshake with the server.

1. The server receives the message and responds with a `ServerHello` message. The server also sends the server certificate to the client.

1. The client validates the server certificate and extracts an OCSP URI from it.

1. The client sends a certificate revocation check request to the OCSP responder.

1. The OCSP responder sends an OCSP response.

1. The client validates the certificate status from the OCSP response.

1. The TLS handshake is completed.

**Server-side OCSP**

1. The client sends a `ClientHello` message to initiate the TLS handshake with the server.

1. The server receives the message and gets the latest cached OCSP response. If the cached response is missing or expired, the server will call the OCSP responder for certificate status.

1. The OCSP responder sends an OCSP response to the server.

1. The server sends a `ServerHello` message. The server also sends the server certificate and the certificate status to the client.

1. The client validates the OCSP certificate status.

1. The TLS handshake is completed.

## How OCSP stapling works
<a name="iot-custom-endpoints-cert-config-ocsp-stapling-what-is"></a>

OCSP stapling is used during the TLS handshake between the client and the server to check the server certificate revocation status. The server makes the OCSP request to the OCSP responder and staples the OCSP responses to the certificates returned to the client. By having the server make the request to the OCSP responder, the responses can be cached and then used multiple times for many clients.

### How OCSP stapling works in AWS IoT Core
<a name="iot-custom-endpoints-ocsp-stapling-iot-core"></a>

The following diagram shows how server-side OCSP stapling works in AWS IoT Core.

![This diagram shows how server-side OCSP stapling works in AWS IoT Core.](http://docs.aws.amazon.com/iot/latest/developerguide/images/custom-domain-ocsp-core-uml.png)


1. The device needs to be registered with custom domains with OCSP stapling enabled.

1. AWS IoT Core calls OCSP responder every hour to get the certificate status.

1. The OCSP responder receives the request, sends the latest OCSP response, and stores the cached OCSP response. 

1. The device sends a `ClientHello` message to initiate the TLS handshake with AWS IoT Core.

1. AWS IoT Core gets the latest OCSP response from the server cache, which responds with an OCSP response of the certificate.

1. The server sends a `ServerHello` message to the device. The server also sends the server certificate and the certificate status to the client.

1. The device validates the OCSP certificate status.

1. The TLS handshake is completed.

### Benefits of using OCSP stapling compared to client-side OCSP checks
<a name="iot-custom-endpoints-ocsp-stapling-benefits"></a>

A few advantages of using server certificate OCSP stapling include the following:

**Improved privacy**

Without OCSP stapling, the client's device can expose information to third-party OCSP responders, potentially compromising user privacy. OCSP stapling mitigates this issue by having the server obtain the OCSP response and deliver it directly to the client.

**Improved reliability**

OCSP stapling can improve the reliability of secure connections because it reduces the risk of OCSP server outages. When OCSP responses are stapled, the server includes the most recent response with the certificate. This is so that clients have access to the revocation status even if the OCSP responder is temporarily unavailable. OCSP stapling helps mitigate these problems because the server fetches OCSP responses periodically and includes the cached responses in the TLS handshake. This reduces reliance on the real-time availability of OCSP responders.

**Reduced server load**

OCSP stapling offloads the burden of responding to OCSP requests from OCSP responders to the server. This can help distribute the load more evenly, making the certificate validation process more efficient and scalable.

**Reduced latency**

OCSP stapling reduces the latency associated with checking the revocation status of a certificate during the TLS handshake. Instead of the client having to query an OCSP server separately, the server sends the request and attaches the OCSP response with the server certificate during the handshake.

## Enabling server certificate OCSP in AWS IoT Core
<a name="iot-custom-endpoints-cert-config-ocsp-manage"></a>

To enable server certificate OCSP stapling in AWS IoT Core, create a domain configuration for a custom domain or update an existing custom domain configuration. For general information about creating a domain configuration with a custom domain, see [Creating and configuring customer managed domains](iot-custom-endpoints-configurable-custom.md).

Use the following instructions to enable OCSP server stapling using AWS Management Console or AWS CLI.

### Console
<a name="iot-custom-endpoints-cert-config-ocsp-manage-console"></a>

**To enable server certificate OCSP stapling using the AWS IoT console:**

1. In the navigation menu, choose **Settings**, and then choose **Create domain configuration**, or choose an existing domain configuration for a custom domain.

1. If you choose to create a new domain configuration in the previous step, you will see the **Create domain configuration** page. In the **Domain configuration properties** section, choose **Custom domain**. Enter the information to create a domain configuration.

   If you choose to update an existing domain configuration for a custom domain, you will see the **Domain configuration details** page. Choose **Edit**.

1. To enable OCSP server stapling, choose **Enable server certificate OCSP stapling** in the **Server certificate configurations** subsection.

1. Choose **Create domain configuration** or **Update domain configuration**.

### AWS CLI
<a name="iot-custom-endpoints-cert-config-ocsp-manage-cli"></a>

**To enable server certificate OCSP stapling using AWS CLI:**

1. If you create a new domain configuration for a custom domain, the command to enable the OCSP server stapling can look like the following:

   ```
   aws iot create-domain-configuration --domain-configuration-name "myDomainConfigurationName" \
           --server-certificate-arns arn:aws:iot:{{us-east-1:123456789012}}:cert/{{f8c1e5480266caef0fdb1bf97dc1c82d7ba2d3e2642c5f25f5ba364fc6b79ba3}} \
           --server-certificate-config "enableOCSPCheck=true|false"
   ```

1. If you update an existing domain configuration for a custom domain, the command to enable the OCSP server stapling can look like the following:

   ```
   aws iot update-domain-configuration --domain-configuration-name "myDomainConfigurationName" \
           --server-certificate-arns arn:aws:iot:{{us-east-1:123456789012}}:cert/{{f8c1e5480266caef0fdb1bf97dc1c82d7ba2d3e2642c5f25f5ba364fc6b79ba3}} \
           --server-certificate-config "enableOCSPCheck=true|false"
   ```

For more information, see [CreateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html) and [UpdateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html) from the AWS IoT API Reference.

## Configuring server certificate OCSP for private endpoints in AWS IoT Core
<a name="iot-custom-endpoints-cert-config-ocsp-private-endpoint"></a>

OCSP for private endpoints lets you use your private OCSP resources within your Amazon Virtual Private Cloud (Amazon VPC) for AWS IoT Core operations. The process involves setting up a Lambda function that acts as an OCSP responder. The Lambda function might use your private OCSP resources to craft OCSP responses that AWS IoT Core will use.

### Lambda function
<a name="iot-custom-endpoints-cert-config-ocsp-private-endpoint-lambda"></a>

Before you configure server OCSP for a private endpoint, create a Lambda function that acts as a Request for Comments (RFC) 6960-compliant Online Certificate Status Protocol (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request in the Distinguished Encoding Rules (DER) format. The Lambda function's response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same AWS account and AWS Region as the domain configuration. The following are example Lambda functions.

#### Example Lambda functions
<a name="ocsp-lambda-example"></a>

------
#### [ JavaScript ]

```
import * as pkijs from 'pkijs';
console.log('Loading function');
 
export const handler = async (event, context) => {
    const requestBytes = decodeBase64(event);
    const ocspRequest = pkijs.OCSPRequest.fromBER(requestBytes);
 
    console.log("Here is a better look at the OCSP request");
    console.log(ocspRequest.toJSON());
 
    const ocspResponse = getOcspResponse();
    
    console.log("Here is a better look at the OCSP response");
    console.log(ocspResponse.toJSON());
 
   const responseBytes = ocspResponse.toSchema().toBER();
   return encodeBase64(responseBytes);
};
 
function getOcspResponse() {
    const responseString = "MIIC/woBAKCCAvgwggL0BgkrBgEFBQcwAQEEggLlMIIC4TCByqFkMGIxJzAlBgNVBAoMHlJpY2hhcmQncyBEaXNjb3VudCBMYW1iZGEgT0NTUDEZMBcGA1UEAwwQcm91bmRhYm91dE5hdGlvbjEPMA0GA1UEBwwGQ2FybWVsMQswCQYDVQQGEwJJThgPMjAyNDA0MjMxODUzMjVaMFEwTzA6MAkGBSsOAwIaBQAEFD2L7Ol/6ieNMaJbwRbxFWFweXGPBBSzSThwzTc3/p5w7WOtPjp3otNtVgIBAYAAGA8yMDI0MDQyMzE4NTMyNVowDQYJKoZIhvcNAQELBQADggIBAJFRyjDAHfazNejo704Ra3FOsGq/+s82R1spDarr3k7Pzkod9jJhwsZ2YgushlS4Npfe4lHCdwFyZR75WXrW55aXFddy03KLz01ZLNYyxkleW3f5dgrUcRU3PMW9TU2gZ0VOV8L5pmxKBoBRFt6EKtyh4CbiuqkTpLdLIMZmTyanhl5GVyU5MBHdbH8YWZoT/DEBiyS7ZsyhKo6igWU/SY7YMSKgwBvFsqSDcOa/hRYQkxWKWJ19gcz8CIkWN7NvfIxCs6VrAdzEJwmE7y3v+jdfhxW9JmI4xStE4K0tAR9vVOOfKs7NvxXj7oc9pCSG60xl96kaEE6PaY1YsfNTsKQ7pyCJ0s7/2q+ieZ4AtNyzw1XBadPzPJNv6E0LvI24yQZqN5wACvtut5prMMRxAHbOy+abLZR58wloFSELtGJ7UD96LFv1GgtC5s+2QlzPc4bEEof7Lo1EISt3j2ibNch8LxhqTQ4ufrbhsMkpSOTFYEJVMJF6aKj/OGXBUUqgc0Jx6jjJXNQd+l5KCY9pQFeb/wVUYC6mYqZOkNNMMJxPbHHbFnqb68yO+g5BE9011N44YXoPVJYoXxBLFX+OpRu9cqPkT9/vlkKd+SYXQknwZ81agKzhf1HsBKabtJwNVMlBKaI8g5UGa7Bxi6ewH3ezdWiERRUK7F56OM53wto/";
    const responseBytes = decodeBase64(responseString);
    return pkijs.OCSPResponse.fromBER(responseBytes);
}
 
function decodeBase64(input) {
    const binaryString = atob(input);
 
    const byteArray = new Uint8Array(binaryString.length);
    for (var i = 0; i < binaryString.length; i++) {
        byteArray[i] = binaryString.charCodeAt(i);
    }
 
    return byteArray.buffer;
}
 
function encodeBase64(buffer) {
    var binary = '';
    const bytes = new Uint8Array( buffer );
    const len = bytes.byteLength;
 
    for (var i = 0; i < len; i++) {
        binary += String.fromCharCode( bytes[ i ] );
    }
 
    return btoa(binary);
}
```

------
#### [ Java ]

```
package com.example.ocsp.responder;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import org.bouncycastle.cert.ocsp.OCSPReq;
import org.bouncycastle.cert.ocsp.OCSPResp;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Base64;
 
public class LambdaResponderApplication implements RequestHandler<String, String> {
    @Override
    public String handleRequest(final String input, final Context context) {
        LambdaLogger logger = context.getLogger();
        
        byte[] decodedInput = Base64.getDecoder().decode(input);
 
        OCSPReq req;
        try {
            req = new OCSPReq(decodedInput);
        } catch (IOException e) {
            logger.log("Got an IOException creating the OCSP request: " + e.getMessage());
            throw new RuntimeException(e);
        }
 
        try {
            OCSPResp response = businessLogic.getMyResponse();
            String toReturn = Base64.getEncoder().encodeToString(response.getEncoded());
            return toReturn;
        } catch (Exception e) {
            logger.log("Got an exception creating the response: " + e.getMessage());
            return "";
        }
    }
}
```

------

#### Authorizing AWS IoT to invoke your Lambda function
<a name="grant-permission-ocsp-lambda"></a>

In the process of creating the domain configuration with a Lambda OCSP responder, you must grant AWS IoT permission to invoke the Lambda function after the function is created. To grant the permission, you can use the [add-permission](https://docs.aws.amazon.com/cli/latest/reference/lambda/add-permission.html) CLI command.

**Grant permission to your Lambda function using the AWS CLI**

1. After inserting your values, enter the following command. Note that the `statement-id` value must be unique. Replace `{{Id-1234}}` with the exact value you have, otherwise, you might get a `ResourceConflictException` error.

   ```
   aws lambda add-permission  \
   --function-name "ocsp-function" \
   --principal "iot.amazonaws.com" \
   --action "lambda:InvokeFunction" \
   --statement-id "{{Id-1234}}" \
   --source-arn {{arn:aws:iot:us-east-1:123456789012}}:domainconfiguration/{{<domain-config-name>/*}}
   --source-account {{123456789012}}
   ```

   IoT domain configuration ARNs will follow the following pattern. The service-generated suffix will not be known prior to creation time, thus you must replace the suffix with a `*`. You can update the permission once the domain configuration has been created and the exact ARN is known.

   `arn:{{aws}}:iot:{{use-east-1:123456789012}}:domainconfiguration/{{domain-config-name/service-generated-suffix}}`

1. If the command succeeds, it returns a permission statement, such as this example. You can continue to the next section to configure OCSP stapling for private endpoints.

   ```
   {
       "Statement": "{\"Sid\":\"{{Id-1234}}\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"iot.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:{{us-east-1}}:123456789012:function:ocsp-function\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:iot:{{us-east-1:123456789012}}:domainconfiguration/{{domain-config-name/*}}\"}}}"
   }
   ```

   If the command doesn't succeed, it returns an error, such as this example. You'll need to review and correct the error before you continue.

   ```
   An error occurred (AccessDeniedException) when calling the AddPermission operation: User: arn:aws:iam::57EXAMPLE833:user/EXAMPLE-1 is not authorized to perform: lambda:AddPer
   mission on resource: arn:aws:lambda:{{us-east-1}}:{{123456789012}}:function:{{ocsp-function}}
   ```

### Configuring server OCSP stapling for private endpoints
<a name="iot-custom-endpoints-cert-config-ocsp-private-endpoints"></a>

#### Console
<a name="iot-custom-endpoints-cert-config-ocsp-private-endpoint-console"></a>

**To configure server certificate OCSP stapling using the AWS IoT console:**

1. From the navigation menu, choose **Settings**, and then choose **Create domain configuration**, or choose an existing domain configuration for a custom domain.

1. If you choose to create a new domain configuration in the previous step, you will see the **Create domain configuration** page. In the **Domain configuration properties** section, choose **Custom domain**. Enter the information to create a domain configuration.

   If you choose to update an existing domain configuration for a custom domain, you will see the **Domain configuration details** page. Choose **Edit**.

1. To enable OCSP server stapling, choose **Enable server certificate OCSP stapling** in the **Server certificate configurations** subsection.

1. Choose **Create domain configuration** or **Update domain configuration**.

#### AWS CLI
<a name="iot-custom-endpoints-cert-config-ocsp-private-endpoint-cli"></a>

**To configure server certificate OCSP stapling using AWS CLI:**

1. If you create a new domain configuration for a custom domain, the command to configure server certificate OCSP for private endpoints can look like the following:

   ```
   aws iot create-domain-configuration --domain-configuration-name "myDomainConfigurationName" \
           --server-certificate-arns arn:aws:iot:{{us-east-1:123456789012}}:cert/{{f8c1e5480266caef0fdb1bf97dc1c82d7ba2d3e2642c5f25f5ba364fc6b79ba3}} \
           --server-certificate-config "enableOCSPCheck=true, ocspAuthorizedResponderArn=arn:aws:acm:{{us-east-1:123456789012}}:certificate/{{certificate_ID}}, ocspLambdaArn=arn:aws:lambda:{{us-east-1:123456789012}}:function:{{my-function}}"
   ```

1. If you update an existing domain configuration for a custom domain, the command to configure server certificate OCSP for private endpoints can look like the following:

   ```
   aws iot update-domain-configuration --domain-configuration-name "myDomainConfigurationName" \
           --server-certificate-arns arn:aws:iot:{{us-east-1:123456789012}}:cert/{{f8c1e5480266caef0fdb1bf97dc1c82d7ba2d3e2642c5f25f5ba364fc6b79ba3}} \
           --server-certificate-config "enableOCSPCheck=true, ocspAuthorizedResponderArn=arn:aws:acm:{{us-east-1:123456789012}}:certificate/{{certificate_ID}}, ocspLambdaArn=arn:aws:lambda:{{us-east-1:123456789012}}:function:{{my-function}}"
   ```

**enableOCSPCheck**  
This is a Boolean value that indicates whether server OCSP stapling check is enabled or not. To enable server certificate OCSP stapling, this value must be true.

**ocspAuthorizedResponderArn**  
This is a string value of the Amazon Resource Name (ARN) for an X.509 certificate stored in AWS Certificate Manager (ACM). If provided, AWS IoT Core will use this certificate to validate the signature of the received OCSP response. If not provided, AWS IoT Core will use the issuing certificate to validate the responses. The certificate must be in the same AWS account and AWS Region as the domain configuration. For more information about how to register your authorized responder certificate, see [Import certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html).

**ocspLambdaArn**  
This is a string value of the Amazon Resource Name (ARN) for a Lambda function that acts as a Request for Comments (RFC) 6960-compliant (OCSP) responder, supporting basic OCSP responses. The Lambda function accepts a base64-encoding of the OCSP request which is encoded using the DER format. The Lambda function's response is also a base64-encoded OCSP response in the DER format. The response size must not exceed 4 kilobytes (KiB). The Lambda function must be in the same AWS account and AWS Region as the domain configuration.

For more information, see [CreateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDomainConfiguration.html) and [UpdateDomainConfiguration](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDomainConfiguration.html) from the AWS IoT API Reference.

## Important notes for using server certificate OCSP stapling in AWS IoT Core
<a name="iot-custom-endpoints-cert-config-ocsp-notes"></a>

When you use server certificate OCSP in AWS IoT Core, keep the following in mind:

1. AWS IoT Core supports only those OCSP responders that are reachable over public IPv4 addresses.

1. The OCSP stapling feature in AWS IoT Core doesn't support authorized responder. All OCSP responses must be signed by the CA that signed the certificate, and the CA must be part of the certificate chain of the custom domain.

1. The OCSP stapling feature in AWS IoT Core doesn't support custom domains that are created using self-signed certificates.

1. AWS IoT Core calls an OCSP responder every hour and caches the response. If the call to the responder fails, AWS IoT Core will staple the most recent valid response.

1. If `nextUpdateTime` is no longer valid, AWS IoT Core will remove the response from the cache, and TLS handshake will not include the OCSP response data until the next successful call to the OCSP responder. This can happen when the cached response has expired before the server gets a valid response from the OCSP responder. The value of `nextUpdateTime` suggests that the OCSP response will be valid until this time. For more information about `nextUpdateTime`, see [Server certificate OCSP log entries](cwl-format.md#server-ocsp-logs).

1. Sometimes, AWS IoT Core fails to receive the OCSP response or removes the existing OCSP response because it's expired. If situations like these happen, AWS IoT Core will continue to use the server certificate provided by the custom domain without the OCSP response.

1. The size of the OCSP response cannot exceed 4 KiB.

## Troubleshooting server certificate OCSP stapling in AWS IoT Core
<a name="iot-custom-endpoints-cert-config-ocsp-troubleshooting"></a>

AWS IoT Core emits the `RetrieveOCSPStapleData.Success` metric and the `RetrieveOCSPStapleData` log entries to CloudWatch. The metric and the log entries can help detect issues related to retrieving OCSP responses. For more information, see [Server certificate OCSP stapling metrics](metrics_dimensions.md#server-ocsp-metrics) and [Server certificate OCSP log entries](cwl-format.md#server-ocsp-logs).