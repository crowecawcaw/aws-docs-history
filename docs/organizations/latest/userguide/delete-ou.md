# Deleting an organizational unit (OU) with AWS Organizations

When you sign in to your organization's management account, you can delete any OUs
that you no longer need.

You must first move all accounts out of the OU and any child OUs, and then you can
delete the child OUs.

###### Minimum permissions

To delete an OU, you must have the following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:DeleteOrganizationalUnit`

###### To delete an OU

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, find the OUs that you want to delete and
   choose the check box
   ![Blue checkmark icon indicating confirmation or completion of a task.](images/checkbox-selected.png)
   next to each OU's name.
3. Choose **Actions**, and then under
   **Organizational unit**, choose
   **Delete**.
4. To confirm that you want to delete the OUs, enter the OU's name
   (if you chose to delete only one) or the word 'delete' (if you chose
   more than one), and then choose **Delete**.

AWS Organizations deletes the OUs and removes them from the list.
**To delete an OU**

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
