# Resolver delegation rules tutorial

The delegation rule allows the Route 53 Resolver to reach the name servers that host the delegated
zone through the specified outbound endpoint. While the forward rule informs the Route 53 Resolver to
forward the DNS queries to the name servers that match the specified domain through outbound
endpoint, the delegation rule informs Route 53 Resolver to reach the delegated name servers via the
outbound endpoint specified when the delegated NS records are returned. Route 53 Resolver sends a
query to the delegated name servers when the NS records in the DNS response match the
domain name specified in the delegation record.

## Steps to Use the Resolver endpoint outbound delegation

1. Create a Route 53 Resolver outbound endpoint in the VPC that you want DNS queries to originate from to
   the resolvers on your network.

You can use either the following API or the CLI command:

    * [`CreateResolverEndpoint` API](../APIReference/API_route53resolver_CreateResolverEndpoint.md "../APIReference/API_route53resolver_CreateResolverEndpoint.md")
    * [`create-resolver-endpoint` CLI](../../../cli/latest/reference/route53resolver/create-resolver-endpoint.md "../../../cli/latest/reference/route53resolver/create-resolver-endpoint.md")

2. Create one or more delegation rules, which specify the domain names for which the queries should be
   delegated to your network through the specified outbound endpoint.

Example delegation rule creation with CLI:

```
aws route53resolver create-resolver-rule \
--region `REGION` \
--creator-request-id `delegateruletest` \
--delegation-record `example.com` \
--name `delegateruletest` \
--rule-type DELEGATE \
--resolver-endpoint-id `outbound endpoint ID`
```

3. Associate the delegation rule with the VPCs for which you want the queries to be delegated.

You can use either the following API or the CLI command:

    * [AssociateResolverRule](../APIReference/API_route53resolver_AssociateResolverRule.md "../APIReference/API_route53resolver_AssociateResolverRule.md") API.
    * [associate-resolver-rules](../../../cli/latest/reference/route53resolver/associate-resolver-rule.md "../../../cli/latest/reference/route53resolver/associate-resolver-rule.md") CLI command.

## Types of delegation supported by Resolver outbound endpoint

Route 53 Resolver supports two types of outbound delegation:

- Route 53 private hosted zone to Route 53 Resolver outbound delegation:

