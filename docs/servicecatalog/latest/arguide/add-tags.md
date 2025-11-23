# Managing tags

Tags act as metadata to organize application resources.
You create tags using key-value pairs.
You add tags to applications and attribute groups, so you can group them by environment, owner, purpose, or other criteria.

###### Note

The tags discussed in this section are **not** the same as the [the `awsApplication` tag](overview-appreg.md#ar-user-tags "overview-appreg.md#ar-user-tags").
The `awsApplication` tag is a tag AppRegistry vends on your behalf when you create an application, and AWS automatically applies it
to all resources in the application.

###### Topics

- [Adding and deleting tags in a new application](#w2aab9c13b9 "#w2aab9c13b9")
- [Adding and deleting tags from the Application details screen](#w2aab9c13c11 "#w2aab9c13c11")
- [Adding and deleting tags in a new attribute group](#w2aab9c13c13 "#w2aab9c13c13")
- [Adding and deleting tags from Attribute group details](#w2aab9c13c15 "#w2aab9c13c15")

##

Adding and deleting tags in a new application

The following procedure describes how to add and delete tags
in a new application.
For information
about creating a new application,
see [Creating applications](create-apps.md "create-apps.md").

###### To add and delete tags in a new application

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen
   where you can view all
   of your applications.
3. On **Applications**,
   choose **Create application**.
4. Under **Application name and description**,
   enter a name
   for your application.
   You can optionally enter a description
   for your application.
5. Under **Application tags**,
   choose **Add tag**,
   and then enter a Key/Value pair.
   1. To add another tag,
      choose **Add another**,
      and then enter a new key/value pair.
      You can create
      up
      to 50 tags
      for an application.
   2. To delete a tag,
      choose **Remove**
      next
      to the tag
      that you want
      to delete.

6. Complete your configuration,
   and then choose **Create application**.

###### Note

AppRegistry creates and adds tags
that begin
with `aws`,
such as `aws:servicecatalog:applicationName`.
These are considered internal tags
and can't be removed.

##

Adding and deleting tags from the Application details screen

The following procedure describes how to add and delete tags
from the **Application details** screen.
For more information
about using application details,
see [Using application details](access-app-details.md "access-app-details.md").

###### To add and delete tags from Application details

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen
   where you can view all
   of your applications.
3. On **Applications**,
   choose the name
   of the application
   that you want
   to create a tag
   for.
   Or select the application
   that you want
   to create a tag
   for,
   and choose **View**.
   You're directed
   to the **Application details** screen.
4. On **Application details**,
   choose **Tags**.
5. Under **Add tags specific to this application**,
   enter a key/value pair,
   and then choose **Add tag**.
   1. To add another tag,
      enter a new key/value pair,
      and then choose **Add tag** again.
      You can create
      up
      to 50 tags
      for an application.
   2. To delete a tag,
      under **Application specific tags**,
      select the key/value pair
      that you want
      to remove,
      and then choose **Delete tag**.

##

Adding and deleting tags in a new attribute group

The following procedure describes how to add and delete
in a new attribute group.
For information
about creating a new attribute group,
see [Creating attribute groups](create-attr-groups.md "create-attr-groups.md").

###### To add and delete tags in a new attribute group

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Attribute groups**.
   You're directed
   to the **Attribute groups** screen.
3. On **Attribute groups**,
   choose **Create attribute group**.
4. Under **New attribute group**,
   enter a name and description
   for your attribute group,
   and and provide the JSON schema that captures your metadata taxonomy.
5. Under **Add tags**,
   enter a key/value pair
   to assign metadata
   to your attribute group.
   1. To add another tag,
      choose **Add new item**,
      and then enter new key/value pair.
      You can create
      up
      to 50 tags
      for an attribute group.
   2. To delete a tag,
      choose **Remove**
      next
      to the tag
      that you want to delete.

6. Complete your configuration,
   and then choose **Create attribute group**.

###### Note

AppRegistry creates and adds tags
that begin
with `aws`,
such as `aws:servicecatalog:attributeGroupName` .
These are considered internal tags
and can't be removed.

##

Adding and deleting tags from Attribute group details

The following procedure describes how to add and delete tags
from the **Attribute group details** screen.
For more information
about using attribute group details,
see [Using attribute group details](access-attr-group-details.md "access-attr-group-details.md").

###### To add and delete tags from Attribute group details

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Attribute groups**.
   You're directed
   to the **Attribute groups** screen
   where you can view all
   of your attribute groups.
3. On **Attribute groups**,
   choose the name
   of the attribute group
   that you want
   to create a tag
   for.
   Or select the attribute group
   that you want
   to create a tag
   for,
   and choose **View**.
   You're directed
   to the **Attribute groups details** screen.
4. On **Attribute group details**,
   choose **Tags**.
5. Under **Add tags specific to this attribute group**,
   enter a key/value pair, and then choose **Add tag**.
   1. To add another tag,
      enter a new key/value pair,
      and then choose **Add tag** again.
      You can create
      up
      to 50 tags
      for an attribute group.
   2. To delete a tag,
      under **Attribute group specific tags**,
      select the key/value pair
      that you want
      to remove,
      and then choose **Delete tag**.
