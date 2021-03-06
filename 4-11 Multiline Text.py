import vtk

font_size = 14

def main():
    singleLineTextProp = vtk.vtkTextProperty()
    singleLineTextProp.SetFontSize(font_size)
    singleLineTextProp.SetFontFamilyToArial()
    singleLineTextProp.BoldOff()
    singleLineTextProp.ItalicOff()
    singleLineTextProp.ShadowOff()

    multiLineTextProp = vtk.vtkTextProperty()
    multiLineTextProp.ShallowCopy(singleLineTextProp)
    multiLineTextProp.SetFontFamilyToArial()
    multiLineTextProp.BoldOn()
    multiLineTextProp.ItalicOn()
    multiLineTextProp.ShadowOn()
    multiLineTextProp.SetLineSpacing(0.8)

    singleLineTextB = vtk.vtkTextMapper()
    singleLineTextB.SetInput("Single line (bottom)")
    tprop = singleLineTextB.GetTextProperty()
    tprop.ShallowCopy(singleLineTextProp)
    tprop.SetVerticalJustificationToBottom()
    tprop.SetColor(1, 0, 0)
    singleLineTextActorB = vtk.vtkActor2D()
    singleLineTextActorB.SetMapper(singleLineTextB)
    singleLineTextActorB.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    singleLineTextActorB.GetPositionCoordinate().SetValue(0.05, 0.85)

    singleLineTextC = vtk.vtkTextMapper()
    singleLineTextC.SetInput("Single line (center)")
    tprop = singleLineTextC.GetTextProperty()
    tprop.ShallowCopy(singleLineTextProp)
    tprop.SetVerticalJustificationToCentered()
    tprop.SetColor(0, 1, 0)
    singleLineTextActorC = vtk.vtkActor2D()
    singleLineTextActorC.SetMapper(singleLineTextC)
    singleLineTextActorC.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    singleLineTextActorC.GetPositionCoordinate().SetValue(0.05, 0.75)

    singleLineTextT = vtk.vtkTextMapper()
    singleLineTextT.SetInput("Single line (top)")
    tprop = singleLineTextT.GetTextProperty()
    tprop.ShallowCopy(singleLineTextProp)
    tprop.SetVerticalJustificationToTop()
    tprop.SetColor(0, 0, 1)
    singleLineTextActorT = vtk.vtkActor2D()
    singleLineTextActorT.SetMapper(singleLineTextT)
    singleLineTextActorT.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    singleLineTextActorT.GetPositionCoordinate().SetValue(0.05, 0.65)

    textMapperL = vtk.vtkTextMapper()
    textMapperL.SetInput("This is\nmulti-line\ntext output\n(left-top)")
    tprop = textMapperL.GetTextProperty()
    tprop.ShallowCopy(multiLineTextProp)
    tprop.SetJustificationToLeft()
    tprop.SetVerticalJustificationToTop()
    tprop.SetColor(1, 0, 0)
    textActorL = vtk.vtkActor2D()
    textActorL.SetMapper(textMapperL)
    textActorL.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    textActorL.GetPositionCoordinate().SetValue(0.05, 0.5)

    textMapperC = vtk.vtkTextMapper()
    textMapperC.SetInput("This is\nmulti-line\ntext output\n(centered)")
    tprop = textMapperC.GetTextProperty()
    tprop.ShallowCopy(multiLineTextProp)
    tprop.SetJustificationToCentered()
    tprop.SetVerticalJustificationToCentered()
    tprop.SetColor(0, 1, 0)
    textActorC = vtk.vtkActor2D()
    textActorC.SetMapper(textMapperC)
    textActorC.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    textActorC.GetPositionCoordinate().SetValue(0.5, 0.5)

    textMapperR = vtk.vtkTextMapper()
    textMapperR.SetInput("This is\nmulti-line\ntext output\n(right-bottom)")
    tprop = textMapperR.GetTextProperty()
    tprop.ShallowCopy(multiLineTextProp)
    tprop.SetJustificationToRight()
    tprop.SetVerticalJustificationToBottom()
    tprop.SetColor(0, 0, 1)
    textActorR = vtk.vtkActor2D()
    textActorR.SetMapper(textMapperR)
    textActorR.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
    textActorR.GetPositionCoordinate().SetValue(0.95, 0.5)

    Pts = vtk.vtkPoints()
    Pts.InsertNextPoint(0.05, 0.0, 0.0)
    Pts.InsertNextPoint(0.05, 1.0, 0.0)
    Pts.InsertNextPoint(0.5, 0.0, 0.0)
    Pts.InsertNextPoint(0.5, 1.0, 0.0)
    Pts.InsertNextPoint(0.95, 0.0, 0.0)
    Pts.InsertNextPoint(0.95, 1.0, 0.0)
    Pts.InsertNextPoint(0.0, 0.5, 0.0)
    Pts.InsertNextPoint(1.0, 0.5, 0.0)
    Pts.InsertNextPoint(0.00, 0.85, 0.0)
    Pts.InsertNextPoint(0.50, 0.85, 0.0)
    Pts.InsertNextPoint(0.00, 0.75, 0.0)
    Pts.InsertNextPoint(0.50, 0.75, 0.0)
    Pts.InsertNextPoint(0.00, 0.65, 0.0)
    Pts.InsertNextPoint(0.50, 0.65, 0.0)

    Lines = vtk.vtkCellArray()
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(0)
    Lines.InsertCellPoint(1)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(2)
    Lines.InsertCellPoint(3)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(4)
    Lines.InsertCellPoint(5)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(6)
    Lines.InsertCellPoint(7)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(8)
    Lines.InsertCellPoint(9)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(10)
    Lines.InsertCellPoint(11)
    Lines.InsertNextCell(2)
    Lines.InsertCellPoint(12)
    Lines.InsertCellPoint(13)

    Grid = vtk.vtkPolyData()
    Grid.SetPoints(Pts)
    Grid.SetLines(Lines)

    normCoords = vtk.vtkCoordinate()
    normCoords.SetCoordinateSystemToNormalizedViewport()

    mapper = vtk.vtkPolyDataMapper2D()
    mapper.SetInputData(Grid)
    mapper.SetTransformCoordinate(normCoords)
    gridActor = vtk.vtkActor2D()
    gridActor.SetMapper(mapper)
    gridActor.GetProperty().SetColor(0.1, 0.1, 0.1)

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.3, 0.5, 0.7)

    renderer.AddActor2D(textActorL)
    renderer.AddActor2D(textActorC)
    renderer.AddActor2D(textActorR)
    renderer.AddActor2D(singleLineTextActorB)
    renderer.AddActor2D(singleLineTextActorC)
    renderer.AddActor2D(singleLineTextActorT)
    renderer.AddActor2D(gridActor)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(500, 300)

    windowInteractor = vtk.vtkRenderWindowInteractor()
    windowInteractor.SetRenderWindow(window)

    window.Render()
    windowInteractor.Start()

if __name__ == "__main__":
    main()
