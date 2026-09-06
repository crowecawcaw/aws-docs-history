

# Assign authorization policies to projects within an Amazon SageMaker Unified Studio domain unit
<a name="assign-authorization-policies-to-projects-in-domain-unit"></a>

In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain entities under specific business units and teams. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md). 

In an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to your projects to grant these entities various authorization permissions within this domain unit:
+ Glossary creation policy
+ Metadata forms creation policy
+ Custom asset type creation policy

To assign authorization policies to projects within a domain unit, complete the following procedure:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your administrator and log in using your SSO or AWS credentials. 

1. In the left navigation pane, choose **Manage**, then under **Domain management**, choose **Domain units**.

1. Choose the domain unit that you want to add an authorization policy grant in.

1. On the domain unit details page, choose the authorization policy that you want to assign to projects and then choose **Add project**.

1. Choose **Add policy grant**.

1. In the **Add projects** pop up window, do one of the following:
   + Choose **Selected projects in a domain unit**, specify projects to which you want to assign the selected authorization policy, and then choose **Add policy grant**.
   + Choose **All projects in a domain unit** and then choose **Add policy grant**.