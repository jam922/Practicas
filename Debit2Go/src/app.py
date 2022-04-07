from datetime import datetime
import json
from webbrowser import get
from flask import Flask, jsonify,render_template,request




app = Flask(__name__)
app.debug= True


@app.route('/')
def home():    
    return render_template('login.html')

    
@app.route('/login', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        with open('../data/usuarios.json') as archivo:
            usuarios =json.load(archivo)
        for usuario in usuarios:
            if usuario['correo'] == request.form.get('username'):
                return render_template('home.html',usuario = request.form.get('username'), passw = request.form.get('password'))
            else:
                return 'No registrado'
            
    return render_template('login.html')        
  
@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'POST':
        fecha = datetime.now()
        usuario={
            "id": "",
            "rol": "CLIENTE",
            "fechaCreacion": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "fechaModificacion": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "correo": request.form.get('username'),
            "prefijoTelefono": request.form.get('prefijo'),
            "telefono": request.form.get('telefono'),
            "nombre": request.form.get('nombre'),
            "apellidos": request.form.get('apellidos')
        }
        with open('../data/usuarios.json','w',encoding ='utf8') as f_obj:
            json.dump(usuario,f_obj)
            return 'usuario registrado'
    else:
        return render_template('register.html')  
            
@app.route('/core/api/suscripcion/<id>')
def suscripcion_id(id):
    with open('../data/suscripciones.json','r') as archivo:
        suscripciones =json.load(archivo)
        for suscripcion in suscripciones:
            if suscripcion['id'] == id:
                return jsonify(suscripcion)

@app.route('/core/api/plan/<id>')
def plan_id(id):
    with open('../data/suscripciones.json','r') as archivo:
        planes =json.load(archivo)
        for plan in planes:
            if plan['plan']['id'] == id:
                return jsonify(plan['plan'])
           
@app.route('/core/api/suscriptor/<id>')
def suscriptor(id):
    with open('../data/suscripciones.json','r') as archivo:
        info =json.load(archivo)
        for inf in info:
            if inf['suscriptor']['id'] == id:
                return jsonify(inf['suscriptor'])

@app.route('/core/api/empresa/<id>/info-publica')
def info_empresa(id):
    with open('../data/suscripciones.json','r') as archivo:
        info_empres =json.load(archivo)
        for informacion in info_empres:
            if informacion['suscriptor']['fkEmpresa'] == id:
                datos = {
                    "id":informacion['plan']['fkEmpresa'],
                    "nombre": informacion['plan']['nombre'],
                    "razonSocial": informacion['suscriptor']['razonSocial'],
                    "nif": informacion['suscriptor']['nif'],
                    "linea1direccion": informacion['ultimaDeuda']['facturaLinea1DirEmpresa'],
                    "linea2direccion": informacion['ultimaDeuda']['facturaLinea2DirEmpresa'],
                    "ciudad": informacion['ultimaDeuda']['facturaCiudadDirEmpresa'],
                    "provinciaRegion": informacion['ultimaDeuda']['facturaProvinciaRegionDirEmpresa'],
                    "codigoPostal": informacion['ultimaDeuda']['facturaLinea1DirEmpresa'],
                    "isoPais":  informacion['ultimaDeuda']['facturaLinea1DirEmpresa'],
                    "urlPaginaWeb":"",
                    "hayLogo": informacion['esCreadaPorSuscriptor'],
                    "hayCondicionesServicio": informacion['plan']['esRecabarDireccionEnvio'],
                }
                return jsonify(datos)

@app.route('/core/api/pais')
def pais():
    with open('../data/listado_paises.json',encoding="utf-8") as archivo:
        paises = json.load(archivo)
        return jsonify(paises)
    
@app.route('/core/api/usuario/<id>')
def usuario(id):
    with open('../data/usuarios.json') as archivo:
        usuarios =json.load(archivo)
        for usuario in usuarios:
            if usuario['id'] == id:
                return jsonify(usuario)

@app.route('/core/api/suscriptor/')
def suscriptor_usuario():
    idUsuario = request.args.get('idUsuario')
    with open('../data/suscripciones.json') as archivo:
        sus_usuarios =json.load(archivo)
        for sus_usuario in sus_usuarios:
            if sus_usuario['suscriptor']['fkUsuario'] == idUsuario:
                datos={
                    "id": sus_usuario['suscriptor']['id'],
                    "nombre":sus_usuario['suscriptor']['nombre'],
                    "correo": sus_usuario['suscriptor']['correo'],
                    "telefono": sus_usuario['suscriptor']['telefono'],
                    "prefijoTelefono":  sus_usuario['suscriptor']['prefijoTelefono'],
                    "apellidos": sus_usuario['suscriptor']['apellidos'],
                    "razonSocial": sus_usuario['suscriptor']['razonSocial'],
                    "esCreadoPorSuscripcion": sus_usuario['suscriptor']['esCreadoPorSuscripcion'],
                    "fechaCreacion": sus_usuario['suscriptor']['fechaCreacion'],
                    "fechaModificacion": sus_usuario['suscriptor']['fechaModificacion'],
                    "nif": sus_usuario['suscriptor']['nif'],
                    "nombreApellidosBusqueda": sus_usuario['suscriptor']['nombreApellidosBusqueda'],
                    "fkEmpresa": sus_usuario['suscriptor']['fkEmpresa'],
                    "fkUsuario": sus_usuario['suscriptor']['fkUsuario'],
                    "fkDireccionFacturacion": sus_usuario['suscriptor']['fkDireccionFacturacion'],
                    "fkMedioPagoSuscriptorPorDefecto":sus_usuario['suscriptor']['fkMedioPagoSuscriptorPorDefecto'],
                }
                return jsonify(datos)

@app.route('/core/api/empresa/', methods=['GET'])
def empresa(id):
    with open('../data/suscripciones.json') as archivo:
        empresa =json.load(archivo)
        for empr in empresa:
            if empr['plan']['fkEmpresa'] == id:
                datos={
                    "id": empr['plan']['fkEmpresa'],
                    "nombre": empr['plan']['nombreEmpresa'],
                    "razonSocial": "Razón Social",
                    "nif": empr['suscriptor']['nif'],
                    "linea1direccion": empr['ultimaDeuda']['facturaLinea1DirEmpresa'],
                    "linea2direccion": empr['ultimaDeuda']['facturaLinea2DirEmpresa'],
                    "ciudad": empr['ultimaDeuda']['facturaCiudadDirEmpresa'],
                    "provinciaRegion": empr['ultimaDeuda']['facturaProvinciaRegionDirEmpresa'],
                    "codigoPostal": empr['ultimaDeuda']['facturaCodigoPostalDirEmpresa'],
                    "isoPais": empr['ultimaDeuda']['facturaIsoPaisDirEmpresa'],
                    "urlPaginaWeb": "",
                    "hayLogo": "true",
                    "hayCondicionesServicio": "false"
                }
                return jsonify(datos)
            
@app.route('/core/api/medio-pago-suscriptor')
def medio_pago():
    idSuscriptor = request.args.get('idSuscriptor')
    
    with open('../data/suscripciones.json') as archivo:
        mediospagoUsuarios = json.load(archivo)
        for mediopagoSuscriptor in mediospagoUsuarios:
            if mediopagoSuscriptor['fkSuscriptor'] == idSuscriptor:
                datos = {
                    "id": mediopagoSuscriptor['fkMedioPagoSuscriptor'],
		            "fkSuscriptor": mediopagoSuscriptor['fkSuscriptor'],
		            "fkMedioPagoEmpresa": mediopagoSuscriptor['plan']['mediosPagoEmpresa'][0]['id'],
		            "servicio": mediopagoSuscriptor['medioPagoSuscriptor']['servicio'],
		            "debtorId": "19af43d6-f548-4ef2-95ee-c858fdbcc4ab",
		            "fechaCreacion": mediopagoSuscriptor['fechaCreacion'],
		            "fechaCaducidad": mediopagoSuscriptor['medioPagoSuscriptor']['fechaCaducidad']
                }
                
                return jsonify(datos)

@app.route('/core/api/deuda')
def lista_deuda():
    idUsuarioSuscriptor = request.args.get('idUsuarioSuscriptor')
    
    with open('../data/suscripciones.json') as archivo:
        listaPagos = json.load(archivo)
        
        for listaPago in listaPagos:
            if listaPago['suscriptor']['fkUsuario'] == idUsuarioSuscriptor:
                return jsonify(listaPago)

@app.route('/tpv-redsys/api/debtor/<id>')
def debtorid(id):
    with open('../data/suscripciones.json') as archivo:
        debtores = json.load(archivo)
        for debtor in debtores:
            if debtor['suscriptor']['id'] == id:
                datos = {
                    "id": debtor['suscriptor']['id'],
	                "fkCreditor": debtor['suscriptor']['fkEmpresa'],
	                "ownerUserId": debtor['suscriptor']['fkUsuario'],
	                "expires": "2212",
	                "cardNumberPartial": "454881******0004",
	                "cardType": null,
	                "cardBrand": "1",
	                "cardCountry": "724",
	                "debtorStatus": debtor['status'],
	                "creationDate": debtor['fechaCreacion']
                }
                return jsonify(datos)

@app.route('/tpv-redsys/api/transaction')
def transacion():
    debtReference = request.args.get('debtReference')
    with open('../data/suscripciones.json') as archivo:
        transaciones = json.load(archivo)
        for transacion in transaciones:
            if transacion['ultimaDeuda']['id']== debtReference:
                return jsonify(transacion)
            else:
                return "Transaccion no encontrada"

@app.route('/core/api/evento-info-publica')
def eventoos():
    idEmpresa = request.args.get('idEmpresa')
    deudaId = request.args.get('deudaId')
    usuarioConAccesoId = request.args.get('usuarioConAccesoId')
    with open('../data/suscripciones.json') as archivo:
        eventos = json.load(archivo)
        for evento in eventos:
            if evento['ultimaDeuda']['fkEmpresa']== idEmpresa:
                if evento['ultimaDeuda']['id']== deudaId:
                    if evento['suscriptor']['fkUsuario']== usuarioConAccesoId:
                        datos={
                            "id": "550456d3-6c80-4c9c-81cb-6f28a977b861",
                            "elemento": "DEUDA",
                            "accion": "ALTA",
                            "fecha": evento['fechaCreacion'],
                            "empresaId": evento['ultimaDeuda']['fkEmpresa'],
                            "empresaNombre": evento['plan']['nombreEmpresa'],
                            "planId": evento['plan']['id'],
                            "planNombre":evento['plan']['nombre'],
                            "suscriptorId":evento['suscriptor']['id'],
                            "suscriptorNombre": evento['suscriptor']['nombre'],
                            "suscriptorApellidos": evento['suscriptor']['apellidos'],
                            "suscriptorFkUsuario": evento['suscriptor']['fkUsuario'],
                            "suscripcionId": evento['ultimaDeuda']['fkSuscripcion'],
                            "suscripcionBeneficiario": evento['beneficiarioServicio'],
                            "suscripcionEstado": evento['estado'],
                            "deudaId": evento['ultimaDeuda']['id'],
                            "deudaEstado": evento['estado'],
                            "deudaConcepto": evento['ultimaDeuda']['concepto'],
                            "deudaFechaVencimiento": "02/12/2022",
                            "deudaFechaInicioPeriodo": "02/12/2022",
                            "deudaFechaFinPeriodo": "01/01/2023",
                            "deudaBeneficiarioServicio": evento['ultimaDeuda']['beneficiarioServicio'],
                            "deudaNumIntentos": evento['ultimaDeuda']['numIntentos'],
                            "importe": evento['plan']['importe'],
                        }
                        return jsonify(datos)
                      
@app.route('/core/api/direccion-suscriptor')
def direccion_uscriptor():
    idSuscriptor = request.args-get('idSuscriptor')
    with open('../data/suscripciones.json') as archivo:
        direcciones = json.load(archivo)
        for direccion in direcciones:
            if direccion['ultimaDeuda']['id'] == idSuscriptor:
                datos = {
                    "id": direccion['ultimaDeuda']['id'],
	                "fkSuscriptor": direccion['ultimaDeuda']['fkSuscriptor'],
	                "linea1direccion": direccion['ultimaDeuda']['facturaLinea1DirSuscriptor'],
	                "linea2direccion": direccion['ultimaDeuda']['facturaLinea2DirSuscriptor'],
	                "ciudad":direccion['ultimaDeuda']['facturaCiudadDirSuscriptor'],
	                "provinciaRegion": direccion['ultimaDeuda']['facturaProvinciaRegionDirSuscriptor'],
	                "codigoPostal": direccion['ultimaDeuda']['facturaCodigoPostalDirSuscriptor'],
	                "isoPais": direccion['ultimaDeuda']['facturaIsoPaisDirSuscriptor'],
	                "prefijoTelefono": direccion['ultimaDeuda']['suscriptor']['prefijoTelefono'],
	                "telefono": direccion['ultimaDeuda']['suscriptor']['telefono'],
	                "nif": direccion['ultimaDeuda']['suscriptor']['nif'],
	                "fechaCreacion": direccion['ultimaDeuda']['fechaCreacion'],
	                "fechaModificacion": direccion['ultimaDeuda']['fechaModificacion']
                }
                return jsonify(datos)
    
@app.route('/core/api/direccion-suscriptor/<id>')
def direccionSuscriptor(id):
    with open('../data/suscripciones.json') as archivo:
        direcciones = json.load(archivo)
        for direccion in direcciones:
            if direccion['ultimaDeuda']['id'] == id:
                datos = {
                    "id": direccion['ultimaDeuda']['id'],
	                "fkSuscriptor": direccion['ultimaDeuda']['fkSuscriptor'],
	                "linea1direccion": direccion['ultimaDeuda']['facturaLinea1DirSuscriptor'],
	                "linea2direccion": direccion['ultimaDeuda']['facturaLinea2DirSuscriptor'],
	                "ciudad":direccion['ultimaDeuda']['facturaCiudadDirSuscriptor'],
	                "provinciaRegion": direccion['ultimaDeuda']['facturaProvinciaRegionDirSuscriptor'],
	                "codigoPostal": direccion['ultimaDeuda']['facturaCodigoPostalDirSuscriptor'],
	                "isoPais": direccion['ultimaDeuda']['facturaIsoPaisDirSuscriptor'],
	                "prefijoTelefono": direccion['ultimaDeuda']['suscriptor']['prefijoTelefono'],
	                "telefono": direccion['ultimaDeuda']['suscriptor']['telefono'],
	                "nif": direccion['ultimaDeuda']['suscriptor']['nif'],
	                "fechaCreacion": direccion['ultimaDeuda']['fechaCreacion'],
	                "fechaModificacion": direccion['ultimaDeuda']['fechaModificacion']
                }
                return jsonify(datos)

@app.route('/core/api/suscripcion')
def suscripcion_usu():
    idUsuario = request.args.get('idUsuario')
    with open('../data/suscripciones.json') as archivo:
        usuarios = json.load(archivo)
        for usuario in usuarios:
            if usuario['suscriptor']['fkUsuario'] == idUsuario:
                return jsonify(usuario)

if __name__ == '__main__':
    app.run()