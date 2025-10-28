# Metrics for continuous monitoring

- **Mean time to detect
  (MTTD)**: The average time it takes to detect a
  performance issue, attack, or compromise. A shorter MTTD
  helps organizations respond more quickly to incidents,
  minimizing damage and downtime. Track this metric by
  calculating the average time from when incidents occur to
  when they're detected by the monitoring systems. This
  includes both automated system detections and manual
  reporting.
- **Mean time between failures
  (MTBF)**: The average time interval between
  consecutive failures in the production environment.
  Tracking this metric helps to gauge the reliability and
  stability of a system. It can be improved by improving
  testing capabilities, proactively monitoring for system
  health, and have post-incident reviews to address root
  causes. Monitor system outages and failures, then
  calculate the average time between these events over a
  given period.
- **Post-incident retrospective
  frequency**: The frequency at which post-incident
  retrospectives are held. Holding regular retrospectives
  help teams continuously improve analysis and incident
  response processes. Measure this metric by counting the
  number of retrospectives conducted within specified
  intervals, such as monthly or quarterly. This can also be
  validated against the total number of incidents to
  understand if all incidents are followed up with a
  retrospective.
- **False positive rate**:
  The percentage of alerts generated that are false
  positives, or incidents that do not require action. A
  lower false positive rate reduces alert fatigue and
  ensures that teams can focus on genuine issues. Calculate
  by dividing the number of false positive alerts by the
  total number of alerts generated and multiplying by 100 to
  get the percentage.
- **Application performance index ([Apdex](https://en.wikipedia.org/wiki/Apdex "https://en.wikipedia.org/wiki/Apdex"))**: Measures user
  satisfaction with application responsiveness using a scale from 0 to 1. A higher Apdex
  score indicates better application performance, likely resulting in improved user
  experience, while a lower score means that users might become frustrated.

To determine the Apdex score, start by defining a target response time that
represents an acceptable user experience for your application. Then, categorize every
transaction in one of three ways:

    + **Satisfied**, if its response time is up to and
     including the target time.
    + **Tolerating**, if its response time is more than
     the target time but no more than four times the target time.
    + **Frustrated**, for any response time beyond four
     times the target time.

Calculate the Apdex score by adding the number of _Satisfied_
transactions with half the _Tolerating_ transactions. Then, divide
this sum by the total number of transactions. Continuously monitor and adjust your
target time based on evolving user expectations and leverage the score to identify and
rectify areas that contribute to user dissatisfaction.
