import pandas as pd
import sqlite3

conn = sqlite3.connect('./data/pesca.db')
df_prod = pd.read_sql_query("SELECT * FROM produttivita", conn)
df_reg = pd.read_sql_query("SELECT * FROM regioni", conn)


# Produttività totale per Area geografica e per anno
df_prod = df_prod.merge(df_reg, left_on='regione', right_on='id_regione')
prod_area_anno = df_prod.groupby(['anno', 'area'])['produttivita_in_migliaia_euro'].sum().reset_index()

"""
SELECT p.anno, r.area, SUM(p.produttivita_migliaia_euro) AS produttivita_tot_area
FROM produttivita p
JOIN regioni r ON p.regione = r.id_regione
GROUP BY p.anno, r.area
ORDER BY p.anno, r.area;
"""
# print(prod_area_anno)

# ----------------------------------------------------------
# Produttività totale NAZIONALE per anno
 
prod_nazionale_anno = df_prod.groupby('anno')['produttivita_in_migliaia_euro'].sum().reset_index()

"""
SELECT anno, SUM(produttivita_migliaia_euro) AS produttivita_tot_nazionale
FROM produttivita
GROUP BY anno
ORDER BY anno;
"""

# print(prod_nazionale_anno)

# ----------------------------------------------------------
# Media percentuale valore aggiunto pesca piscicoltura per Area e anno
df_imp = pd.read_sql_query("SELECT * FROM importanza", conn)
df_imp = df_imp.merge(df_reg, left_on='regione', right_on='id_regione')
media_perc_valore_aggiunto = df_imp.groupby(['anno', 'area'])['perc_valore_servizi'].mean().reset_index()

"""
SELECT i.anno, r.area, AVG(i.perc_valore_aggiunto) AS media_perc_valore_aggiunto
FROM importanza i
JOIN regioni r ON i.regione = r.id_regione
GROUP BY i.anno, r.area
ORDER BY i.anno, r.area;
"""

# print(media_perc_valore_aggiunto)

# ----------------------------------------------------------
# Media variazione percentuale occupazione NAZIONALE per anno
df_and = pd.read_sql_query("SELECT * FROM andamento", conn)
media_var_occupazione_nazionale = df_and.groupby('anno')['variazione_perc_occupazione'].mean().reset_index()

"""
SELECT anno, AVG(variazione_perc_occupazione) AS media_var_occupazione
FROM andamento
GROUP BY anno
ORDER BY anno;
"""

# print(media_var_occupazione_nazionale)

# ----------------------------------------------------------
# Media variazione percentuale occupazione per Area e anno
df_and = df_and.merge(df_reg, left_on='regione', right_on='id_regione')
media_var_occupazione_area = df_and.groupby(['anno', 'area'])['variazione_perc_occupazione'].mean().reset_index()

"""
SELECT a.anno, r.area, AVG(a.variazione_perc_occupazione) AS media_var_occupazione_area
FROM andamento a
JOIN regioni r ON a.regione = r.id_regione
GROUP BY a.anno, r.area
ORDER BY a.anno, r.area;
"""

# print(media_var_occupazione_area)
