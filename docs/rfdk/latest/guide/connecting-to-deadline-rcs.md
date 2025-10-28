# Creating a Remote Terminal Session into the Render Queue

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

You can create a remote terminal session into the Render Queue to perform administrative tasks with [DeadlineCommand](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html") or to diagnose issues in your render farm. The `RenderQueue` construct deploys an [Elastic Container Service (ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") service that runs the Deadline Remote Connection Server (RCS) in an ECS task. To gain access to the instance running the Deadline RCS, you can grant Session Manager permissions to the `RenderQueue` with the [`SessionManagerHelper` class](../../api/latest/docs/aws-rfdk.md#static-grantwbrpermissionswbrtograntable "../../api/latest/docs/aws-rfdk.md#static-grantwbrpermissionswbrtograntable"):

Python

```
render_queue = RenderQueue(self, 'RenderQueue',
  # ...
)
SessionManagerHelper.grant_permissions_to(render_queue.asg)
```

TypeScript

```
const renderQueue = new RenderQueue(this, 'RenderQueue', {
  // ...
});
SessionManagerHelper.grantPermissionsTo(renderQueue.asg);
```

With this in place, you can connect to your `RenderQueue` instance by following these steps:

1. Navigate to the Amazon EC2 console in the region your RFDK farm is deployed in.
2. Select the instance with a name that ends in `*<render-queue-construct-id>*/Cluster/RCS Capacity`.
3. Click the "Connect" button.
4. Choose the "Session Manager" tab.
5. Click "Connect".
   Once you are on the instance, you will need to enter the Docker container that is running the Deadline RCS.

6. List all running Docker containers.

```
sudo docker container ls
```

2. Copy the "ID" of the container that is running the Deadline RCS. This container should be using an image from an ECR repository in your account or from the [AWS Thinkbox ECR Public account](https://gallery.ecr.aws/aws-thinkbox/deadline/rcs "https://gallery.ecr.aws/aws-thinkbox/deadline/rcs"). The `entrypoint` of the container should be `./configure-rcs.sh`.
3. Create a bash shell inside the Docker container by running the following command, replacing `<container-id>` with the value from the previous step.

```
sudo docker exec -it <container-id> bash
```

This will put you in the Docker container running the Deadline RCS, where you can inspect the system and perform administrative tasks via [DeadlineCommand](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/command.html") (typically located at `/opt/Thinkbox/Deadline10/bin/deadlinecommand`). For more information about Deadline, please see [Deadline documentation](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html").
