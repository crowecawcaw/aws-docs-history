

# How point-based scoring is calculated in Connect Customer
<a name="about-pointbased-scoring"></a>

The overall evaluation score in point-based mode is calculated as follows:

`Score Percentage = (Total Earned Points / Total Maximum Base Points) x 100`
+ **Earned Points** – The sum of point values for all selected answers across all scored questions.
+ **Maximum Base Points** – The sum of the highest achievable point values for each non-bonus question.

## Example: Point-based score calculation
<a name="pointbased-scoring-example"></a>

Consider a form with one section containing six questions:


| Question | Type | Answer | Earned Points | Max Base Points | 
| --- | --- | --- | --- | --- | 
| 1.1 | Single select (Regular) | b | 20 | 20 | 
| 1.2 | Single select with Bonus Option | a (bonus) | 30 | 20 | 
| 1.3 | Bonus Question | b | 20 | 0 (bonus) | 
| 1.4 | Excluded from Scoring | a | N/A | N/A | 
| 1.5 | Numeric (Regular) | 5 | 20 | 20 | 
| 1.6 | Multiple selection | c, b, a | 60 | 60 | 

**Calculation:**
+ Total Earned Points: 20 \+ 30 \+ 20 \+ 20 \+ 60 = 150
+ Total Max Base Points: 20 \+ 20 \+ 0 \+ 20 \+ 60 = 120
+ Score Percentage: (150 / 120) x 100 = **125%**

The score exceeds 100% because Q1.2 has a bonus option (which adds 10 extra points beyond the question's max of 20) and Q1.3 is a bonus question (its earned points of 20 contribute to the numerator but its max does not contribute to the denominator). Q1.4 is excluded from scoring and does not affect the calculation at all.

The following image shows this evaluation with all maximum scores achieved.

![Evaluation preview showing a score of 150/120 (125%) with bonus options and bonus questions contributing extra points.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-score-example-full.png)


The following image shows the same form with partial scores, resulting in a score of 70/120 (58.3%). In this example, Q1.1 earned 10 out of 20 points, Q1.5 earned 10 out of 20 points, and Q1.6 (multiple selection) earned 0 out of 60 points because "None of the options" was selected.

![Evaluation preview showing a score of 70/120 (58.3%) with partial scores across questions.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-pointbased-score-example-partial.png)


## Question-level scoring details
<a name="pointbased-scoring-details"></a>
+ **Single selection questions** – The earned points equal the point value of the selected option. The max base points equal the highest non-bonus option value.
+ **Numeric questions** – The same logic applies as single selection, but the "option" is the range that the numeric answer falls into.
+ **Multiple selection questions** – The earned points equal the sum of all selected options' point values. If a cap is configured, the sum is clamped at the cap value. The max base points equal the sum of all option values (or the configured cap).
+ **Bonus options** – When a bonus option is selected, the earned points include the bonus value on top of the question's normal maximum. The max base points remain unchanged. This means the earned points for that question can exceed its max.
+ **Bonus questions** – The earned points from a bonus question are added to the total earned points, but the question's max base points are 0 (not counted in the denominator). This allows the overall score to exceed 100%.
+ **Excluded questions** – Excluded questions do not contribute to either earned points or max base points. They are completely removed from the score calculation.
+ **Automatic fail** – If an automatic fail option is selected, the earned points for the affected scope (section or entire form) are set to zero. The max base points remain unchanged.
+ **"None of the options" (multiple selection)** – When the evaluator selects "None of the options" on a multiple selection question, the earned points for that question are zero. The question still contributes its maximum base points to the denominator.