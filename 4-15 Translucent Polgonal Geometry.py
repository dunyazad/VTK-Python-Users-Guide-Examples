import vtk

def main():
    source = vtk.vtkImageSinusoidSource()
    source.SetWholeExtent(0, 9, 0, 9, 0, 9)
    source.SetPeriod(5)
    source.Update()

    image = source.GetOutput()
    range = image.GetScalarRange()

    surface = vtk.vtkDataSetSurfaceFilter()
    surface.SetInputConnection(source.GetOutputPort())

    lut = vtk.vtkLookupTable()
    lut.SetTableRange(range)
    lut.SetAlphaRange(0.5, 0.5)
    lut.SetHueRange(0.2, 0.7)
    lut.SetNumberOfTableValues(256)
    lut.Build()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(surface.GetOutputPort())
    mapper.SetScalarVisibility(1)
    mapper.SetLookupTable(lut)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(1, 1, 1)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.3, 0.5, 0.7)
    renderer.SetUseDepthPeeling(1);
    renderer.SetMaximumNumberOfPeels(200);
    renderer.SetOcclusionRatio(0.1)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)
    window.SetMultiSamples(0)
    window.SetAlphaBitPlanes(1)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    if renderer.GetLastRenderingUsedDepthPeeling():
        print("Depth Peeling was used.")
    else:
        print("Depth Peeling was not used. (Alpha blending instead)")
    
    camera = renderer.GetActiveCamera()
    camera.Azimuth(-40)
    camera.Elevation(20)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
