# Kiro in Amazon SageMaker Unified Studio

Kiro is Amazon's AI-powered agentic IDE that you can use as a local IDE to connect to
your Amazon SageMaker Unified Studio Spaces and resources.

These instructions assume you already have an Amazon SageMaker Unified Studio domain, project, and Space set
up.

###### To set up Kiro

1. Download and install Kiro from [kiro.dev](https://kiro.dev "https://kiro.dev")
   (minimum version 0.8.0 or later).
2. Open the AWS Toolkit panel in Kiro and navigate to the Amazon SageMaker Unified Studio
   section.
3. Choose **Sign in to get started**, and then choose
   **IAM Credentials**. You can also use IAM Identity
   Center.
4. Create or choose a credential profile using the same IAM role you use to
   access your project in the AWS Management Console. Choose the Region your
   project is in, and then sign in. Your Amazon SageMaker Unified Studio resources (Data, Compute,
   Spaces) appear in the panel.
5. Under your project, choose **Compute**, and then choose
   **Spaces**. Hover over the Space you want to connect to and
   choose the **Connect** button.
6. When prompted to install the Amazon SageMaker SSH Plugin for Kiro, choose
   **Install**. This enables remote access, starts the Space,
   and connects to it.
7. Sign in to Kiro on the Space when prompted. After you connect, all project
   files are available in your remote workspace.

###### Note

Instances must have a minimum of 8 GB RAM. The following instance types are not
supported: `ml.t3.medium`, `ml.c7i.large`,
`ml.c6i.large`, `ml.c6id.large`,
`ml.c5.large`.

You can provide your AI assistant with more context about Amazon SageMaker Unified Studio workspaces by
linking a service-provided context file, smus-context.md, to the your existing AGENTS.md
file or by creating a new one if it doesn't already exist. It is strongly recommended to
use the Amazon SageMaker Unified Studio context file for a better user experience. As this is a
service-provided context file and subject to change, you can edit other context files
linked to AGENTS.md or to AGENTS.md directly.
