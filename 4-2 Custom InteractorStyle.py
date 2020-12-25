import vtk

class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, parent=None):
        self.AddObserver("LeftButtonPressEvent", self.OnLeftButtonPress)
        self.AddObserver("LeftButtonReleaseEvent", self.OnLeftButtonRelease)
        self.AddObserver("MiddleButtonPressEvent", self.OnMiddleButtonPress)
        self.AddObserver("MiddleButtonReleaseEvent", self.OnMiddleButtonRelease)
        self.AddObserver("RightButtonPressEvent", self.OnRightButtonPress)
        self.AddObserver("RightButtonReleaseEvent", self.OnRightButtonRelease)

    def OnLeftButtonPress(self, object, event):
        self.OnLeftButtonDown()
        return

    def OnLeftButtonRelease(self, object, event):
        self.OnLeftButtonUp()
        return

    def OnMiddleButtonPress(self, object, event):
        self.OnMiddleButtonDown()
        return

    def OnMiddleButtonRelease(self, object, event):
        self.OnMiddleButtonUp()
        return

    def OnRightButtonPress(self, object, event):
        self.OnRightButtonDown()
        return

    def OnRightButtonRelease(self, object, event):
        self.OnRightButtonUp()
        return

def main():
    source = vtk.vtkCylinderSource()
    source.SetResolution(32)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(source.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(0.3, 0.5, 0.7)

    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    window.SetSize(800, 600)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(window)
    interactor.SetInteractorStyle(CustomInteractorStyle())
    
    interactor.Initialize()

    window.Render()
    interactor.Start()

if(__name__ == "__main__"):
    main()
