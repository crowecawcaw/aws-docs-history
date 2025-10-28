# Creating an organizational unit (OU) with AWS Organizations

When you sign in to your organization's management account, you can create an OU in
your organization's root. OUs can be nested up to five levels deep. To create an OU,
complete the following steps.

###### Important

If this organization is managed with AWS Control Tower, then create your OUs with the
AWS Control Tower console or APIs. If you create the OU in Organizations, then that OU isn't
registered with AWS Control Tower. For more information, see [Referring to Resources Outside of AWS Control Tower](../../../controltower/latest/userguide/external-resources.md#ungoverned-resources "../../../controltower/latest/userguide/external-resources.md#ungoverned-resources") in the _AWS Control Tower
User Guide_.

###### Minimum permissions

To create an OU within a root in your organization, you must have the following
permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:CreateOrganizationalUnit`

###### To create an OU

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page.

The console displays the Root OU and its contents. The first time
you visit the Root, the console displays all of your AWS accounts
in that top-level view. If you previously created OUs and moved
accounts into them, the console shows only the top-level OUs and any
accounts that you have not yet moved into an OU. 3. (Optional) If you want to create an OU inside an existing OU,
[navigate to the child OU](navigate_tree.md "navigate_tree.md") by
choosing the name (not the check box) of the child OU, or by
choosing the
![Gray cloud icon with an arrow pointing downward, indicating download or cloud storage.](images/expand-icon.png)
next to OUs in the tree view until you see the
one you want, and then choosing its name. 4. When you've selected the correct parent OU in the hierarchy, on
the **Actions** menu, under
**Organizational Unit**, choose
**Create new** 5. In the **Create organizational unit** dialog box,
enter the name of the OU that you want to create. 6. (Optional) Add one or more tags by choosing **Add
tag** and then entering a key and an optional value.
Leaving the value blank sets it to an empty string; it isn't
`null`. You can attach up to 50 tags to an OU. 7. Finally, choose **Create organizational
unit**.
Your new OU appears inside the parent. You now can [move accounts to this OU](move_account_to_ou.md "move_account_to_ou.md") or attach
policies to it.

**To create an OU**

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
