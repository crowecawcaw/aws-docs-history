# ML lifecycle phase - Data

processing

In ML workloads, the data (inputs and corresponding desired
output) serves important functions including:

- Defining the goal of the system: the output representation and
  the relationship of each output to each input, by means of the
  input and output pairs.
- Training the algorithm that associates inputs to outputs.
- Measuring the performance of the model against changes in data
  distribution or data drift.
- Building a baseline dataset to capture data drift.

As shown in Figure 7, data processing consists of data collection
and data preparation. Data preparation includes data preprocessing
and feature engineering. It mainly uses data wrangling for
interactive data analysis and data visualization for exploratory
data analysis (EDA). EDA focuses on understanding data, sanity
checks, and validation of data quality. 

It is important to note that the same sequence of data processing
steps that is applied to the training data needs to also be
applied to the inference requests.

![7. Figure 7 includes the key components of data processing. Each component will be expanded in later figures in this whitepaper.](images/data-processing-components.png)

_Figure 7: Data processing components_

###### Best practices

- [Data collection](data-collection.md "data-collection.md")
- [Data preparation](data-preparation.md "data-preparation.md")
- [Operational excellence pillar - Best practices](operational-excellence-pillar-best-practices-2.md "operational-excellence-pillar-best-practices-2.md")
- [Security pillar - Best practices](security-pillar-best-practices-2.md "security-pillar-best-practices-2.md")
- [Reliability pillar - Best practices](reliability-pillar-best-practices-2.md "reliability-pillar-best-practices-2.md")
- [Performance efficiency pillar - Best practices](performance-efficiency-pillar-best-practices-2.md "performance-efficiency-pillar-best-practices-2.md")
- [Cost optimization pillar - Best practices](cost-optimization-pillar-best-practices-2.md "cost-optimization-pillar-best-practices-2.md")
- [Sustainability pillar - Best practices](sustainability-pillar-best-practices-2.md "sustainability-pillar-best-practices-2.md")
