

# Use `ListOrganizationalUnitsForParent` with an AWS SDK or CLI
<a name="example_organizations_ListOrganizationalUnitsForParent_section"></a>

The following code examples show how to use `ListOrganizationalUnitsForParent`.

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples). 

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Lists the AWS Organizations organizational units that belong to an
    /// organization.
    /// </summary>
    public class ListOrganizationalUnitsForParent
    {
        /// <summary>
        /// Initializes the Organizations client object and then uses it to
        /// call the ListOrganizationalUnitsForParentAsync method to retrieve
        /// the list of organizational units.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var parentId = "r-0000";

            var request = new ListOrganizationalUnitsForParentRequest
            {
                ParentId = parentId,
                MaxResults = 5,
            };

            var response = new ListOrganizationalUnitsForParentResponse();
            try
            {
                do
                {
                    response = await client.ListOrganizationalUnitsForParentAsync(request);
                    response.OrganizationalUnits.ForEach(u => DisplayOrganizationalUnit(u));
                    if (response.NextToken is not null)
                    {
                        request.NextToken = response.NextToken;
                    }
                }
                while (response.NextToken is not null);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }

        /// <summary>
        /// Displays information about an Organizations organizational unit.
        /// </summary>
        /// <param name="unit">The OrganizationalUnit for which to display
        /// information.</param>
        public static void DisplayOrganizationalUnit(OrganizationalUnit unit)
        {
            string accountInfo = $"{unit.Id} {unit.Name}\t{unit.Arn}";

            Console.WriteLine(accountInfo);
        }
    }
```
+  For API details, see [ListOrganizationalUnitsForParent](https://docs.aws.amazon.com/goto/DotNetSDKV3/organizations-2016-11-28/ListOrganizationalUnitsForParent) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To retrieve a list of the OUs in a parent OU or root**  
The following example shows you how to get a list of OUs in a specified root:  

```
aws organizations list-organizational-units-for-parent --parent-id {{r-examplerootid111}}
```
The output shows that the specified root contains two OUs and shows details of each:  

```
{
        "OrganizationalUnits": [
                {
                        "Name": "AccountingDepartment",
                        "Arn": "arn:aws:organizations::o-exampleorgid:ou/r-examplerootid111/ou-examplerootid111-exampleouid111",
                        "Id": "ou-examplerootid111-exampleouid111",
                        "Path": "o-exampleorgid/r-examplerootid111/ou-examplerootid111-exampleouid111/"
                },
                {
                        "Name": "ProductionDepartment",
                        "Arn": "arn:aws:organizations::o-exampleorgid:ou/r-examplerootid111/ou-examplerootid111-exampleouid222",
                        "Id": "ou-examplerootid111-exampleouid222",
                        "Path": "o-exampleorgid/r-examplerootid111/ou-examplerootid111-exampleouid222/"
                }
        ]
}
```
+  For API details, see [ListOrganizationalUnitsForParent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-organizational-units-for-parent.html) in *AWS CLI Command Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Organizations with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.