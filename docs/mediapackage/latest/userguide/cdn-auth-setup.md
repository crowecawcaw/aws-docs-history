# Configure MediaPackage CDN authorization setup

Configure AWS Elemental MediaPackage CDN authorization to secure your streaming content by setting up
custom HTTP headers, storing secrets, and configuring IAM permissions. This procedure
ensures that only authorized CDN requests can access your MediaPackage endpoints.

###### To set up CDN authorization

1. **Configure a CDN custom origin HTTP header.** In
   your CDN, configure a custom origin HTTP header that contains the header
   `X-MediaPackageV2-CDNIdentifier` and a value. For the
   value, we recommend that you use the [UUID version 4](https://www.ietf.org/rfc/rfc4122.txt "https://www.ietf.org/rfc/rfc4122.txt") format,
   which produces a 36-character string. If you aren't using the UUID version 4
   format, the value must be 8-256 characters long.

###### Important

The value you choose should be a static value. There isn't native
integration between your CDN and AWS Secrets Manager, so the value should be static
both in your CDN and in AWS Secrets Manager. If you change this value after you
configure your CDN and your secret, you have to manually rotate the value.
For more information, see [Rotate MediaPackage CDN authorization secrets](cdn-auth-rotate.md "cdn-auth-rotate.md").

**Example header and value**

```
X-MediaPackageV2-CDNIdentifier: `9ceebbe7-9607-4552-8764-876e47032660`
```

These steps will vary depending on your CDN. For distribution setup with
custom headers in Amazon CloudFront, see the [Distribution settings reference](../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md "../../../AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.md") in the Amazon CloudFront developer
guide. 2. **Store the value as a secret in AWS Secrets Manager.**
Store the custom header value as a _secret_ in
AWS Secrets Manager. The secret must use the same AWS account and Region settings as
your MediaPackage resources. MediaPackage doesn't support sharing secrets across accounts or
Regions. However, you can use the same secret across multiple endpoints in the
same Region and on the same account.

###### Important

The secret must be created in the same AWS Region as your MediaPackage endpoint.
Cross-Region secret access is not supported.

    1. Sign in to the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
    2. Choose **Store a new secret**. For **Secret
     type**, choose **Other type of
     secrets**.
    3. For **Key/value pairs**, enter the key and value
     information.




    	* In the box on the left (key), enter
    	 `MediaPackageV2CDNIdentifier`.
    	* In the box on the right (value), enter the value that you
    	 configured for your custom origin HTTP header. For example,
    	 `9ceebbe7-9607-4552-8764-876e47032660`.
    4. For **Encryption key**, you can use the AWS KMS key
     that Secrets Manager creates by default.
    5. Choose **Next**.
    6. For **Secret name**, we recommend that you prefix it
     with `MediaPackageV2/` so that you know it's a
     secret used for MediaPackage. For example,
     `MediaPackageV2/cdn_auth_us-west-2`.
    7. Choose **Next**.
    8. For **Configure automatic rotation**, keep the
     default **Disable automatic rotation** setting.


    If you need to rotate the key later, see [Rotate MediaPackage CDN authorization secrets](cdn-auth-rotate.md "cdn-auth-rotate.md").
    9. Choose **Next**, and then choose
     **Store**.


    This takes you to the list of your secrets.
    10. Select your secret name to view the **Secret ARN**.
     The ARN has a value similar to
     `arn:aws:secretsmanager:us-west-2:123456789012:secret:MediaPackageV2/cdn_auth_test-xxxxxx`.
     You use the ARN for the secret when you configure CDN authorization for
     MediaPackage in step 4.

3. **Create an IAM role for MediaPackage access to Secrets Manager.**
   Create an IAM role to give MediaPackage access to Secrets Manager and AWS Key Management Service (AWS KMS). When
   MediaPackage receives a playback request from the CDN that includes a secret value in
   the custom headers, MediaPackage retrieves the stored secret value from AWS KMS and
   verifies that the secret values match. Follow the steps in [Allowing MediaPackage to access other
   AWS services](setting-up-create-trust-rel.md "setting-up-create-trust-rel.md") to set up the policy and
   role.

You use the ARN for the IAM role that you created when you enable CDN
authorization in MediaPackage in the next step. 4. **Enable CDN authorization in MediaPackage.** You can
enable CDN authorization for your channel endpoints from the MediaPackage console,
AWS CLI, or MediaPackage API.

###### Tip

Use the same secret across multiple endpoints in the same Region and on
the same account. Reduce costs by creating a new secret only when necessary
for your workflow.

    1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
    2. Under **Live v2**, create or edit a channel group and
     channel. For help, see [Creating a channel group in AWS Elemental MediaPackage](channel-group-create.md "channel-group-create.md").
    3. On the channel, create or edit an endpoint.
    4. In **Endpoint policy**, select **Attach a

     custom policy** and add a policy for the endpoint.


    ###### Example policy with CDN auth condition


    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "AllowGetObjectAccessForAuthorizedRequest",
     "Effect": "Allow",
     "Principal": "*",
     "Action": "mediapackagev2:GetObject",
     "Resource": "arn:aws:mediapackagev2:us-east-1:111122223333:channelGroup/`channelGroupName`/channel/`channelName`/originEndpoint/`originEndpointName`",
     "Condition": {
     "Bool": {
     "mediapackagev2:RequestHasMatchingCdnAuthHeader": "true"
     }
     }
     }
     ]
    }`

    ```
    5. In **CDN authorization configuration**, complete the
     fields:




    	* In **Secrets role ARN**, enter the ARN for
    	 the IAM role that you created in step 3.
    	* In **CDN identifier secret ARN**, enter the
    	 ARN for the secret in Secrets Manager that your CDN uses for authorization
    	 to access your endpoint.
    6. Complete the remaining fields as needed and save the endpoint.You have now completed the setup for CDN authorization. Requests to this

endpoint must contain the same authorization code that you saved in
Secrets Manager.

###### To enable CDN authorization via the MediaPackage API

For information about enabling CDN authorization with the MediaPackage API, see
[AWS Elemental MediaPackage V2 Live
API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").
