# Use the `smdebug`

client library to create a custom rule as a Python script

The `smdebug` Rule API provides an interface to set up your own custom rules.
The following python script is a sample of how to construct a custom rule, `CustomGradientRule`.
This tutorial custom rule watches if the gradients are getting too large and set the default threshold as 10.
The custom rule takes a base trial created by a SageMaker AI estimator when it initiates training job.

```
from smdebug.rules.rule import Rule

class CustomGradientRule(Rule):
    def __init__(self, base_trial, threshold=10.0):
        super().__init__(base_trial)
        self.threshold = float(threshold)

    def invoke_at_step(self, step):
        for tname in self.base_trial.tensor_names(collection="gradients"):
            t = self.base_trial.tensor(tname)
            abs_mean = t.reduction_value(step, "mean", abs=True)
            if abs_mean > self.threshold:
                return True
        return False
```

You can add multiple custom rule classes as many as you want in the same python script
and deploy them to any training job trials by constructing custom rule objects in the following section.
