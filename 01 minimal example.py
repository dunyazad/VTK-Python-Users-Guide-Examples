#!/usr/bin/env python
import vtk


def main():
    cylinder = vtk.vtkCylinderSource()

    cylinderMpper = vtk.vtkPolyDataMapper()
    cylinderMpper.SetInputConnection(cylinder.GetOutputPort())

    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMpper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(cylinderActor)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderWindow.Render()
    renderWindowInteractor.Start()
    
if __name__ == '__main__':
    main()
