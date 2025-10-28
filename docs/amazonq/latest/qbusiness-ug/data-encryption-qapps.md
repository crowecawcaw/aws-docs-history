# Data encryption for Q Apps

Q Apps stores the following data:

- Title and description of the Q Apps.
- Titles of the individual cards.
- Prompts the builders may specify for the “Text output” cards.
- Any files uploaded as default values for “File upload” cards.
- The data that users put into the “Text input” cards when running the Q Apps.
- Any files uploaded by users when running the Q Apps.
  When you create a Amazon Q Business "application" as the application environment for Q Apps
  after April 30th 2024, Q Apps will be enabled out of the box. If a customer managed key is
  not configured, then Q Apps encrypts all the above data using AWS-owned keys. For more
  information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the
  _AWS Key Management Service Developer Guide_.

###### Note

If you configure a customer managed key when creating an Amazon Q Business
application environment, then Q Apps uses the same customer managed key to encrypt all of the above
data in Q Apps as well.

Q Apps requires a grant to use your customer managed key. When you create an Amazon Q Business application environment resource encrypted with a customer managed key, Q Apps,
creates a grant on your behalf by sending a `CreateGrant` request to AWS KMS.
Grants in AWS KMS are used to give Q Apps, access to a KMS key in a customer
account.

Q Apps requires the grant to use your customer managed key for the following internal
operations:

- Send `DescribeKey` requests to AWS KMS to verify that the symmetric
  customer managed key ID entered when creating application environment is valid.
- Send `GenerateDataKeyWithoutPlainText` requests to AWS KMS to generate
  data keys encrypted by your customer managed key.
- Send `Decrypt` requests to AWS KMS to decrypt the encrypted data keys so
  that they can be used to encrypt your data.
  You can revoke access to the grant, or remove the service's access to the customer managed
  key at any time. If you do, Q Apps won't be able to access any of the data encrypted by the
  customer managed key, which affects operations that are dependent on that data.

###### Note

Q Apps has a different service principal and Q Apps creates a different grant from the
grant created for "Amazon Q Business". You can specifically revoke access to the grant
for "Q Apps" without revoking access to the grant for "Amazon Q Business" or vice
versa.

**Enabling Q Apps on Q applications created before April 30th
2024**

If you have already configured a Amazon Q Business application environment to use a customer managed
key, when you enable Q Apps feature in the web experience for the first time, under the
global controls, a new grant shall be created to the same customer managed key specified when
configuring data encryption Amazon Q Business.

Note that disabling Q Apps in the web experience will not automatically revoke this grant
because administrators can still list and delete Q Apps in the admin console, even though
Q Apps web experience is disabled. But if you delete the Amazon Q Business
application environment altogether, then both grants to `qbusiness` and `qapps`
shall be revoked.

You can always revoke access to both the grants or remove access to the customer managed
key at any time.
