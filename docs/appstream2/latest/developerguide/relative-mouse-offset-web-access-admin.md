# Relative Mouse Offset

By default, during users' streaming sessions, AppStream 2.0 transmits information about
mouse movements to the streaming instance by using absolute coordinates and
rendering the mouse movements locally. For graphics-intensive applications, such as
computer-aided design (CAD)/computer-aided manufacturing (CAM) software or video
games, mouse performance improves when relative mouse mode is enabled. Relative
mouse mode uses relative coordinates, which represent how far the mouse moved since
the last frame, rather than the absolute x-y coordinate values within a window or
screen. When relative mouse mode is enabled, AppStream 2.0 renders the mouse movements
remotely.

Users can enable this feature during their AppStream 2.0 streaming sessions by doing either of the following:

- Windows: Pressing Ctrl+Shift+F8
- Mac: Pressing Control+Fn+Shift+F8
