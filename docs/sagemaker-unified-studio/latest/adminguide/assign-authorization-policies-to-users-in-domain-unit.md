

# Assign authorization policies to users and groups within an Amazon SageMaker Unified Studio domain unit
<a name="assign-authorization-policies-to-users-in-domain-unit"></a>

In an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to your users and groups to grant them various authorization permissions within this domain unit:
+ Domain unit creation policy
+ Project creation policy
+ Project membership policy
+ Domain unit ownership assumption policy
+ Project ownership assumption policy

To assign authorization policies to users and groups within a domain unit, complete the following procedure:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your administrator and log in using your SSO or AWS credentials. 

1. In the left navigation pane, choose **Manage**, then under **Govern**, choose **Domain units**.

1. Choose the domain unit that you want to add an authorization policy grant in.

1. On the domain unit details page, choose the authorization policy that you want to assign to users or groups.

1. Choose **Add users and groups**.

1. In the **Add users and groups** window, do one of the following:
   + Choose **Select users and groups**, specify the users and groups, then choose **Add grant**.
   + Choose **All users**, then choose **Add grant**.

1. You can enable or disable cascade permissions for the selected users. When you add users and groups, select the **Apply to child domain units** checkbox. You can also enable it in the **Authorized users and groups** table by setting the dropdown in the **Cascade permissions** column to **True**. The selected users then have the permissions granted by this policy in all child domain units under this domain unit. To turn it off, set the dropdown in the **Cascade permissions** column to **False**.

To view examples of project membership policies in domain unit hierarchies, see [Project membership policy in the hierarchy of domain units in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/projectmembershippolicy.html) in the Amazon Amazon DataZone User Guide.