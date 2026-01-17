
/*### Query 1: Total de ventas por cliente  **/
SELECT 
    cliente_id, 
    SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY cliente_id;


/*### Query 2: Total de ventas por mes **/
SELECT 
    DATE_TRUNC(fecha, MONTH) AS mes, 
    SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY 1
ORDER BY mes DESC;

/*### Query 3: Top 5 clientes por ventas **/
SELECT 
    cliente_id, 
    SUM(valor_venta) AS total_ventas
FROM `project.dataset.ventas_diarias`
GROUP BY 1
ORDER BY total_ventas DESC
LIMIT 5;