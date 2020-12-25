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

    light = vtk.vtkLight()
    light.SetColor(1, 0, 0)
    light.SetFocalPoint(renderer.GetActiveCamera().GetFocalPoint())
    light.SetPosition(renderer.GetActiveCamera().GetPosition())
    renderer.AddLight(light)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
