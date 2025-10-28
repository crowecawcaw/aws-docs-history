# Enabling Runtime Monitoring for a

standalone account

A standalone account owns the decision to enable or disable a protection plan in their
AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method
of invitation, this section doesn't apply to your account. For more information,
see [Enabling Runtime Monitoring for
multiple-account environments](enable-runtime-monitoring-multiple-acc-env.md "enable-runtime-monitoring-multiple-acc-env.md").

After you enable Runtime Monitoring, ensure to install GuardDuty security agent through automated
configuration or manual deployment. As a part of completing all the steps listed in the
following procedure, make sure to install the security agent.

###### To enable Runtime Monitoring in standalone account

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Runtime Monitoring**.
3. Under the **Configuration** tab, choose
   **Enable** to enable Runtime Monitoring for your account.
4. For GuardDuty to receive the runtime events from one or more resource types
   – an Amazon EC2 instance, Amazon ECS cluster, or an Amazon EKS cluster, use the
   following options to manage the security agent for these resources:

###### To enable GuardDuty security agent

    * [Enabling automated security agent for
     Amazon EC2 instance](managing-gdu-agent-ec2-automated.md "managing-gdu-agent-ec2-automated.md")
    * [Managing security agent manually for Amazon EC2 resource](managing-gdu-agent-ec2-manually.md "managing-gdu-agent-ec2-manually.md")
    * [Managing automated security agent for
     Fargate (Amazon ECS only)](managing-gdu-agent-ecs-automated.md "managing-gdu-agent-ecs-automated.md")
    * [Managing security agent automatically
     for Amazon EKS resources](managing-gdu-agent-eks-automatically.md "managing-gdu-agent-eks-automatically.md")
    * [Managing security agent manually for
     Amazon EKS cluster](managing-gdu-agent-eks-manually.md "managing-gdu-agent-eks-manually.md")
