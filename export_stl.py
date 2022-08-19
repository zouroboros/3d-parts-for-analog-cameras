from pathlib import Path

import FreeCAD
import Mesh

files = list(Path('.').glob('**/*.FCStd'))

for file in files:
	doc = FreeCAD.open(str(file))
	parts = [object for object in doc.Objects if object.isDerivedFrom('PartDesign::Body')]
	for part in parts:
		stl_file_name = file.with_name(f'{doc.Label}-{part.Label}.stl')
		Mesh.export([part], str(stl_file_name))
		
exit()
