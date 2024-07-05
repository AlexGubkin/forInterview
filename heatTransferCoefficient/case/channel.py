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

ductMeshMinSize = 0.25
ductMeshMaxSize = 0.4
pipeMeshMinSize = 0.25
pipeMeshMaxSize = 0.25

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

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

# tube = geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2])
# flowDuct = geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2])

# Geometry
pipeWithDuct =\
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

geompy.addToStudy(pipeWithDuct, 'pipeWithDuct')

# Volume regions
# Flow duct
ductIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
            -0.5*channelSize[0], -0.5*channelSize[1], 0
        ),
        pipeWithDuct,
        geompy.ShapeType["SOLID"],
        GEOM.ST_ONIN
    )

duct = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["SOLID"])
geompy.UnionIDs(duct, ductIDs)

geompy.addToStudyInFather(pipeWithDuct, duct, 'duct')

# Pipe
pipeIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
            -0.5*channelSize[0], -0.5*channelSize[1], 0
        ),
        pipeWithDuct,
        geompy.ShapeType["SOLID"],
        GEOM.ST_OUT
    )

pipe = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["SOLID"])
geompy.UnionIDs(pipe, pipeIDs)

geompy.addToStudyInFather(pipeWithDuct, pipe, 'pipe')

# Boundaries
inletIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
            -0.5*channelSize[0], -0.5*channelSize[1], -channelSize[2]
        ),
        pipeWithDuct,
        geompy.ShapeType["FACE"],
        GEOM.ST_ON
    )

inlet = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, inletIDs)

geompy.addToStudyInFather(pipeWithDuct, inlet, 'inlet')

inletEdgesIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
            -0.5*channelSize[0], -0.5*channelSize[1], -channelSize[2]
        ),
        pipeWithDuct,
        geompy.ShapeType["EDGE"],
        GEOM.ST_ON
    )

inletEdges = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["EDGE"])
geompy.UnionIDs(inletEdges, inletEdgesIDs)

geompy.addToStudyInFather(pipeWithDuct, inletEdges, 'inletEdges')

outletIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
            -0.5*channelSize[0], -0.5*channelSize[1], channelSize[2]
        ),
        pipeWithDuct,
        geompy.ShapeType["FACE"],
        GEOM.ST_ON
    )

outlet = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, outletIDs)

geompy.addToStudyInFather(pipeWithDuct, outlet, 'outlet')

# ductWallIDs =\
#     geompy.GetShapesOnShapeIDs(
#         geompy.MakeTranslation(
#             geompy.MakeBoxDXDYDZ(channelSize[0], channelSize[1], channelSize[2]),
#             -0.5*channelSize[0], -0.5*channelSize[1], 0
#         ),
#         pipeWithDuct,
#         geompy.ShapeType["FACE"],
#         GEOM.ST_ON
#     )
#
# ductWall = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
# geompy.UnionIDs(ductWall, ductWallIDs)
# ductWall = geompy.CutListOfGroups([ductWall], [inlet, outlet])
#
# geompy.addToStudyInFather(pipeWithDuct, ductWall, 'ductWall')

inletEndFaceIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2]),
            -0.5*(channelSize[0] + 2*tubeThikness), -0.5*(channelSize[1] + 2*tubeThikness), -channelSize[2]
        ),
        pipeWithDuct,
        geompy.ShapeType["FACE"],
        GEOM.ST_ON
    )

inletEndFace = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
geompy.UnionIDs(inletEndFace, inletEndFaceIDs)
inletEndFace = geompy.CutListOfGroups([inletEndFace], [inlet])

geompy.addToStudyInFather(pipeWithDuct, inletEndFace, 'inletEndFace')

outleteEndFaceIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2]),
            -0.5*(channelSize[0] + 2*tubeThikness), -0.5*(channelSize[1] + 2*tubeThikness), channelSize[2]
        ),
        pipeWithDuct,
        geompy.ShapeType["FACE"],
        GEOM.ST_ON
    )

outleteEndFace = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
geompy.UnionIDs(outleteEndFace, outleteEndFaceIDs)
outleteEndFace = geompy.CutListOfGroups([outleteEndFace], [outlet])

geompy.addToStudyInFather(pipeWithDuct, outleteEndFace, 'outleteEndFace')

outsideWallIDs =\
    geompy.GetShapesOnShapeIDs(
        geompy.MakeTranslation(
            geompy.MakeBoxDXDYDZ(channelSize[0] + 2*tubeThikness, channelSize[1] + 2*tubeThikness, channelSize[2]),
            -0.5*(channelSize[0] + 2*tubeThikness), -0.5*(channelSize[1] + 2*tubeThikness), 0
        ),
        pipeWithDuct,
        geompy.ShapeType["FACE"],
        GEOM.ST_ON
    )

