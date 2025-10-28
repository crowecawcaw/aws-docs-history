# Making REST Requests

###### Topics

- [About REST Requests](#AboutRESTRequests "#AboutRESTRequests")
- [Structure of a GET Request](#GETRequestStructure "#GETRequestStructure")
- [Structure of a POST Request](#POSTRequestStructure "#POSTRequestStructure")
- [Using Parameters with REST](#UsingParameterswithREST "#UsingParameterswithREST")
- [Sample REST Requests](#SampleRESTRequest "#SampleRESTRequest")
  This section provides information on making REST requests with the Amazon SimpleDB web service.

## About REST Requests

For Amazon SimpleDB requests, use HTTP GET requests that are URLs with query strings, or use
HTTP POST requests with a body of query parameters. You can use either HTTPS or HTTP for
your requests. If the length of the query string that you are constructing exceeds the
maximum allowed length of an HTTP GET URL, use the HTTP POST method, instead.

The response is an XML document that conforms to a schema.

## Structure of a GET Request

This guide presents the Amazon SimpleDB GET requests as URLs. The URL consists of:

- Endpoint—The Amazon SimpleDB endpoints, see [Regions and Endpoints](../../../general/latest/gr/rande.md#sdb_region "../../../general/latest/gr/rande.md#sdb_region").
- Action—The action you want to perform. For example,
  creating a new domain (CreateDomain). For a complete list, see [Operations](SDB_API_Operations.md "SDB_API_Operations.md").
- Parameters—A set of parameters that might be specific to
  the operation, such as an `ItemName`, or common to all
  operations, such as your `AWSAccessKeyId`.
- AWSAccessKeyId— The Access Key ID
  associated with your account.
- Version—The current API version for
  Amazon SimpleDB.
- Signature—The signature authenticates
  your request to AWS and must be accompanied by a valid timestamp. For
  information about calculating the signature value and providing the correct
  timestamp, see [HMAC-SHA Signature](HMACAuth.md "HMACAuth.md").
- SignatureVersion—Currently for Amazon SimpleDB, this value should
  always be `2`.
- SignatureMethod—`HmacSHA256`.
- Timestamp—A valid time stamp (instead of an expiration
  time) within 15 minutes before or after the request, see [About the Time Stamp](HMACAuth.md#AboutTimestamp "HMACAuth.md#AboutTimestamp").

## Structure of a POST Request

Amazon SimpleDB `POST` requests consists of:

- HTTP Headers—The following headers
  are required:

```
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: sdb.amazonaws.com
```

The `Host` value is one of the Amazon SimpleDB endpoints, see
[Regions and Endpoints](../../../general/latest/gr/rande.md#sdb_region "../../../general/latest/gr/rande.md#sdb_region").

- Action—The action you want to perform. For example,
  creating a new domain (CreateDomain). For a complete list, see [Operations](SDB_API_Operations.md "SDB_API_Operations.md").
- Parameters—A set of parameters that might be specific to
  the operation, such as an `ItemName`.
- AWSAccessKeyId— The Access Key ID associated with your
  account.
- Version—The current API version for Amazon SimpleDB.
- Signature—The signature authenticates your request to
  AWS, see [HMAC-SHA Signature](HMACAuth.md "HMACAuth.md").
- SignatureVersion—Currently for Amazon SimpleDB, this value should
  always be `2`.
- SignatureMethod—`HmacSHA256`
- Timestamp—A valid time stamp (instead of an expiration
  time) within 15 minutes before or after the request, see [About the Time Stamp](HMACAuth.md#AboutTimestamp "HMACAuth.md#AboutTimestamp").

## Using Parameters with REST

In a REST request, each parameter is separated with an ampersand (&). The
following is an example of the DomainName parameter and ItemName parameter using the
ampersand (&) separator.
`DomainName=MyDomain&ItemName=Item123`

Parameters that have specific properties start with the main parameter name (such as
`Attribute`), a dot, a sequence number, a dot, and the property
name (such as `Name`). For example:
`&Attribute.1.Name=Color`.

###### Note

Format the parameters as defined by the [HTML 4.01
specification (section 17.13.4)](http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4 "http://www.w3.org/TR/html401/interact/forms.html#h-17.13.4") for
`application/x-www-form-urlencoded`. Parameter names become
control names, and their values become control values. The order is not significant.
However, also note that Amazon SimpleDB is more strict than the specification about what is
URL encoded.

## Sample REST Requests

This section provides sample REST requests and responses.

### REST Request as a URL

The following shows a REST request that puts three attributes and values for an item named
Item123 into the domain named MyDomain.

###### Note

A valid request does not contain line breaks. The following request contains line breaks to
show each parameter clearly.

```
https://sdb.amazonaws.com/?Action=PutAttributes
&DomainName=MyDomain
&ItemName=Item123
&Attribute.1.Name=Color&Attribute.1.Value=Blue
&Attribute.2.Name=Size&Attribute.2.Value=Med
&Attribute.3.Name=Price&Attribute.3.Value=0014.99
&AWSAccessKeyId=`your_access_key`
&Version=2009-04-15
&Signature=`valid_signature`
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A01%3A28-07%3A00

```

### REST Response

The following is the sample response:

```
<PutAttributesResponse>
  <ResponseMetadata>
    <StatusCode>Success</StatusCode>
    <RequestId>f6820318-9658-4a9d-89f8-b067c90904fc</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>
```

### REST Request using HTTP POST

The following shows a REST request that puts three attributes and values for an item named
Item123 into the domain named MyDomain.

###### Note

A valid request does not contain line breaks in the body of the request. The following request
contains line breaks to show each parameter clearly.

```
POST / HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: sdb.amazonaws.com

Action=PutAttributes
&DomainName=MyDomain
&ItemName=Item123
&Attribute.1.Name=Color&Attribute.1.Value=Blue
&Attribute.2.Name=Size&Attribute.2.Value=Med
&Attribute.3.Name=Price&Attribute.3.Value=0014.99
&AWSAccessKeyId=`your_access_key`
&Version=2009-04-15
&Signature=`valid_signature`
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A01%3A28-07%3A00
```

### REST Response

The following is the sample response:

```
<PutAttributesResponse>
  <ResponseMetadata>
    <StatusCode>Success</StatusCode>
    <RequestId>f6820318-9658-4a9d-89f8-b067c90904fc</RequestId>
    <BoxUsage>0.0000219907</BoxUsage>
  </ResponseMetadata>
</PutAttributesResponse>
```
