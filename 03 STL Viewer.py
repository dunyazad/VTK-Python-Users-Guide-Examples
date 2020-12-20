import vtk

def main():
    mx = vtk.vtkSTLReader()
    mx.SetFileName("./Resources/MX.stl")

    mxMapper = vtk.vtkPolyDataMapper()
    mxMapper.SetInputConnection(mx.GetOutputPort())

    mxActor = vtk.vtkActor()
    mxActor.SetMapper(mxMapper)
    mxActor.GetProperty().SetColor(1, 1, 1)

    md = vtk.vtkSTLReader()
    md.SetFileName("./Resources/MD.stl")

    mdMapper = vtk.vtkPolyDataMapper()
    mdMapper.SetInputConnection(md.GetOutputPort())

    mdActor = vtk.vtkActor()
    mdActor.SetMapper(mdMapper)
    mdActor.GetProperty().SetColor(1, 1, 1)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(mxActor)
    renderer.AddActor(mdActor)
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
