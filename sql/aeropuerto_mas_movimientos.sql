WITH movimientos_total AS (

SELECT id_aeropuerto, 
       COUNT(*) AS total
  FROM vuelos
 GROUP BY id_aeropuerto
),
aeropuerto_posiciones AS (

SELECT id_aeropuerto, 
       RANK () OVER(ORDER BY total DESC) AS position
       FROM movimientos_total
)
SELECT aeropuertos.nombre
  FROM aeropuerto_posiciones
       LEFT JOIN aeropuertos
       ON aeropuerto_posiciones.id_aeropuerto = aeropuertos.id
 WHERE position = 1;