# Anti-patterns for code review

- **Infrequent code reviews**: Skipping or only occasionally
  performing code reviews misses opportunities to catch errors early and can lead to
  isolated development work. For higher quality code, faster error detection,
  incorporation of additional perspectives, and sharing knowledge, regularly schedule code
  reviews and make them a mandatory step before merging.
- **Excessive required
  reviewers**: Overloading the review process by
  involving too many reviewers can lead to bottlenecks and
  unwarranted delays. Define a practical number of reviewers
  based on the complexity and criticality of the code
  changes.
- **Lack of automated
  feedback**: Neglecting automated tools extends
  the review duration by requiring peers to focus on trivial
  issues rather than complex logic. Automated quality
  assurance and feedback mechanisms can help ensure
  consistent and efficient code review by catching common
  issues and providing feedback before manual review.
  Incorporate automated code review tools to complement
  manual, human-driven reviews. While automated tools can
  help catch certain issues, relying too heavily on them can
  lead to a false sense of security and miss issues that
  require human judgment. Find a balance that meets the
  needs of the organization and team preferences.
- **Large batch reviews**:
  Combining multiple code changes into a single request
  clutters and lead to a longer review cycle. Including
  multiple changes, especially if they are unrelated, into a
  single review makes it more difficult to identify and
  address issues with individual changes. Submit smaller,
  more focused pull requests to keep reviews concise and
  enable a faster feedback loop.
- **Unconstructive reviews**:
  Code reviews which are lead with harsh or hostile tones or
  include unhelpful or vague feedback can create an
  environment leading to unconstructive reviews. These
  unconstructive reviews demoralize developers,  prevent
  open dialogue, and impede development progress. Maintain a
  positive review culture by training reviewers to offer
  clear, constructive feedback, emphasizing the importance
  of specificity and positive tone. Implement healthy
  escalation methods and establish team norms to address and
  resolve disputes as they arise.
- **Lack of action on
  findings**: Code review findings that are not
  acted upon or followed up on can lead to missed
  opportunities for improvement and perpetuate the same
  issues in future code changes. Unaddressed feedback makes
  the review process redundant. Ensure a system where
  feedback is tracked, and necessary actions are taken
  promptly.
