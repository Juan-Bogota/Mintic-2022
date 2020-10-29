def caso_who(ruta_archivo_csv: str) -> dict:
    import pandas as pd
    if ruta_archivo_csv[-4:] != ".csv":
        return "Extensión inválida."
    try:
        df = pd.read_csv(ruta_archivo_csv)
    except:
        return "Error al leer el archivo de datos."
    df['date'] = pd.to_datetime(df['date'])
    df_calc = pd.DataFrame({'date': df['date'], 'continent': df['continent'], 'ratio': ((df['population'] * df['total_cases_per_million'])/1000000)/((df['population'] * df['hospital_beds_per_thousand'])/1000)})
    df_calc.dropna(inplace=True)
    df_groupby = df_calc.groupby(by = ['date', 'continent'])['ratio'].mean().reset_index()
    pivot_df = df_groupby.pivot(index='date', columns='continent', values='ratio')
    return pivot_df.to_dict()