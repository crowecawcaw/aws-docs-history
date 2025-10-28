# Relative Mouse Offset

By default, during a streaming session, AppStream 2.0 transmits information about
mouse movements by using absolute coordinates and
rendering the mouse movements locally. For graphics-intensive applications, such as
computer-aided design (CAD)/computer-aided manufacturing (CAM) software or video
games, mouse performance improves when relative mouse mode is enabled. Relative
mouse mode uses relative coordinates, which represent how far the mouse moved since
the last frame, rather than the absolute x-y coordinate values within a window or
screen. When you enable relative mouse mode, AppStream 2.0 renders the mouse movements
remotely.

You can enable this feature during an AppStream 2.0 streaming session in either of the following ways:

- Pressing Ctrl+Shift+Fn+F8
- Choosing **Enable relative mouse** from the **Settings**
  and enabling it.
