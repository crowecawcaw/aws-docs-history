

# AWS Network Security Manager quotas
<a name="quotas"></a>

Your AWS account has the following default quotas for AWS Network Security Manager. Unless otherwise noted, each quota is per account, per Region.

## Resource quotas
<a name="quotas-resources"></a>

The following table lists the maximum number of AWS Network Security Manager resources you can create per account in each Region.


| Resource | Default quota | Adjustable | 
| --- | --- | --- | 
| Rules per account | 200 | No | 
| Templates per account | 100 | No | 
| Policies per account | 100 | No | 
| Scopes per account | 100 | No | 
| Deployments per account | 100 | No | 
| Snapshots per resource | 10 | No | 

## Resource composition quotas
<a name="quotas-composition"></a>

The following table lists the quotas for how AWS Network Security Manager resources reference each other within the resource hierarchy.


| Quota | Value | 
| --- | --- | 
| Rules per template | 1 to 50 | 
| Templates per AWS WAF policy | 1 to 2 | 
| Rules and templates combined per AWS WAF policy | 1 to 100 | 
| Templates or rules per AWS Shield Advanced policy | 0 (must be empty) | 
| Policies per deployment | 1 to 2 | 
| Scopes per deployment | 1 (exactly one) | 

## Scope configuration quotas
<a name="quotas-scope"></a>

The following table lists the quotas for scope configuration expressions.


| Quota | Value | 
| --- | --- | 
| Resource type scopes per scope | 20 | 
| Scope expression depth (nested levels) | 2 | 
| Scope expression breadth (criteria per level) | 20 | 

## Administrator account quotas
<a name="quotas-admin"></a>

The following table lists the quotas for AWS Network Security Manager administrator account priority levels.


| Quota | Value | 
| --- | --- | 
| Administrator priority levels | 1 to 10 | 

## API pagination quotas
<a name="quotas-api"></a>

The following table lists the pagination limits for List operations.


| Quota | Value | 
| --- | --- | 
| Maximum results per page (maxResults) | 100 | 
| Minimum results per page (maxResults) | 1 | 

## Quota adjustability
<a name="quotas-fixed"></a>

The quotas listed in the preceding sections are fixed and cannot be increased at this time.