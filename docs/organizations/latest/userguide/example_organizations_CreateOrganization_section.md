

# Use `CreateOrganization` with an AWS SDK or CLI
<a name="example_organizations_CreateOrganization_section"></a>

The following code examples show how to use `CreateOrganization`.

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
    /// Creates an organization in AWS Organizations.
    /// </summary>
    public class CreateOrganization
    {
        /// <summary>
        /// Creates an Organizations client object and then uses it to create
        /// a new organization with the default user as the administrator, and
        /// then displays information about the new organization.
        /// </summary>
        public static async Task Main()
        {
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var response = await client.CreateOrganizationAsync(new CreateOrganizationRequest
            {
                FeatureSet = "ALL",
            });

            Organization newOrg = response.Organization;

            Console.WriteLine($"Organization: {newOrg.Id} Main Accoount: {newOrg.MasterAccountId}");
        }
    }
```
+  For API details, see [CreateOrganization](https://docs.aws.amazon.com/goto/DotNetSDKV3/organizations-2016-11-28/CreateOrganization) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To create a new organization**  
The following `create-organization` example creates an organization using credentials from Bill's account 111111111111. The account becomes the master account in the new organization. Because he does not specify a features set, the new organization defaults to all features enabled and service control policies are enabled on the root.  

```
aws organizations create-organization
```
Output:  

```
{
    "Organization": {
        "AvailablePolicyTypes": [
            {
                "Status": "ENABLED",
                "Type": "SERVICE_CONTROL_POLICY"
            }
        ],
        "MasterAccountId": "123456789012",
        "MasterAccountArn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
        "MasterAccountEmail": "bill@example.com",
        "FeatureSet": "ALL",
        "Id": "o-exampleorgid",
        "Arn": "arn:aws:organizations::123456789012:organization/o-exampleorgid"
    }
}
```
For more information, see [Creating an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations User Guide*.  
**Example 2: To create a new organization with only consolidated billing features enabled**  
The following `create-organization` example creates an organization that supports only the consolidated billing features.  

```
aws organizations create-organization \
    --feature-set {{CONSOLIDATED_BILLING}}
```
Output:  

```
{
    "Organization": {
        "Arn": "arn:aws:organizations::123456789012:organization/o-exampleorgid",
        "AvailablePolicyTypes": [],
        "Id": "o-exampleorgid",
        "MasterAccountArn": "arn:aws:organizations::123456789012:account/o-exampleorgid/123456789012",
        "MasterAccountEmail": "bill@example.com",
        "MasterAccountId": "123456789012",
        "FeatureSet": "CONSOLIDATED_BILLING"
    }
}
```
For more information, see [Creating an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) in the *AWS Organizations User Guide*.  
+  For API details, see [CreateOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html) in *AWS CLI Command Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Organizations with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.