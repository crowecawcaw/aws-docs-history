# API Usage

This section provides a high-level overview of the Amazon SimpleDB API. It describes API
conventions, API versioning used to minimize the impact of service changes, and
API-specific information for making REST requests.

## API Conventions

### Overview

This topic discusses the conventions used in the Amazon SimpleDB API reference. This includes terminology, notation, and
any abbreviations used to describe the API.

The API reference is broken down into a collection of _Actions_ and _Data Types_.

### Actions

Actions encapsulate the possible interactions with Amazon SimpleDB. These can be viewed as remote procedure calls and consist of a request and response message pair. Requests must be signed, allowing Amazon SimpleDB to authenticate the caller.

### Data Types

Values provided as parameters to the various operations must be of the indicated type. Standard XSD types (like
`string`, `boolean`, `int`) are prefixed with xsd:. Complex types defined by the
Amazon SimpleDB WSDL are prefixed with `sdb:`.

## WSDL Location and API Version

The Amazon SimpleDB API is published through a Web Services Description Language (WSDL) and an XML schema document. The version of the Amazon SimpleDB API supported with this document is 2009-04-15.

The Amazon SimpleDB WSDL is located at: [http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.wsdl](http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.wsdl "http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.wsdl").

The Amazon SimpleDB schema is located at: [http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.xsd](http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.xsd "http://sdb.amazonaws.com/doc/2009-04-15/AmazonSimpleDB.xsd").

Some libraries can generate code directly from the WSDL. Other libraries require a little more work on your part.

### API Versions

All Amazon SimpleDB API operations are versioned. This minimizes the impact of API changes on client software by sending back a response that the client can process. New versions are designed to be backward-compatible with older API revisions. However, there might be occasions where an incompatible API change is required. Additionally, newer API responses might include additional fields and, depending on how the client software is written, it might not be able to handle additional fields. Including a version in the request guarantees that it will always be sent a response that it expects.

Each API revision is assigned a version in date form. This version is included in the
request as a version parameter when using REST. The response returned by Amazon SimpleDB
honors the version included in the request. Fields introduced in a later API
version are not returned in the response.

The WSDL for each supported API version is available using the following URI format:

http://sdb.amazonaws.com/doc/<api-version>/AmazonSimpleDB.wsdl

### Specifying the API Version

For all requests, you must explicitly request the API version you want to use. Specifying the version ensures that the service does not return response elements that your application is not designed to handle.

In REST requests, you include the Version parameter.

```

http://sdb.amazonaws.com
?Action=CreateDomain
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A01%3A28-07%3A00
&Version=`2009-04-15`
&Signature=[valid signature]

```

## API Error Retries

This section describes how to handle client and server errors.

###### Note

For information on specific error messages, see [API Error Codes](APIError.md "APIError.md")

### Client Errors

REST client errors are indicated by a 4xx HTTP response code.

Do not retry client errors. Client errors indicate that Amazon SimpleDB found a problem
with the client request and the application should address the issue before
submitting the request again.

### Server Errors

For server errors, you should retry the original request.

REST server errors are indicated by a 5xx HTTP response code.

### Retries and Exponential Backoff

The AWS SDKs that support Amazon SimpleDB implement retries and exponential backoff. For more information, see [Error Retries and Exponential Backoff](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md") in the AWS General Reference.