Delegates a sub-domain from a private hosted zone to either to on-premises DNS server
or a public hosted zone on the internet using outbound delegation. This outbound
delegation allows you to split management of your DNS records between the private hosted
zone and the delegated zone. The delegation can be done with or without glue record in
private hosted zone based on your DNS setup.For more information see [Private hosted zone to
outbound](#phz-to-outbound-delegation "#phz-to-outbound-delegation").

- Route 53 Resolver outbound to outbound delegation:

Delegates a subdomain from your on-premises DNS server to another on-premises server in
a same or different location using outbound to outbound delegation. This is similar to
delegating from a private hosted zone to an outbound endpoint, where you can delegate to
zone hosted on your on-premises name server. For more information see [Outbound to outbound](#outbound-to-outbound-delegation "#outbound-to-outbound-delegation").

### Route 53 private hosted zone to Route 53 Resolver outbound delegation example configuration

Let's assume a DNS setup where the parent hosted zone is hosted in an Route 53 private
hosted zone in an Amazon VPC and subdomains are being delegated to name servers hosted in
Europe, Asia and North America. All the DNS queries are passed thorough the Route 53 Resolver.

Follow the example steps to configure your private hosted zone and Route 53 Resolver.

###### Configure private hosted zone for outbound delegation

1. For the private hosted zone setup:

Parent hosted zone: `hr.example.com`

```
$TTL    86400 ; 24 hours
$ORIGIN hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @
eu.hr.example.com IN NS ns1.eu.hr.example.com.
apac.hr.example.com IN NS ns2.apac.hr.example.com.
na.hr.example.com IN NS ns3.na.hr.example.net. # Out of Zone Delegation

ns1.eu.hr.example.com IN A 10.0.0.30 # Glue Record
ns2.apac.hr.example.com IN A 10.0.0.40 # Glue Record
```

2. For the on-premises name server in the Europe on-premises region:
   - Hosted Zone: `eu.hr.example.com` NS IP: `10.0.0.30`

```
$TTL    86400 ; 24 hours
$ORIGIN eu.hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @

test.eu.hr.example.com IN A 1.2.3.4
```

3. For the on-premises name server in the Asia on-premises region:

Hosted Zone: `apac.hr.example.com`, `10.0.0.40`

The apac name server can delegate the subdomain to other name servers.

```
$TTL    86400 ; 24 hours
$ORIGIN apac.hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @

test.apac.hr.example.com IN A 5.6.7.8
engineering.apac.hr.example.com IN NS ns1.engineering.apac.hr.example.com
sales.apac.hr.example.com IN NS ns2.sales.apac.hr.example.com
ns1.engineering.apac.hr.example.com IN A 10.0.0.80
ns2.sales.apac.hr.example.com IN A 10.0.0.90
```

Hosted Zone: `engineering.apac.hr.example.com`,
`10.0.0.80`

```
$TTL 86400 ; 24 hours
$ORIGIN engineering.apac.hr.example.com
@ 1D IN SOA @ root (20200322001 3H 15 1w 3h)
@ 1D IN NS @
test.engineering.apac.hr.example.com IN A 1.1.1.1
```

4. For the on-premises name server in the North America on-premises region:

Hosted Zone: `na.hr.example.net` NS IP: `10.0.0.50`

```
$TTL    86400 ; 24 hours
$ORIGIN na.hr.example.net
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @
ns3.na.hr.example.net. IN A 10.0.0.50
test.na.hr.example.com  IN A 9.10.11.12
```

###### Route 53 Resolver setup

- For the Route 53 Resolver you need to set up one forward rule and two delegation rules:

**Forward rule**

    1. For forwarding the out-of-zone delegation record,
     so the Route 53 Resolver knows the IP of the delegated NS to forward the initial request.


    domain-name: `hr.example.net` target-ips:
     `10.0.0.50`

**Delegation rules**

    1. Delegation rule for in-zone delegation:


    delegation-record: `hr.example.com`
    2. Delegation rule for out-of zone delegation:


    delegation-record: `hr.example.net`

### Outbound to outbound delegation example configuration

Instead of having the parent hosted zone in an Amazon VPC, let's assume a DNS setup where
the parent hosted zone is in the central on-premises location and subdomains are being
delegated to name servers hosted in Europe, Asia, and North America. All the DNS queries are
passed thorough the Route 53 Resolver.

Follow the example steps to configure your on-premises DNS and the Route 53 Resolver.

###### Configure on-premise DNS

1. For the on-premises name server in the central on-premises region:
   - **Parent hosted zone:**
     `hr.example.com`

   Hosted Zone `hr.example.com`, NS IP: `10.0.0.20`

```
$TTL    86400 ; 24 hours
$ORIGIN hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @
eu.hr.example.com IN NS ns1.eu.hr.example.com.
apac.hr.example.com IN NS ns2.apac.hr.example.com.
na.hr.example.com IN NS ns3.na.hr.example.net. # Out of zone delegation

ns1.eu.hr.example.com IN A 10.0.0.30 # Glue record
ns2.apac.hr.example.com IN A 10.0.0.40 # Glue record
```

2. For the on-premises name server in the Europe on-premises region (the configuration for the
   Europe, Asia, and North America name servers is the same as for the private hosted zone
   to outbound delegation):
   - Hosted Zone: `eu.hr.example.com` NS IP: `10.0.0.30`

```
$TTL    86400 ; 24 hours
$ORIGIN eu.hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @

test.eu.hr.example.com IN A 1.2.3.4
```

3. For the on-premises name server in the Asia on-premises region:

Hosted Zone: `apac.hr.example.com`, `10.0.0.40`

The apac name server can delegate the subdomain to other name servers.

```
$TTL    86400 ; 24 hours
$ORIGIN apac.hr.example.com
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @

test.apac.hr.example.com IN A 5.6.7.8
engineering.apac.hr.example.com IN NS ns1.engineering.apac.hr.example.com
sales.apac.hr.example.com IN NS ns2.sales.apac.hr.example.com
ns1.engineering.apac.hr.example.com IN A 10.0.0.80
ns2.sales.apac.hr.example.com IN A 10.0.0.90
```

Hosted Zone: `engineering.apac.hr.example.com`,
`10.0.0.80`

```
$TTL 86400 ; 24 hours
$ORIGIN engineering.apac.hr.example.com
@ 1D IN SOA @ root (20200322001 3H 15 1w 3h)
@ 1D IN NS @
test.engineering.apac.hr.example.com IN A 1.1.1.1
```

4. For the on-premises name server in the North America on-premises region:

Hosted Zone: `na.hr.example.net` NS IP: `10.0.0.50`

```
$TTL    86400 ; 24 hours
$ORIGIN na.hr.example.net
@  1D  IN     SOA @    root (20200322001 3H 15 1w 3h)
@  1D  IN  NS @
ns3.na.hr.example.net. IN A 10.0.0.50
test.na.hr.example.com  IN A 9.10.11.12
```

###### Route 53 Resolver setup

- For the Route 53 Resolver you need to set up forward rules and delegation rules:

**Forward rules**

    1. For forwarding the initial request so the queries will be forwarded to the parent hosted zone
     `hr.example.com` in the central location:


    domain-name: `hr.example.com` target-ips:
     `10.0.0.20`
    2. For forwarding the out-of-zone delegation record, so the Route 53 Resolver knows the IP address of the delegated
     name server to forward the initial request:


    domain-name: `hr.example.net` target-ips:
     `10.0.0.50`

**Delegation rules**

    1. Delegation rule for in-zone delegation:


    delegation record: `hr.example.com`
    2. Delegation Rule for out-of zone delegation:


    delegation-record: `hr.example.net`
