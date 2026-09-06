

# Create your first Channel
<a name="msk-data-delivery-s3-first-channel"></a>

1. Create the general-purpose S3 bucket and the DLQ S3 bucket.

1. Create the IAM service role with the required permissions and trust policy (see [IAM permissions](msk-data-delivery-s3-iam.md)).

1. In the Amazon MSK console, open your Express cluster, choose the **Channel** tab, and choose **Create Channel** (see [Manage Channels](msk-data-delivery-s3-manage.md) for full steps).

1. Wait for the Channel to transition from **Creating** to **Active**.

1. Produce records to the topic and verify delivery by inspecting objects in the S3 bucket.