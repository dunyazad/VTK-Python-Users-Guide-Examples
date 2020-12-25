import vtk

def main():
    bmpReader = vtk.vtkBMPReader()
    bmpReader.SetFileName("./resources/curr.bmp")

    texture = vtk.vtkTexture()
    texture.SetInputConnection(bmpReader.GetOutputPort())
    texture.InterpolateOn()

    source = vtk.vtkPlaneSource()
   
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)
    actor.SetTexture(texture)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
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
