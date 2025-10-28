# Edit access settings for a VPC Lattice service

Access settings enable you to configure and manage client access to a service.
Access settings include _auth type_ and _auth policies_. Auth policies help you authenticate
and authorize traffic flowing to services within VPC Lattice.

You can apply auth policies at the service network level, the service level, or both.
At the service level, service owners can apply fine-grained controls, which can be more
restrictive. Typically, auth policies are applied by the network owners or cloud
administrators. They can implement course-grained authorization, for example, allowing
authenticated calls from within the organization, or allowing anonymous GET requests
that match a certain condition. For more information, see [Control access to VPC Lattice services using auth policies](auth-policies.md "auth-policies.md").

###### To add or update access policies using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **VPC Lattice**, choose
   **Services**.
3. Select the name of the service to open its details page.
4. Choose the **Access** tab to check the current access settings.
5. To update the access settings, choose **Edit access settings**.
6. If you want the clients in VPCs in the associated service network to access your service,
   choose **None** for **Auth type**.
7. To apply a resource policy to control access to the service, choose
   **AWS IAM** for **Auth type** and do
   one the following for **Auth policy**:
   - Enter a policy in the input field. For example policies that you can
     copy and paste, choose **Policy examples**.
   - Choose **Apply policy template** and select the
     **Allow authenticated and unauthenticated access**
     template. This template allows a client from another account to access
     the service either by signing the request (meaning authenticated) or
     anonymously (meaning unauthenticated).
   - Choose **Apply policy template** and select the
     **Allow only authenticated access** template. This
     template allows a client from another account to access the service
     only by signing the request (meaning authenticated).

8. Choose **Save changes**.

###### To add or update an access policy using the AWS CLI

Use the [put-auth-policy](../../../cli/latest/reference/vpc-lattice/put-auth-policy.md "../../../cli/latest/reference/vpc-lattice/put-auth-policy.md") command.
