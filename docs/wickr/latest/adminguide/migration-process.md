This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Migration from docker method

If you currently use the Docker-based data retention bot, you can migrate to the
Serverless method with no data loss.

## Phase 1: Dual-mode operation (Recommended 60 day)

1. Keep your existing Docker bot running.
2. Follow the [Configure serverless method](configure-serverless-method.md "configure-serverless-method.md") to deploy Serverless
   method.
3. Both methods will capture messages simultaneously during
   transition.
4. Validate that Serverless method is capturing all messages
   correctly.
5. Compare message counts and spot-check content between both systems.

## Phase 2: Validation

1. Monitor CloudWatch dashboards for 1-2 weeks.
2. Verify S3 bucket contains expected messages.
3. Test decryption Lambda function with sample messages.
4. Confirm no gaps in message capture.

## Phase 3: Disable docker method

1. In the AWS Wickr console, navigate to the **Data
   Retention** settings.
2. You'll see both **Docker** and
   **Serverless** methods marked as
   **Active**.
3. Select **Docker configuration**.
4. Choose **Disable Docker Method**.
5. Type **DISABLE** in the confirmation dialog to
   confirm.
6. Docker bot will stop receiving new messages.
7. You can safely decommission your Docker infrastructure.

## Phase 4: Cleanup

1. Stop your Docker container.
2. Archive any Docker bot data you wish to retain.
3. Terminate EC2 instances (if applicable).
4. Remove Docker bot infrastructure.

If you need to revert to Docker method, you cannot re-enable a disabled Docker bot
device, however, you can deploy a new Docker bot following the traditonal setup. Once
the new docker bot is deployed, it will start capturing messages going forward. Previous
messages will remain in your existing storage.
