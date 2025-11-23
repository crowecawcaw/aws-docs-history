# Responsible AI Lens - AWS Well-Architected Framework

Publication date: **November 19, 2025** ([Document revisions](document-revisions.md "document-revisions.md"))

The AWS Well-Architected Framework Responsible AI (RAI) Lens assists builder teams
succeed at responsibly building and operating AI solutions that
solve specific AI use cases. It complements existing
Well-Architected publications.

**Challenges**: AI technology is
disrupting existing business processes and powering the next wave of
transformational capabilities in business, consumer, and public
sector systems and applications. However, AI technology that uses
machine-learning differs from rule-based software technology, and
moving an AI use case from idea to trusted production workload
requires builder teams to balance benefits and risks using best
practices that are specific to AI, as well as best practices for
rule-based software technology. An increasingly complex AI
application stack, consisting of customer and third-party data,
models, agents, MCP tools, open and closed-source libraries,
retrieval augmented generation libraries, guardrails, and other
specialized components, increases the complexity of making design
decisions.

Specifically, teams building or deploying AI technology (models or
applications) confront a range of risks that are not typically
covered in academic or on-the-job training in AI/ML. These risks, if
not blocked or mitigated, can undermine the reliability and utility
of an AI system. As an example, consider a generative AI application
that creates descriptions of condominiums for sale from retrieved
private and public data sources. Is the generated text equally
welcoming to each buyer demographic group? Are the property features
accurately captured from the inputs and not hallucinated? Have
private details about the owners or past occupants leaked into the
descriptions? Are uploaded condo images free of unsafe content? Are
generated images both accurate and protected by watermarking?

_Responsible AI_ is the discipline of designing,
developing, and using AI technology with the goal of maximizing
benefits and minimizing risks. At AWS, we define Responsible AI
using a core set of dimensions that we update over time as AI
evolves. These dimensions are specific to AI and complementary to
engineering considerations such as cloud security, cloud privacy,
operational excellence and other factors covered already in the AWS
Well-Architected Framework. We use these responsible AI dimensions
to assist builders identify benefits and risks inherent in an AI use
case, and to organize their decision-making around responsibly
designing and evaluating their AI system. The dimensions are:

- **Controllability:** Having
  mechanisms to monitor and steer AI system behavior.
- **Privacy:** Appropriately
  obtaining, using, and managing data.
- **Security:** Protecting data and
  models from exfiltration and adversarial inputs.
- **Safety:** Blocking harmful
  system output and misuse.
- **Veracity:** Achieving factually
  correct system outputs.
- **Robustness:** Achieving correct
  system outputs for both expected and unexpected inputs.
- **Fairness:** Considering impacts
  on different groups of stakeholders.
- **Explainability:** Having
  mechanisms to understand system behavior.
- **Transparency:** Enabling
  stakeholders to make informed choices about their engagement
  with an AI system.
- **Governance:** Incorporating
  best practices into the AI supply chain, including providers and
  deployers.

The Responsible AI Lens has three audiences:

- **AI builders:** Engineers,
  product managers, and scientists who develop and deploy AI
  systems to solve AI use cases. Builders get guidance on how to
  structure their work to identify and optimize benefit and risk
  tradeoffs specific to AI applications.
- **AI technical leaders:** Oversee
  teams building AI systems and implement enterprise-wide
  responsible AI practices. Leaders get a framework they can use
  to standardize their approaches to balancing portfolio risk and
  earning their own customers' trust.
- **Responsible AI specialists:**
  Establish the specific policies needed by their organizations to
  assist you to comply with applicable regulations and industry
  standards, and work with builder teams to meet the policies.
  Specialists benefit from having a science-based best practice
  framework to assist them set and implement their own
  organization's AI-related policies.

## How to use this guidance

The Responsible AI Lens is structured as a set of eight focus
areas, each of which aligns with a phase in the machine learning
lifecycle. Each focus area contains a set of key questions for
builders to consider, and each question is answered with a set of
best practices. Builders determine for themselves if a given
question or best practice is relevant to their situation. Since AI
development can be iterative and nonlinear, we do not expect that
builders will sequentially work through the focus areas, the
questions within the focus areas, and the best practices for each
question. However, we do recommend that builders familiarize
themselves with the guidance by sequentially reading through the
focus areas and questions and then working through the focus areas
in an order appropriate to their situation. Builders should also
consider the following factors in deciding how and when to use the
guidance:

1. This guidance is aimed at assisting teams design an AI
   solution to solve a specific use case. It is not aimed at
   assisting teams to design general-purpose AI systems (for
   example, foundation models). The guidance is also not
   appropriate for AI use cases that can be solved without
   machine learning, for example, by using expert systems.
2. This guidance does not cover best practices for cloud
   security, cloud privacy, project management, software
   engineering, data management, or other areas for which
   builders already have many resources (like many other lenses
   and guidance in the AWS Well-Architected Framework).
3. Treat each question, best practice, and implementation
   guidance as considerations, not recommendations or
   requirements. Not every consideration will apply to each use
   cases or type of AI solution.
4. This guidance does not provide specific solutions for each of
   many possible AI use cases. Instead, the guidance articulates
   questions that are generally applicable across use cases.
   Therefore, expect that solving your specific use case will
   require additional digging, for example to identify the best
   metrics for your release criteria.
5. Many aspects of responsible AI, like security and post-release
   monitoring, are evolving quickly. We include best practices
   only when we feel they are sufficiently mature.
6. Do not use this guidance as a compliance or assurance
   checklist. There are an increasing number of AI-related
   regulations and standards (for example, the EU AI Act, NIST AI
   600, and ISO 42001). Every organization must decide for itself
   how to interpret and implement the regulations and standards
   to which it is subject. You should consult with your legal
   counsel to understand legal or compliance obligations that may
   apply.
7. The term _risk_ appears in the Responsible AI Lens in two contexts.
   First, some best practices use the term _risk_ to refer to a
   potential responsible AI risk. Second, each best practice
   within the AWS Well-Architected Framework is labeled as high risk or medium
   risk depending on the potential risk to the reader's project
   or business of not considering the best practice (see
   [Identify and understand risks](../userguide/identify-and-understand-risks.md "../userguide/identify-and-understand-risks.md")
   for more information).

In neither case does the term _risk_
refer to a potential or actual legal or compliance risk. The
information and recommendations provided in the Responsible
AI Lens are advisory in nature and should be modified
to fit the specifics of your situation. You should consult
with your legal counsel to understand legal or compliance
obligations that may apply.

## Lens availability

Custom lenses extend the best practice guidance provided by AWS Well-Architected Tool. AWS WA Tool allows you to create your own
[custom
lenses](../userguide/lenses-custom.md "../userguide/lenses-custom.md"), or to use lenses created by others that have been
shared with you.

To begin reviewing your AI workload, download and import the [Responsible AI Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/responsible-ai-lens/responsible-ai-lens.json "https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/responsible-ai-lens/responsible-ai-lens.json") into AWS Well-Architected Tool from the public [AWS Well-Architected custom lens GitHub repository](https://github.com/aws-samples/sample-well-architected-custom-lens "https://github.com/aws-samples/sample-well-architected-custom-lens").
