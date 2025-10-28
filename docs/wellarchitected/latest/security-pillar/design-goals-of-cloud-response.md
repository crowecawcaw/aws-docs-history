# Design goals of cloud response

Although the general processes and mechanisms of incident response, such as those defined
in the [NIST SP
800-61 Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final"), remain true, we encourage you to
evaluate these specific design goals that are relevant to responding to security incidents in
a cloud environment:

- **Establish response objectives:** Work with stakeholders, legal counsel, and organizational leadership to determine the goal of responding to an incident. Some common goals include containing and mitigating the issue, recovering the aﬀected resources, preserving data for forensics, returning to known safe operations, and ultimately learning from incidents.
- **Respond using the cloud:** Implement response patterns within the cloud, where the event and data occurs.
- **Know what you have and what you need:** Preserve logs, resources, snapshots, and other evidence by copying and storing them in a centralized cloud account dedicated to response. Use tags, metadata, and mechanisms that enforce retention policies. You’ll need to understand what services you use and then identify requirements for investigating those services. To help you understand your environment, you can also use tagging.
- **Use redeployment mechanisms:** If a security anomaly can be attributed to a misconﬁguration, the remediation might be as simple as removing the variance by redeploying resources with the proper conﬁguration. If a possible compromise is identiﬁed, verify that your redeployment includes successful and veriﬁed mitigation of the root causes.
- **Automate where possible:** As issues arise or incidents repeat, build mechanisms to programmatically triage and respond to common events. Use human responses for unique, complex, or sensitive incidents where automations are insuﬃcient.
- **Choose scalable solutions:** Strive to match the scalability of your organization's approach to cloud computing. Implement detection and response mechanisms that scale across your environments to eﬀectively reduce the time between detection and response.
- **Learn and improve your process:** Be proactive in identifying gaps in your processes, tools, or people, and implement a plan to ﬁx them. Simulations are safe methods to ﬁnd gaps and improve processes.
  These design goals are a reminder to review your architecture implementation for the ability to conduct both incident response and threat detection. As you plan your cloud implementations, think about responding to an incident, ideally with forensically sound response methodology. In some cases, this means you might have multiple organizations, accounts, and tools speciﬁcally set up for these response tasks. These tools and functions should be made available to the incident responder by deployment pipeline. They should not be static because it can cause a larger risk.
