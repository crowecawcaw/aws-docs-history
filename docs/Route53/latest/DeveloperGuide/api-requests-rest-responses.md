# REST Responses

Amazon Route 53 responses are just standard HTTP responses. Some of the Route 53 actions return special information specific to Route 53
in the form of an HTTP header or XML in the body of the response. The specific details are covered in the API reference topic for the
particular action.

Each response contains a request ID that you can use if you need to troubleshoot a request with Route 53. The ID is contained in an HTTP header
called `x-amz-request-id`. An example of a request ID is `647cd254-e0d1-44a9-af61-1d6d86ea6b77`.

The following example shows a response to a request to create a hosted zone. The `CreatedHostedZoneResponse` element
contains information about the hosted zone including an Route 53 identifier, the domain that the hosted zone is associated
with, and a reference description and comment. The change request itself is associated with a submittal time, an identifier and a status, shown as
`PENDING`. Most importantly, the `CreatedHostedZoneResponse` includes the Route 53 name servers assigned to the
hosted zone; this information is contained in the `DelegationSet` element.

###### Example Response

```
HTTP/1.1 201 Created
x-amz-request-id: *request\_id*
<?xml version="1.0" encoding="UTF-8"?>
<CreateHostedZoneResponse xmlns="https://route53.amazonaws.com/doc/
2013-04-01/">
   <HostedZone>
      <Id>/hostedzone/Z1PA6795UKMFR9</Id>
      <Name>example.com.</Name>
      <CallerReference>myUniqueIdentifier</CallerReference>
      <Config>
         <Comment>This is my first hosted zone.</Comment>
      </Config>
   </HostedZone>
   <ChangeInfo>
      <Id>/change/C1PA6795UKMFR9</Id>
      <Status>PENDING</Status>
      <SubmittedAt>2010-09-10T01:36:41.958Z</SubmittedAt>
   </ChangeInfo>
   <DelegationSet>
      <NameServers>
         <NameServer>ns-2048.awsdns-64.com</NameServer>
         <NameServer>ns-2049.awsdns-65.net</NameServer>
         <NameServer>ns-2050.awsdns-66.org</NameServer>
         <NameServer>ns-2051.awsdns-67.co.uk</NameServer>
      </NameServers>
   </DelegationSet>
</CreateHostedZoneResponse>

```

## Error Responses

If a REST request results in an error, the HTTP response has:

- An XML error document as the response body
- Content-Type header: text/xml
- An appropriate 3xx, 4xx, or 5xx HTTP status code

Following is an example of the XML error document in a REST error response.

```
<ErrorResponse xmlns="https://route53.amazonaws.com/doc/2013-04-01/">
   <Error>
      <Type>Sender</Type>
      <Code>InvalidInput</Code>
      <Message>The input is not valid.</Message>
   </Error>
   <RequestId>410c2a4b-e435-49c9-8382-3770d80d7d4c</RequestId>
</ErrorResponse>
```
