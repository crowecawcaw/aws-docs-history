# Use `CreateOrganizationalUnit` with an AWS SDK or CLI

The following code examples show how to use `CreateOrganizationalUnit`.

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
    /// Creates a new organizational unit in AWS Organizations.
    /// </summary>
    public class CreateOrganizationalUnit
    {
        /// <summary>
        /// Initializes an Organizations client object and then uses it to call
        /// the CreateOrganizationalUnit method. If the call succeeds, it
        /// displays information about the new organizational unit.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var orgUnitName = "ProductDevelopmentUnit";

            var request = new CreateOrganizationalUnitRequest
            {
                Name = orgUnitName,
                ParentId = "r-0000",
            };

            var response = await client.CreateOrganizationalUnitAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully created organizational unit: {orgUnitName}.");
                Console.WriteLine($"Organizational unit {orgUnitName} Details");
                Console.WriteLine($"ARN: {response.OrganizationalUnit.Arn} Id: {response.OrganizationalUnit.Id}");
            }
            else
            {
                Console.WriteLine("Could not create new organizational unit.");
            }
        }
    }



```

- For API details, see
  [CreateOrganizationalUnit](../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateOrganizationalUnit.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateOrganizationalUnit.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To create an OU in a root or parent OU**

The following example shows how to create an OU that is named AccountingOU:

```
`aws organizations create-organizational-unit --parent-id `r-examplerootid111` --name `AccountingOU``

```

The output includes an organizationalUnit object with details about the new OU:

```
{
        "OrganizationalUnit": {
                "Id": "ou-examplerootid111-exampleouid111",
                "Arn": "arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111",
                "Name": "AccountingOU"
        }
}
```

- For API details, see
  [CreateOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organizational-unit.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organizational-unit.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Organizations with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
