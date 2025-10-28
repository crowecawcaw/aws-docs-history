# Metrics for functional testing

- **Defect density:** The number of defects identified per
  unit of code, typically per thousand lines of code (KLOC). A high defect density can
  indicate areas of the code that might require additional scrutiny or rework. By focusing
  on these areas, teams can enhance code quality. Improve this metric by increasing the
  rigor of code reviews, using static code analysis tools, and ensure developers have
  access to training and best practices. To measure this metric, compare the number of
  defects to the size of the codebase in KLOC.
- **Test pass rate:** The percentage of test cases that pass
  successfully. This metric provides an overview of the software's health and readiness
  for release. A declining pass rate can indicate emerging issues or code instability.
  Monitoring the test pass rate helps to evaluate the effectiveness of quality assurance
  testing process. Measure this by comparing the number of successful tests to the total
  tests run.
- **Escaped defect rate:** The number of defects found by
  users post-release compared to those identified during testing. A higher rate can
  suggest gaps in the testing process and areas where user flows are not effectively
  tested. Track this metric by comparing the number of post-release defects to the total
  defects identified.
- **Test case run time:** The duration taken to run a test
  case or a suite of test cases. Increasing the duration can highlight bottlenecks in the
  test process or performance issues emerging in the software under test. Improve this
  metric by optimizing test scripts and the order they run in, enhancing testing
  infrastructure, and running tests in parallel. Measure the timestamp difference between
  the start and end of test case execution.
- **Test coverage:** The percentage of the codebase tested.
  This is generally further segmented as the percentage of functions, statements,
  branches, or conditions. Test coverage gives an overview of potential untested or
  under-tested areas of the application. Improve this metric by prioritizing areas with
  lower coverage, using automation and tools to enhance coverage, and regularly review
  test strategies. Measure this metric by calculating the ratio of code covered by tests
  to the total lines of code in the application.
- **Feature-to-bug ratio:** The proportion of new features
  developed compared to the number of bugs fixed. This metric provides insight into the
  balance between innovation and quality assurance. A higher ratio might indicate a focus
  on feature development, while a lower ratio can suggest a phase of stabilization or
  significant technical debt. To strike a balance, align your software development
  strategy with business goals and feedback loops. Regularly assess the ratio to determine
  if there's a need to prioritize defect resolution over new feature development, or vice
  versa. Measure by dividing the total number of new features by the total number of bugs
  fixed in a given period.
