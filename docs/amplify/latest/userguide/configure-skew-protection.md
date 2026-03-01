# Configuring deployment skew protection for an Amplify application

You can add or remove deployment skew protection for an application using the Amplify
console, the AWS Command Line Interface, or the SDKs. The feature is applied at the branch level. Only new
deployments, that are made after skew protection is enabled for a branch, will be skew
protected.

To add or remove deployment skew protection using the AWS CLI or SDKs, use the
`CreateBranch.enableSkewProtection` and
`UpdateBranch.enableSkewProtection` fields. For more information, see [CreateBranch](../APIReference/API_CreateBranch.md "../APIReference/API_CreateBranch.md") and [UpdateBranch](../APIReference/API_UpdateBranch.md "../APIReference/API_UpdateBranch.md") in the
_Amplify API reference_ documentation.

If you want to remove a specific deployment so that it no longer gets served, use the
`DeleteJob` API. For more information, see [DeleteJob](../APIReference/API_DeleteJob.md "../APIReference/API_DeleteJob.md") in the
_Amplify API reference_ documentation.

At this time, you can only enable skew protection on an application that is already
deployed to Amplify Hosting. Use the following instructions to add skew protection to a
branch using the Amplify console.

###### Enable skew protection for branch of an Amplify application

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose the name of the deployed app to
   enable skew protection on.
3. In the navigation pane, choose **App settings**, then choose
   **Branch settings**.
4. In the **Branches** section, choose the name of the branch to
   update.
5. On the **Actions** menu, choose **Enable skew
   protection**.
6. In the confirmation window, choose **Confirm**. Skew protection is
   now enabled for the branch.
7. Redeploy your application branch. Only deployments that are made after skew protection
   is enabled are skew protected.
   Use the following instructions to remove skew protection from a branch of an application
   using the Amplify console.

###### Remove skew protection from a branch of an Amplify application

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. On the **All apps** page, choose the name of the deployed app to
   remove skew protection from.
3. In the navigation pane, choose **App settings**, then choose
   **Branch settings**.
4. In the **Branches** section, choose the name of the branch to
   update.
5. On the **Actions** menu, choose **Disable skew
   protection**. Skew protection is now disabled for the branch and only the
   latest content will be served.
