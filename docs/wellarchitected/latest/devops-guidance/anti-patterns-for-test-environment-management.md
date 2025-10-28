# Anti-patterns for test environment management

- **Low test data coverage:** Using a limited set of test
  data that does not cover all known scenarios, leading to testing gaps and unexpected
  issues. Effective test data management should include the creation of a comprehensive
  and diverse set of test data that covers all possible scenarios. Reduce the likelihood
  of low data coverage occurring by being proactive about test data requirements at the
  start of the development lifecycle rather than creating and managing test data after a
  change has been made.
- **Insecure test data:** Not having the proper policies and
  security measures in place when generating, storing, or using test data can lead to
  potential data breaches, inaccuracies, and inefficiencies in the test process. Test data
  management strategies should prioritize data security and governance practices to ensure
  that data is accurately and securely managed throughout the testing process. For
  example, using actual production data without proper obfuscation or sanitization in test
  environments has the potential of exposing sensitive information. Use automated
  governance capabilities to apply guardrails, set up secure access to test data, and
  automate the lifecycle of test data.
- **Centralized testing:** Maintaining a traditional,
  centralized approach to quality assurance and testing can create bottlenecks, reduce
  agility, and inhibit teams from taking full ownership of their value stream. Instead,
  focus on providing stream-aligned teams with the tools, knowledge, and resources to
  self-manage their testing requirements. Distribute quality assurance functions by
  creating platform teams and enabling teams to support others by offering scalable
  testing services, tools, and guidance.
