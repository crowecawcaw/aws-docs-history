# HTTP targets in VPC Lattice

HTTP requests and HTTP responses use header fields to send information about the HTTP
messages. HTTP headers are added automatically. Header fields are colon-separated
name-value pairs that are separated by a carriage return (CR) and a line feed (LF). A
standard set of HTTP header fields is defined in RFC 2616, [Message
Headers](https://datatracker.ietf.org/doc/html/rfc2616 "https://datatracker.ietf.org/doc/html/rfc2616"). There are also non-standard HTTP headers available that are
automatically added and widely used by the applications. For example, there are
non-standard HTTP headers with the `x-forwarded` prefix.

## x-forwarded headers

Amazon VPC Lattice adds the following `x-forwarded` headers:

`x-forwarded-for`

The source IP address.

`x-forwarded-port`

The destination port.

`x-forwarded-proto`

The connection protocol (`http` | `https`).

## Caller identity headers

Amazon VPC Lattice adds the following caller identity headers:

`x-amzn-lattice-identity`

The identity information. The following fields are present if AWS
authentication is successful.

- `Principal` – The authenticated
  principal.
- `PrincipalOrgID` – The ID of the organization
  for the authenticated principal.
- `PrincipalOrgPath` – The organization paths
  for the authenticated principal.
- `SessionName` – The name of the authenticated
  session.

The following fields are present if Roles Anywhere credentials are used and authentication
is successful.

- `X509Issuer/OU` – The issuer (OU).
- `X509SAN/DNS` – The subject alternative name (DNS).
- `X509SAN/NameCN` – The issuer alternative name (Name/CN).
- `X509SAN/URI` – The subject alternative name (URI).
- `X509Subject/CN` – The subject name (CN).

`x-amzn-lattice-identity-tags`

The principal ID and any principal tags. The format is as follows.

```
principal=`principal`;principalorgid=`orgid`;principalorgpath=`orgpath`;`principal-tag1`=`value1`; ...;`principal-tag99`=`value99`
```

VPC Lattice escapes any semicolons (;) in a value
with backslashes (\).

`x-amzn-lattice-network`

The VPC. The format is as follows.

```
SourceVpcArn=arn:aws:ec2:`region`:`account`:vpc/`id`
```

`x-amzn-lattice-target`

The target. The format is as follows.

```
ServiceArn=`arn`;ServiceNetworkArn=`arn`;TargetGroupArn=`arn`
```

For information about the resource ARNs for VPC Lattice, see [Resource types defined by Amazon VPC Lattice](../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonvpclattice.md#amazonvpclattice-resources-for-iam-policies").

The caller identity headers can't be spoofed. VPC Lattice strips these headers from any
incoming requests. These identity headers express a map that supports empty values using
the following format. When parsing, you should not rely on the specific order of the KEYs
in these headers, you should expect that new KEYs may be added any time and you should be
prepared to handle empty values.

The format is as follows.

```
`key-0`=`value-0`;`key-1`=`value-1`;....`;key-n`=`value-n`;
```
