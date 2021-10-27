# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-yF16MXfbs8l6dAZ5kUbCUZNtrqsYwGE

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
ns = Namespace("http://somewhere#")

from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
    SELECT ?sub WHERE { 
    ?sub rdfs:subClassOf ns:Person. 
    }
    ''',
  initNs = {"ns": Namespace("http://somewhere#"), "rdfs": RDFS}
)

# Visualize the results
for r in g.query(q1):
  print(r.sub)

for s,p,o in g.triples((None,RDFS.subClassOf, ns.Person)):
  print(s)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO

for s,p,o in g.triples((None,RDF.type, ns.Person)):
  print(s)


q2 = prepareQuery('''
    SELECT ?p WHERE { 
    ?p rdf:type ns:Person. 
    }
    ''',
  initNs = {"ns": Namespace("http://somewhere#"), "rdfs": RDFS}
)

for r in g.query(q2):
  print(r.p)

# Visualize the results

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
for s,p,o in g.triples((None,RDF.type, ns.Person)):
  for sub, prop, val in g.triples((s,None,None)):
    print(sub,prop,val)


q3 = prepareQuery('''
    SELECT ?x ?s ?o WHERE { 
    ?x rdf:type ns:Person.
    ?x ?s ?o 
    }
    ''',
  initNs = {"ns": Namespace("http://somewhere#"), "rdfs": RDFS}
)

for r in g.query(q3):
  print(r)
# Visualize the results