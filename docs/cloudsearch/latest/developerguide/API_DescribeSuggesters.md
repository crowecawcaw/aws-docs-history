# DescribeSuggesters

## Description

Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the `Deployed` option to `true` to show the active configuration and exclude pending changes. For more information, see [Getting Search Suggestions](getting-suggestions.md "getting-suggestions.md") in the _Amazon CloudSearch Developer Guide_.

## Request Parameters

For information about the common parameters that all actions use, see [Common Parameters](CommonParameters.md "CommonParameters.md").

**Deployed**

Whether to display the deployed configuration (`true`) or include any pending changes (`false`). Defaults to `false`.

Type:
Boolean

Required: No

**DomainName**

The name of the domain you want to describe.

Type:
String

Length constraints:

Minimum length of 3.

Maximum length of 28.

Required: Yes

**SuggesterNames.member.N**

The suggesters you want to describe.

Type:
String
list

Length constraints:

Minimum length of

1.

Maximum length of 64.

Required: No

## Response Elements

The following
element is
returned in a structure named `DescribeSuggestersResult`.

**Suggesters**

The suggesters configured for the domain specified in the request.

Type:
[SuggesterStatus](API_SuggesterStatus.md "API_SuggesterStatus.md")
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

**ResourceNotFound**

The request was rejected because it attempted to reference a resource that does not exist.

HTTP Status Code: 409
