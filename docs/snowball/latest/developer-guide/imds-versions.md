Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# IMDS versions on a Snowball Edge

You can access instance metadata from a running instance using IMDS version 2 or IMDS version 1:

- Instance Metadata Service version 2 (IMDSv2), a session‐oriented method
- Instance Metadata Service version 1 (IMDSv1), a request‐response method
  Depending on the version of your Snow software, you can use IMDSv1, IMDSv2, or both. This
  also depends on the type of AMI running in the EC2-compatible instance. Some AMIs, such as those running
  Ubuntu 20.04, require IMDSv2. The instance metadata service distinguishes between IMDSv1 and
  IMDSv2 requests based on the presence of `PUT` or `GET` headers. IMDSv2
  uses both of these headers. IMDSv1 uses only the `GET` header.

AWS encourages the use of IMDSv2 rather than IMDSv1 because IMDSv2 includes higher
security. For more information, see [Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with
enhancements to the EC2 Instance Metadata Service](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/ "https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/").

## IMDSv2 on a Snowball Edge

When you use IMDSv2 to request instance metadata, the request must follow these rules:

1. Use a `PUT` request to initiate a session to the instance metadata service. The `PUT` request returns a session token that must be included in subsequent `GET` requests to the instance metadata service. The session token that defines the session duration. Session duration can be a minimum of one second and a maximum of six hours. During this duration, you can use the same session token for subsequent requests. After this duration expires, you must create a new session token for future requests. The token is required to access metadata using IMDSv2.
2. Include the token in all `GET` requests to the instance metadata service.
   1. The token is an instance‐specific key. The token is not valid on other EC2-compatible instances and will be rejected if you attempt to use it outside of the instance on which it was generated.
   2. The `PUT` request must include a header that specifies the time to live (TTL) for the token, in seconds, up to a maximum of six hours (21,600 seconds). The token represents a logical session. The TTL specifies the length of time that the token is valid and, therefore, the duration of the session.
   3. After a token expires, to continue accessing instance metadata, you must create a new session using another `PUT` request.
   4. You can choose to reuse a token or create a new token with every request. For a small number of requests, it might be easier to generate and immediately use a token each time you need to access the instance metadata service. But for efficiency, you can specify a longer duration for the token and reuse it rather than having to write a `PUT` request every time you need to request instance metadata. There is no practical limit on the number of concurrent tokens, each representing its own session.

HTTP `GET` and `HEAD` methods are allowed in IMDSv2 instance metadata requests. `PUT` requests are rejected if they contain an `X-Forwarded-For` header.

By default, the response to `PUT` requests has a response hop limit (time to live) of 1 at the IP protocol level. IMDS for Snow does not have ability to modify the hop limit on `PUT` responses.

The following example uses a Linux shell script and IMDSv2 to retrieve the top‐level instance metadata items. This example:

1. Creates a session token lasting six hours (21,600 seconds) using the `PUT` request.
2. Stores the session token header in a variable named `TOKEN`.
3. Requests the top‐level metadata items using the token.

Use two commands to generate the EC2-compatible token. You can run the commands seperately or as one command.

First, generate a token using the following command.

###### Note

`X-aws-ec2-metadata-token-ttl-seconds` is a required header. If this header is
not included, you will receive an **400 - Missing or Invalid
Parameters** error code.

```

    [ec2-user ~]$ TOKEN=curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"

```

Then, use the token to generate top‐level metadata items using the following command.

```

    [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/

```

###### Note

If there is an error in creating the token, an error message is stored in the variable instead of a valid token and the command will not work.

You can store the token and combine the commands. The following example combines the above two commands and stores the session token header in a variable named `TOKEN`.

###### Example of combined commands

```

    [ec2-user ~]$ TOKEN=curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600" \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/

```

After you've created a token, you can reuse it until it expires. The following example command gets the ID of the AMI used to launch the instance and stores it in the `$TOKEN` created in the previous example.

###### Example of reusing a token

```

    [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/ami-id

```

## IMDSv1 on a Snowball Edge

IMDSv1 uses the request‐response model. To request instance metadata, you send a `GET` request to the instance metadata service.

```

    [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/

```

Your instance metadata is available from your running instance, so you do not need to use Amazon EC2 console or the AWS CLI to access it. This can be helpful when you're writing scripts to run from your instance. For example, you can access the local IP address of your instance from instance metadata to manage a connection to an external application.
Instance metadata is divided into categories. For a description of each instance metadata category, see [Supported Instance Metadata and User Data](edge-compute-instance-metadata.md "edge-compute-instance-metadata.md") in this guide.

To view all categories of instance metadata from within a running instance, use the following IPv4 URI:

```

    http://169.254.169.254/latest/meta-data/

```

The IP addresses are link-local addresses and are valid only from the instance. For more information, see [Link-local address](https://en.wikipedia.org/wiki/Link-local_address "https://en.wikipedia.org/wiki/Link-local_address") on Wikipedia.

All instance metadata is returned as text (HTTP content type `text/plain`).

A request for a specific metadata resource returns the appropriate value, or an **404 - Not Found** HTTP error code, if the resource is not available.

A request for a general metadata resource (when the URI ends with a `/` character) returns a list of available resources, or an **404 - Not Found** HTTP error code if there is no such resource. The list items are on separate lines, terminated by line feeds (ASCII character code 10).

For requests made using IMDSv1, the following HTTP error codes can be returned:

- **400 ‐ Missing or Invalid Parameters** — The
  `PUT` request is not valid.
- **401 ‐ Unauthorized** — The `GET` request uses an invalid token. The recommended action is to generate a new token.
- **403 ‐ Forbidden** — The request is not allowed or the instance metadata service is turned off.
