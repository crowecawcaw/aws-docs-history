# LSSEC01-BP02 Maintain a history of IAM configurations and

changes over time

By logging the IAM policy that was assigned to an IAM user, group,
or role, you can determine the permissions that belonged to a user
at a specific time. For example, you can view whether a user had
permission to modify settings on a specific date in the past.

**Desired outcome:** A complete
history of IAM configurations is maintained and available for
review.

**Benefits of establishing this best
practice:** Provide the ability to view the IAM policy that
was assigned to an IAM user, group, or role over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Customize AWS Config to record configuration changes to IAM global
resources in your home Region.

### Implementation steps

1. Determine a home AWS Region where you want AWS Config to
   record and store configuration changes to IAM resources, as
   the same IAM data is available in different AWS Regions.
2. In your home region, enable recording
   by [AWS Config](../../../config/latest/developerguide/view-manage-resource.md "../../../config/latest/developerguide/view-manage-resource.md") and enable recording of global resources or
   select specific IAM resources.
3. Create a service control policy (SCP) to stop recording
   being turned off.

## Resources

**Related documents:**

- [How
  to Record and Govern Your IAM Resource Configurations Using
  AWS Config](https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/ "https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/")
