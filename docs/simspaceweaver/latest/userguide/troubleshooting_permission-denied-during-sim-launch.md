End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Permission denied

during simulation start

When you start a simulation, you might get an error message indicating that permission
was denied or that there was an error accessing your app artifacts. This problem can
occur when you specify Amazon S3 buckets for your simulation that SimSpace Weaver didn't create
for you (either through the console or the SimSpace Weaver app SDK scripts).

The following situations are the most likely root causes:

- The service doesn't have permission to access one or
  more of the Amazon S3 buckets you specified in your simulation schema
  – check your app role permissions policy, Amazon S3 bucket policies, and Amazon S3
  bucket permissions to make sure that `simspaceweaver.amazonaws.com`
  has the correct permissions to access your buckets. For more information about
  the app role permissions policy, see [Permissions that SimSpace Weaver creates for you](security_iam_service-created-permissions.md "security_iam_service-created-permissions.md").
- Your Amazon S3 bucket could be in a different AWS Region
  than your simulation – Your Amazon S3 buckets for your simulation
  artifacts must be in the same AWS Region as your simulation. Check your Amazon S3
  console to see what AWS Region your bucket is in. If your Amazon S3 bucket is in a
  different AWS Region, select a bucket that is in the same AWS Region as your
  simulation.
