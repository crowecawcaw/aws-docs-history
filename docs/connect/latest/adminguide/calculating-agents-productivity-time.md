

# Examples of Agent Adherence calculations in Connect Customer
<a name="calculating-agents-productivity-time"></a>

This topic shows two examples that illustrate how Adherent time and Non-adherent time are calculated in Connect Customer. It also includes two examples that show adherence with thresholds, one within a shift and one at the start and end of a shift.

## Example 1
<a name="example1-calculating-prod-time"></a>

**The schedule**: Agent A is scheduled to work from 8:00 to 11:00.

**What the agent does**: Agent A begins working at 7:30 and then takes a break from 10:30 to 11:00. 

**Their adherence**: 
+ From 7:30 to 8:00 Agent A is neither adherent nor non-adherent because this time is outside the schedule. The adherence calculation does not include unscheduled time.
+ From 8:00 to 10:30 Agent A is adherent and from 10:30 to 11:00 they are non-adherent because: 
  + Their status was "Break" when it should have been "Available" because they were scheduled for "Work" and the "Work" activity is mapped to only the "Available" status.

 This means that Agent A's Adherence was 83%. Adherence was calculated as follows:
+  (Total Adherent time 150 minutes / (Total Adherent time 150 minutes \+ Total Non-adherent time 30 minutes)) 

## Example 2
<a name="example2-calculating-prod-time"></a>

**The schedule**: Agent B is scheduled to work from 9:00 to 10:30. They are scheduled to go on "Break" from 10:30 to 11:00, and then go to a team meeting from 11:00 to 12:00. 

**What the agent does**: Agent B begins working at 9:00 and ends up working until 10:45. Then they set their status as "Break" at 10:45 and forget to switch it to "Team Meeting" at 11. They leave their status as "Break" from 10:45 to 12:00. 

**Their adherence**: 
+ From 9:00 to 10:30 Agent B was adherent but from 10:30 to 10:45 they were non-adherent because: 
  + They were scheduled for "Break," which was mapped to the "Break" status, but their actual status was "Available."
+ They were also non-adherent from 11:00 to 12:00 because:
  + They were scheduled for the team meeting activity which maps to the "Team Meeting" status, but their actual status was "Break."

 This means that Agent B's adherence was 58%. Adherence was calculated as follows:
+ (Total Adherent time: 105 minutes / (Total Adherent time: 105 minutes \+ Total Non-adherent time: 75 minutes))

## Example: Adherence with thresholds
<a name="example-adherence-thresholds"></a>

The schedule: Agent C is scheduled for a break at 10:00 AM

Configured threshold: 5 minutes early/late allowed for break activity

**What the agent does:**
+ Starts break at 10:03 AM (3 minutes late).
+ Returns from break at scheduled time.

**Their adherence:**
+ Agent remains adherent because starting break 3 minutes late falls within the configured 5-minute threshold.
+ The "Using thresholds" status would be displayed during this period.

## Example: Adherence with thresholds at the start and end of a shift
<a name="example-adherence-shift-boundary-thresholds"></a>

The schedule: Agent D is scheduled to work from 8:00 AM to 4:00 PM, a total of 480 minutes, including a 30-minute lunch at 11:30 AM.

Configured threshold: 5 minutes early/late allowed at the start and end of the shift.

**What the agent does:**
+ Becomes available at 7:55 AM, 5 minutes before the shift starts.
+ Stays available until 11:45 AM, 15 minutes into their scheduled lunch, then takes lunch from 11:45 AM until 12:00 PM as scheduled.
+ Stays available until 4:05 PM, 5 minutes after the shift ends.

**Their adherence:**
+ The 5 minutes before the shift and the 5 minutes after it are adherent, because both fall within the configured threshold. Neither period is scheduled time.
+ The 15 minutes of lunch during which the agent stayed available are non-adherent.

The metrics for this agent are:
+ Scheduled time: 480 minutes. The 10 minutes of threshold time are not included, because they are outside the scheduled shift.
+ Adherent time: 475 minutes. This is the 465 adherent minutes inside the shift plus the 10 threshold minutes outside it.
+ Non-adherent time: 15 minutes.
+ Adherence: 96.94%, calculated as (Adherent time 475 minutes / (Adherent time 475 minutes \+ Non-adherent time 15 minutes)).

In this example, Adherent time plus Non-adherent time is 490 minutes, which is greater than the Scheduled time of 480 minutes. Adherence is always calculated from Adherent time and Non-adherent time. Dividing Adherent time by Scheduled time does not produce the Adherence percentage shown.