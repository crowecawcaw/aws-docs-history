# Metrics for data testing

- **Data test coverage:** The percentage of your dataset or
  data processing logic covered by tests. Data test coverage gives an overview of
  potential untested or under-tested areas of the application. A high coverage helps
  ensure a comprehensive evaluation, while low coverage can indicate blind spots in
  testing. Improve this metric by prioritizing areas with lower coverage, using automation
  and tools to enhance coverage, and regularly review test strategies to help ensure they
  align with recent changes in the dataset or processing logic. Measure this metric by
  calculating the ratio of code or data elements covered by tests to the total lines of
  code or data elements in the application.
- **Test case run time**: The duration taken to run a test
  case or a suite of test cases. Increasing duration may highlight bottlenecks in the test
  process or performance issues emerging in the software under test. Improve this metric
  by optimizing test scripts and the order they run in, enhancing testing infrastructure,
  and running tests in parallel. Measure the timestamp difference between the start and
  end of test case execution.
- **Data quality score**: The
  combined quality of data in a system, encompassing facets
  such as consistency, completeness, correctness, accuracy,
  validity, and timeliness. Derive the data quality score by
  individually assessing each facet. Then aggregate and
  normalize them into a single metric, typically ranging
  from 0 to 100, with higher scores indicating better data
  quality. The specific method for aggregating the scores
  may vary depending on the organization's data quality
  framework and the relative importance assigned to each
  facet. Consider factors like the uniformity of data values
  (consistency), the presence or absence of missing values
  (completeness), the degree of data accuracy relative to
  real-world entities (correctness and accuracy), the
  adherence of the data to predefined rules (validity), and
  the currency and relevance of the data (timeliness).
