# Assign

authorization policies to users and groups within an Amazon SageMaker Unified Studio domain unit

In Amazon SageMaker Unified Studio, domain units enable you to organize your assets and other domain
entities under specific business units and teams. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

In an Amazon SageMaker Unified Studio domain unit, you can assign the following authorization policies to
your users and groups to grant them various authorization permissions within this domain
unit:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy
  To assign authorization policies to users and groups within a domain unit, complete
  the following procedure:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your administrator and log in
   using your SSO or AWS credentials.
2. Choose **Govern**.
3. Choose **Domain units**.
4. Navigate to the **Domain units** tab and choose the domain
   unit that you want to add an authorization policy grant in.
5. On the domain unit details page, choose the authorization policy that you want
   to assign to users or groups to.
6. Choose **Add policy grant**.
7. In the **Add users** pop up window, do one of the
   following:
   - Choose **Select users and groups**, specify users and
     groups to which you want to assign the selected authorization policy,
     and then choose **Add policy grant**.
   - Choose **All users** and then choose **Add
     policy grant**.

8. You can also enable or disable the cascade permissions of the selected
   authorization policy for the selected users. To do so, select the user(s) for
   which you want to enable the cascade permissions, then expand
   **Actions**, and then choose **Set cascade
   permissions to true**. The selected users will have permissions
   granted by this policy in all child domain units under this domain unit. Or you
   can choose the user(s) for which you want to disable the cascade permissions,
   then expand **Actions**, and set **Set cascade
   permissions to false**.
   To view examples of project membership policies in domain unit hierarchies, see [Project membership policy in the hierarchy of domain units in Amazon
   DataZone](../../../datazone/latest/userguide/projectmembershippolicy.md "../../../datazone/latest/userguide/projectmembershippolicy.md") in the Amazon Amazon DataZone User Guide.
