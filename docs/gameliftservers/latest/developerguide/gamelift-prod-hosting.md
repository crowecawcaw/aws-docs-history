# Managing game hosting in production with Amazon GameLift Servers

After you've launched your game with Amazon GameLift Servers, you'll need to manage your game hosting infrastructure to ensure optimal performance, reliability, and player experience. This topic covers the key features and tools for managing game hosting lifecycles during production.

## Monitoring hosting health and performance

Amazon GameLift Servers provides comprehensive monitoring tools to help you track the health and performance of your game hosting infrastructure:

- **Performance metrics** – Monitor key performance
  indicators for managed fleets, such as instance utilization, player sessions, and game
  session placements. Track these metrics in Amazon GameLift Servers or in Amazon CloudWatch, where you can also set up
  alarms to get notifications when metrics exceed thresholds.
- **Fleet metrics and events** – Track
  fleet-specific metrics including active server processes, available game sessions, and
  active player sessions to ensure optimal capacity.
- **Game session placement metrics and events** –
  Track metrics and events to monitor the health and performance of your game session
  placement system.
- **Game session logs** - Access and analyze game session logs to identify issues and understand player behavior patterns.
- **Realtime script logs** - For games using
  Real-time Servers, monitor script execution and performance through detailed logs.
- **AWS Health Dashboard** - Stay informed about AWS service health that might affect your Amazon GameLift Servers deployments.

You can access these monitoring tools through the Amazon GameLift Servers console, AWS CLI, or use the AWS SDK for Amazon GameLift Servers to
create custom dashboards and monitoring solutions.

## Managing game server updates and patches

Keeping your game servers updated is critical for security, performance, and adding new features. Amazon GameLift Servers provides several approaches for managing updates:

- **Build management** - Upload and manage multiple versions of your game server builds. Each build is versioned and can be deployed to different fleets.
- **Fleet replacement** - Create new fleets with AMI
  versions and game server build updates, and gradually shift traffic from old fleets to new
  ones using game session placement queues and aliases.
- **Script updates** - For Real-time Servers, update server scripts without replacing the entire fleet by uploading new script versions.
- **Container updates** - For container-based deployments,
  update container images and definitions. Deploy new versions of your game servers to
  existing fleets. Replace fleets to update AMI versions.
- **Automated deployments** - Use AWS CodePipeline and AWS CodeDeploy to create CI/CD pipelines for automated game server updates.

When planning updates, consider using blue/green deployment strategies to minimize disruption to active players and allow for quick rollbacks if issues are detected.

## Optimizing performance and scaling

As your player base evolves, you'll need to adjust your hosting configuration to maintain optimal performance and cost-efficiency:

- **Auto scaling** - Configure fleet scaling policies based
  on metrics like player count or game session utilization to automatically adjust
  capacity.
- **Regional deployment adjustments** - Add or remove regions from your multi-region deployments based on player demographics and latency requirements.
- **Queue management** - Optimize game session placement queue configurations to balance player experience and hosting costs.
- **Instance type selection** - Analyze performance metrics to determine the most cost-effective instance types for your game server requirements.
- **Spot Instance usage** - Leverage Spot Instances for non-critical workloads to reduce costs, with appropriate fallback strategies to On-Demand instances.
- **FlexMatch tuning** - Refine matchmaking rules and algorithms based on actual player data and feedback.

Regularly review CloudWatch metrics and cost reports to identify optimization
opportunities and implement changes through the Amazon GameLift Servers console or API.

## Troubleshooting and live operations

Effective troubleshooting and live operations management are essential for maintaining a positive player experience:

- **Fleet event notifications** - Set up Amazon Simple Notification Service notifications for fleet events such as scaling activities, instance terminations, or game session placement failures.
- **Game session placement debugging** - Use detailed placement logs to identify and resolve issues with game session placements.
- **Server process health checks** - Monitor server process health and automatically replace processes that fail health checks.
- **Remote access** - Connect to fleet instances for direct troubleshooting using AWS Systems Manager Session Manager.
- **Alias management** - Use aliases to quickly redirect player traffic away from problematic fleets without changing client configurations.
- **Backup and recovery** - Implement regular backups of critical game data and configuration to enable quick recovery from failures.

Establish clear incident response procedures and runbooks for common issues to minimize downtime and impact on players.

## Tools and integration

Amazon GameLift Servers integrates with various AWS services and third-party tools to enhance your
production management capabilities:

- **AWS CloudFormation** - Define and manage your GameLift resources as infrastructure as code for consistent deployments.
- **AWS Lambda** - Create serverless functions to automate routine management tasks and respond to events.
- **Amazon EventBridge** - Build event-driven architectures that
  respond automatically to changes in your Amazon GameLift Servers environment.
- **AWS SDK integration** - Use AWS SDKs to build custom management tools and dashboards tailored to your specific needs.
- **Third-party monitoring** - Integrate with third-party monitoring and analytics platforms using CloudWatch metrics export.

Leverage these integrations to create a comprehensive management solution that aligns with your team's workflows and requirements.

## Related resources

- [Monitoring Amazon GameLift with Amazon CloudWatch](../../../gamelift/latest/developerguide/monitoring-cloudwatch.md "../../../gamelift/latest/developerguide/monitoring-cloudwatch.md")
- [Updating Your Amazon GameLift Fleets](../../../gamelift/latest/developerguide/fleets-updating.md "../../../gamelift/latest/developerguide/fleets-updating.md")
- [Scaling Game Hosting Capacity with Amazon GameLift](../../../gamelift/latest/developerguide/fleets-autoscaling.md "../../../gamelift/latest/developerguide/fleets-autoscaling.md")
- [Amazon GameLift Server SDK Reference](../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md "../../../gamelift/latest/developerguide/gamelift-sdk-server-api.md")
