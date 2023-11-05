import xml.etree.ElementTree as ET

def create_mxCell(id, parent, value):
    # Crea l'elemento mxCell
    mxCell = ET.Element('mxCell', {
        'id': id,
        'value': value,
        'style': "edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;",
        'vertex': "1",
        'connectable': "0",
        'parent': parent
    })

    # Crea l'elemento mxGeometry e aggiungilo a mxCell
    mxGeometry = ET.SubElement(mxCell, 'mxGeometry', {
        'x': "-0.2109",
        'relative': "1",
        'as': "geometry"
    })

    # Crea l'elemento mxPoint e aggiungilo a mxGeometry
    mxPoint = ET.SubElement(mxGeometry, 'mxPoint', {
        'as': "offset"
    })

    # Ritorna una stringa dell'elemento XML
    return ET.tostring(mxCell, encoding='unicode')

# Testa la funzione
print(create_mxCell('label1', 'edge1', 'Inizializzazione'))