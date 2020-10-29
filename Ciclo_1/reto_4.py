def promedio_facultades(info: dict, contando_externos : bool = True ) -> tuple:
    '''
    CONSIDERACIONES IMPORTANTES PARA LOS CORREOS ELECTRÓNICOS:
    * No debe tener duplicados
    * Debe estar completamente en minúsculas
    * No debe tener acentos
    
    EL PROMEDIO DE LA FACULTAD: 
    * Debe reportarse redondeado a dos decimales
    * No debe considerar las materias retiradas
    * Si contando_externos es False, no debe considerar materias electivas ni vacacionales
    '''
    import operator

    def normalize(text):
        """Funcion que valida y reemplaza los acentos a texto normal"""
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("ñ", "n"),
        )
        for a, b in replacements:
            text = text.replace(a, b)
        return text
    
    # Variables iniciales
    promedio_facultad = dict()
    facultad_dict = dict()
    list_mail = list()
    correo = False

    
    for codigo, informacion in info.items():
        materias = informacion.get('materias')

        if not contando_externos:
            validation = str(codigo)[4:6]
            if validation == '05':
                continue
        programa = informacion.get('programa')
        for x in materias:
                        
            facultad = x.get('facultad')
            if not promedio_facultad.get(facultad):
                promedio_facultad[facultad] = []
            if not contando_externos and programa == x.get('codigo')[0:4] and x.get('retirada') == "No" and x.get('creditos') != 0:
                promedio_facultad[facultad] += [(x.get('nota'), x.get('creditos'))]
                correo = True
                    
            if x.get('retirada') == "No" and x.get('creditos') != 0 and contando_externos:
                promedio_facultad[facultad] += [(x.get('nota'), x.get('creditos'))]
                correo = True
                    
        if correo:
            nombre = informacion.get('nombres')
            list_name = nombre.split()
            if len(list_name) == 1:
                mail = nombre[0].lower() + informacion.get('apellidos').split(", ")[1][0].lower() + "." + informacion.get('apellidos').split(", ")[0].lower() + str(informacion.get('documento') % 100).zfill(2)
            else:
                mail = nombre[0].lower() + informacion.get('nombres').split(" ")[1][0].lower() + "." + informacion.get('apellidos').split(", ")[1].lower() + str(informacion.get('documento') % 100).zfill(2)
            mail = normalize(mail)
            list_mail.append(mail)
            correo = False
    
    for facultad, notas in promedio_facultad.items():
        try:
            multiplicar, divisor = 0, 0
            for nota in notas:
                multiplicar += nota[0] * nota[1]
                divisor += nota[1]
            promedio = multiplicar / divisor
            facultad_dict[facultad] = round(promedio, 2)
        except:
            return 'Error numérico.'
    
    facultad_dict = dict(sorted(facultad_dict.items(), key=operator.itemgetter(0)))
        
    return facultad_dict, sorted(list_mail)

