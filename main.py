import pygame
from view import View
from controller import Controller
from model import Model

#pygame constants

model = Model()
view = View(model)
controller = Controller(view,model)

while True:
    #Event Handling / Controller
    controller.updateController()

    #update Model
    model.updateModel()

    #View builder
    view.updateView()
    


 