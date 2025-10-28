# Assign

authorization policies to users and groups within an Amazon DataZone domain unit

In Amazon DataZone, domain units enable you to organize your assets and other domain
entities under specific business units and teams. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

In an Amazon DataZone domain unit, you can assign the following authorization policies to
your users and groups to grant them various authorization permissions within this domain
unit:

- Domain unit creation policy
- Project creation policy
- Project membership policy
- Domain unit ownership assumption policy
- Project ownership assumption policy
  To assign authorization policies to users and groups within a domain unit, complete
  the following procedure:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **View domains** and choose the domain and the domain
   unit where you want to assign authorization policies.
3. On the domain unit details page, choose the authorization policy that you want
   to assign to users/groups and then choose **Add users**.
4. In the **Add users** pop up window, do one of the
   following:
   - Choose **Selected users and groups**, specify users
     and groups to which you want to assign the selected authorization
     policy, and then choose **Add users**.
   - Choose **All users** and then choose **Add
     users**.
   - Choose **All groups** and then choose **Add
     users**.

5. You can also enable or disable the cascade permissions of the selected
   authorization policy for the selected users. To do so, choose the user(s) for
   which you want to enable the cascade permissions, then expand
   **Actions**, and then choose **Set cascade
   permissions to true**. The selected users will have permissions
   granted by this policy in all child domain units under this domain unit. Or you
   can choose the user(s) for which you want to disable the cascade permissions,
   then expand **Actions**, and set **Set cascade
   permissions to false**.
