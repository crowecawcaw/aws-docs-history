

# Use tags to manage access to purchase orders
<a name="manage-access-to-purchase-orders-with-tags"></a>

You can use attribute-based access control (ABAC) to manage access to your purchase orders. When you create your purchase orders, you can tags with key-value pairs. You can then create IAM policies and specify the tags. For example, if you add the `project` key and assign it a value of `test`, your IAM policies can explicitly allow or deny access to any purchase order that has this tag.

To add tags to new purchase orders or update existing ones, see [Adding a purchase order](adding-po.md) and [Editing your purchase orders](edit-po.md).

**Example: Use tags to allow access**  
The following policy allows the IAM entity to add, modify, or tag purchase orders that have the `project` key and a value of `test`.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "purchase-orders:AddPurchaseOrder",
            "purchase-orders:TagResource",
            "purchase-orders:ModifyPurchaseOrders"
        ],
        "Resource": "arn:aws:purchase-orders::*:purchase-order/*",
        "Condition": {
            "StringEquals": {
                "aws:RequestTag/project": "test"
            },
            "ForAllValues:StringEquals": {
                "aws:TagKeys": "project"
            }
        }
    }]
}
```

**Example: Use tags to deny access**  
The following policy denies the IAM entity from completing any purchase order action on purchase orders that have the `project` key and a value of `test`.    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
        "Effect": "Deny",
        "Action": "purchase-orders:*",
        "Resource": "arn:aws:purchase-orders::*:purchase-order/*"
        }]
    }
```

For more information, see the following topics in the *IAM User Guide*:
+ [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
+ [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)