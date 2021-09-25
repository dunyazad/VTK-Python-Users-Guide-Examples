import vtk
from vtk.util.colors import *

scalars = vtk.vtkFloatArray()
scalars.InsertNextValue(1.0)
scalars.InsertNextValue(0.0)
scalars.InsertNextValue(0.0)
scalars.InsertNextValue(1.0)
scalars.InsertNextValue(0.0)
scalars.InsertNextValue(0.0)
scalars.InsertNextValue(0.0)
scalars.InsertNextValue(0.0)

points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(1, 0, 0)
points.InsertNextPoint(1, 1, 0)
points.InsertNextPoint(0, 1, 0)
points.InsertNextPoint(0, 0, 1)
points.InsertNextPoint(1, 0, 1)
points.InsertNextPoint(1, 1, 1)
points.InsertNextPoint(0, 1, 1)

ids = vtk.vtkIdList()
ids.InsertNextId(0)
ids.InsertNextId(1)
ids.InsertNextId(2)
ids.InsertNextId(3)
ids.InsertNextId(4)
ids.InsertNextId(5)
ids.InsertNextId(6)
ids.InsertNextId(7)

grid = vtk.vtkUnstructuredGrid()
grid.Allocate(10, 10)
grid.InsertNextCell(12, ids)
grid.SetPoints(points)
grid.GetPointData().SetScalars(scalars)

marching = vtk.vtkContourFilter()
marching.SetInputData(grid)
marching.SetValue(0, 0.5)
marching.Update()

triangleEdges = vtk.vtkExtractEdges()
triangleEdges.SetInputConnection(marching.GetOutputPort())

triangleEdgeTubes = vtk.vtkTubeFilter()
triangleEdgeTubes.SetInputConnection(triangleEdges.GetOutputPort())
triangleEdgeTubes.SetRadius(0.005)
triangleEdgeTubes.SetNumberOfSides(6)
triangleEdgeTubes.UseDefaultNormalOn()
triangleEdgeTubes.SetDefaultNormal(0.577, 0.577, 0.577)

triangleEdgeMapper = vtk.vtkPolyDataMapper()
triangleEdgeMapper.SetInputConnection(triangleEdgeTubes.GetOutputPort())
triangleEdgeMapper.ScalarVisibilityOff()

triangleEdgeActor = vtk.vtkActor()
triangleEdgeActor.SetMapper(triangleEdgeMapper)
triangleEdgeActor.GetProperty().SetDiffuseColor(lamp_black)
triangleEdgeActor.GetProperty().SetSpecular(0.4)
triangleEdgeActor.GetProperty().SetSpecularPower(10)

shrinker = vtk.vtkShrinkPolyData()
shrinker.SetShrinkFactor(1)
shrinker.SetInputConnection(marching.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.ScalarVisibilityOff()
mapper.SetInputConnection(shrinker.GetOutputPort())

triangles = vtk.vtkActor()
triangles.SetMapper(mapper)
triangles.GetProperty().SetDiffuseColor(banana)
triangles.GetProperty().SetOpacity(0.6)

cubeModel = vtk.vtkCubeSource()
cubeModel.SetCenter(0.5, 0.5, 0.5)
edges = vtk.vtkExtractEdges()
edges.SetInputConnection(cubeModel.GetOutputPort())
tubes = vtk.vtkTubeFilter()
tubes.SetInputConnection(edges.GetOutputPort())
tubes.SetRadius(0.01)
tubes.SetNumberOfSides(6)
tubes.UseDefaultNormalOn()
tubes.SetDefaultNormal(0.577, 0.577, 0.577)

tubeMapper = vtk.vtkPolyDataMapper()
tubeMapper.SetInputConnection(tubes.GetOutputPort())
cubeEdges = vtk.vtkActor()
cubeEdges.SetMapper(tubeMapper)
cubeEdges.GetProperty().SetDiffuseColor(khaki)
cubeEdges.GetProperty().SetSpecular(0.4)
cubeEdges.GetProperty().SetSpecularPower(10)

sphere = vtk.vtkSphereSource()
sphere.SetRadius(0.04)
sphere.SetPhiResolution(20)
sphere.SetThetaResolution(20)

thresholdIn = vtk.vtkThresholdPoints()
thresholdIn.SetInputData(grid)
thresholdIn.ThresholdByUpper(0.5)

vertices = vtk.vtkGlyph3D()
vertices.SetInputConnection(thresholdIn.GetOutputPort())
vertices.SetSourceConnection(sphere.GetOutputPort())

sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(vertices.GetOutputPort())
sphereMapper.ScalarVisibilityOff()

cubeVertices = vtk.vtkActor()
cubeVertices.SetMapper(sphereMapper)
cubeVertices.GetProperty().SetDiffuseColor(tomato)

caseLabel = vtk.vtkVectorText()
caseLabel.SetText("Case 1")

aLabelTransform = vtk.vtkTransform()
aLabelTransform.Identity()
aLabelTransform.Translate(-0.2, 0, 1.25)
aLabelTransform.Scale(0.05, 0.05, 0.05)

labelTransform = vtk.vtkTransformPolyDataFilter()
labelTransform.SetTransform(aLabelTransform)
labelTransform.SetInputConnection(caseLabel.GetOutputPort())

labelMapper = vtk.vtkPolyDataMapper()
labelMapper.SetInputConnection(labelTransform.GetOutputPort())

labelActor = vtk.vtkActor()
labelActor.SetMapper(labelMapper)

baseModel = vtk.vtkCubeSource()
baseModel.SetXLength(1.5)
baseModel.SetYLength(0.01)
baseModel.SetZLength(1.5)

baseMapper = vtk.vtkPolyDataMapper()
baseMapper.SetInputConnection(baseModel.GetOutputPort())

base = vtk.vtkActor()
base.SetMapper(baseMapper)
base.SetPosition(0.5, -0.09, 0.5)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(640, 480)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(triangleEdgeActor)
renderer.AddActor(base)
renderer.AddActor(labelActor)
renderer.AddActor(cubeEdges)
renderer.AddActor(cubeVertices)
renderer.AddActor(triangles)

renderer.SetBackground(slate_grey)

def case12(scalars, caselabel, IN, OUT):
    scalars.InsertValue(0, OUT)
    scalars.InsertValue(1, IN)
    scalars.InsertValue(2, OUT)
    scalars.InsertValue(3, IN)
    scalars.InsertValue(4, IN)
    scalars.InsertValue(5, IN)
    scalars.InsertValue(6, OUT)
    scalars.InsertValue(7, OUT)
    if IN == 1:
        caselabel.SetText("Case 12 - 00111010")
    else:
        caselabel.SetText("Case 12 - 11000101")

case12(scalars, caseLabel, 0, 1)

grid.Modified()

renderer.ResetCamera()
renderer.GetActiveCamera().Dolly(1.2)
renderer.GetActiveCamera().Azimuth(30)
renderer.GetActiveCamera().Elevation(20)
renderer.ResetCameraClippingRange()

renderWindowInteractor.Initialize()
renderWindow.Render()
renderWindowInteractor.Start()