import vtk

sphere = vtk.vtkSphereSource()
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)

cone = vtk.vtkConeSource()
glyph = vtk.vtkGlyph3D()
glyph.SetInputConnection(sphere.GetOutputPort())
glyph.SetSourceConnection(cone.GetOutputPort())
glyph.SetVectorModeToUseNormal()
glyph.SetScaleModeToScaleByVector()
glyph.SetScaleFactor(0.25)
spikeMapper = vtk.vtkPolyDataMapper()
spikeMapper.SetInputConnection(glyph.GetOutputPort())
spikeActor = vtk.vtkLODActor()
spikeActor.SetMapper(spikeMapper)

textMapper = vtk.vtkTextMapper()
tprop = textMapper.GetTextProperty()
tprop.SetFontFamilyToArial()
tprop.SetFontSize(10)
tprop.BoldOn()
tprop.ShadowOn()
tprop.SetColor(1, 0, 0)
textActor = vtk.vtkActor2D()
textActor.VisibilityOff()
textActor.SetMapper(textMapper)

picker = vtk.vtkCellPicker()

def annotatePick(object, event):
    print("pick")
    global picker, textActor, textMapper
    if picker.GetCellId() < 0:
        textActor.VisibilitiOff()
    else:
        selPt = picker.GetSelectionPoint()
        pickPos = picker.GetPickPosition()
        textMapper.SetInput("(%.6f, %.6f, %.6f)"%pickPos)
        textActor.SetPosition(selPt[:2])
        textActor.VisibilityOn()

picker.AddObserver("EndPickEvent", annotatePick)

renderer = vtk.vtkRenderer()
renderer.AddActor2D(textActor)
renderer.AddActor(sphereActor)
renderer.AddActor(spikeActor)
renderer.SetBackground(1, 1, 1)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(300, 300)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindowInteractor.SetPicker(picker)

renderer.ResetCamera()
camera = renderer.GetActiveCamera()
camera.Zoom(1.4)

renderWindowInteractor.Initialize()
picker.Pick(85, 126, 0, renderer)

renderWindow.Render()
renderWindowInteractor.Start()
