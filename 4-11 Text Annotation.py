import vtk

sphere = vtk.vtkSphereSource()

sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())
# sphereMapper.GlobalImmediateModeRenderingOn()
sphereActor = vtk.vtkLODActor()
sphereActor.SetMapper(sphereMapper)

textActor = vtk.vtkTextActor()
textActor.SetTextScaleModeToProp()
textActor.SetDisplayPosition(90, 50)
textActor.SetInput("This is a sphere")

textActor.GetPosition2Coordinate().SetCoordinateSystemToNormalizedViewport()
textActor.GetPosition2Coordinate().SetValue(0.6, 0.1)

tprop = textActor.GetTextProperty()
tprop.SetFontSize(18)
tprop.SetFontFamilyToArial()
tprop.SetJustificationToCentered()
tprop.BoldOn()
tprop.ItalicOn()
tprop.ShadowOn()
tprop.SetColor(0, 0, 1)

renderer = vtk.vtkRenderer()

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(rendererWindow)

renderer.AddActor2D(textActor)
renderer.AddActor(sphereActor)

renderer.SetBackground(0.3, 0.5, 0.7)
rendererWindow.SetSize(250, 125)
renderer.ResetCamera()
renderer.GetActiveCamera().Zoom(1.5)

renderWindowInteractor.Initialize()
rendererWindow.Render()
renderWindowInteractor.Start()
