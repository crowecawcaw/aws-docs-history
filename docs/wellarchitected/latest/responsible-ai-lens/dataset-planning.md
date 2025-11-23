# Dataset planning

Developing an AI system to solve a use case requires developing two logically distinct
solution stacks: the _AI evaluation stack_ and the _AI system
stack_.

The _AI evaluation stack_ consists of a suite of evaluation datasets,
associated mechanisms to produce the datasets, and the set of release criteria and metrics used
to evaluate the system on the data. An evaluation dataset is used to test the performance of the
AI system against one or more release criteria. An evaluation dataset may consist of inputs and
their expected outputs, or just inputs where a separate mechanism (for example, a human
workforce or another AI model) is used as part of the evaluation stack to evaluate the
correctness of an AI system output for the input in the evaluation dataset.

The _AI system stack_ consists of the AI system itself, required
training or auxiliary datasets, and mechanisms needed to produce them. Training datasets are
used for building the AI system and support learning, validation, calibration, and component and
parameter selection. Auxiliary datasets provide information required during operation (for
example, the policies used in automated ground truth checks or the document libraries used in a
retrieval-augmented generation (RAG) system).

You can develop AI evaluation and AI system stacks independently. For example, your team
and your downstream stakeholders may have their own AI evaluation stacks. Your downstream
stakeholder may build their stack based on your documentation (see focus area User Guidance) and
still end up making different tactical decisions about the design of their evaluation datasets.
This will yield different evaluations of AI system performance.

Alternatively, you may discover that your ideal robustness evaluation dataset has a large
statistical power requirement, so you build it out in increments, which results in your
robustness performance dropping as each increment is added, even though your AI system stack
remains unchanged.

The dataset planning focus area provides best practices for designing the datasets needed
in both stacks. The System Planning focus area covers designing the AI system and the Evaluate
and Release focus area covers using the evaluation stack to assess the AI system.

Datasets are often thought of as a fixed set of data objects (inputs or input and output
pairs, in the case of training or evaluation datasets) that reside in permanent storage.
However, the datasets used in training, evaluation, and operation are often dynamically
constructed from the static stored version. For example, given a use case of recognizing cats
and dogs in images and a static dataset of images labeled cat or not cat, a builder might
construct an evaluation dataset for robustness by augmenting each image in the static dataset
with rotated versions of the image, increasing the sensitivity of the test datasets to a key
confounding variation (image rotation) without needing new labels. The best practices in the
Dataset Planning focus area are ideally applied to the final datasets, including dynamic
augmentation. However, but this may not be feasible as some static datasets may be augmented
dynamically online throughout training.

###### Focus areas

- [Identify datasets](raidp01.md "raidp01.md")
- [Dataset quality](raidp02.md "raidp02.md")
- [Dataset issues](raidp03.md "raidp03.md")
- [Dataset access and versioning](raidp04.md "raidp04.md")
