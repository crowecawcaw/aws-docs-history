# Find and run the candidate definition

notebook

The candidate definition notebook contains each suggested preprocessing step, algorithm,
and hyperparameter ranges.

You can choose which candidate to train and tune in two ways. The first, by running
sections of the notebook. The second, by running the entire notebook to optimize all
candidates to identify a best candidate. If you run the entire notebook, only the best
candidate is displayed after job completion.

To run Autopilot from SageMaker Studio Classic, open the candidate definition notebook by following
these steps:

1. Choose the **Home** icon
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   from the left navigation pane to view the top-level
   **Amazon SageMaker Studio Classic** navigation menu.
2. Select the **AutoML** card from the main working area. This opens a
   new **Autopilot** tab.
3. In the **Name** section, select the Autopilot job that has the candidate
   definition notebook that you want to examine. This opens a new **Autopilot
   job** tab.
4. Choose **Open candidate generation notebook** from the top right
   section of the **Autopilot job** tab. This opens a new read-only preview of
   the **Amazon SageMaker Autopilot Candidate Definition Notebook**.
   To run the candidate definition notebook, follow these steps:

5. Choose **Import notebook** at the top right of the **Amazon SageMaker
   Autopilot Candidate Definition Notebook** tab. This opens a tab to set up a new
   notebook environment to run the notebook.
6. Select an existing SageMaker **Image** or use a **Custom
   Image**.
7. Select a **Kernel**, an **Instance type**, and an
   optional **Start-up script**.
   You can now run the notebook in this new environment.
