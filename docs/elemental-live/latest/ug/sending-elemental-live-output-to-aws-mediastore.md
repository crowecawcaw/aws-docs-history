# Sending

Elemental Live output to AWS Elemental MediaStore

In AWS Elemental Live , you can set up a container on AWS Elemental MediaStore as the destination for Apple HLS and DASH outputs.

This article assumes you know how to use the AWS Management Console and AWS Identity and Access Management, and that you have
access to [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

This article assumes that you or someone in your organization has created the MediaStore
container where Elemental Live will deliver the output. Make sure you have the path to this
container or containers.

## Step A: Set up Elemental Live in AWS Identity and Access Management

You must use the IAM (AWS Identity and Access Management) service to set up
Elemental Live as an AWS user (the "Elemental user") and give it permissions so that it can
communicate with MediaStore. You must do the following:

- Create a policy that contains specific permissions.
- Create the Elemental Live user in your AWS account. The user must be in the
  same AWS account as the user who is operating AWS Elemental MediaStore.
- Associate the Elemental Live user with the policy, which gives the user the
  permissions of that policy.

You perform this setup only once. You can use the same "Elemental user" every time
you want to send output to MediaStore.

###### Create a policy for Elemental Live to Make Requests to MediaStore

Elemental Live must have permissions on MediaStore. Follow this procedure to set up
these permissions:

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  On the left menu, choose **Policies**. Use the
    filters to determine if there is already a policy with a name
    similar to `ElementalAccessToMediaStore`.
3.  If the policy does not exist, choose **Create policy**. Choose the **Visual editor** tab
    and create the policy using the IAM policy generator. This generator lets you choose
    the service from a list and then choose operations from a list:

        * Service: **MediaStore**
        * **Actions**:Under **List**, choose **DescribeContainer**,
        * **Actions**: Under **Read**, choose **GetObject**, **DescribeObject**,
         **GetContainerPolicy**.
        * **Actions**: Under **Write**, choose **PutObject**.
        * **Resources**: If your organization does not have strict rules about accessing
         containers on MediaStore, you can ignore this section; you will have access to
         all containers. Otherwise, follow your internal policies to identify specific
         containers.
        * Give the group a name such as `ElementalAccessToMediaStore`.

    For detailed instructions on creating a policy, see
    [IAM User Guide Creating IAM Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

###### Create a user

Follow this procedure to create a user:

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the left menu, choose **User**. Use the filters to determine if there is already a
   user for Elemental products. The user might be called `ElementalUser`.
3. If the user does not exist or it does exist but you want to create separate users
   for each Elemental product, choose **Add User**. (Note that you may want separate users
   for separate _products_, but there is probably no
   need to create a separate user for each Elemental _node_.) Follow the prompts to add the user with this
   information:
   - Give the user a name such as `ElementalUser`.
   - For **Access type**, choose **Programmatic access**. Do not choose **Console access**.
   - In permissions, choose **Attach existing policies directly**. Attach the policy
     you created above. For example, `ElementalAccessToMediaStore`.
   - Ignore tags.

4. Create the user and choose **Close**.
5. On the left menu, choose **Users** again:
   - Choose the user name, for example, `ElementalUser`.
   - Choose the **Security** tab.
   - Choose **Create Access Key**.
   - On the **Create access** key dialog, choose to download the `.csv` file. Save the
     file in a safe place, so that you have a permanent record of the
     `Access key ID`
     and the `Secret access key`.

   The Access key ID looks like this:KIAIOSFODNNYEXAMPLE

   The Secret access key looks like this:
   94afd1f2e64d908bc90dbca0035a5b567EXAMPLE

6. Give the `Access key ID` and the `Secret access key` to the Elemental Live operator.
   Do _not_ give the username and password to the
   operator.
   This creates an AWS user with the permissions required to let Elemental Live make
   requests to MediaStore. When the Elemental Live operator sets up the output with MediaStore
   as the destination, they will enter the `Access key ID` and `Secret access key`. When the
   Elemental Live event is running, Elemental Live sends these two IDs to the AWS service,
   instead of sending the user name and password. These IDs provide authorization to AWS for
   the Elemental Live node to make requests to MediaStore.

## Step

B: Create the Elemental Live output group

To set up MediaStore as the destination in the HLS or DASH output group:

1. Obtain the endpoint for the MediaStore container where you want to send the output. For more information, see [AWS Elemental MediaStore User Guide Viewing the Details for a Container](../../../mediastore/latest/ug/containers-view-details.md "../../../mediastore/latest/ug/containers-view-details.md").

The following is an example of an endpoint:

```
https://w9710g.data.mediastore.us-west-2.amazonaws.com
```

2. In the Elemental Live event, go to the HLS or DASH output group and in
   **Output** > **HTTP Push Dialect** field,
   choose **AWS Elemental MediaStore**.
3. Complete the fields that appear: **Retry Interval**,
   **Num Retries**, **FileCache Size**,
   **Restart Delay**, **Log Uploads**.

For details on these fields, see the field tooltips. 4. In the output group > **Output** >
**Destination** field (above the HTTP Push Dialect field), enter
the destination in the format `<endpoint>/path/file/`.

For example:
`https://w9710g.data.mediastore.us-west-2.amazonaws.com/sports/curling/`,
where `https://w9710g.data.mediastore.us-west-2.amazonaws.com/` is the
endpoint for the MediaStore container and `/sports/curling/` is the name of the
MediaStore object. 5. Choose the **Lock** icon. Two more fields appear.

    * **Username/Access Key ID**: The Access key ID you
     created in IAM. For example, AKIAIOSFODNNYEXAMPL
    * **Password/Secret Access Key**: The Secret access key
     you created in IAM. For example,
     wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

Repeat the preceding steps to create a second output in this output group, if
applicable.
