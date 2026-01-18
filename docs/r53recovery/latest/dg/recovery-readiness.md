# Creating

and updating readiness checks in ARC

This section provides procedures for readiness checks and resource sets, including creating,
updating, and deleting these resources.

## Creating and updating a readiness check

The steps in this section explain how to create a readiness check on the ARC console. To learn about using recovery readiness API operations with
Amazon Application Recovery Controller (ARC), see [Readiness check API operations](actions.md "actions.md").

To update a readiness check, you can edit the resource set for the readiness check, to add or remove resources or to change the readiness scope for a
resource.

## To create a readiness check

1.  Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2.  Choose **Readiness check**.
3.  On the **Readiness** page, choose **Create**, and then choose a
    **Readiness check**.
4.  Enter a name for your readiness check, choose the resource type that you want to check,
    and then choose **Next**.
5.  Add a resource set for your readiness check. A resource set is a group of resources of the same type
    in different replicas. Choose one of the following:

        * Create a readiness check with resources in a resource set that you've already created.
        * Create a new resource set.

    If you choose to create a new resource set, enter a name for it and choose **Add**.

6.  Copy and paste Amazon Resource Names (ARNs) one by one for each resource that you want to include in the set, and then choose
    **Next**.

###### Tip

For examples and more information about the ARN format that ARC expects for each resource type, see
[Resource types and ARN formats
in ARC](recovery-readiness.md "recovery-readiness.md"). 7. If you like, view the readiness rules that will be used when ARC checks the
type of resource you included in this readiness check. Then choose
**Next**. 8. (Optional) Under **Recovery group name**, choose a recovery group to
associate the readiness check with and then, for each resource ARN, choose a
cell (Region or Availability Zone) from the drop-down menu that the resource is in. If it's an application-level
resource, like a DNS routing policy, choose **global resource (no cell)**.

_This specifies the readiness scopes for the resources in the readiness check._

###### Important

Although this step is optional, readiness scopes must be added to get summary readiness information for your recovery group and cells. If you skip this
step and don't associate the readiness check with your recovery group's resources by choosing readiness scopes here, ARC cannot return
summary readiness information for the recovery group or cells. 9. Choose **Next**. 10. Review the information on the confirmation page, and then choose **Create readiness check**.

## To delete a readiness check

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. Choose a readiness check, and under **Actions**, choose **Delete**.

## Creating and editing resource sets

Typically, you create a resource set as part of creating a readiness check, but you can create a resource set separately as well. You can also edit a
resource set to add or remove resources. The steps in this section explain how to create or edit a resource set on the ARC console. To learn about using
recovery readiness API operations with Amazon Application Recovery Controller (ARC), see [Readiness check API operations](actions.md "actions.md").

## To create a resource set

1. Open the Route 53 console at [https://console.aws.amazon.com/route53/home](https://console.aws.amazon.com/route53/home "https://console.aws.amazon.com/route53/home").
2. Under **Application Recovery Controller**, choose **Resource sets**.
3. Choose **Create**.
4. Enter a name for the resource set, and then choose the type of resource to include in the set.
5. Choose **Add**, and then enter the Amazon Resource Name (ARN) for the resource to add to the set.
6. After you've finished adding resources, choose **Create resource set**.

## To edit a resource set

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Readiness check**.
3. Under **Resource sets**, choose **Action**, and then choose
   **Edit**.
4. Do one of the following:
   - To remove a resource from the set, choose **Remove**.
   - To add a resource to the set, choose **Add**, and then enter the Amazon Resource
     Name (ARN) for the resource.

5. You can also edit the readiness scope for the resource, to associate the resource with a different cell for the readiness check.
6. Choose **Save**.
