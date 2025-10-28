# Model evaluation

After you’ve built your model, you can evaluate how well your model performed on your data
before using it to make predictions. You can use information, such as the model’s accuracy
when predicting labels and advanced metrics, to determine whether your model can make
sufficiently accurate predictions for your data.

The section [Evaluate your model's performance](canvas-scoring.md "canvas-scoring.md") describes how
to view and interpret the information on your model's **Analyze** page. The
section [Use advanced metrics in your analyses](canvas-advanced-metrics.md "canvas-advanced-metrics.md")
contains more detailed information about the **Advanced metrics** used to
quantify your model’s accuracy.

You can also view more advanced information for specific _model
candidates_, which are all of the model iterations that Canvas runs
through while building your model. Based on the advanced metrics for a given model
candidate, you can select a different candidate to be the default, or the version that is
used for making predictions and deploying. For each model candidate, you can view the
**Advanced metrics** information to help you decide which model
candidate you’d like to select as the default. You can view this information by selecting
the model candidate from the **Model leaderboard**. For more information,
see [View model candidates in the model
leaderboard](canvas-evaluate-model-candidates.md "canvas-evaluate-model-candidates.md").

Canvas also provides the option to download a Jupyter notebook so that you can view and
run the code used to build your model. This is useful if you’d like to make adjustments to
the code or learn more about how your model was built. For more information, see [Download a model notebook](canvas-notebook.md "canvas-notebook.md").
