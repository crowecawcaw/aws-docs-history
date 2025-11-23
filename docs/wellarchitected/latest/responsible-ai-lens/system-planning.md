# System planning

The system planning focus area provides best practices for designing
the AI system stack introduced in the Dataset Planning focus area.
The AI system stack consists of training and auxiliary datasets
designed in Dataset Planning, and the AI system solving your use
case. The AI system itself decomposes into a
_core AI system_ and an optional
set of _filters_ (also referred to as
_guardrails_) that block or augment data as it flows through, into, or
out of the core AI system. The primary design strategies for
designing the AI system stack to meet your release criteria are:

- Design choices that directly impact the core AI system (baking)
- Designing data filters (filtering)
- Communicating proper usage to users through documentation, legal
  terms of usage, classes, or similar channels (guiding)

Refer back to [Dataset planning](dataset-planning.md "dataset-planning.md") for best practices that
apply to designing training and auxiliary datasets. The Monitoring
focus area addresses guiding. Best practices for ML engineering and
for optimizing overall ML performance can be found in the
[Machine Learning Lens](../machine-learning-lens/machine-learning-lens.md "../machine-learning-lens/machine-learning-lens.md").

###### Focus areas

- [AI system architecture design](raisp01.md "raisp01.md")
- [AI system baking](raisp02.md "raisp02.md")
- [Filtering](raisp03.md "raisp03.md")
- [Choosing a system configuration](raisp04.md "raisp04.md")
