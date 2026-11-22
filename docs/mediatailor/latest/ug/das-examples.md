

# Examples

The following examples show how dynamic avail sizing handles underfill, inflation, the inflation cap, the replenishment threshold, and underfill larger than the reserve.

Each figure in these examples is a timeline that ends at the origin live edge. The part up to the virtual live edge is the content in the personalized manifest, including any ads that MediaTailor inserted. The rest is the reserve. Numbers in the figures mark the following parts:

**1**  
Content in the personalized manifest

**2**  
Reserve

**3**  
Virtual live edge

**4**  
Origin live edge

**5**  
Ads

**6**  
Omitted underfill

**7**  
Slate or unpersonalized avail content

## Example 1: underfill and replenishment
<a name="das-example-underfill"></a>

This example uses three ad avails (90, 90, and 180 seconds) to show how underfill and inflation work together. It uses the following configuration.


**Example 1 session configuration**  

| Parameter | Value | 
| --- | --- | 
| aws.contentReserveSeconds | 180 | 
| aws.maxAvailInflationSeconds | 60 | 
| aws.replenishmentThresholdSeconds | 0 (inflate on any deficit) | 

Before avail 1, the reserve is full at 180 seconds, so the personalized manifest ends 180 seconds behind the origin live edge.

For the numbered parts in the figures, see [the figure key](#das-examples-figure-key).

![Reserve full at 180 seconds; the virtual live edge is 180 seconds behind the origin live edge.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex1-before-diagram.png)


In avail 1, the ADS returns 60 seconds of ads for the 90-second avail. MediaTailor omits the 30-second underfill and programming resumes early.
+ The reserve drops from 180 to 150 seconds.
+ Because `aws.replenishmentThresholdSeconds` is `0`, the 30-second deficit makes the next avail eligible for inflation.
+ As the origin publishes the rest of the avail, MediaTailor reveals 30 seconds of reserved content in place of the omitted underfill. By the time the avail would have ended, the virtual live edge is 30 seconds closer to the origin live edge.

![After avail 1, the reserve is 150 seconds and the virtual live edge is 150 seconds behind the origin live edge.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex1-avail1-diagram.png)


In avail 2, MediaTailor inflates the 90-second avail. To refill the reserve to 180 seconds, MediaTailor would need 120 seconds of ads: the 90-second avail plus the 30-second deficit. That's within the 60-second cap, so MediaTailor requests up to 120 seconds of ads. The ADS returns 120 seconds of ads.
+ The 120 seconds of ads play, and the avail fills completely with no underfill.
+ The 30-second surplus returns to the reserve.
+ The reserve goes from 150 to 180 seconds.

![After avail 2 inflates, the reserve is back to 180 seconds behind the origin live edge.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex1-avail2-diagram.png)


In avail 3, the ADS returns no ads for the 180-second avail, so MediaTailor omits the entire 180-second underfill. The underfill equals the reserve (180 seconds), so dynamic avail sizing absorbs it fully and the reserve drops from 180 to 0 seconds. The virtual live edge reaches the origin live edge.

![After avail 3, the reserve is 0 and the virtual live edge meets the origin live edge.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex1-avail3-diagram.png)


With the reserve empty, dynamic avail sizing can't shorten a later avail until inflation replenishes the reserve. Avail 2's inflation is what kept the reserve full enough to absorb avail 3's 180-second underfill. Without it, the reserve would have been 150 seconds before avail 3. That can't cover the 180-second underfill, so MediaTailor wouldn't have shortened avail 3 at all, and viewers would have seen 180 seconds of slate or unpersonalized avail content.

## Example 2: maximum avail inflation cap
<a name="das-example-inflation-cap"></a>

This example shows how `aws.maxAvailInflationSeconds` limits how much a single avail can inflate. With a small cap, recovery takes more than one avail. It uses the following configuration.


**Example 2 session configuration**  

| Parameter | Value | 
| --- | --- | 
| aws.contentReserveSeconds | 180 | 
| aws.maxAvailInflationSeconds | 30 | 
| aws.replenishmentThresholdSeconds | 0 | 

Prior underfills have depleted the reserve to 90 seconds, so the deficit is 90 seconds.

For the numbered parts in the figures, see [the figure key](#das-examples-figure-key).

![Before the avail, the reserve is depleted to 90 seconds.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex2-before-diagram.png)


For the 90-second avail, MediaTailor inflates to refill the reserve. To refill the reserve to 180 seconds, MediaTailor would need 180 seconds of ads: the 90-second avail plus the 90-second deficit. The inflation cap is 30 seconds, so MediaTailor requests up to 120 seconds of ads: the 90-second avail plus 30 seconds. The ADS returns 120 seconds of ads.
+ The 120 seconds of ads play, and the avail fills completely with no underfill.
+ The 30-second surplus returns to the reserve.
+ The reserve goes from 90 to 120 seconds, and the deficit goes from 90 to 60 seconds.

![After one inflated avail, the reserve is 120 seconds.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex2-after-diagram.png)


The deficit is still 60 seconds, so MediaTailor continues to inflate later avails. With a 90-second deficit and a 30-second cap, three inflated avails in total (this one plus two more) are needed to return the reserve to 180 seconds, if the ADS fills each one. A higher cap recovers the reserve faster but produces longer individual avails. A lower cap spreads recovery across more avails and keeps avail lengths more predictable.

## Example 3: replenishment threshold
<a name="das-example-threshold"></a>

This example shows how `aws.replenishmentThresholdSeconds` delays inflation until enough deficit has accumulated. Two avails underfill before inflation starts. It uses the following configuration.


**Example 3 session configuration**  

| Parameter | Value | 
| --- | --- | 
| aws.contentReserveSeconds | 180 | 
| aws.maxAvailInflationSeconds | 60 | 
| aws.replenishmentThresholdSeconds | 60 | 

The deficit must reach 60 seconds before MediaTailor inflates an avail. Before avail 1, the reserve is full at 180 seconds and the deficit is 0.

For the numbered parts in the figures, see [the figure key](#das-examples-figure-key).

![Before avail 1, the reserve is full at 180 seconds.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex3-before-diagram.png)


In avail 1, the ADS returns 60 seconds of ads for the 90-second avail. MediaTailor omits the 30-second underfill.
+ The reserve drops from 180 to 150 seconds.
+ The deficit goes from 0 to 30 seconds.
+ The deficit (30 seconds) hasn't reached the threshold (60 seconds), so MediaTailor doesn't inflate avail 2.

![After avail 1, the reserve is 150 seconds and the deficit is 30 seconds, below the threshold.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex3-avail1-diagram.png)


In avail 2, the ADS again returns 60 seconds of ads for the 90-second avail. MediaTailor omits the 30-second underfill.
+ The reserve drops from 150 to 120 seconds.
+ The deficit goes from 30 to 60 seconds.
+ The deficit (60 seconds) has reached the threshold (60 seconds), so MediaTailor inflates the next avail.

![After avail 2, the reserve is 120 seconds and the deficit reaches the 60-second threshold.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex3-avail2-diagram.png)


In avail 3, MediaTailor inflates the 90-second avail. To refill the reserve to 180 seconds, MediaTailor would need 150 seconds of ads: the 90-second avail plus the 60-second deficit. That's within the 60-second cap, so MediaTailor requests up to 150 seconds of ads. The ADS returns 120 seconds of ads.
+ The 120 seconds of ads play, and the avail fills completely with no underfill.
+ The 30-second surplus returns to the reserve.
+ The reserve goes from 120 to 150 seconds, and the deficit goes from 60 to 30 seconds.

![After avail 3 inflates, the reserve is 150 seconds and the deficit is 30 seconds.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex3-avail3-diagram.png)


The deficit (30 seconds) is now below the threshold again, so MediaTailor doesn't inflate the next avail unless further underfill pushes the deficit back to 60 seconds. Compared to Example 1, where the threshold is `0`, the viewer sees two shorter-than-scheduled avails before avail lengths increase.

## Example 4: underfill larger than the reserve
<a name="das-example-fallback"></a>

This example shows what happens when an avail's underfill exceeds the reserve. Dynamic avail sizing can't shorten the avail, so the viewer sees slate or unpersonalized avail content. It uses the following configuration.


**Example 4 session configuration**  

| Parameter | Value | 
| --- | --- | 
| aws.contentReserveSeconds | 180 | 
| aws.maxAvailInflationSeconds | 60 | 
| aws.replenishmentThresholdSeconds | 0 | 

Prior underfills have depleted the reserve to 30 seconds, so the deficit is 150 seconds.

For the numbered parts in the figures, see [the figure key](#das-examples-figure-key).

![Before the avail, the reserve is depleted to 30 seconds.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex4-before-diagram.png)


Because the deficit (150 seconds) is above the threshold, MediaTailor inflates this 90-second avail. To refill the reserve to 180 seconds, MediaTailor would need 240 seconds of ads: the 90-second avail plus the 150-second deficit. The inflation cap is 60 seconds, so MediaTailor requests up to 150 seconds of ads: the 90-second avail plus 60 seconds. But the ADS only returns 30 seconds of ads. The underfill against the avail's original 90 seconds is 60 seconds. The 30-second reserve can't cover the 60-second underfill, so MediaTailor doesn't shorten the avail: it plays the avail at its original 90 seconds and cancels the inflation. The viewer sees 30 seconds of ads, and then 60 seconds of slate or unpersonalized avail content. The reserve stays 30 seconds, and the virtual live edge doesn't move.

![With the underfill larger than the reserve, the reserve is unchanged at 30 seconds and the virtual live edge doesn't move.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-ex4-after-diagram.png)


After the avail, inflation continues on later avails. As the ADS fills the extra time, the surplus replenishes the reserve, and the viewer stops seeing slate or unpersonalized avail content once the reserve grows large enough to cover underfill again.