# Enable HTTP header modification for your Application Load Balancer

Header modification is turned off by default and must be enabled on each listener.
For more information, see [HTTP header modification](header-modification.md "header-modification.md").

Console

###### To enable header modification

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the Application Load Balancer.
4. On the **Listeners and rules** tab, select the protocol and port
   to open the details page for your listener.
5. On the **Attributes** tab, select **Edit**.

Listener attributes are organized into groups. You'll choose which features to enable. 6. [HTTPS listeners] **Modifiable mTLS/TLS header names**

    1. Expand **Modifiable mTLS/TLS header names**.
    2. Enable the request headers to modify and provide names for them.
     For more information, see [Rename mTLS/TLS headers](header-modification.md#rename-header "header-modification.md#rename-header").

7. **Add response headers**
   1. Expand **Add response headers**.
   2. Enable the response headers to add and provide values for them.
      For more information, see [Add response headers](header-modification.md#insert-header "header-modification.md#insert-header").

8. **ALB server response header**
   1. Enable or disable **Server header**.

9. Choose **Save changes**.

AWS CLI

###### To enable header modification

Use the [modify-listener-attributes](../../../cli/latest/reference/elbv2/modify-listener-attributes.md "../../../cli/latest/reference/elbv2/modify-listener-attributes.md") command. For the list of attributes,
see [Header modification attributes](#header-modification-attributes "#header-modification-attributes").

```
aws elbv2 modify-listener-attributes \
    --listener-arn `listener-arn` \
    --attributes "Key=`attribute-name`,Value=`attribute-value`"
```

CloudFormation

###### To enable header modification

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource
to include the attributes. For the list of attributes, see
[Header modification attributes](#header-modification-attributes "#header-modification-attributes").

```
Resources:
  myHTTPlistener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTP
    Port: 80
    DefaultActions:
      - Type: "forward"
        TargetGroupArn: !Ref myTargetGroup
    ListenerAttributes:
      - Key: "`attribute-name`"
        Value: "`attribute-value`"
```

## Header modification attributes

The following are the header modification attributes supported by Application Load Balancers.

`routing.http.request.x_amzn_mtls_clientcert_serial_number.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert-Serial-Number**.

`routing.http.request.x_amzn_mtls_clientcert_issuer.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert-Issuer**.

`routing.http.request.x_amzn_mtls_clientcert_subject.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert-Subject**.

`routing.http.request.x_amzn_mtls_clientcert_validity.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert-Validity**.

`routing.http.request.x_amzn_mtls_clientcert_leaf.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert-Leaf**.

`routing.http.request.x_amzn_mtls_clientcert.header_name`

Modify the header name of
**X-Amzn-Mtls-Clientcert**.

`routing.http.request.x_amzn_tls_version.header_name`

Modify the header name of
**X-Amzn-Tls-Version**.

`routing.http.request.x_amzn_tls_cipher_suite.header_name`

Modify the header name of
**X-Amzn-Tls-Cipher-Suite**.

`routing.http.response.server.enabled`

Indicates whether to allow or remove the HTTP response server
header.

`routing.http.response.strict_transport_security.header_value`

Add the **Strict-Transport-Security** header to
inform browsers that the site should only be accessed using HTTPS, and
that any future attempts to access it using HTTP should automatically be
converted to HTTPS.

`routing.http.response.access_control_allow_origin.header_value`

Add the **Access-Control-Allow-Origin** header to
specify which origins are allowed to access the server.

`routing.http.response.access_control_allow_methods.header_value`

Add the **Access-Control-Allow-Methods** header to specify
which HTTP methods are allowed when accessing the server from a different origin.

`routing.http.response.access_control_allow_headers.header_value`

Add the **Access-Control-Allow-Headers** header to specify
which headers are allowed during a cross-origin request.

`routing.http.response.access_control_allow_credentials.header_value`

Add the **Access-Control-Allow-Credentials** header to indicate
whether the browser should include credentials such as cookies or authentication in
cross-origin requests.

`routing.http.response.access_control_expose_headers.header_value`

Add the **Access-Control-Expose-Headers** header to indicate
which headers the browser can expose to the requesting client.

`routing.http.response.access_control_max_age.header_value`

Add the **Access-Control-Max-Age** header to specify
how long the results of a preflight request can be cached, in seconds.

`routing.http.response.content_security_policy.header_value`

Add the **Content-Security-Policy** header to specify
restrictions enforced by the browser to help minimize the risk of certain
types of security threats.

`routing.http.response.x_content_type_options.header_value`

Add the **X-Content-Type-Options** header to indicate
whether the MIME types advertised in the **Content-Type**
headers should be followed and not be changed.

`routing.http.response.x_frame_options.header_value`

Add the **X-Frame-Options** header to indicate whether
the browser is allowed to render a page in a
**frame**, **iframe**,
**embed**, or **object**.
