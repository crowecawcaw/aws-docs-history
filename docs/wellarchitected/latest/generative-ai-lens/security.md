# Security

The security best practices introduced in this paper are represented
by at least one of the following principles:

- **Implement comprehensive access
  controls:** Apply the principle of least privilege
  across all components of your generative AI system. By carefully
  managing permissions for models, data stores, endpoints, and
  agent workflows, you can make sure that each component has only
  the access required for its specific function. This layered
  approach to access control reduces the potential exploit surface
  and limits the scope of security incidents.
- **Secure data and communication
  flows:** Protect all interactions between system
  components and external inputs. By implementing private network
  communications, sanitizing user inputs, securing prompt
  catalogs, governed data access and filtering training data, you
  can maintain data integrity and stop unauthorized access or
  manipulation. This principle helps you verify that sensitive
  information remains protected throughout every stage of
  processing and transmission.
- **Monitor and enforce security
  boundaries:** Establish comprehensive monitoring and
  control mechanisms across both control and data planes. By
  implementing access monitoring, security guardrails, and
  response filters, you can detect and address security violations
  while keeping model outputs within acceptable parameters. This
  active approach to security helps maintain system integrity
  while helping to protect against unauthorized actions and harmful
  responses.
- **Control AI system behaviors:**
  Implement guardrails and boundaries that govern how AI systems
  interact with data and execute workflows. By establishing
  security controls for model responses, implementing secure
  prompt catalogs, and defining clear boundaries for agentic
  behaviors, you can keep AI systems operating within
  predetermined safety parameters. This principle helps reduce the
  risk of unauthorized actions, maintains predictable system
  behavior, and reduces the risk of AI systems being used in
  unintended or harmful ways.

###### Focus areas

- [Endpoint security](gensec01.md "gensec01.md")
- [Response validation](gensec02.md "gensec02.md")
- [Event monitoring](gensec03.md "gensec03.md")
- [Prompt security](gensec04.md "gensec04.md")
- [Excessive agency](gensec05.md "gensec05.md")
- [Data poisoning](gensec06.md "gensec06.md")
