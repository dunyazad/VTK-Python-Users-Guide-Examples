import vtk

def main():
    source = vtk.vtkCylinderSource()
    source.SetResolution(36)
   
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.3, 0.5, 0.7)

    camera = vtk.vtkCamera()
    camera.SetClippingRange(0.0475572, 2.37786)
    camera.SetFocalPoint(0.052665, -0.129454, -0.0573973)
    camera.SetPosition(0.327637, -0.116299, -0.256418)
    camera.ComputeViewPlaneNormal()
    camera.SetViewUp(-0.0225386, 0.999137, 0.034901)
    camera.Zoom(1.4)
    camera.Azimuth(150)
    camera.Elevation(60)
    renderer.SetActiveCamera(camera)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
