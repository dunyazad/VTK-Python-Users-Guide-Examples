import vtk

def main():
    source = vtk.vtkCylinderSource()
    source.SetResolution(36)
   
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)
    actor.SetPosition(0, 5, 0)

    bannerMapper = vtk.vtkTextMapper()
    bannerMapper.SetInput("banner")
    tprop = bannerMapper.GetTextProperty()
    tprop.SetFontFamilyToArial()
    tprop.SetFontSize(100)
    tprop.BoldOn()
    tprop.ShadowOn()
    tprop.SetColor(1, 0, 0)
    bannerActor = vtk.vtkActor2D()
    #bannerActor.SetPosition(400, 300)
    bannerActor.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    bannerActor.GetPositionCoordinate().SetValue(0.5, 0.5)
    bannerActor.SetMapper(bannerMapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.AddActor2D(bannerActor)
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
