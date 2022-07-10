WITH vuelos_total AS (

SELECT id_aerolinea, 
       COUNT(*) AS total
  FROM vuelos
 GROUP BY id_aerolinea
),
aerolinea_posiciones AS (

SELECT id_aerolinea, 
       RANK () OVER(ORDER BY total DESC) AS position
       FROM vuelos_total
)
SELECT aerolineas.nombre
  FROM aerolinea_posiciones
       LEFT JOIN aerolineas
       ON aerolinea_posiciones.id_aerolinea = aerolineas.id
 WHERE position = 1;