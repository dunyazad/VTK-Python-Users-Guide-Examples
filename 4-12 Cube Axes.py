import vtk
from vtk.util.misc import vtkGetDataRoot
# VTK_DATA_ROOT = vtkGetDataRoot()
VTK_DATA_ROOT = "D:/Library/VTKData"

def main():
    fohe = vtk.vtkBYUReader()
    fohe.SetGeometryFileName(VTK_DATA_ROOT + "/Data/teapot.g")

    normals = vtk.vtkPolyDataNormals()
    normals.SetInputConnection(fohe.GetOutputPort())

    foheMapper = vtk.vtkPolyDataMapper()
    foheMapper.SetInputConnection(normals.GetOutputPort())

    foheActor = vtk.vtkLODActor()
    foheActor.SetMapper(foheMapper)

    outline = vtk.vtkOutlineFilter()
    outline.SetInputConnection(normals.GetOutputPort())
    
    outlineMapper = vtk.vtkPolyDataMapper()
    outlineMapper.SetInputConnection(outline.GetOutputPort())

    outlineActor = vtk.vtkActor()
    outlineActor.SetMapper(outlineMapper)
    outlineActor.GetProperty().SetColor(0, 0, 0)

    camera = vtk.vtkCamera()
    camera.SetClippingRange(1.60187, 20.0842)
    camera.SetFocalPoint(0.21406, 1.5, 0)
    camera.SetPosition(8.3761, 0.549245, -0.815974)
    camera.SetViewUp(0.180324, 0.439245, -0.815974)

    light = vtk.vtkLight()
    light.SetFocalPoint(0.21406, 1.5, 0)
    light.SetPosition(8.3761, 0.549245, -0.815974)

    renderer = vtk.vtkRenderer()
    renderer.SetViewport(0, 0, 0.5, 1.0)
    renderer.SetBackground(0.3, 0.5, 0.7)
    renderer.SetActiveCamera(camera)
    renderer.AddLight(light)

    renderer2 = vtk.vtkRenderer()
    renderer2.SetViewport(0.5, 0, 1.0, 1.0)
    renderer2.SetBackground(0.3, 0.5, 0.7)
    renderer2.SetActiveCamera(camera)
    renderer2.AddLight(light)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.AddRenderer(renderer2)
    renderWindow.SetWindowName("VTK - Cube Axes")
    renderWindow.SetSize(600, 300)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddViewProp(foheActor)
    renderer.AddViewProp(outlineActor)
    renderer2.AddViewProp(foheActor)
    renderer2.AddViewProp(outlineActor)

    tprop = vtk.vtkTextProperty()
    tprop.SetColor(1, 1, 1)
    tprop.ShadowOn()

    axes = vtk.vtkCubeAxesActor2D()
    axes.SetInputConnection(normals.GetOutputPort())
    axes.SetCamera(renderer.GetActiveCamera())
    axes.SetLabelFormat("%6.4g")
    axes.SetFlyModeToOuterEdges()
    axes.SetFontFactor(0.8)
    axes.SetAxisTitleTextProperty(tprop)
    axes.SetAxisLabelTextProperty(tprop)
    renderer.AddViewProp(axes)

    axes2 = vtk.vtkCubeAxesActor2D()
    axes2.SetViewProp(foheActor)
    axes2.SetCamera(renderer2.GetActiveCamera())
    axes2.SetLabelFormat("%6.4g")
    axes2.SetFlyModeToClosestTriad()
    axes2.SetFontFactor(0.8)
    axes2.ScalingOff()
    axes2.SetAxisTitleTextProperty(tprop)
    axes2.SetAxisLabelTextProperty(tprop)
    renderer2.AddViewProp(axes2)

    renderWindow.AddObserver("AbortCheckEvent", CheckAbor)

    renderWindowInteractor.Initialize()
    renderWindow.Render()
    renderWindowInteractor.Start()

def CheckAbor(obj, event):
    if obj.GetEventPending() != 0:
        obj.SetAbortRender(1)

if __name__ == "__main__":
    main()
