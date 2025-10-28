# Configuring a job for Kantar watermarking

After you've established your relationship with Kantar, stored your Kantar credentials
in AWS Secrets Manager, and granted permission to AWS Elemental MediaConvert to get these credentials, set
up your MediaConvert job to encode the Kantar watermarks.

###### To set up your job to encode Kantar watermarks

1. Set up your job as usual. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
2. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose **Partner
   integrations**.
3. Enable **Kantar SNAP file watermarking**.
4. Provide values for the Kantar settings.
   1. For **Credentials secret name**, type the name of the
      Secrets Manager secret that you created to store your Kantar credentials. For
      example, `KantarCreds`.
   2. For **Kantar license ID**, type the license ID that
      Kantar provides you.
   3. For **Channel name**, type one of the channel names
      that are listed in your Kantar audio license.
   4. For **Content reference**, type the unique identifier
      that Kantar uses for the asset that you're encoding.

5. Confirm that the service role you've specified in the job is the same one that
   you, in the previous topic, attached permissions to that grant access to your
   Kantar credentials. If that role Is MediaConvert_Default_Role, you don't need to
   choose it explicitly, because MediaConvert will use that role by default. To
   specify the role if it has a different name, do the following:
   1. In the **Job** pane on the left, choose **AWS integration**.
   2. In the **Service access** section, find
      **Service role**. Confirm that the specified role
      is the one with the correct
      permissions.
