""" ===================================================================
|   Main loop                                                         |
=================================================================== """

import sys
sys.path.append("lib")
import numpy as np
import glfw
from OpenGL.GL import *
import grafica.scene_graph as sg
import grafica.transformations as tr
import grafica.easy_shaders as es
import blocks


class Controller:
    def __init__(self):
        self.fillPolygon = True
        self.currentMino = ""
        self.nextMino = ""
        self.rotateMino = ""
        self.translateMino = ""
        self.softDrop = False
        self.hardDrop = False


controller = Controller()


def on_key(window, key, scancode, action, mods):
    global controller

    if action == glfw.PRESS:
        if key == glfw.KEY_LEFT:
            controller.rotateMino = "cClockWise"

        if key == glfw.KEY_RIGHT:
            controller.rotateMino = "ClockWise"

        if key == glfw.KEY_A:
            controller.hardDrop = True

        if key == glfw.KEY_Q:
            glfw.set_window_should_close(window, True)

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_D:
            controller.translateMino = "right"

        elif key == glfw.KEY_A:
            controller.translateMino = "left"

        elif key == glfw.KEY_S:
            controller.softDrop = True

    # Release
    else:
        if key == glfw.KEY_S:
            controller.softDrop = False


if __name__ == "__main__":
    if not glfw.init():
        glfw.set_window_should_close(window, True)

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Tetorice", None, None)

    if not window:
        glfw.terminate()
        glfw.set_window_should_close(window, True)

    glfw.make_context_current(window)

    glfw.set_key_callback(window, on_key)

    pipeline = es.SimpleTransformShaderProgram()

    glClearColor(0.3, 0.3, 0.3, 1.0)

    controller.currentMino = blocks.create_mino(blocks.create_S(pipeline))

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(pipeline.shaderProgram)

        sg.drawSceneGraphNode(controller.currentMino, pipeline, "transform")

        glfw.swap_buffers(window)

    controller.currentMino.clear()

    glfw.terminate()
