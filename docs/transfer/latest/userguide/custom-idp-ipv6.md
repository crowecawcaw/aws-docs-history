# IPv6 support for custom identity providers

AWS Transfer Family custom identity providers fully support IPv6 connections. When implementing a
custom identity provider, your Lambda function can receive and process authentication
requests from both IPv4 and IPv6 clients without any additional configuration. The Lambda
function receives the client's IP address in the `sourceIp` field of the request,
which can be either an IPv4 address (for example, `203.0.113.42`) or an IPv6
address (for example, `2001:db8:85a3:8d3:1319:8a2e:370:7348`). Your custom
identity provider implementation should handle both address formats appropriately.

###### Important

If your custom identity provider performs IP-based validation or logging, ensure your
implementation properly handles IPv6 address formats. IPv6 addresses are longer than
IPv4 addresses and use a different notation format.

###### Note

When handling IPv6 addresses in your custom identity provider, ensure you're using
proper IPv6 address parsing functions rather than simple string comparisons. IPv6
addresses can be represented in various canonical formats (for example
`fd00:b600::ec2` or `fd00:b600:0:0:0:0:0:ec2`). Use
appropriate IPv6 address libraries or functions in your implementation language to
correctly validate and compare IPv6 addresses.

###### Example Handling both IPv4 and IPv6 addresses in a custom identity provider

```

def lambda_handler(event, context):
    # Extract the source IP address from the request
    source_ip = event.get('sourceIp', '')

    # Log the client IP address (works for both IPv4 and IPv6)
    print(f"Authentication request from: {source_ip}")

    # Example of IP-based validation that works with both IPv4 and IPv6
    if is_ip_allowed(source_ip):
        # Continue with authentication
        # ...
    else:
        # Reject the authentication request
        return {
            "Role": "",
            "HomeDirectory": "",
            "Status": "DENIED"
        }

```

For more information about implementing custom identity providers, see [Using AWS Lambda to integrate your identity
provider](custom-lambda-idp.md "custom-lambda-idp.md").
