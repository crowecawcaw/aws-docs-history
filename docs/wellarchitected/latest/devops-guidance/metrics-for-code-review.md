# Metrics for code review

- **Review time to merge (RTTM):** The duration from the
  start of the review process to the merging of code. This metric can indicate gaps in the
  review process and can be improved by streamlining reviews, provide timely feedback, and
  automating trivial checks. Monitor the timestamp of the start of review and the
  timestamp of code merge.
- **Reviewer load:** The number of open pull requests
  assigned to each reviewer. High reviewer loads can lead to bottlenecks and
  inefficiencies in the code review process, while low reviewer loads when paired with a
  high review time to merge can indicate that the team is not focused enough on reviewing
  changes. This metric can be improved by rebalancing pull request assignments, assigning
  code owners, and adding more reviewers or resources. Count the number of pull requests
  per reviewer periodically to track this metric.
- **Code ownership health:** This metric evaluates how well
  the codebase is covered by designated code owners, ensuring that there are enough domain
  experts to review relevant sections of the code. It uses the current number of code
  owners listed in the `CODEOWNERS` file and compares it against a desired
  benchmark target. Calculate the benchmark target by dividing the number of pull requests
  by the average number of pull requests a code owner can handle while accounting for
  actual code owner availability. Compare the current count of code owners to this derived
  benchmark target.
- **Merge request type distribution:** Distribution of merge
  requests based on their nature, such as new features, enhancements, maintenance, or bug
  fixes. This metric provides insight into the team's focus and can help to plan and
  allocate resources effectively. Categorize each pull request, ideally using a common
  commit convention, and monitor the distribution on a regular basis, such as monthly or
  quarterly.
- **Change failure
  rate:** The rate at which code changes lead to
  errors or bugs in the system after being merged. A high
  failure rate might indicate issues in the review or
  testing processes, while a low rate suggests effective
  review and quality control. Calculate the rate by dividing
  the number of post-merge failures by the total number of
  merges made during a specific time frame, such as monthly
  or quarterly.
