import vtk

def main():
    source = vtk.vtkSphereSource()
    # source.SetResolution(36)
   
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)
    # actor.GetProperty().SetRepresentationToPoints()
    # actor.GetProperty().SetPointSize(2.0)
    # actor.GetProperty().SetRepresentationToWireframe()
    # actor.GetProperty().SetLineWidth(2.0)
    actor.GetProperty().SetRepresentationToSurface()
    actor.GetProperty().SetLighting(0)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.3, 0.5, 0.7)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)
    window.SetMultiSamples(0)
    # window.SetPointSmoothing(1)
    # window.SetLineSmoothing(1)
    # window.PolygonSmoothing(1)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
