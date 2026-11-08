

# Use `DeleteConfigurationSet` with an AWS SDK
<a name="sesv2_example_sesv2_DeleteConfigurationSet_section"></a>

The following code example shows how to use `DeleteConfigurationSet`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Search and filter SES resources](sesv2_example_sesv2_SearchFilterBasics_section.md) 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sesv2/search_filter_scenario#code-examples). 
Delete a configuration set that was created by the Amazon SES API v2 search-and-filter scenario.  

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


    def delete_configuration_set(self, configuration_set_name: str) -> None:
        """
        Deletes a configuration set.

        :param configuration_set_name: The name of the configuration set to
            delete.
        """
        try:
            self.sesv2_client.delete_configuration_set(
                ConfigurationSetName=configuration_set_name
            )
            logger.info("Deleted configuration set '%s'.", configuration_set_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "NotFoundException":
                logger.warning(
                    "Configuration set '%s' not found. Skipping deletion.",
                    configuration_set_name,
                )
            else:
                logger.error(
                    "Error deleting configuration set '%s': %s",
                    configuration_set_name,
                    err.response["Error"]["Message"],
                )
                raise
```
+  For API details, see [DeleteConfigurationSet](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteConfigurationSet) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using Amazon SES with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.