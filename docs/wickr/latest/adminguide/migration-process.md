

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Migration from docker method
<a name="migration-process"></a>

If you currently use the Docker-based data retention bot, you can migrate to the Serverless method with no data loss.

## Phase 1: Dual-mode operation (Recommended 60 day)
<a name="dual-mode-operation"></a>

1. Keep your existing Docker bot running.

1. Follow the [Configure serverless method](configure-serverless-method.md) to deploy Serverless method.

1. Both methods will capture messages simultaneously during transition.

1. Validate that Serverless method is capturing all messages correctly.

1. Compare message counts and spot-check content between both systems.

## Phase 2: Validation
<a name="validation"></a>

1. Monitor CloudWatch dashboards for 1-2 weeks.

1. Verify S3 bucket contains expected messages.

1. Test decryption Lambda function with sample messages.

1. Confirm no gaps in message capture.

## Phase 3: Disable docker method
<a name="disable-docker-method"></a>

1. In the AWS Wickr console, navigate to the **Data Retention** settings.

1. You'll see both **Docker** and **Serverless** methods marked as **Active**.

1. Select **Docker configuration**.

1. Choose **Disable Docker Method**.

1. Type **DISABLE** in the confirmation dialog to confirm.

1. Docker bot will stop receiving new messages.

1. You can safely decommission your Docker infrastructure.

## Phase 4: Cleanup
<a name="cleanup"></a>

1. Stop your Docker container.

1. Archive any Docker bot data you wish to retain.

1. Terminate EC2 instances (if applicable).

1. Remove Docker bot infrastructure.

 If you need to revert to Docker method, you cannot re-enable a disabled Docker bot device, however, you can deploy a new Docker bot following the traditonal setup. Once the new docker bot is deployed, it will start capturing messages going forward. Previous messages will remain in your existing storage.