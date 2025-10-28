# Step 5: Add a template constraint to limit instance size

Constraints add another layer of control over products at the portfolio level. Constraints
can control the launch context of a product (launch constraints), or add rules to the AWS CloudFormation
template (template constraints). For more information, see [Using AWS Service Catalog Constraints](constraints.md "constraints.md").

Add a template constraint to the Linux Desktop product that prevents users from selecting
large instance types at launch time. The development-environment template allows the user to
select from six instance types; this constraint limits valid instance types to the two smallest
types, `t2.micro` and `t2.small`. For more information, see [T2 Instances](../../../AWSEC2/latest/UserGuide/t2-instances.md "../../../AWSEC2/latest/UserGuide/t2-instances.md") in the
_Amazon EC2 User Guide_.

###### To add a template constraint to the Linux Desktop product

1. On the **Portfolio details** page, choose **Constraints**, then choose **Create
   constraint**.
2. In the **Create constraint** page, for **Product,** choose **Linux Desktop**.
   Then, for **Constraint type**, choose **Template**.
3. In the T**emplate constraint** section, choose **Text editor**.
4. Paste the following into the text editor:

```
{
  "Rules": {
    "Rule1": {
      "Assertions": [
        {
          "Assert" : {"Fn::Contains": [["t2.micro", "t2.small"], {"Ref": "InstanceType"}]},
          "AssertDescription": "Instance type should be t2.micro or t2.small"
        }
      ]
    }
  }
}
```

5. For **Constraint description**, enter `Small instance
sizes`.
6. Choose **Create**.
