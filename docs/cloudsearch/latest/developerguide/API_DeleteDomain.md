# DeleteDomain

## Description

Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information,
see [Deleting a Search Domain](deleting-domains.md "deleting-domains.md") in the _Amazon CloudSearch Developer Guide_.

## Request Parameters

For information about the common parameters that all actions use, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**DomainName**

The name of the domain you want to permanently delete.

Type:
String

Length constraints:

Minimum length of 3.

Maximum length of 28.

Required: Yes

## Response Elements

The following
element is
returned in a structure named `DeleteDomainResult`.

**DomainStatus**

The current status of the search domain.

Type:
[DomainStatus](API_DomainStatus.md "API_DomainStatus.md")

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**Base**

An error occurred while processing the request.

HTTP Status Code: 400

**Internal**

An internal error occurred while processing the request. If this problem persists,
report an issue from the [Service Health Dashboard](http://status.aws.amazon.com/ "http://status.aws.amazon.com/").

HTTP Status Code: 500