outsideWall = geompy.CreateGroup(pipeWithDuct, geompy.ShapeType["FACE"])
geompy.UnionIDs(outsideWall, outsideWallIDs)
outsideWall = geompy.CutListOfGroups([outsideWall], [inletEndFace, outleteEndFace, inlet, outlet])

geompy.addToStudyInFather(pipeWithDuct, outsideWall, 'outsideWall')

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

pipeWithDuctMesh = smesh.Mesh(pipeWithDuct,'pipeWithDuctMesh')
Prism_3D = pipeWithDuctMesh.Prism()
Regular_1D = pipeWithDuctMesh.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(200)

duct_1 = pipeWithDuctMesh.GroupOnGeom(duct,'duct',SMESH.VOLUME)
pipe_1 = pipeWithDuctMesh.GroupOnGeom(pipe,'pipe',SMESH.VOLUME)
inlet_1 = pipeWithDuctMesh.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = pipeWithDuctMesh.GroupOnGeom(outlet,'outlet',SMESH.FACE)
# ductWall_1 = pipeWithDuctMesh.GroupOnGeom(ductWall,'ductWall',SMESH.FACE)
inletEndFace_1 = pipeWithDuctMesh.GroupOnGeom(inletEndFace,'inletEndFace',SMESH.FACE)
outleteEndFace_1 = pipeWithDuctMesh.GroupOnGeom(outleteEndFace,'outleteEndFace',SMESH.FACE)
outsideWall_1 = pipeWithDuctMesh.GroupOnGeom(outsideWall,'outsideWall',SMESH.FACE)

NETGEN_1D_2D = pipeWithDuctMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=inlet)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMinSize(ductMeshMinSize)
NETGEN_2D_Parameters_1.SetMaxSize(ductMeshMaxSize)
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 4 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 32767 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(0.8, 20, 1.2, inletEdgesIDs, 0)

NETGEN_1D_2D_1 = pipeWithDuctMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D,geom=inletEndFace)
NETGEN_2D_Parameters_2 = NETGEN_1D_2D_1.Parameters()
NETGEN_2D_Parameters_2.SetMinSize( pipeMeshMinSize )
NETGEN_2D_Parameters_2.SetMaxSize( pipeMeshMaxSize )
NETGEN_2D_Parameters_2.SetSecondOrder( 0 )
NETGEN_2D_Parameters_2.SetOptimize( 1 )
NETGEN_2D_Parameters_2.SetFineness( 4 )
NETGEN_2D_Parameters_2.SetChordalError( -1 )
NETGEN_2D_Parameters_2.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_2.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_2.SetFuseEdges( 1 )
NETGEN_2D_Parameters_2.SetUseDelauney( 0 )
NETGEN_2D_Parameters_2.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 32767 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
Viscous_Layers_2D_2 = NETGEN_1D_2D_1.ViscousLayers2D(0.25, 5, 1.2, inletEdgesIDs, 0)

isDone = pipeWithDuctMesh.Compute()

[duct_1, pipe_1, inlet_1, outlet_1, inletEndFace_1, outleteEndFace_1, outsideWall_1] = pipeWithDuctMesh.GetGroups()

try:
    pipeWithDuctMesh.ExportUNV(r'/home/alex/forInterview/heatTransferCoefficient/case/pipeWithDuct.unv', 0)
    pass
except:
    print('ExportUNV() failed. Invalid file name?')

# Sub_mesh_1 = NETGEN_1D_2D.GetSubMesh()
# Sub_mesh_2 = NETGEN_1D_2D_1.GetSubMesh()


# ## Set names of Mesh objects
# smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
# smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
# smesh.SetName(Prism_3D.GetAlgorithm(), 'Prism_3D')
# smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
# smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
# smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
# smesh.SetName(NETGEN_2D_Parameters_2, 'NETGEN 2D Parameters_2')
# smesh.SetName(inlet_1, 'inlet')
# smesh.SetName(outlet_1, 'outlet')
# smesh.SetName(ductWall_1, 'ductWall')
# smesh.SetName(inletEndFace_1, 'inletEndFace')
# smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
# smesh.SetName(outleteEndFace_1, 'outleteEndFace')
# smesh.SetName(outsideWall_1, 'outsideWall')
# smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
# smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
# smesh.SetName(pipe_1, 'pipe')
# smesh.SetName(duct_1, 'duct')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
