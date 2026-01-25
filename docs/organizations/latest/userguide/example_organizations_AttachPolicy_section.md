# Use `AttachPolicy` with an AWS SDK or CLI

The following code examples show how to use `AttachPolicy`.

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
    /// Shows how to attach an AWS Organizations policy to an organization,
    /// an organizational unit, or an account.
    /// </summary>
    public class AttachPolicy
    {
        /// <summary>
        /// Initializes the Organizations client object and then calls the
        /// AttachPolicyAsync method to attach the policy to the root
        /// organization.
        /// </summary>
        public static async Task Main()
        {
            IAmazonOrganizations client = new AmazonOrganizationsClient();
            var policyId = "p-00000000";
            var targetId = "r-0000";

            var request = new AttachPolicyRequest
            {
                PolicyId = policyId,
                TargetId = targetId,
            };

            var response = await client.AttachPolicyAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully attached Policy ID {policyId} to Target ID: {targetId}.");
            }
            else
            {
                Console.WriteLine("Was not successful in attaching the policy.");
            }
        }
    }



```

- For API details, see
  [AttachPolicy](../../../goto/DotNetSDKV3/organizations-2016-11-28/AttachPolicy.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/AttachPolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To attach a policy to a root, OU, or account**

**Example 1**

The following example shows how to attach a service control policy (SCP) to an OU:

```
`aws organizations attach-policy
 --policy-id `p-examplepolicyid111`
 --target-id `ou-examplerootid111-exampleouid111``

```

**Example 2**

The following example shows how to attach a service control policy directly to an account:

```
`aws organizations attach-policy
 --policy-id `p-examplepolicyid111`
 --target-id `333333333333``

```

- For API details, see
  [AttachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/attach-policy.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/organizations#code-examples").

```
def attach_policy(policy_id, target_id, orgs_client):
    """
    Attaches a policy to a target. The target is an organization root, account, or
    organizational unit.

    :param policy_id: The ID of the policy to attach.
    :param target_id: The ID of the resources to attach the policy to.
    :param orgs_client: The Boto3 Organizations client.
    """
    try:
        orgs_client.attach_policy(PolicyId=policy_id, TargetId=target_id)
        logger.info("Attached policy %s to target %s.", policy_id, target_id)
    except ClientError:
        logger.exception(
            "Couldn't attach policy %s to target %s.", policy_id, target_id
        )
        raise




```

- For API details, see
  [AttachPolicy](../../../goto/boto3/organizations-2016-11-28/AttachPolicy.md "../../../goto/boto3/organizations-2016-11-28/AttachPolicy.md")
  in _AWS SDK for Python (Boto3) API Reference_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples").

```
    TRY.
        lo_org->attachpolicy(
          iv_policyid = iv_policy_id
          iv_targetid = iv_target_id ).
        MESSAGE 'Policy attached to target.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to attach the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgtargetnotfoundex.
        MESSAGE 'The specified target does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgduplicateplyatta00.
        MESSAGE 'The policy is already attached to the target.' TYPE 'E'.
    ENDTRY.


```

- For API details, see
  [AttachPolicy](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Organizations with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
