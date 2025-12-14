# Create CloudFront Connection Functions for mutual TLS (viewer) validation

You create a CloudFront Connection Function in two stages:

1. Create the function code as JavaScript. You can use the default example from the CloudFront console or write your own. For more information, see the following topics:
   - Write CloudFront Connection Function code for mTLS validation
   - CloudFront Connection Function event structure and response format
   - Connection function code examples

2. Use CloudFront to create the Connection Function and include your code. The code exists inside the function (not as a reference).

###### Topics

- [CloudFront console](#create-connection-function-console "#create-connection-function-console")
- [AWS CLI](#create-connection-function-cli "#create-connection-function-cli")

## CloudFront console

###### To create a Connection Function

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **Create function**.
3. Enter a function name that is unique within the AWS account, choose
   **Connection function** as the function
   type, and then choose **Continue**.
4. The details page for the new Connection Function appears.

###### Note

Connection functions only support JavaScript runtime 2.0. To use CloudFront
Connection Function KeyValueStore integration in the function, you must
use this runtime version. 5. In the **Function code** section, choose the
**Build** tab and enter your connection
function code. The sample code that is included in the Build tab illustrates
the basic syntax for Connection Function code. 6. Choose **Save changes**. 7. If the Connection Function code uses KeyValueStore for certificate
revocation checking or device validation, you must associate a
KeyValueStore.

You can associate the KeyValueStore when you first create the function.
Or, you can associate it later, by associating Connection Functions.

To associate a KeyValueStore now, follow these steps:

    * Go to the **Associate KeyValueStore**
     section and choose **Associate existing
     KeyValueStore**.
    * Select the KeyValueStore that contains the certificate data for
     your Connection Function, and then choose **Associate KeyValueStore**.

CloudFront immediately associates the store with the function. You don't need to
save the function.

## AWS CLI

If you use the AWS CLI, you typically first create the Connection Function code in a
file, and then create the function with the AWS CLI.

###### To create a Connection Function

1. Create the Connection Function code in a file, and store it in a directory
   that your computer can connect to.
2. Run the command as shown in the example. This example uses the
   `fileb://` notation to pass in the file. It also includes
   line breaks to make the command more readable.

```
aws cloudfront create-connection-function \
    --name CertificateValidator \
    --connection-function-config '{
        "Comment":"Device certificate validation",
        "Runtime":"cloudfront-js-2.0",
        "KeyValueStoreAssociations":{
            "Quantity":1,
            "Items":[{
                "KeyValueStoreARN":"arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            }]
        }
    }' \
    --connection-function-code fileb://certificate-validator.js
```

###### Note

    * **Runtime** – Connection
     functions only support JavaScript runtime 2.0
     (cloudfront-js-2.0).
    * **KeyValueStoreAssociations** –
     If your Connection Function uses KeyValueStore for certificate
     validation, you can associate the KeyValueStore when you first
     create the function. Or, you can associate it later, by using
     update-connection-function. The Quantity is always 1 because
     each Connection Function can have only one KeyValueStore
     associated with it.

3. When the command is successful, you see output like the following.

```
ETag: ETVABCEXAMPLE
ConnectionFunctionSummary:
  ConnectionFunctionConfig:
    Comment: Device certificate validation
    Runtime: cloudfront-js-2.0
    KeyValueStoreAssociations:
      Quantity: 1
      Items:
        - KeyValueStoreARN: arn:aws:cloudfront::111122223333:key-value-store/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
  ConnectionFunctionMetadata:
    CreatedTime: '2024-09-04T16:32:54.292000+00:00'
    ConnectionFunctionARN: arn:aws:cloudfront::111122223333:connection-function/CertificateValidator
    LastModifiedTime: '2024-09-04T16:32:54.292000+00:00'
    Stage: DEVELOPMENT
  Name: CertificateValidator
  Status: UNPUBLISHED
Location: https://cloudfront.amazonaws.com/2020-05-31/connection-function/arn:aws:cloudfront:::connection-function/CertificateValidator
```

Most of the information is repeated from the request. Other information is
added by CloudFront.

###### Note

    * **ETag** – This value changes
     each time you modify the Connection Function. You need this
     value to update or publish the function.
    * **Stage** – New connection
     functions start in the DEVELOPMENT stage. You must publish the
     function to move it to the LIVE stage before associating it with
     a distribution.
    * **Status** – The function status
     is UNPUBLISHED until you publish it to the LIVE stage.
