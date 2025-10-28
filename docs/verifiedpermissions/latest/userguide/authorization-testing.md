# Testing your authorization model

To understand the effect of Amazon Verified Permissions authorization decision when you deploy your
application, you can evaluate your policies as you develop them with the [Using the Amazon Verified Permissions test bench](test-bench.md "test-bench.md") and with HTTPS REST API requests
to Verified Permissions. The test bench is a tool in the AWS Management Console to evaluate authorization requests
and responses in your policy store.

The Verified Permissions REST API is the next step in your development as you move from a conceptual
understanding to application design. The Verified Permissions API accepts authorization requests with
[IsAuthorized](../apireference/API_IsAuthorized.md "../apireference/API_IsAuthorized.md"), [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md"), and [BatchIsAuthorized](../apireference/API_BatchIsAuthorized.md "../apireference/API_BatchIsAuthorized.md") as [signed AWS API
requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") to Regional [service endpoints](../../../general/latest/gr/verifiedpermissions.md "../../../general/latest/gr/verifiedpermissions.md"). To test
your authorization model, you can generate requests with any API client and verify that
your policies are returning authorization decisions as expected.

For example, you can test `IsAuthorized` in a sample policy store with the
following procedure.

Test bench

1. Open the Verified Permissions console at [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Create a policy
   store from the **Sample policy store** with the
   name **DigitalPetStore**.
2. Select **Test bench** in your new policy store.
3. Populate your test bench request from [IsAuthorized](../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples "../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples") in the Verified Permissions API reference. The following
   details replicate the conditions in **Example 4**
   that references the **DigitalPetStore**
   sample.
   1. Set Alice as the principal. For **Principal taking
      action**, choose
      `DigitalPetStore::User` and enter
      `Alice`.
   2. Set Alice's role as customer. Choose **Add a
      parent**, choose
      `DigitalPetStore::Role`, and enter
      Customer.
   3. Set the resource as order "1234." For **Resource
      that the principal is acting on**, choose
      `DigitalPetStore::Order` and enter
      `1234`.
   4. The `DigitalPetStore::Order` resource requires
      an `owner` attribute. Set Alice as the owner of
      the order. Choose `DigitalPetStore::User` and
      enter `Alice`
   5. Alice requested to view the order. For **Action
      that principal is taking**, choose
      `DigitalPetStore::Action::"GetOrder"`.

4. Choose **Run authorization request**. In an
   unmodified policy store, this request results in an `ALLOW`
   decision. Note the **Satisfied policy** that
   returned the decision.
5. Choose **Policies** from the left navigation bar.
   Review the static policy with the description **Customer Role - Get
   Order**.
6. Observe that Verified Permissions allowed the request because the principal was
   in a customer role and was the owner of the resource.

REST API

1. Open the Verified Permissions console at [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Create a policy
   store from the **Sample policy store** with the
   name **DigitalPetStore**.
2. Note the **Policy store ID** of your new
   policy store.
3. From [IsAuthorized](../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples "../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples") in the Verified Permissions API reference, copy the
   request body of **Example 4** that references the
   **DigitalPetStore** sample.
4. Open your API client and create a request to the Regional service
   endpoint for your policy store. Populate the headers as shown in the
   [example](../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples "../apireference/API_IsAuthorized.md#API_IsAuthorized_Examples").
5. Paste in the sample request body and change the value of
   `policyStoreId` to the policy store ID you noted
   earlier.
6. Submit the request and review the results. In a default
   **DigitalPetStore** policy store, this request returns
   an `ALLOW` decision.

You can make changes to policies, schema, and requests in your test environment to
change the outcomes and produce more complex decisions.

1. Change the request in a way that changes the decision from Verified Permissions. For example,
   change Alice's role to `Employee` or change the `owner`
   attribute of order 1234 to `Bob`.
2. Change policies in ways that affect authorization decisions. For example,
   modify the policy with the description **Customer Role - Get
   Order** to remove the condition that the `User` must be
   the owner of the `Resource` and modify the request so that
   `Bob` wants to view the order.
3. Change the schema to allow policies to make a more complex decision. Update
   the request entities so that Alice can satisfy the new requirements. For
   example, edit the schema to allow `User` to be a member of
   `ActiveUsers` or `InactiveUsers`. Update the policy so
   that only active users can view their own orders. Update the request entities so
   that Alice is an active or inactive user.
