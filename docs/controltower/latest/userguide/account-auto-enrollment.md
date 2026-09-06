

# Move and enroll accounts with auto-enrollment
<a name="account-auto-enrollment"></a>

The account auto-enrollment feature is available for landing zones of version 3.1 and above.

If you optionally enable this feature, you can utilize the AWS Organizations APIs and console to move accounts into AWS Control Tower, without creating [*inheritance drift*](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html). The account automatically receives baseline resources and control configurations from the destination organizational unit (OU) in AWS Control Tower. This optional capability also allows you to move accounts between OUs within AWS Control Tower, without creating inheritance drift, if the two OUs have the same baseline configuration and the same controls enabled.

**To activate auto-enrollment:** You can select auto-enrollment of accounts on the landing zone **Settings** page in the AWS Control Tower console, or by calling the AWS Control Tower `CreateLandingZone` or `UpdateLandingZone` APIs, with the value of the `RemediationType` parameter set to **Inheritance Drift**.

**To enroll accounts:** After you activate auto-enrollment, move an account into a registered OU using the AWS Organizations console, the AWS Organizations `MoveAccount` API, or the AWS Control Tower console. The account automatically receives baseline resources and controls from that OU. This applies to both existing accounts and newly created accounts (which are created in the organization root by default).

**To unenroll an account:** Move the account to an OU that is not registered with AWS Control Tower, or to the root of the organization. AWS Control Tower removes all deployed baseline resources and controls automatically.

**Note**  
If the source and destination OUs in AWS Control Tower have different configurations, the account may show [Moved member account](governance-drift.md#drift-account-moved) drift.

## Prerequisites: Configure for auto-enrollment
<a name="w2aac44c24c18c15"></a>
+ You must be running AWS Control Tower landing zone version 3.1 or later.
+ Opt into the AWS Control Tower auto-enrollment capability through the landing zone **Settings** page in the console, or through the AWS Control Tower landing zone APIs, by setting the value of the `RemediationTypes` parameter to `Inheritance Drift`. When you have opted in, AWS Control Tower reacts to `move account` events for AWS Organizations, and it remediates inheritance drift for the moved accounts immediately, on your behalf.

## Required permissions
<a name="w2aac44c24c18c17"></a>

Specific roles and permissions are required for you to use the AWS Organizations `CreateAccount` API and `MoveAccount` API. For more information about using AWS Organizations with AWS Control Tower, see [AWS Control Tower and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-CTower.html).

## API usage examples
<a name="w2aac44c24c18c19"></a>

For more information and examples regarding these APIs, see [`CreateAccount`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html) and [`MoveAccount`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_MoveAccount.html) in the *AWS Organizations API Reference*.

## Considerations
<a name="w2aac44c24c18c21"></a>
+  **Enrollment timeline:** An account moved to an OU that's registered with AWS Control Tower is enrolled with an *eventual consistency* model. This process typically takes a few minutes, up to several hours, depending on the number of accounts being moved.
+  **AWS Service Catalog provisioned products:** Auto-enrollment does not create, modify, or terminate AWS Service Catalog provisioned products. If an account was previously enrolled through Account Factory and has an associated provisioned product, that provisioned product remains in the management account after the account is unenrolled. To clean up orphaned provisioned products, see [Deleting provisioned products](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-delete.html) in the *AWS Service Catalog User Guide*.