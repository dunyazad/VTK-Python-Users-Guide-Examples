import vtk

def main():
    source = vtk.vtkCylinderSource()
    source.SetResolution(36)
   
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)

    scalarBar = vtk.vtkScalarBarActor()
    scalarBar.SetLookupTable(mapper.GetLookupTable())
    scalarBar.SetTitle("Temperature")
    scalarBar.GetPositionCoordinate().SetCoordinateSystemToNormalizedViewport()
    scalarBar.GetPositionCoordinate().SetValue(0.1, 0.01)
    scalarBar.SetOrientationToHorizontal()
    scalarBar.SetWidth(0.8)
    scalarBar.SetHeight(0.17)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.AddActor(scalarBar)
    renderer.SetBackground(0.3, 0.5, 0.7)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
