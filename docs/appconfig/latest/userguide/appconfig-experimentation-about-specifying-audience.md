

# Specifying the target audience for the experiment
<a name="appconfig-experimentation-about-specifying-audience"></a>

The target audience defines which users are eligible to be assigned to treatments during an experiment run. Selecting the right audience is important for collecting reliable data, reducing risk, and ensuring that experiment results apply to your production environment. When you configure an experiment, choose an audience that is appropriate for the change you are evaluating and the outcomes you want to measure. Consider the following important details for selecting a target audience:

**Representativeness**  
Choose an audience that reflects the users you plan to impact. Include key user segments, such as new and returning users, if they are relevant to your experiment. If the audience is not representative, experiment results may not generalize to your broader user base. Conversely, choose an audience that does not bias too much toward your launch criteria.

**Audience size**  
Ensure that the eligible audience is large enough to produce meaningful results. Small audiences can lead to inconclusive or highly variable results. Larger audiences provide more reliable comparisons between treatments. Use the exposure setting to control risk — start at low exposure and increase gradually, rather than restricting the audience pool itself.

**Risk level**  
Consider the potential impact of the experiment on users. Begin with lower-risk segments, such as internal users or a limited subset of your audience. Exclude critical workloads or sensitive user groups if needed. Gradually increasing exposure helps reduce the impact of unexpected issues.

**Eligibility criteria**  
Define clear rules for including users in the target audience. Clear eligibility criteria help prevent unintended exposure. You can create audience rules that filter users based on attributes such as:  
+ Location or region
+ Account type or user segment
+ Application context, such as device type, OS type, or app version

**Interaction with other experiments**  
Be aware of overlapping experiments. Avoid assigning the same users to multiple experiments that could conflict. Consider isolating audiences when running concurrent experiments. Overlapping experiments can make results difficult to interpret.

**Alignment with rollout plans**  
Align the experiment audience with your intended rollout strategy. Choose an audience that reflects the users you plan to expose to the final treatment. If needed, start additional experiment runs to validate results across broader audiences. This helps ensure that experiment results remain valid as exposure increases.