# Configure desync mitigation mode for your Classic Load Balancer

Desync mitigation mode protects your application from issues due to HTTP Desync. The
load balancer classifies each request based on its threat level, allows safe requests,
and then mitigates risk as specified by the mitigation mode that you specify. The desync
mitigation modes are monitor, defensive, and strictest. The default is the defensive
mode, which provides durable mitigation against HTTP desync while maintaining the
availability of your application. You can switch to strictest mode to ensure that your
application receives only requests that comply with RFC 7230.

The http_desync_guardian library analyzes HTTP requests to prevent HTTP Desync
attacks. For more information, see [HTTP Desync Guardian](https://github.com/aws/http-desync-guardian "https://github.com/aws/http-desync-guardian") on
github.

###### Contents

- [Classifications](#desync-mitigation-classification "#desync-mitigation-classification")
- [Modes](#desync-mitigation-modes "#desync-mitigation-modes")
- [Modify desync mitigation
  mode](#update-desync-mitigation-mode "#update-desync-mitigation-mode")

###### Tip

This configuration applies only to Classic Load Balancers. For information that applies to Application Load
Balancers, see [Desync
mitigation mode for Application Load Balancers](../application/application-load-balancers.md#desync-mitigation-mode "../application/application-load-balancers.md#desync-mitigation-mode").

## Classifications

The classifications are as follows.

- Compliant — Request complies with RFC 7230 and poses no known
  security threats.
- Acceptable — Request does not comply with RFC 7230 but poses no
  known security threats.
- Ambiguous — Request does not comply with RFC 7230 but poses a risk,
  as various web servers and proxies could handle it differently.
- Severe — Request poses a high security risk. The load balancer
  blocks the request, serves a 400 response to the client, and closes the
  client connection.

The following lists describe the issues for each classification.

###### Acceptable

- A header contains a non-ASCII or control character.
- The request version contains a bad value.
- There is a Content-Length header with a value of 0 for a GET or HEAD
  request.
- The request URI contains a space that is not URL encoded.

###### Ambiguous

- The request URI contains control characters.
- The request contains both a Transfer-Encoding header and a Content-Length
  header.
- There are multiple Content-Length headers with the same value.
- A header is empty or there is a line with only spaces.
- There is a header that can be normalized to Transfer-Encoding or
  Content-Length using common text normalization techniques.
- There is a Content-Length header for a GET or HEAD request.
- There is a Transfer-Encoding header for a GET or HEAD request.

###### Severe

- The request URI contains a null character or carriage return.
- The Content-Length header contains a value that cannot be parsed or is not
  a valid number.
- A header contains a null character or carriage return.
- The Transfer-Encoding header contains a bad value.
- The request method is malformed.
- The request version is malformed.
- There are multiple Content-Length headers with different values.
- There are multiple Transfer-Encoding: chunked headers.

If a request does not comply with RFC 7230, the load balancer increments the
`DesyncMitigationMode_NonCompliant_Request_Count` metric. For more
information, see [Classic Load Balancer metrics](elb-cloudwatch-metrics.md#loadbalancing-metrics-clb "elb-cloudwatch-metrics.md#loadbalancing-metrics-clb").

## Modes

The following table describes how Classic Load Balancers treat requests based on mode and
classification.

| Classification | Monitor mode | Defensive mode | Strictest mode |
| -------------- | ------------ | -------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compliant      | Allowed      | Allowed        | Allowed        |
| Acceptable     | Allowed      | Allowed        | Blocked        |
| Ambiguous      | Allowed      | Allowed¹       | Blocked        |
| Severe         | Allowed      | Blocked        | Blocked        | ¹ Routes the requests but closes the client and target connections. ## Modify desync mitigation mode ###### To update desync mitigation mode using the console 1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"). 2. On the navigation pane, under **Load Balancing**, choose **Load Balancers**. 3. Choose the name of the load balancer to open its detail page. 4. On the **Attributes** tab, choose **Edit**. 5. On the **Edit load balancer attributes** page, under **Traffic configuration**, choose **Defensive - recommended**, **Strictest**, or **Monitor**. 6. Choose **Save changes**. ###### To update desync mitigation mode using the AWS CLI Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elb/modify-load-balancer-attributes.md "../../../cli/latest/reference/elb/modify-load-balancer-attributes.md") command with the `elb.http.desyncmitigationmode` attribute set to `monitor`, `defensive`, or `strictest`. ``aws elb modify-load-balancer-attributes --load-balancer-name `my-load-balancer` --load-balancer-attributes file://attribute.json`` The following is the contents of `attribute.json`. `{ "AdditionalAttributes": [ { "Key": "elb.http.desyncmitigationmode", "Value": "strictest" } ] }` |
