WITH total_vuelos_fecha AS (

SELECT fecha, 
       COUNT(*) AS total
  FROM vuelos
 GROUP BY fecha
),
fecha_posiciones AS (

SELECT fecha, 
       RANK () OVER(ORDER BY total DESC) AS position
       FROM total_vuelos_fecha
)
SELECT fecha_posiciones.fecha
  FROM fecha_posiciones
 WHERE position = 1;