

# Actions, resources, and condition keys for Amazon CloudSearch
<a name="list_cloudsearch"></a>

Amazon CloudSearch (service prefix: `cloudsearch`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/api-ref.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudsearch/cloudsearch.json) for this service.

**Topics**
+ [API operations defined by Amazon CloudSearch](#list_cloudsearch-operations)
+ [Actions defined by Amazon CloudSearch](#list_cloudsearch-actions-as-permissions)
+ [Permission-only actions for Amazon CloudSearch](#list_cloudsearch-permission-only-actions)
+ [Resource types defined by Amazon CloudSearch](#list_cloudsearch-resources-for-iam-policies)
+ [Condition keys for Amazon CloudSearch](#list_cloudsearch-policy-keys)

## API operations defined by Amazon CloudSearch
<a name="list_cloudsearch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudsearch-actions-as-permissions).




- **   BuildSuggesters  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:BuildSuggesters](#list_cloudsearch-action-BuildSuggesters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomain  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:CreateDomain](#list_cloudsearch-action-CreateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DefineAnalysisScheme  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DefineAnalysisScheme](#list_cloudsearch-action-DefineAnalysisScheme) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DefineExpression  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DefineExpression](#list_cloudsearch-action-DefineExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DefineIndexField  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DefineIndexField](#list_cloudsearch-action-DefineIndexField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DefineSuggester  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DefineSuggester](#list_cloudsearch-action-DefineSuggester) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnalysisScheme  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DeleteAnalysisScheme](#list_cloudsearch-action-DeleteAnalysisScheme) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DeleteDomain](#list_cloudsearch-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExpression  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DeleteExpression](#list_cloudsearch-action-DeleteExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndexField  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DeleteIndexField](#list_cloudsearch-action-DeleteIndexField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSuggester  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DeleteSuggester](#list_cloudsearch-action-DeleteSuggester) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAnalysisSchemes  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeAnalysisSchemes](#list_cloudsearch-action-DescribeAnalysisSchemes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAvailabilityOptions  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeAvailabilityOptions](#list_cloudsearch-action-DescribeAvailabilityOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainEndpointOptions  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeDomainEndpointOptions](#list_cloudsearch-action-DescribeDomainEndpointOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomains  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeDomains](#list_cloudsearch-action-DescribeDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeExpressions  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeExpressions](#list_cloudsearch-action-DescribeExpressions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeIndexFields  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeIndexFields](#list_cloudsearch-action-DescribeIndexFields) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScalingParameters  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeScalingParameters](#list_cloudsearch-action-DescribeScalingParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceAccessPolicies  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeServiceAccessPolicies](#list_cloudsearch-action-DescribeServiceAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSuggesters  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:DescribeSuggesters](#list_cloudsearch-action-DescribeSuggesters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   IndexDocuments  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:IndexDocuments](#list_cloudsearch-action-IndexDocuments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListDomainNames  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:ListDomainNames](#list_cloudsearch-action-ListDomainNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpdateAvailabilityOptions  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:UpdateAvailabilityOptions](#list_cloudsearch-action-UpdateAvailabilityOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomainEndpointOptions  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:UpdateDomainEndpointOptions](#list_cloudsearch-action-UpdateDomainEndpointOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScalingParameters  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:UpdateScalingParameters](#list_cloudsearch-action-UpdateScalingParameters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceAccessPolicies  **
  - **SDK client:** cloudsearch
  - **IAM action:**  [cloudsearch:UpdateServiceAccessPolicies](#list_cloudsearch-action-UpdateServiceAccessPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write



## Actions defined by Amazon CloudSearch
<a name="list_cloudsearch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTags](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AddTags.html)  **
  - **Description:** Attaches resource tags to an Amazon CloudSearch domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [BuildSuggesters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_BuildSuggesters.html)  **
  - **Description:** Indexes the search suggestions
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_CreateDomain.html)  **
  - **Description:** Creates a new search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DefineAnalysisScheme](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineAnalysisScheme.html)  **
  - **Description:** Configures an analysis scheme that can be applied to a text or text-array field to define language-specific text processing options
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DefineExpression](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineExpression.html)  **
  - **Description:** Configures an Expression for the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DefineIndexField](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineIndexField.html)  **
  - **Description:** Configures an IndexField for the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DefineSuggester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DefineSuggester.html)  **
  - **Description:** Configures a suggester for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAnalysisScheme](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteAnalysisScheme.html)  **
  - **Description:** Deletes an analysis scheme
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteDomain.html)  **
  - **Description:** Permanently deletes a search domain and all of its data
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteExpression](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteExpression.html)  **
  - **Description:** Removes an Expression from the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIndexField](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteIndexField.html)  **
  - **Description:** Removes an IndexField from the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSuggester](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DeleteSuggester.html)  **
  - **Description:** Deletes a suggester
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAnalysisSchemes](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAnalysisSchemes.html)  **
  - **Description:** Gets the analysis schemes configured for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeAvailabilityOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeAvailabilityOptions.html)  **
  - **Description:** Gets the availability options configured for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDomainEndpointOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeDomainEndpointOptions.html)  **
  - **Description:** Gets the domain endpoint options configured for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDomains](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeDomains.html)  **
  - **Description:** Gets information about the search domains owned by this account
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeExpressions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeExpressions.html)  **
  - **Description:** Gets the expressions configured for the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeIndexFields](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeIndexFields.html)  **
  - **Description:** Gets information about the index fields configured for the search domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeScalingParameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeScalingParameters.html)  **
  - **Description:** Gets the scaling parameters configured for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceAccessPolicies](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeServiceAccessPolicies.html)  **
  - **Description:** Gets information about the access policies that control access to the domain's document and search endpoints
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSuggesters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_DescribeSuggesters.html)  **
  - **Description:** Gets the suggesters configured for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [IndexDocuments](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexDocuments.html)  **
  - **Description:** Tells the search domain to start indexing its documents using the latest indexing options
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListDomainNames](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ListDomainNames.html)  **
  - **Description:** Lists all search domains owned by an account
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ListTags.html)  **
  - **Description:** Displays all of the resource tags for an Amazon CloudSearch domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [RemoveTags](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_RemoveTags.html)  **
  - **Description:** Removes the specified resource tags from an Amazon ES domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UpdateAvailabilityOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateAvailabilityOptions.html)  **
  - **Description:** Configures the availability options for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDomainEndpointOptions](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateDomainEndpointOptions.html)  **
  - **Description:** Configures the domain endpoint options for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateScalingParameters](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateScalingParameters.html)  **
  - **Description:** Configures scaling parameters for a domain
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateServiceAccessPolicies](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_UpdateServiceAccessPolicies.html)  **
  - **Description:** Configures the access rules that control access to the domain's document and search endpoints
  - **Resource types (\*required):** [domain\*](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Permission-only actions for Amazon CloudSearch
<a name="list_cloudsearch-permission-only-actions"></a>

The following actions are defined by Amazon CloudSearch but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [document](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html#cloudsearch-actions)  **
  - **Description:** Allows access to the document service operations
  - **Resource types (\*required):** [domain](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Write

- **   [search](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html#cloudsearch-actions)  **
  - **Description:** Allows access to the search operations
  - **Resource types (\*required):** [domain](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read

- **   [suggest](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html#cloudsearch-actions)  **
  - **Description:** Allows access to the suggest operations
  - **Resource types (\*required):** [domain](#list_cloudsearch-resource-domain)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon CloudSearch
<a name="list_cloudsearch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html)  | arn:${Partition}:cloudsearch:${Region}:${Account}:domain/${DomainName} |   | 

## Condition keys for Amazon CloudSearch
<a name="list_cloudsearch-policy-keys"></a>

Amazon CloudSearch has no service-specific condition keys that can be used in the `Condition` element of policy statements.