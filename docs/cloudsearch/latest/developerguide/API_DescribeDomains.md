# DescribeDomains

## Description

Gets information about the search domains owned by this account. Can be limited to specific domains. Shows
all domains by default. To get the number of searchable documents in a domain, use the console or submit a `matchall` request to your domain's search endpoint: `q=matchall&q.parser=structured&size=0`. For more information,
see [Getting Information about a Search Domain](getting-domain-info.md "getting-domain-info.md") in the _Amazon CloudSearch Developer Guide_.

## Request Parameters

For information about the common parameters that all actions use, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DomainNames.member.N**

The names of the domains you want to include in the response.

Type:
String
list

Length constraints:

Minimum length of 3.

Maximum length of 28.

Required: No

## Response Elements

The following
element is
returned in a structure named `DescribeDomainsResult`.

**DomainStatusList**

A list that contains the status of each requested domain.

Type:
[DomainStatus](API_DomainStatus.md "API_DomainStatus.md")
list

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**Base**

An error occurred while processing the request.

HTTP Status Code: 400

**Internal**

An internal error occurred while processing the request. If this problem persists,
report an issue from the [Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/").

HTTP Status Code: 500
