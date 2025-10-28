# Anti-patterns for functional testing

- **Over indexing on coverage metrics:** Relying heavily on
  test coverage metrics can lead teams to believe that the software is comprehensively
  tested. However, high test coverage might not catch all potential defects, as tests can
  run code without truly validating its correctness. This can result in overlooked defects
  and misplaced trust in the efficacy of the tests. To address this issue, incorporate
  regular test suite reviews focusing on meaningful assertions, rather than just coverage
  percentages. Introducing additional metrics like [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing "https://en.wikipedia.org/wiki/Mutation_testing") scores
  can help to continuously measure and assess unit tests to help ensure they are
  meaningful. Improve the effectiveness of tests over time by tracking the number of
  defects escaping to production against test coverage percentages.
- **Reactive test writing:** Adopting a strategy where tests
  are primarily written post-software development and after defects emerge can produce
  software with undiscovered bugs. While writing code before tests might seem
  time-efficient, it can lengthen overall development cycles, increase costs, and erode
  trust in software quality. Provide developers with training to encourage adopting
  both [Test-Driven Development
  (TDD)](https://www.agilealliance.org/glossary/tdd/ "https://www.agilealliance.org/glossary/tdd/") and [Behavior-Driven Development (BDD)](https://www.agilealliance.org/glossary/bdd/ "https://www.agilealliance.org/glossary/bdd/") practices to introduce testing early in the
  development lifecycle. These approaches emphasize designing and writing tests before
  code, ensuring that testing considerations are embedded from the start.
- **Only testing functional requirements:** Focusing only on
  functional tests while sidelining non-functional aspects like accessibility,
  performance, and security can lead to vulnerabilities, poor user experience, and
  performance issues. Ongoing feedback loops with end users is the key to ensuring a
  well-rounded testing approach that strikes a balance between functional and
  non-functional tests. Engage with users early in the development process, conduct
  experiments, and iterate based on their feedback. Assess the ratio of functional to
  non-functional test activities, and pay attention to post-release incidents related to
  non-functional aspects of the application.
- **Neglecting to address flaky tests:** Continuously
  unreliable or inconsistent test results, known as flaky tests, can diminish trust in the
  test suite. These tests can lead to wasted time addressing false positives and as teams
  become accustomed to flaky tests they may begin to ignore them. This can lead to real
  defects being missed or ignored, drawing parallels to the story of _The boy who
  cried wolf_. Recognize the importance of consistent test outcomes. Address
  flakiness by rigorously investigating and resolving its root causes of failing tests,
  refining test design, and ensuring the testing environment is stable and reproducible.
  Establish a policy to handle flaky tests, such as quarantining them until resolved, to
  maintain the integrity of the test suite.
