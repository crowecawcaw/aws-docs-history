# Theming Workspaces with Views

When Views are used in the Workspace or agent workspace with custom theming, UI components can inherit workspace themes or use custom styling. Keep in mind a few principles:

- When a workspace theme is set, a View's global primary color, secondary color, default color and components will inherit workspace-level styling by default when users don't make custom edits.
- When a view has custom global styles such as primary, secondary, and default colors defined in the UI builder, the custom styling will take precedence over workspace theming.
- When components have custom styles defined in the UI builder, the component styling will take precedence over workspace theming.
- Custom component colors are preserved across different workspaces.
