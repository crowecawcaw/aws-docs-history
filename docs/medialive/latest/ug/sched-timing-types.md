

# Types of timing for actions
<a name="sched-timing-types"></a>

There are several ways to specify the timing for an action:
+ Fixed – Perform the action at a specific time that you specify.

  For most actions, the specified time must be at least 15 seconds in the future. For input prepare actions, the specified time must be at least 15 seconds before the start of the associated input switch. 
+ Immediate – Perform the action as soon as possible. 

  You don't specify a time.
+ Follow – Perform the action just before the specified input switch starts, or just after the currently running input has finished. 

The following table shows the types of timing that apply to each type of action. To read this table, find an action in the first column, then read across the row for the applicable types of timing.


<table>
<thead>
  <tr><th>Type of action</th><th colspan="3">Supported types of timing</th></tr>
  <tr><th></th><th>Fixed</th><th>Follow (Note A)</th><th>Immediate</th></tr>
</thead>
<tbody>
  <tr><td>Switch the input (perform an input switch)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Prepare the input (perform an input prepare)</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Activate a global static image overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Activate a per-outputs static image overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Activate a motion graphics overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Deactivate a global static image overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Deactivate a per-outputs static image overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Deactivate a motion graphics overlay</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Insert a SCTE 35 message</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  <tr><td>Insert ID3 metadata</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Insert an ID3 segment tag</td><td>Yes</td><td></td><td>Yes</td></tr>
  <tr><td>Pause or unpause one or both pipelines</td><td>Yes</td><td></td><td>Yes</td></tr>
</tbody>
</table>


**Note A**  
With a follow, the applicable action can follow an input switch. It can't follow other types of actions. Therefore, the action that is *being followed *is always an input switch. The action that does the follow is an input switch, an input prepare, or a SCTE 35 message. 