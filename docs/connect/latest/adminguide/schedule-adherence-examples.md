

# Examples of adherence thresholds for agent shifts in Connect Customer
<a name="schedule-adherence-examples"></a>

Assume a shift that starts at 9:00 AM and ends at 5:00 PM with a 30-minute break and a 1-hour lunch. This arrangement is shown in the following image of the shift profile.

![A shift that starts at 9:00 AM and ends at 5:00 PM with a 30-minute break and a 1-hour lunch.](http://docs.aws.amazon.com/connect/latest/adminguide/images/adherence-fig1.png)


Also assume that the activities are set up as shown in the following Activity setup table. 


**Activity setup**  
<a name="activity-setup"></a>
<table>
<thead>
  <tr><th></th><th colspan="2">START (Min)</th><th colspan="2">END (Min)</th></tr>
  <tr><th></th><th>EARLY</th><th>LATE</th><th>EARLY</th><th>LATE</th></tr>
</thead>
<tbody>
  <tr><td>Work</td><td>5</td><td>7</td><td>10</td><td>15</td></tr>
  <tr><td>Break</td><td>-</td><td>5</td><td>5</td><td>-</td></tr>
  <tr><td>Lunch</td><td>-</td><td>10</td><td>10</td><td>-</td></tr>
</tbody>
</table>


Use Case 1: Agent Group 1 has been set up to use the shift profile shown in the previous image, with no overrides. As a result, agents assigned to Agent Group 1 will have the following tolerances for schedule adherence. 


**Agent Group 1, Adherence thresholds with NO shift overrides**  
<a name="agent-group-1"></a>
<table>
<thead>
  <tr><th></th><th colspan="3">START</th><th colspan="3">END</th></tr>
  <tr><th></th><th>EARLY</th><th>AT</th><th>LATE</th><th>EARLY</th><th>AT</th><th>LATE</th></tr>
</thead>
<tbody>
  <tr><td>Work</td><td>8:55 AM</td><td>9:00 AM</td><td>9:07 AM</td><td>9:50 AM</td><td>10:00 AM</td><td>10:15 AM</td></tr>
  <tr><td>Break</td><td>-</td><td>10:00 AM</td><td>10:05 AM</td><td>10:25 AM</td><td>10:30 AM</td><td>-</td></tr>
  <tr><td>Work</td><td>10:25 AM</td><td>10:30 AM</td><td>10:37 AM</td><td>11:50 AM</td><td>12:00 PM</td><td>12:15 PM</td></tr>
  <tr><td>Lunch</td><td>-</td><td>12:00 PM</td><td>12:10 PM</td><td>12:50 PM</td><td>1:00 PM</td><td>-</td></tr>
  <tr><td>Work</td><td>12:55 PM</td><td>1:00 PM</td><td>1:07 PM</td><td>4:50 PM</td><td>5:00 PM</td><td>5:15 PM</td></tr>
</tbody>
</table>


Use Case 2: Agent Group 2 has been set up to use the shift profile in the previous image. The administrator has set up a shift profile override as shown in the following table.


**Agent Group 2, Shift profile is overridden**  
<a name="agent-group-2-override"></a>
<table>
<thead>
  <tr><th></th><th colspan="2">START (Min)</th><th colspan="2">END (Min)</th></tr>
  <tr><th></th><th>EARLY</th><th>LATE</th><th>EARLY</th><th>LATE</th></tr>
</thead>
<tbody>
  <tr><td>Shift</td><td>10</td><td>7</td><td>-</td><td>10</td></tr>
</tbody>
</table>


As a result of these overrides, agents assigned to Agent Group 2 will have the following tolerances for schedule adherence. 


**Agent Group 2, Adherence thresholds with shift overrides**  
<a name="agent-group-2-thresholds"></a>
<table>
<thead>
  <tr><th></th><th colspan="3">START</th><th colspan="3">END</th></tr>
  <tr><th></th><th>EARLY</th><th>AT</th><th>LATE</th><th>EARLY</th><th>AT</th><th>LATE</th></tr>
</thead>
<tbody>
  <tr><td>Shift</td><td><b>8:50 AM</b></td><td><b>9:00 AM</b></td><td><b>9:07 AM</b></td><td><b>-</b></td><td><b>5:00 PM</b></td><td><b>5:10 PM</b></td></tr>
  <tr><td>Work</td><td><b>8:50 AM</b></td><td>9:00 AM</td><td><b>9:07 AM</b></td><td>9:50 AM</td><td>10:00 AM</td><td>10:15 AM</td></tr>
  <tr><td>Break</td><td><b>-</b></td><td>10:00 AM</td><td>10:05 AM</td><td>10:25 AM</td><td>10:30 AM</td><td>-</td></tr>
  <tr><td>Work</td><td>10:25 AM</td><td>10:30 AM</td><td>10:37 AM</td><td>11:50 AM</td><td>12:00 PM</td><td>12:15 PM</td></tr>
  <tr><td>Lunch</td><td>-</td><td>12:00 PM</td><td>12:10 PM</td><td>12:50 PM</td><td>1:00 PM</td><td>-</td></tr>
  <tr><td>Work</td><td><b>12:50 PM</b></td><td>1:00 PM</td><td><b>1:07 PM</b></td><td><b>4:50 PM</b></td><td>5:00 PM</td><td><b>5:10 PM</b></td></tr>
</tbody>
</table>


The bold cells are changed due to the override. The cells are overridden because:
+ **Shift start:** Originally set to start at 9:00 AM, however, it can start 10 minutes early or 7 minutes late. As a result, for Agent Group 2, the shift can start at:
  + 8:50 AM (10 minutes early)
  + 9:07 AM (7 minutes late)
  + 9:00 AM (set time)
+ **Shift end:** Originally set to end at 5:00 PM, however, due to the override setup, it still needs to end at 5:00 PM or it could end 10 minutes later. As a result, for Agent Group 2, the shift needs to end at:
  + 5:00 PM (as set in the original shift profile)
  + 5:10 PM (10 minutes late)
+ The first and the last activities within the shift are impacted due to the shift profile override in place. This impact is as follows:
  + **First Activity: Work.** The Work adherence tolerance is overridden by the shift profile override. As a result:
    + Start time: Can start early at 8:50 AM or start late at 9:07 AM
    + End time: Can use the override at the Agent Group 2 level and end at 5:00 PM or at 5:10 PM
  + **Last Activity: Work.** The Work adherence tolerance is overridden by the shift profile override. As a result:
    + Start time: Can start early at 12:50 PM or start late at 1:07 PM
    + End time: Can end 10 mins early at 4:50 PM or end late at 5:10 PM