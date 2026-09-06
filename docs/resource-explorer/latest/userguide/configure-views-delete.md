

# Deleting views in Resource Explorer
<a name="configure-views-delete"></a>

When you no longer need an AWS Resource Explorer view, you can delete it. You can delete views by using the AWS Management Console or by running AWS CLI commands or their equivalent API operations in an AWS SDK.

**Note**  
You can't delete a view that is currently designated as the default for its AWS Region. To delete the view, you must remove the view as the default. To do this, you can run the [DisassociateDefaultView](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_DisassociateDefaultView.html) API operation in that Region.

**Minimum permissions**  
To run this procedure, you must have the following permissions:
+ **Action:** `resource-explorer-2:DeleteView`

  **Resource:** The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the view to delete

------
#### [ AWS Management Console ]

**To delete a view**

1. On the Resource Explorer console **[Views](https://console.aws.amazon.com/resource-explorer/home#/views)** page, choose the option button next to the view that you want to delete.

1. Choose **Actions**, and then choose **Delete**.

1. In the confirmation dialog box, type the name of the view, and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a view**  
Run the following command to delete the view with the specified Amazon Resource Name (ARN).

```
$ aws resource-explorer-2 delete-view \
    --view-arn arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyViewName/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111
{
    "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/MyViewName/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111"
}
```

------