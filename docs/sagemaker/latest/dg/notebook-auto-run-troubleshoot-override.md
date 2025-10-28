# Parameterize your notebook

To pass new parameters or parameter overrides to your scheduled notebook job, you might
optionally want to modify your Jupyter notebook if you want your new parameters values to be
applied after a cell. When you pass a parameter, the notebook job executor uses the
methodology enforced by Papermill. The notebook job executor searches for a Jupyter cell tagged
with the `parameters` tag and applies the new parameters or parameter overrides
immediately after this cell. If you don’t have any cells tagged with `parameters`,
the parameters are applied at the beginning of the notebook. If you have more than one cell
tagged with `parameters`, the parameters are applied after the first cell tagged
with `parameters`.

To tag a cell in your notebook with the `parameters` tag, complete the
following steps:

1. Select the cell to parameterize.
2. Choose the **Property Inspector** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/gears.png)
   ) in the right sidebar.
3. Type `parameters` in the **Add Tag** box.
4. Choose the **+** sign.
5. The `parameters` tag appears under **Cell Tags** with a
   check mark, which means the tag is applied to the cell.
