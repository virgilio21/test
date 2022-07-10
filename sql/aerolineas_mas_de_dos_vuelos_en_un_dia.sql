SELECT id_aerolinea, 
       fecha,
       COUNT(*) AS total
  FROM vuelos
 GROUP BY id_aerolinea, fecha
HAVING COUNT(*) > 2;