

# Edit access settings for a VPC Lattice service network
<a name="service-network-access"></a>

Access settings enable you to configure and manage client access to a service network. Access settings include *auth type* and *auth policies*. Auth policies help you authenticate and authorize traffic flowing to services within VPC Lattice. Access settings of the service network do not apply to the resource configurations associated to the service network.

You can apply auth policies at the service network level, the service level, or both. Typically, auth policies are applied by the network owners or cloud administrators. They can implement coarse-grained authorization, for example, allowing authenticated calls from within the organization, or allowing anonymous GET requests that match a certain condition. At the service level, service owners can apply fine-grained controls, which can be more restrictive. For more information, see [Control access to VPC Lattice services using auth policies](auth-policies.md).

**To add or update access policies using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **VPC Lattice**, choose **Service networks**.

1. Select the name of the service network to open its details page.

1. Choose the **Access** tab to check the current access settings.

1. To update the access settings, choose **Edit access settings**.

1. If you want the clients in the associated VPCs to access the services in this service network, choose **None** for **Auth type**.

1. To apply a resource policy to the service network, choose **AWS IAM** for **Auth type** and do one the following for **Auth policy**:
   + Enter a policy in the input field. For example policies that you can copy and paste, choose **Policy examples**.
   + Choose **Apply policy template** and select the **Allow authenticated and unauthenticated access** template. This template allows a client from another account to access the service either by signing the request (meaning authenticated) or anonymously (meaning unauthenticated).
   + Choose **Apply policy template** and select the **Allow only authenticated access** template. This template allows a client from another account to access the service only by signing the request (meaning authenticated).

1. Choose **Save changes**.

**To add or update an access policy using the AWS CLI**  
Use the [put-auth-policy](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/put-auth-policy.html) command.