

# Resolver DNS Firewall events detail reference
<a name="events-detail-reference"></a>

All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others. For definitions of these general fields, see [Event structure reference](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html) in the *Amazon EventBridge User Guide*. 

In addition, each event has a `detail` field that contains data specific to that particular event. The reference below defines the detail fields for the various DNS Firewall events.

When using EventBridge to select and manage DNS Firewall events, it's useful to keep the following in mind:
+ The `source` field for all events from DNS Firewall is set to `aws.route53resolver`.
+ The `detail-type` field specifies the event type. 

  For example, `DNS Firewall Block` or `DNS Firewall Alert`.
+ The `detail` field contains the data that is specific to that particular event. 

For information on constructing event patterns that enable rules to match DNS Firewall events, see [Event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) in the *Amazon EventBridge User Guide*.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.

**Topics**
+ [DNS Firewall alert event detail](#dns-firewall-alert)
+ [DNS Firewall block event detail](#dns-firewall-block)

## DNS Firewall alert event detail
<a name="dns-firewall-alert"></a>

Below are the detail fields for Alert status event detail .

The `source` and `detail-type` fields are included because they contain specific values for Route 53 events.

```
{...,
 "detail-type": "DNS Firewall Alert",
  "source": "aws.route53resolver",
 ...,
 "detail": {
      "account-id": "string",
      "last-observed-at": "string",
      "query-name": "string",
      "query-type": "string",
      "query-class": "string",
      "transport": "string",
      "firewall-rule-action": "string",
      "firewall-rule-group-id": "string",
      "firewall-domain-list-id": "string",
      "firewall-protection": "string",
      "resources": [{
         "resource-type": "string",
         "instance-details": {
             "id": "string",
       }
     },
     { 
         "resource-type": "string",
         "resolver-endpoint-details": {
         "id": "string"
       }
     }
 ]
```

`detail-type`  
Identifies the type of event.  
For this event, this value is `DNS Firewall Alert`.

`source`  
Identifies the service that generated the event. For DNS Firewall events, this value is `aws.route53resolver`.

`detail`  
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For this event, this data includes:    
`account-id`  
The ID of the AWS account that created the VPC.  
`last-observed-at`  
The timestamp of when the Alert/Block query was made in the VPC.  
`query-name`  
The domain name (example.com) or subdomain name (www.example.com) that was specified in the query.  
`query-type`  
Either the DNS record type that was specified in the request, or ANY. For information about the types that Route 53 supports, see [Supported DNS record types](ResourceRecordTypes.md).  
`query-class`  
The class of the query.  
`transport`  
The protocol used to submit the DNS query.  
`firewall-rule-action`  
The action specified by the rule that matched the domain name in the query. Either `ALERT` or `BLOCK`.  
`firewall-rule-group-id`  
The ID of the DNS Firewall rule group that matched the domain name in the query. For more information about the firewall rule groups, see DNS Firewall [DNS Firewall rule groups and rules](resolver-dns-firewall-rule-groups.md).  
`firewall-domain-list-id`  
The domain list used by the rule that matched the domain name in the query.   
`firewall-protection`  
The DNS Firewall Advanced protection: DGA, DICTIONARY\_DGA, or DNS\_TUNNELING. For more information, see DNS Firewall [DNS Firewall Advanced Rules](firewall-advanced.md).   
`resourcese`  
Contains resource types and additional details about them.  
`resource-type`  
Specifies the resource type, such as resolver endpoint or a VPC instance.  
`{{resource-type}}-detail`  
Additional details about the resource.

**Example DNS Firewall alert event**  <a name="dns-firewall-alert.example"></a>
The following is an example alert event.  

```
{
 "version": "1.0",
 "id": "8e5622f9-d81c-4d81-612a-9319e7ee2506",
 "detail-type": "DNS Firewall Alert",
 "source": "aws.route53resolver",
 "account": "123456789012",
 "time": "2023-05-30T21:52:17Z",
 "region": "us-west-2",
 "resources": [],
 "detail": {
 "account-id": "123456789012",
 "last-observed-at": "2023-05-30T20:15:15.900Z",
 "query-name": "15.3.4.32.in-addr.arpa.",
 "query-type": "A",
 "query-class": "IN",
 "transport": "UDP",
 "firewall-rule-action": "ALERT",
 "firewall-rule-group-id": "rslvr-frg-01234567890abcdef",
 "firewall-domain-list-id": "rslvr-fdl-01234567890abcdef",
 "firewall-protection": "DGA",
 "resources": [{
      "resource-type": "instance",
      "instance-details": {
         "id": "i-05746eb48123455e0",
       }
     },
     { 
      "resource-type": "resolver-endpoint",
      "resolver-endpoint-details": {
         "id": "i-05746eb48123455e0"
       }
     }
 ],
"src-addr": "4.5.64.102",
"src-port": "56067",
"vpc-id": "vpc-7example"
 }
}
```

## DNS Firewall block event detail
<a name="dns-firewall-block"></a>

Below are the detail fields for {{event name}}.

The `source` and `detail-type` fields are included because they contain specific values for Route 53 events.

```
{...,
 "detail-type": "DNS Firewall Block",
  "source": "aws.route53resolver",
 ...,
 "detail": {
      "account-id": "string",
      "last-observed-at": "string",
      "query-name": "string",
      "query-type": "string",
      "query-class": "string",
      "transport": "string",
      "firewall-rule-action": "string",
      "firewall-rule-group-id": "string",
      "firewall-domain-list-id": "string",
      "firewall-protection": "string",
      "resources": [{
         "resource-type": "string",
         "instance-details": {
             "id": "string",
       }
     },
     { 
         "resource-type": "string",
         "resolver-endpoint-details": {
         "id": "string"
       }
     }
 ]
```

`detail-type`  
Identifies the type of event.  
For this event, this value is `DNS Firewall Alert`.

`source`  
Identifies the service that generated the event. For DNS Firewall events, this value is `aws.route53resolver`.

`detail`  
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For this event, this data includes:    
`account-id`  
The ID of the AWS account that created the VPC.  
`last-observed-at`  
The timestamp of when the Alert/Block query was made in the VPC.  
`query-name`  
The domain name (example.com) or subdomain name (www.example.com) that was specified in the query.  
`query-type`  
Either the DNS record type that was specified in the request, or ANY. For information about the types that Route 53 supports, see [Supported DNS record types](ResourceRecordTypes.md).  
`query-class`  
The class of the query.  
`transport`  
The protocol used to submit the DNS query.  
`firewall-rule-action`  
The action specified by the rule that matched the domain name in the query. Either `ALERT` or `BLOCK`.  
`firewall-rule-group-id`  
The ID of the DNS Firewall rule group that matched the domain name in the query. For more information about the firewall rule groups, see DNS Firewall [DNS Firewall rule groups and rules](resolver-dns-firewall-rule-groups.md).  
`firewall-domain-list-id`  
The domain list used by the rule that matched the domain name in the query.   
`firewall-protection`  
The DNS Firewall Advanced protection: DGA, DICTIONARY\_DGA, or DNS\_TUNNELING. For more information, see DNS Firewall [DNS Firewall Advanced Rules](firewall-advanced.md).   
`resourcese`  
Contains resource types and additional details about them.  
`resource-type`  
Specifies the resource type, such as resolver endpoint or a VPC instance.  
`{{resource-type}}-detail`  
Additional details about the resource.

**Example event**  <a name="dns-firewall-block.example"></a>
The following is an example block event.  

```
{
 "version": "1.0",
 "id": "8e5622f9-d81c-4d81-612a-9319e7ee2506",
 "detail-type": "DNS Firewall Block",
 "source": "aws.route53resolver",
 "account": "123456789012",
 "time": "2023-05-30T21:52:17Z",
 "region": "us-west-2",
 "resources": [],
 "detail": {
 "account-id": "123456789012",
 "last-observed-at": "2023-05-30T20:15:15.900Z",
 "query-name": "15.3.4.32.in-addr.arpa.",
 "query-type": "A",
 "query-class": "IN",
 "transport": "UDP",
 "firewall-rule-action": "BLOCK",
 "firewall-rule-group-id": "rslvr-frg-01234567890abcdef",
 "firewall-domain-list-id": "rslvr-fdl-01234567890abcdef",
 "firewall-protection": "DNS_TUNNELING",
 "resources": [{
      "resource-type": "instance",
      "instance-details": {
         "id": "i-05746eb48123455e0"
       }
     },
     { 
      "resource-type": "resolver-endpoint",
      "resolver-endpoint-details": {
         "id": "i-05746eb48123455e0",
       }
     }
 ],
"src-addr": "4.5.64.102",
"src-port": "56067",
"vpc-id": "vpc-7example"
 }
}
```