# RAIRC03-BP10 Measure transparency quality

Consider situations where system documentation is insufficient,
users do not understand the probabilistic nature of a system output,
or where users are unaware of AI system presence. Transparency
deficits might conceal or amplify potential harms while evaluating
impacts on different stakeholder groups. The goal is finding the
right transparency level for your situation by balancing enough
openness to build trust and meet requirements without creating new
vulnerabilities or unintended consequences.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Plan how you'll test transparency effectiveness before
   building your disclosure features by identifying which
   stakeholders from your RAIBR02 risk assessment need what level
   of transparency about AI system presence, capabilities, and
   limitations. Create simple tests that check whether users
   understand when they're interacting with AI, grasp the
   probabilistic nature of outputs, and recognize potential
   biases. This upfront planning assists you to build
   transparency features that inform users without overwhelming
   them.
2. Design tests that measure whether your transparency
   disclosures assist users to make better decisions or
   accidentally create new problems. Build tests that track
   decision quality when users have different levels of system
   information and measure whether transparency improves outcomes
   or leads to misinterpretation. Test across different user
   expertise levels to see where more transparency assists versus
   where it might create confusion.
3. Build measurement approaches that capture both positive
   transparency outcomes like increased trust alongside potential
   negative effects like exposure or security risks. Create
   simple metrics that track user confidence, stakeholder
   satisfaction, and compliance-aligned measures while also
   checking for unintended information leakage or misuse. This
   balanced approach assists you to spot where transparency
   creates value and where it might cause harm.
4. Test transparency calibration by creating scenarios where
   users need to understand system confidence levels,
   limitations, and appropriate use cases for high-stakes
   decisions like financial or health recommendations. Build
   measurement tools that check whether users correctly interpret
   uncertainty indicators and make appropriately cautious
   decisions when system confidence is low. This testing catches
   cases where transparency gaps might lead to harmful
   over-reliance on uncertain outputs.
