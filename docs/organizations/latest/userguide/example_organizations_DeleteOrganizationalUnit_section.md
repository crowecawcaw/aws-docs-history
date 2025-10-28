# Use `DeleteOrganizationalUnit` with an AWS SDK or CLI

The following code examples show how to use `DeleteOrganizationalUnit`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Shows how to delete an existing AWS Organizations organizational unit.
    /// </summary>
    public class DeleteOrganizationalUnit
    {
        /// <summary>
        /// Initializes the Organizations client object and calls
        /// DeleteOrganizationalUnitAsync to delete the organizational unit
        /// with the selected ID.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var orgUnitId = "ou-0000-00000000";

            var request = new DeleteOrganizationalUnitRequest
            {
                OrganizationalUnitId = orgUnitId,
            };

            var response = await client.DeleteOrganizationalUnitAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully deleted the organizational unit with ID: {orgUnitId}.");
            }
            else
            {
                Console.WriteLine($"Could not delete the organizational unit with ID: {orgUnitId}.");
            }
        }
    }



```

- For API details, see
  [DeleteOrganizationalUnit](../../../goto/DotNetSDKV3/organizations-2016-11-28/DeleteOrganizationalUnit.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/DeleteOrganizationalUnit.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete an OU**

The following example shows how to delete an OU. The example assumes that you previously removed all accounts and other OUs from the OU:

```
`aws organizations delete-organizational-unit --organizational-unit-id `ou-examplerootid111-exampleouid111``

```

- For API details, see
  [DeleteOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Organizations with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
