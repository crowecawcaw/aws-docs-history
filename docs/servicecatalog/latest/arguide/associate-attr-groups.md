# Associating and disassociating attribute groups

This topic describes how to associate and disassociate attribute groups
in AppRegistry.

###### Topic

- [Associate attribute groups to a new application](#w60aab9b9c19b7 "#w60aab9b9c19b7")
- [Associate attribute groups to an existing application from the Applications screen](#w60aab9b9c19b9 "#w60aab9b9c19b9")
- [Associate attribute groups to an existing application from the Attribute groups screen](#w60aab9b9c19c11 "#w60aab9b9c19c11")
- [Disassociate attribute groups from an existing application](#w60aab9b9c19c13 "#w60aab9b9c19c13")

## Associate attribute groups to a new application

The following procedure describes how to associate attribute groups
to a new application.

###### To associate attribute groups to a new application

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose **Create application**.
4. Under **Application name and description**,
   enter a name
   for your application.
   You can optionally enter a description
   for your application.
5. Under **Attribute groups**,
   select one or more attribute groups
   from the dropdown menu
   to associate
   to your application.
6. Choose **Create application**.

## Associate attribute groups to an existing application from the Applications screen

The following procedure describes how to associate attribute groups
to an existing application
from the **Applications** screen.

###### To associate attribute groups to an existing application from the Applications screen

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose the name
   of the application
   that you want
   to associate an attribute group
   to.
   Or select the application
   that you want
   to associate an attribute group
   to,
   and then choose **View**.
   You're directed to the **Application details** screen.
4. Choose **Attribute groups**,
   and then choose **Associate attribute group**.
5. Under **Attribute groups**,
   select an attribute group
   from the dropdown menu
   to associate
   to your application,
   and then choose **Save changes**.

## Associate attribute groups to an existing application from the Attribute groups screen

The following procedure describes how to associate an attribute group
to an existing application
from the **Attribute groups** screen.

###### To associate attribute groups to an existing application from the Attribute groups screen

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Attribute groups**.
   You're directed
   to the **Attribute groups** screen.
3. On **Attribute groups**,
   choose **Create Attribute group**.
4. Under **New attribute group**,
   enter a name and description
   for your attribute group,
   and provide the JSON schema
   that captures your metadata taxonomy.

**Example: attribute group metadata**

```
{
 "Team" : "WebTeam",
 "Department": "10006",
 "ParentDept": "Research",
 "ContactAlias": "research@team.com"
}
```

5. Under **Assign attribute group to an application**,
   select one or more applications
   to associate
   to your attribute group.
6. Choose **Create attribute group**.

## Disassociate attribute groups from an existing application

The following procedure describes how to disassociate an attribute group
from an existing application.

###### To disassociate attribute groups from an existing application

1. Open the AWS Service Catalog console
   at [https://console.aws.amazon.com/servicecatalog/](https://console.aws.amazon.com/servicecatalog/ "https://console.aws.amazon.com/servicecatalog/")
2. From the navigation pane,
   choose **AppRegistry**,
   and then choose **Applications**.
   You're directed
   to the **Applications** screen.
3. On **Applications**,
   choose the name
   of the application
   that you want
   to disassociate an attribute group
   from.
   Or select the application
   that you want
   to disassociate an attribute group
   from,
   and then choose **View**.
   You're directed
   to the **Application details** screen.
4. Choose **Attribute groups**,
   and then select the attribute group
   that you want
   to disassociate
   from your application.
5. Choose **Disassociate**,
   confirm your disassociation,
   and then choose **Save changes**.
