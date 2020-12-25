import vtk

def main():
    # Sphere
    sphere = vtk.vtkSphereSource()
   
    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphere.GetOutputPort())

    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.GetProperty().SetColor(1, 0, 1)
    sphereActor.SetOrigin(2, 1, 3)
    sphereActor.RotateY(6)
    sphereActor.SetPosition(2.25, 0, 0)

    # Cube
    cube = vtk.vtkSphereSource()
   
    cubeMapper = vtk.vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cube.GetOutputPort())

    cubeActor = vtk.vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.GetProperty().SetColor(0, 0, 1)
    cubeActor.SetPosition(0, 0.25, 0)

    # Cone
    cone = vtk.vtkSphereSource()
   
    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(0, 1, 0)
    coneActor.SetPosition(0, 0, 0.25)

    # Cylinder
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(36)
   
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(1, 0, 0)

    # Assembly
    assembly = vtk.vtkAssembly()
    assembly.AddPart(cylinderActor)
    assembly.AddPart(sphereActor)
    assembly.AddPart(coneActor)
    assembly.SetOrigin(5, 10, 15)
    assembly.AddPosition(5, 0, 0)
    assembly.RotateX(15)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(assembly)
    renderer.AddActor(coneActor)
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
