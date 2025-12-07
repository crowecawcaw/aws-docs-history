# Human-in-the-loop (HITL)

Nova Act’s Human-in-the-Loop (HITL) capability enables seamless human supervision within autonomous web workflows. HITL is available in the Nova Act SDK for you to implement in your workflows (not provided as a managed AWS service). When your workflow encounters scenarios requiring human judgment or intervention, HITL provides tools and interfaces for supervisors to assist, verify, or take control of the process.

## HITL patterns

Nova Act supports the following HITL patterns:

### Human approval

Human approval enables asynchronous human decision-making in automated processes. When Nova Act encounters a decision point requiring human judgment, it captures a screenshot of the current state and presents it to a human reviewer via a browser-based interface. Use this when you need binary or multi-choice decisions (Approve/Reject, Yes/No, or selecting from predefined options).

### UI takeover

UI takeover enables real-time human control of a remote browser session. When Nova Act encounters a task that requires human interaction, it hands control of the browser to a human operator via a live-streaming interface. The operator can interact with the browser using mouse and keyboard in real-time.

## Understanding HITL scenarios

Nova Act HITL supports the following intervention scenarios:

Using Human Approval. Useful for:

- **Expense and Purchase Approval**: Approve expense reports or purchase approvals.
- **Data Validation**: Confirm accuracy of data before submission.

Using UI Takeover. Useful for:

- **CAPTCHA Resolution**: Solve CAPTCHA challenges.
- **Login/AuthN Flows**: Enter username and password or MFA/2FA codes during login workflows.

Visit the [nova-act-samples](https://github.com/amazon-agi-labs/nova-act-samples/tree/main/examples/human_in_the_loop "https://github.com/amazon-agi-labs/nova-act-samples/tree/main/examples/human_in_the_loop") Github repository for examples of HITL use.

## Implementing HITL

Nova Act provides two approaches for implementing HITL capabilities:

### Option 1: Managed Human Intervention Service (Recommended)

Deploy the provided Human Intervention Service (HIS) that runs entirely within your AWS environment using the AWS CDK. This turnkey solution includes pre-built interfaces, workflows, and infrastructure.

Setup steps:

1. **Deploy the infrastructure:** Use the Human Intervention CDK package from the [nova-act-human-intervention](https://github.com/amazon-agi-labs/nova-act-human-intervention "https://github.com/amazon-agi-labs/nova-act-human-intervention") GitHub repository to deploy the HIS to your AWS account.
2. **Configure notifications:** The managed HIS supports Slack and email notifications to alert supervisors when intervention is needed.
   - **Slack**: Real-time notifications via Slack Bot SDK with rich formatting and threaded conversations
   - **Email**: HTML-formatted email notifications via AWS SES

3. **Integrate with your workflows:** Integrate the Human Intervention Service client SDK into your Nova Act workflows and configure callbacks for human approval or UI takeover patterns at the identified points with appropriate timeouts and retry policies. The managed HIS automatically handles supervisor routing and response collection. See the [nova-act-human-intervention](https://github.com/amazon-agi-labs/nova-act-human-intervention "https://github.com/amazon-agi-labs/nova-act-human-intervention") repository for code examples.
4. **Train supervisors:** Ensure your supervisors are familiar with the HIS interfaces.
   - **One-off action interface**: Streamlined experience for quick approvals or interventions
   - **Supervisor dashboard**: Comprehensive view of all HITL activities, including pending requests, historical actions, and performance metrics.

### Option 2: Custom implementation

Implement the HITL interface yourself and integrate it with your own management system. This gives you complete control over the user interface, workflows, notifications, and integration with existing systems.

Setup steps:

- Integrate the HITL patterns (human approval and UI takeover) into your workflow code
- Build your own notification system to alert supervisors when intervention is needed
- Create interfaces for supervisors to respond to HITL requests
- Implement monitoring and logging for HITL interactions

This approach is ideal when you need to integrate with existing internal systems or require custom workflows that don’t fit the managed HIS model.

## Best practices

When you implement HITL, follow these best practices:

- Set appropriate timeouts based on session age. For example, login interventions might need longer timeouts than CAPTCHA resolutions.
- Implement robust error handling to manage timeout and rejection scenarios gracefully.
- Maintain comprehensive logs of all HITL interactions for audit and analysis purposes.

## Additional resources

Visit the [nova-act-human-intervention](https://github.com/amazon-agi-labs/nova-act-human-intervention "https://github.com/amazon-agi-labs/nova-act-human-intervention") GitHub repository for CDK code and detailed setup instructions.
