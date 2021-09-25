import vtk

sphere = vtk.vtkSphereSource()
cone = vtk.vtkConeSource()
glyph = vtk.vtkGlyph3D()
glyph.SetInputConnection(sphere.GetOutputPort())
glyph.SetSourceConnection(cone.GetOutputPort())
glyph.SetVectorModeToUseNormal()
glyph.SetScaleModeToScaleByVector()
glyph.SetScaleFactor(0.25)

apd = vtk.vtkAppendPolyData()
apd.AddInputConnection(glyph.GetOutputPort())
apd.AddInputConnection(sphere.GetOutputPort())

maceMapper = vtk.vtkPolyDataMapper()
maceMapper.SetInputConnection(apd.GetOutputPort())

maceActor = vtk.vtkLODActor()
maceActor.SetMapper(maceMapper)
maceActor.VisibilityOn()

plane = vtk.vtkPlane()
clipper = vtk.vtkClipPolyData()
clipper.SetInputConnection(apd.GetOutputPort())
clipper.SetClipFunction(plane)
clipper.InsideOutOn()

selectMapper = vtk.vtkPolyDataMapper()
selectMapper.SetInputConnection(clipper.GetOutputPort())

selectActor = vtk.vtkLODActor()
selectActor.SetMapper(selectMapper)
selectActor.GetProperty().SetColor(0, 1, 0)
selectActor.VisibilityOff()
selectActor.SetScale(1.01, 1.01, 1.01)

renderer = vtk.vtkRenderer()
renderer.AddActor(maceActor)
renderer.AddActor(selectActor)
renderer.SetBackground(0.3, 0.5, 0.7)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
window.SetSize(800, 600)

windowInteractor = vtk.vtkRenderWindowInteractor()
windowInteractor.SetRenderWindow(window)

def myCallback(obj, event):
    global plane, selectActor
    obj.GetPlane(plane)
    selectActor.VisibilityOn()

planeWidget = vtk.vtkImplicitPlaneWidget()
planeWidget.SetInteractor(windowInteractor)
planeWidget.SetPlaceFactor(1.25)
planeWidget.SetInputConnection(glyph.GetOutputPort())
planeWidget.PlaceWidget()
planeWidget.AddObserver("InteractionEvent", myCallback)

windowInteractor.Initialize()
window.Render()
windowInteractor.Start()