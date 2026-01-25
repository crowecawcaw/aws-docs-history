# Enabling organizational view

You can use the AWS Health console to get a centralized view for health events in your
AWS organization.

Organizational view is available in the AWS Health console for all AWS Support plans at no
additional cost.

###### Note

If you want to allow users access to this feature in the management account, they must
have permissions such as the [AWSHealthFullAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess") policy. For more information, see
[AWS Health identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

Enabling organizational view (Console)
You can enable organizational view from the AWS Health console. You must sign
in to the management account of your AWS organization.

###### To view the AWS Health Dashboard for your organization

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. In the navigation pane, under **Your organization
   health**, choose
   **Configurations**.
3. On the **Enable organizational view** page, choose
   **Enable organizational view**.
4. (Optional) If you want to make changes to your AWS organizations,
   such as creating organizational units (OUs), choose **Manage
   AWS Organizations**.

For more information, see [Getting started with AWS Organizations](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md") in the
_AWS Organizations User Guide_.

###### Notes

- When you enable AWS Health organizational view, the initial account loading process runs in the background and might take several minutes to complete. You can close the AWS Health console and return later, as you don't need to wait for the process to finish. Historical health events (those created before you enabled the feature) might take up to 24 hours to appear in your organizational view.
- If you have a AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan, you can call the [DescribeHealthServiceStatusForOrganization](../APIReference/API_DescribeHealthServiceStatusForOrganization.md "../APIReference/API_DescribeHealthServiceStatusForOrganization.md") API
  operation to check the status of the process.
- When you enable this feature, the
  `AWSServiceRoleForHealth_Organizations`
  service-linked role with the
  `Health_OrganizationsServiceRolePolicy` AWS managed
  policy is applied to the management account in the organization. For
  more information, see [Using service-linked roles for
  AWS Health](using-service-linked-roles.md "using-service-linked-roles.md").

Enabling organizational view (CLI)
You can enable organizational view by using the [EnableHealthServiceAccessForOrganization](../APIReference/API_EnableHealthServiceAccessForOrganization.md "../APIReference/API_EnableHealthServiceAccessForOrganization.md") API operation.

You can use the AWS Command Line Interface (AWS CLI) or your own code to call this operation.

###### Note

- You must have a [Business](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/"), [Enterprise On-Ramp](https://aws.amazon.com/premiumsupport/plans/enterprise-onramp "https://aws.amazon.com/premiumsupport/plans/enterprise-onramp"), or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise "https://aws.amazon.com/premiumsupport/plans/enterprise") Support
  plan to call the AWS Health API.
- You must use the US East (N. Virginia) Region endpoint.

The following AWS CLI command enables this feature from your AWS account.
You can use this command from the management account or from an account that
can assume the role with the required permissions.

```
aws health enable-health-service-access-for-organization --region us-east-1
```

The following code examples call the [EnableHealthServiceAccessForOrganization](../APIReference/API_EnableHealthServiceAccessForOrganization.md "../APIReference/API_EnableHealthServiceAccessForOrganization.md") API operation.

**Python**

```
import boto3

client = boto3.client('health', region_name='us-east-1')

response = client.enable_health_service_access_for_organization()

print(response)
```

**Java**

You can use the AWS SDK for version Java 2.0 for the following
example.

```
import software.amazon.awssdk.services.health.HealthClient;
import software.amazon.awssdk.services.health.HealthClientBuilder;

import software.amazon.awssdk.services.health.model.ConcurrentModificationException;
import software.amazon.awssdk.services.health.model.EnableHealthServiceAccessForOrganizationRequest;
import software.amazon.awssdk.services.health.model.EnableHealthServiceAccessForOrganizationResponse;
import software.amazon.awssdk.services.health.model.DescribeHealthServiceStatusForOrganizationRequest;
import software.amazon.awssdk.services.health.model.DescribeHealthServiceStatusForOrganizationResponse;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;

import software.amazon.awssdk.regions.Region;

public class EnableHealthServiceAccessDemo {
    public static void main(String[] args) {
        HealthClient client = HealthClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(
                DefaultCredentialsProvider.builder().build()
            )
            .build();

        try {
            DescribeHealthServiceStatusForOrganizationResponse statusResponse = client.describeHealthServiceStatusForOrganization(
                DescribeHealthServiceStatusForOrganizationRequest.builder().build()
            );

            String status = statusResponse.healthServiceAccessStatusForOrganization();
            if ("ENABLED".equals(status)) {
                System.out.println("EnableHealthServiceAccessForOrganization already enabled!");
                return;
            }

            client.enableHealthServiceAccessForOrganization(
                EnableHealthServiceAccessForOrganizationRequest.builder().build()
            );

            System.out.println("EnableHealthServiceAccessForOrganization is in progress");
        } catch (ConcurrentModificationException cme) {
            System.out.println("EnableHealthServiceAccessForOrganization is already in progress. Wait for the action to complete before trying again.");
        } catch (Exception e) {
            System.out.println("EnableHealthServiceAccessForOrganization FAILED: " + e);
        }
    }
}
```

For more information, see the [AWS SDK for Java
2.0 Developer Guide](../../../sdk-for-java/latest/developer-guide.md "../../../sdk-for-java/latest/developer-guide.md").

When you enable this feature, the
`AWSServiceRoleForHealth_Organizations`
[service-linked
role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") with the `Health_OrganizationsServiceRolePolicy`
AWS managed policy is applied to the management account in the
organization.

###### Note

Enabling this feature is an asynchronous process and takes time to
complete. You can call the [DescribeHealthServiceStatusForOrganization](../APIReference/API_DescribeHealthServiceStatusForOrganization.md "../APIReference/API_DescribeHealthServiceStatusForOrganization.md") operation to check
the status of the process.
