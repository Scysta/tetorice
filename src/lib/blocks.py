import sys
from OpenGL.GL import *
import grafica.basic_shapes as bs
import grafica.easy_shaders as es
import grafica.scene_graph as sg
import grafica.transformations as tr


class L:
    def __init__(self):
        self

    def translate(self, dx):
        pass

    def rotate(self, direction):
        pass


def create_gpu_shape(pipeline, shape):
    gpuShape = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpuShape)
    gpuShape.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
    return gpuShape


def create_quad():
    return bs.createRainbowQuad()


def create_L(pipeline):
    shape = bs.createRainbowQuad()
    gpuBase = create_gpu_shape(pipeline, shape)
    gpuTop = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(3, 1, 1)
    base.childs += [gpuBase]

    top = sg.SceneGraphNode("top")
    top.transform = tr.translate(1, 1, 0)
    top.childs += [gpuTop]

    return [base, top]


def create_J(pipeline):
    shape = bs.createRainbowQuad()
    gpuBase = create_gpu_shape(pipeline, shape)
    gpuTop = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(3, 1, 1)
    base.childs += [gpuBase]

    top = sg.SceneGraphNode("top")
    top.transform = tr.translate(-1, 1, 0)
    top.childs += [gpuTop]

    return [base, top]


def create_S(pipeline):
    shape = bs.createRainbowQuad()
    gpuBase = create_gpu_shape(pipeline, shape)
    gpuTop = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(2, 1, 1)
    base.childs += [gpuBase]

    top = sg.SceneGraphNode("top")
    top.transform = tr.matmul([
        tr.translate(1, 1, 0),
        tr.scale(2, 1, 1)
    ])
    top.childs += [gpuTop]

    return [base, top]


def create_Z(pipeline):
    shape = bs.createRainbowQuad()
    gpuBase = create_gpu_shape(pipeline, shape)
    gpuTop = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(2, 1, 1)
    base.childs += [gpuBase]

    top = sg.SceneGraphNode("top")
    top.transform = tr.matmul([
        tr.translate(-1, 1, 0),
        tr.scale(2, 1, 1)
    ])
    top.childs += [gpuTop]

    return [base, top]


def create_I(pipeline):
    shape = bs.createRainbowQuad()
    gpuShape = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(1, 4, 1)
    base.childs += [gpuShape]

    return [base]


def create_T(pipeline):
    shape = bs.createRainbowQuad()
    gpuBase = create_gpu_shape(pipeline, shape)
    gpuTop = create_gpu_shape(pipeline, shape)

    base = sg.SceneGraphNode("base")
    base.transform = tr.scale(3, 1, 1)
    base.childs += [gpuBase]

    top = sg.SceneGraphNode("top")
    top.transform = tr.translate(0, 1, 0)
    top.childs += [gpuTop]

    return [base, top]


def create_mino(minoShape):
    mino = sg.SceneGraphNode("mino")
    mino.transform = tr.uniformScale(0.2)
    mino.childs += [*minoShape]

    rotatedMino = sg.SceneGraphNode("rotated")
    rotatedMino.childs += [mino]

    translatedMino = sg.SceneGraphNode("translated")
    translatedMino.childs += [rotatedMino]

    return translatedMino
