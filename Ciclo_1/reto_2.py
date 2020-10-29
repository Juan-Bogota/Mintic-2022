def prestamo(informacion: dict) -> dict:
    prestamo_dict = {}
    prestamo_dict["id_prestamo"] = informacion["id_prestamo"]
    aprobado = dict(aprobado=False)

    i_c = informacion["ingreso_codeudor"]
    i_d = informacion["ingreso_deudor"]
    c_p = informacion["cantidad_prestamo"]

    if isinstance(informacion["dependientes"], str):
        informacion["dependientes"] = 3
    if informacion["independiente"] == "Si":
        independiente = True
    else:
        independiente = False

    if informacion["historia_credito"]:
        if i_c > 0 and i_d / 9 > c_p:
            aprobado = True
        else:
            if informacion["dependientes"] > 2 and independiente:
                if i_c / 12 > c_p:
                    aprobado = True
                else:
                    aprobado = False
            else:
                if c_p < 200:
                    aprobado = True
                else:
                    aprobado = False
    else:
        if independiente:
            if informacion["casado"] == "Si":
                casado = True
            else:
                casado: False
            if not (casado and informacion["dependientes"] > 1):
                if i_d / 10 > c_p or i_c / 10 > c_p:
                    if c_p < 180:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                aprobado = False
        else:
            if not(informacion["tipo_propiedad"] == "Semiurbano") and informacion["dependientes"] < 2:
                if informacion["educacion"] == "Graduado":
                    if i_d / 11 > c_p and i_c / 11 > c_p:
                        aprobado = True
                    else:
                        aprobado = False
                else:
                    aprobado = False
            else:
                aprobado = False

    prestamo_dict.update(aprobado=aprobado)
    return prestamo_dict


print(prestamo({'id_prestamo': 'RETOS2_001', 'casado': 'No', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si',
                'ingreso_deudor': 4692, 'ingreso_codeudor': 0, 'cantidad_prestamo': 106, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
# {'id_prestamo': 'RETOS2_001', 'aprobado': True}
print(prestamo({'id_prestamo': 'RETOS2_002', 'casado': 'No', 'dependientes': '3+', 'educacion': 'No Graduado', 'independiente': 'No',
                'ingreso_deudor': 1830, 'ingreso_codeudor': 0, 'cantidad_prestamo': 100, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
# {'id_prestamo': 'RETOS2_002', 'aprobado': False}
print(prestamo({'id_prestamo': 'RETOS2_003', 'casado': 'No', 'dependientes': 0, 'educacion': 'No Graduado', 'independiente': 'No', 'ingreso_deudor': 3748,
                'ingreso_codeudor': 1668, 'cantidad_prestamo': 110, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Semiurbano'}))
# {'id_prestamo': 'RETOS2_003', 'aprobado': True}
print(prestamo({'id_prestamo': 'RETOS2_011', 'casado': 'No', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'No',
                'ingreso_deudor': 3083, 'ingreso_codeudor': 0, 'cantidad_prestamo': 255, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))
# {'id_prestamo': 'RETOS2_011', 'aprobado': False}
print(prestamo({'id_prestamo': 'RETOS2_012', 'casado': 'Si', 'dependientes': 1, 'educacion': 'Graduado', 'independiente': 'Si',
                'ingreso_deudor': 11500, 'ingreso_codeudor': 0, 'cantidad_prestamo': 286, 'plazo_prestamo': 360, 'historia_credito': 0, 'tipo_propiedad': 'Urbano'}))
# {'id_prestamo': 'RETOS2_012', 'aprobado': False}
