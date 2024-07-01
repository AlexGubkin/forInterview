#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.12.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/alex')

channelSize = [8, 15, 400]
tubeThikness = 1

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

# tube = geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2])
# flowDuct = geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2])

# geompy.MakeTranslation(cylinder, 40, 40, 0)
# geompy.TranslateDXDYDZ(Box_1, -5, -8.5, 0)
# geompy.TranslateDXDYDZ(Box_2, -4, -7.5, 0)
Partition_1 =\
    geompy.MakePartition(
        [
            geompy.MakeTranslation(
                geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2]),
                -0.5*(channelSize[0] + 2*tubeThikness), -0.5*(channelSize[1] + 2*tubeThikness), 0
            )
        ],
        [
            geompy.MakeTranslation(
                geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
                -0.5*channelSize[0], -0.5*channelSize[1], 0
            )
        ],
        [], [], geompy.ShapeType["SOLID"], 0, [], 0
    )

# Box_3 = geompy.MakeBoxDXDYDZ(8, 15, 8)
# Box_4 = geompy.MakeBoxDXDYDZ(10, 17, 10)
# geompy.TranslateDXDYDZ(Box_3, -4, -7.5, -8)
# geompy.TranslateDXDYDZ(Box_4, -5, -8.5, -10)
# Get_shapes_on_shape_1 = geompy.GetShapesOnShapeAsCompound(Box_3, Partition_1, geompy.ShapeType["FACE"], GEOM.ST_ONIN)
# Get_shapes_on_shape_2 = geompy.GetShapesOnShapeAsCompound(Box_4, Partition_1, geompy.ShapeType["FACE"], GEOM.ST_ONIN)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

# geompy.addToStudy( Box_1, 'Box_1' )
# geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Partition_1, 'Partition_1' )
# geompy.addToStudy( Box_3, 'Box_3' )
# geompy.addToStudy( Box_4, 'Box_4' )
# geompy.addToStudy( Get_shapes_on_shape_1, 'Get shapes on shape_1' )
# geompy.addToStudy( Get_shapes_on_shape_2, 'Get shapes on shape_2' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
