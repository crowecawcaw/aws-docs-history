

# Use `ListTenants` with an AWS SDK
<a name="sesv2_example_sesv2_ListTenants_section"></a>

The following code example shows how to use `ListTenants`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Search and filter SES resources](sesv2_example_sesv2_SearchFilterBasics_section.md) 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sesv2/search_filter_scenario#code-examples). 
Filter tenants by name using the Amazon SES API v2 filter support.  

```
class SearchFilterWrapper:
    """Encapsulates Amazon SES v2 search-and-filter operations."""

    def __init__(self, sesv2_client: boto3.client):
        """
        Initializes the SearchFilterWrapper with an Amazon SES v2 client.

        :param sesv2_client: A Boto3 Amazon SES v2 client.
        """
        self.sesv2_client = sesv2_client

    @classmethod
    def from_client(cls) -> "SearchFilterWrapper":
        """
        Creates a SearchFilterWrapper instance with a default Boto3 SES v2 client.

        :return: An initialized SearchFilterWrapper instance.
        """
        sesv2_client = boto3.client("sesv2")
        return cls(sesv2_client)


    def list_tenants(
        self,
        filter_params: Optional[Dict[str, str]] = None,
        page_size: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Lists tenants associated with the account. Supports optional filter
        parameters and pagination.

        :param filter_params: Optional dictionary of filter key-value pairs
            (e.g., {"TENANT_NAME_CONTAINS": "customer"}).
        :param page_size: Optional number of results per page.
        :return: A list of tenant info dictionaries.
        """
        try:
            # Pagination is handled manually using the NextToken field to keep
            # the three list methods consistent. The sibling list operations
            # (configuration sets, email identities) have no registered Boto3
            # paginator, so the same manual approach is used here.
            tenants = list()
            next_token = None
            while True:
                kwargs = dict()
                if filter_params is not None:
                    kwargs["Filter"] = filter_params
                if page_size is not None:
                    kwargs["PageSize"] = page_size
                if next_token is not None:
                    kwargs["NextToken"] = next_token

                response = self.sesv2_client.list_tenants(**kwargs)
                tenants.extend(response.get("Tenants", list()))
                next_token = response.get("NextToken")
                if not next_token:
                    break
            logger.info("Listed %d tenants.", len(tenants))
            return tenants
        except ClientError as err:
            if err.response["Error"]["Code"] == "TooManyRequestsException":
                logger.error(
                    "Too many requests when listing tenants: %s",
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error listing tenants: %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListTenants](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListTenants) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon SES with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.