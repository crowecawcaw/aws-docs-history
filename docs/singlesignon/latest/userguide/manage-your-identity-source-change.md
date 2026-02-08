# Change your identity source

The following procedure describes how to change from a directory that IAM Identity Center provides (the
default Identity Center directory) to Active Directory or an external identity provider, or the
other way around. Before you proceed, review the information in [Considerations for changing
your identity source](manage-your-identity-source-considerations.md "manage-your-identity-source-considerations.md"). To complete this procedure, you'll need an Organization instance of IAM Identity Center.
For more information, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").

###### Warning

Depending on your current deployment, this change removes any user and group assignments
that you configured in IAM Identity Center. This change will also remove permission set IAM roles from
your AWS accounts. As a result, you may need to update your resource policies, and should
ensure this will not disrupt your access to AWS KMS keys and Amazon EKS clusters. To learn more, see
[Referencing permission sets in resource
policies, Amazon EKS Cluster config maps, and AWS KMS key policies](referencingpermissionsets.md "referencingpermissionsets.md").

When this occurs, all users and groups, including the administrative user in IAM Identity Center, will
lose single sign-on access to their AWS accounts and applications.

###### To change your identity source

1. Open the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab. Choose **Actions**, and then choose
   **Change identity source**.
4. Under **Choose identity source**, select the source that you want to
   change to, and then choose **Next**.

If you are changing to Active Directory, choose the available directory from the menu on
the next page.

###### Important

Changing your identity source to or from Active Directory deletes users and groups
from the Identity Center directory. This change also removes any assignments that you
configured in IAM Identity Center.

###### Note

If you replicated IAM Identity Center to additional Regions, you won’t be able to change your identity source type. You can only replace the current external IdP
with another one. To change the identity source type, you will need to remove all additional Regions first. For more information,
see [Using IAM Identity Center across multiple
AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md")

If you are switching to an external identity provider, we recommend that you follow the
steps in [How to connect to an external identity provider](how-to-connect-idp.md "how-to-connect-idp.md"). 5. After you read the disclaimer and are ready to proceed, type
**ACCEPT**. 6. Choose **Change identity source**. If you are changing your identity
source to Active Directory, proceed to the next step. 7. Changing your identity source to Active Directory takes you to the
**Settings** page. On the **Settings** page, do either
of the following:

    * Choose **Start guided setup**. For information about how to
     complete the guided setup process, see [Guided setup](manage-sync-configurable-ADsync.md#manage-sync-guided-setup-configurable-ADsync "manage-sync-configurable-ADsync.md#manage-sync-guided-setup-configurable-ADsync").
    * In the **Identity source** section, choose
     **Actions**, and then choose **Manage sync** to
     configure your *sync scope*, the list of users and groups to
     sync.
