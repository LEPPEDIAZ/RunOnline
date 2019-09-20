#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xmlrpc.client
import json

class GisOdoo(object):
    """docstring for ."""

    def __init__(self):
        #self.url = 'http://192.168.99.100:29069'
        #self.url = 'http://localhost:8069'
        self.url = 'http://ec2-3-212-63-228.compute-1.amazonaws.com:8079'
        self.db = 'Odoo12_LogistikTest'
        #self.db = 'Odoo12_LogistikGis'
        self.username = 'admin'
        self.password = 'logistik2019'
        self.datos = []
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

    def validarAccesos(self):
        db = self.db
        uid = self.uid
        password = self.password
        url = self.url
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        #access me permite validar que el usuario tenga accesos al modelo (tabla).
        access = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
        return access

    def GR_QueryTest(self):
        db = self.db
        uid = self.uid
        password = self.password
        url = self.url
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        contacto_id = 4085

        #Funcion que retorna una lista de elementos de todos los clientes
        p = self.models.execute_kw(db, uid, password, 'res.partner', 'GR_QueryClients', [[]])
        p = json.dumps(p)
        
        f= open("clientlocations.json","w+")
        f.write(str(p))
        f.close()
        #for contacto in p:
        #    print("ClientLocations",contacto)
            #p = p.replace('', "")
        #    f= open("clientlocations.json","w+")
        #    f.write(str(p))
        #    f.close()

        #Funcion que retorna un elemento, dependiendo del paramentro del codigo id del cliente (ej. 4085)
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[4085],{}]
        p = self.models.execute_kw(db, uid, password, 'res.partner', 'GR_QueryClientByIDClient', register_row)
        
        #p = p.replace('', "")
        p = json.dumps(p)
        
        f= open("clientlocations1.json","w+")
        f.write(str(p))
        f.close()

        #Funcion que retorna una lista de elementos, dependiendo del parametro de la fecha de modificacion, (ej. 01/08/2019)
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],{"fecha": "01-08-2019"}]
        p = self.models.execute_kw(db, uid, password, 'res.partner', 'QueryClientsBySyncDate', register_row)
        
        p = json.dumps(p)
        
        f= open("clientlocations2.json","w+")
        f.write(str(p))
        f.close()

        #Funcion para modificar los datos del cliente en base al codigo del cliente como paramentro, (ej. 4085)
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[6876],{
            "nombre_negocio": "Prueba 2 de proveedores",
            "direccion_ubicacion_cliente": "3 CALLE 1-76 zona 3 Boca del monte Villa Canales 1.1",
            "codigo_pais" : 90,
            "codigo_departamento": 185,
            "codigo_municipio": 1,
            "zona": 21,
            "colonia": "colonia mariscal",
            "latitud": 13.12345,
            "longitud": 14.25877,

        }]
        p = self.models.execute_kw(db, uid, password, 'res.partner', 'GR_UpdateClientbyIDClientLocation', register_row)
        
        p = json.dumps(p)
       
        f= open("clientlocations3.json","w+")
        f.write(str(p))
        f.close()

        #Consultar Pedidos por Agencia Fecha Despacho
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],{
            "codigo_agencia": 25,
            "fecha_despacho": "10/09/2019",

        }]
        p = self.models.execute_kw(db, uid, password, 'pedidos', 'GR_QueryOrdersByIDLocationDeliveryDate', register_row)
        
        p = json.dumps(p)
       
        f= open("clientlocations4.json","w+")
        f.write(str(p))
        f.close()

        #CConsultar Pedidos por Código Cliente Rango Fechas Despacho
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        #**************************************************************************************************************************
        register_row = [[],{
            "codigo_cliente": 7752,
            "fecha_despacho_del": "10/09/2019",
            "fecha_despacho_al": "10/09/2019",

        }]
        p = self.models.execute_kw(db, uid, password, 'pedidos', 'GR_QueryOrdersByIDClientDateRanges', register_row)
        
        p = json.dumps(p)
 
        f= open("clientlocations5.json","w+")
        f.write(str(p))
        f.close()


        return True

odoo = GisOdoo()
if odoo.validarAccesos():
    clientes = odoo.GR_QueryTest()
def echo(event):
    odoo = GisOdoo()
    if odoo.validarAccesos():
        clientes = odoo.GR_QueryTest()

    #print(clientes)
