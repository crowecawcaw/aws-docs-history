# Tag your Classic Load Balancer

Tags help you to categorize your load balancers in different ways, for example, by
purpose, owner, or environment.

You can add multiple tags to each Classic Load Balancer. Tag keys must be unique for each load
balancer. If you add a tag with a key that is already associated with the load balancer,
it updates the value of that tag.

When you are finished with a tag, you can remove it from your load balancer.

###### Contents

- [Tag restrictions](#tag-restrictions "#tag-restrictions")
- [Add a tag](#add-tags "#add-tags")
- [Remove a tag](#remove-tags "#remove-tags")

## Tag restrictions

The following basic restrictions apply to tags:

- Maximum number of tags per resource—50
- Maximum key length—127 Unicode characters
- Maximum value length—255 Unicode characters
- Tag keys and values are case sensitive. Allowed characters are letters,
  spaces, and numbers representable in UTF-8, plus the following special
  characters: + - = . \_ : / @. Do not use leading or trailing spaces.
- Do not use the `aws:` prefix in your tag names or values
  because it is reserved for AWS use. You can't edit or delete tag names or
  values with this prefix. Tags with this prefix do not count against your
  tags per resource limit.

## Add a tag

You can add tags to your load balancer at any time.

###### To add a tag using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Tags** tab, choose **Manage tags**.
5. On the **Manage tags** page, for each tag, choose
   **Add new tag** and then specify a key and a
   value.
6. After you have finished adding tags, choose
   **Save changes**.

###### To add a tag using the AWS CLI

Use the following [add-tags](../../../cli/latest/reference/elb/add-tags.md "../../../cli/latest/reference/elb/add-tags.md")
command to add the specified tag:

```
`aws elb add-tags --load-balancer-name `my-loadbalancer` --tag "Key=`project`,Value=`lima`"`
```

## Remove a tag

You can remove tags from your load balancer whenever you are finished with
them.

###### To remove a tag using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Tags** tab, choose **Manage tags**.
5. On the **Manage tags** page, choose
   **Remove** next to each tag you want to remove.
6. After you have finished removing tags, choose
   **Save changes**.

###### To remove a tag using the AWS CLI

Use the following [remove-tags](../../../cli/latest/reference/elb/remove-tags.md "../../../cli/latest/reference/elb/remove-tags.md") command to remove the tag with the specified
key:

```
`aws elb remove-tags --load-balancer-name `my-loadbalancer` --tag `project``
```
