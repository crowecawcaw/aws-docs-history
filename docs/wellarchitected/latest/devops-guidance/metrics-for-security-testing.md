# Metrics for security testing

- **Escaped defect rate**: The number of defects found by
  users post-release compared to those identified during testing. A higher rate can
  suggest gaps in the testing process and areas where user flows are not effectively
  tested. An effective security testing process should aim to reduce the escaped defect
  rate by increasing the vulnerability discovery rate. Track this metric by comparing the
  number of post-release defects to the total defects identified.
- **False positive rate**: The ratio of identified security
  threats that are later determined to be non-actionable or actual threats. Too many false
  positives can lead to _alert fatigue_, causing genuine threats to be
  overlooked. This metric indicates the accuracy and relevance of your security testing
  tools. Compare the number of false positives against the total number of security alerts
  raised over a period, such as monthly or quarterly.
- **Mean time to detect**: The average time it takes for an
  organization to detect a security breach or vulnerability.  A shorter mean time
  indicates that testing, monitoring, and alert systems are effective, leading to faster
  detection of issues. A longer mean time may expose the organization to greater risks.
  With effective security testing, you can detect anomalies faster—ideally before they are
  deployed to production. Measure the time from when a vulnerability occurs to the time it
  is detected. Calculate the average detection time over a defined period, such as monthly
  or quarterly.
- **Mean time to remediate**:
  The average time it takes for an organization to address
  and resolve a detected security issue. A shorter mean time
  implies that once a vulnerability is detected, the
  organization can act quickly to mitigate risks. A longer
  mean time suggests potential inefficiencies in the
  incident response process. Having a strong security
  testing practices in place ensures that you are
  well-equipped to understand and remediate vulnerabilities
  when they are detected, leading to faster
  resolution. Measure the time from when a security issue is
  detected to when it is resolved. Calculate the average
  remediation time over a defined period, such as monthly or
  quarterly.
- **Test pass rate**: The
  percentage of test cases that pass successfully. This
  metric provides an overview of the software's health and
  readiness for release. If both the test pass rate and the
  escaped defect rate are high, it could indicate that your
  security tests are not effective enough. Conversely, a
  declining pass rate can indicate emerging security issues.
  Monitoring the test pass rate helps to evaluate the
  effectiveness of quality assurance testing process.
  Measure this by comparing the number of successful tests
  to the total tests run.
- **Test case run
  time**: The duration taken to run a test case
  or a suite of test cases. Increasing duration may
  highlight bottlenecks in the test process or performance
  issues emerging in the software under test. Improve this
  metric by optimizing test scripts and the order they run
  in, enhancing testing infrastructure, and running tests in
  parallel. Measure the timestamp difference between the
  start and end of test case execution.
- **Vulnerability discovery rate**: The number of
  vulnerabilities discovered during the testing phase per defined time period or release.
  This metric helps assess the effectiveness of the security testing process. A higher
  rate, especially when paired with a low false positive rate, may indicate a very
  effective testing process, though if it remains high over time, it might indicate
  recurring coding vulnerabilities. An unusually low vulnerability discovery rate could
  indicate ineffective tests or lack of test coverage. Regularly track the number of
  vulnerabilities detected in each testing cycle and compare it over time to determine
  trends.
