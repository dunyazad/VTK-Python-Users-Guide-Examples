import vtk

def main():
    axes = vtk.vtkAxes()
    axes.SetOrigin(0, 0, 0)
    axesMapper = vtk.vtkPolyDataMapper()
    axesMapper.SetInputConnection(axes.GetOutputPort())
    axesActor = vtk.vtkActor()
    axesActor.SetMapper(axesMapper)

    atext = vtk.vtkVectorText()
    atext.SetText("Origin")
    textMapper = vtk.vtkPolyDataMapper()
    textMapper.SetInputConnection(atext.GetOutputPort())
    textActor = vtk.vtkFollower()
    textActor.SetMapper(textMapper)
    textActor.SetScale(0.2, 0.2, 0.2)
    textActor.AddPosition(0, -0.1, 0)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(axesActor)
    renderer.AddActor(textActor)
    renderer.SetBackground(0.3, 0.5, 0.7)
    renderer.ResetCamera()
    renderer.GetActiveCamera().Zoom(1.6)
    renderer.ResetCameraClippingRange()

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    textActor.SetCamera(renderer.GetActiveCamera())

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
